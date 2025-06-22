import csv
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from itertools import zip_longest
import time
from datetime import datetime
import os

# ========== Configuration ==========
DRIVER_PATH = r"C:\Users\SMSMAAA\scraping & automation\wuzzuf-scraper-project\chromedriver.exe"
BASE_URL = "https://wuzzuf.net/search/jobs/?a=navbl&q=python&start="
CSV_PATH = r"C:\Users\SMSMAAA\scraping & automation\wuzzuf-scraper-project\data"
DELAY_SECONDS = 5
HEADERS = {'User-Agent': 'Mozilla/5.0'}
MAX_RETRIES = 3
# ====================================

def log(message):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {message}")

def fetch_job_page(link):
    for _ in range(MAX_RETRIES):
        try:
            res = requests.get(link, headers=HEADERS, timeout=10)
            if res.status_code == 200:
                return BeautifulSoup(res.content, "lxml")
        except Exception:
            time.sleep(1)
    return None

def scrape_wuzzuf_jobs():
    job_titles, post_dates, company_names, company_locations = [], [], [], []
    job_skills, links, salaries, requirements = [], [], [], []

    page_num = 0

    while True:
        # Setup driver
        service = Service(executable_path=DRIVER_PATH)
        driver = webdriver.Chrome(service=service)

        try:
            log(f"Scraping page {page_num}...")
            driver.get(f"{BASE_URL}{page_num}")
            time.sleep(DELAY_SECONDS)

            soup = BeautifulSoup(driver.page_source, "lxml")

            # Stop if page limit reached
            try:
                page_limit = int(soup.find("strong").text)
                if page_num > page_limit // 15:
                    log("Reached last page.")
                    break
            except Exception:
                log("Can't determine page limit. Stopping.")
                break

            job_cards = soup.find_all("div", class_="css-1gatmva")
            if not job_cards:
                log("No job listings found. Done.")
                break

            for card in job_cards:
                # Job title + link
                title_tag = card.find("h2", class_="css-m604qf")
                if title_tag and title_tag.a:
                    job_titles.append(title_tag.a.text.strip())
                    link = title_tag.a["href"]
                    links.append(f"https://wuzzuf.net{link}" if not link.startswith("http") else link)
                else:
                    job_titles.append("Not found")
                    links.append("")

                # Post date
                date_tag = card.find("div", class_=["css-4c4ojb", "css-do6t5g"])
                post_dates.append(date_tag.text.strip() if date_tag else "Not specified")

                # Company name
                company_tag = card.find("a", class_="css-17s97q8")
                company_names.append(company_tag.text.strip() if company_tag else "Not listed")

                # Location
                location_tag = card.find("span", class_="css-5wys0k")
                company_locations.append(location_tag.text.strip() if location_tag else "Not listed")

                # Skills
                skills_block = card.find("div", class_="css-y4udm8")
                if skills_block:
                    inner_divs = skills_block.find_all("div", recursive=False)
                    if len(inner_divs) > 1:
                        skills_div = inner_divs[1]
                        skills = skills_div.find_all("a")
                        job_skills.append(", ".join([s.text.strip() for s in skills]))
                    else:
                        job_skills.append("Not listed")
                else:
                    job_skills.append("Not listed")
        finally:
            driver.quit()

        page_num += 1

    log("Scraping job details from individual pages...")

    for i, link in enumerate(links):
        log(f"({i+1}/{len(links)}) → {link}")
        soup = fetch_job_page(link)
        if not soup:
            salaries.append("Failed")
            requirements.append("Failed")
            continue

        # Salary
        salary_tag = soup.find("span", class_="css-4xky9y")
        salaries.append(salary_tag.text.strip() if salary_tag else "Not specified")

        # Requirements
        req_block = soup.find("div", class_="css-1t5f0fr")
        if req_block:
            items = req_block.find_all("li")
            requirements.append(" | ".join([li.text.strip() for li in items]))
        else:
            requirements.append("Not listed")

    # Save data
    filename = f"jobs_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"
    output_path = os.path.join(CSV_PATH, filename)

    log(f"Saving data to {output_path}...")
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "Job Title", "Post Date", "Company Name",
            "Location", "Skills", "Link",
            "Salary", "Requirements"
        ])
        for row in zip_longest(
            job_titles, post_dates, company_names,
            company_locations, job_skills, links,
            salaries, requirements, fillvalue="N/A"
        ):
            writer.writerow(row)

    log("✅ Scraping completed successfully.")

# Run
if __name__ == "__main__":
    scrape_wuzzuf_jobs()
