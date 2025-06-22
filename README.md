# Wuzzuf Job Scraper (Python Jobs)

This is a Python-based web scraper that extracts job postings for **Python-related roles** from [Wuzzuf](https://wuzzuf.net), one of Egypt’s largest job platforms.

It automatically collects key job data like:
- 🏷 Job Title  
- 🏢 Company Name  
- 📍 Location  
- 📅 Post Date  
- 🔗 Direct Job Link  
- 🧠 Required Skills  
- 💰 Salary (if listed)  
- 📌 Job Requirements  

---

📂 Project Structure


wuzzuf-scraper-project/

│
├── data/
│ └── jobs.csv # Auto-generated CSV file
├── src/
│ └── scraper.py # Main scraping script
├── .gitignore
├── requirements.txt
└── README.md



---

## 🚀 Features

✅ Fully automated scraping using **Selenium + BeautifulSoup**  
✅ Parses multiple pages dynamically (pagination support)  
✅ Extracts detailed job data using `requests`  
✅ Graceful error handling & logging  
✅ Clean CSV output  
✅ Beginner-friendly & production-ready code

---

## 🧪 Sample Output

| Job Title        | Company       | Location      | Post Date | Salary         |
|------------------|---------------|---------------|-----------|----------------|
| Python Developer | SoftTech Inc. | Cairo, Egypt  | 2 days ago| EGP 10k–15k     |
| AI Engineer      | Vision AI     | Giza, Egypt   | 1 day ago | Not specified   |

_All scraped data is saved to: `data/jobs.csv`_

---

## 🛠 Installation

1. **Clone the repository**
bash
git clone https://github.com/your-username/wuzzuf-scraper-project.git
cd wuzzuf-scraper-project


2- (Optional) Create virtual environment

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # Windows

Download ChromeDriver
Match your Chrome version from:
https://sites.google.com/chromium.org/driver/
Then update the path inside scraper.py if needed.

⚙️ Tech Stack
🐍 Python 3.x

🌐 Selenium WebDriver

🧼 BeautifulSoup4

💾 CSV & Requests

📌 Notes
Script is for educational / portfolio use.

Please scrape responsibly — don’t overload servers.

Ensure your ChromeDriver version matches your browser version.

🙋‍♂️ Author
Islam Osama
GitHub • LinkedIn
Python Web Scraping & Automation Expert

💼 Need a custom scraper or automation bot?
👉 Available for freelance work on Fiverr (insert your Fiverr link)

yaml
Copy
Edit

---

✅ Let me know if you want me to generate the `requirements.txt`, `.gitignore`, or help prepare your GitHub commit message.








