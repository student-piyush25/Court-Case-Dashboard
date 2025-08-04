# 🧾 Court Case Info Dashboard (Simulated)

A mini Flask web application to simulate fetching Indian court case details using case type, number, and filing year. Built as part of the Think Act Rise Foundation Python Internship Task.

---

## 🚀 Features

- Input: Case Type, Case Number, Filing Year
- Stores submitted cases in a SQLite database
- View all saved cases at `/cases`
- Simulated court details:
  - Petitioner and Respondent names
  - Next hearing date
  - Latest order PDF link (dummy)
- Clean UI styled with custom CSS

---

## ⚠️ Why Simulated?

Most Indian court websites (like Delhi High Court) use CAPTCHA, which blocks automated scraping with tools like Selenium.

This app uses a **simulated function** to mimic real scraper behavior, allowing you to demonstrate logic without violating scraping policies.

---

## 🛠 Tech Stack

- Python 3.11
- Flask 3.1
- Flask-SQLAlchemy
- Jinja2 Templates (HTML)
- SQLite (via SQLAlchemy)
- CSS (static file)

---

## 🧪 How to Run Locally

```bash
# Clone this repository
git clone https://github.com/your-username/court-case-dashboard.git
cd court-case-dashboard

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt

# Start the Flask server
python run.py


