# security-news-scraper-dashboard

A simple cybersecurity news scraper and dashboard built with Python.

The project collects cybersecurity news from RSS feeds, stores the articles in a local SQLite database, and displays them through a Streamlit dashboard.

🚀 Features

- Scrape cybersecurity news from RSS feeds
- Store articles locally using SQLite
- Prevent duplicate articles
- Search stored news
- Filter news by source
- Display article statistics
- Simple web dashboard

🛠️ Technologies

- Python 3
- Requests
- Feedparser
- SQLite
- Streamlit

📁 Project Structure

security-news-dashboard/
│
├── main.py
├── scraper.py
├── database.py
├── dashboard.py
├── requirements.txt
├── README.md
│
└── data/
    └── news.db

⚙️ Installation

Clone the repository:

git clone https://github.com/yourusername/security-news-dashboard.git
cd security-news-dashboard

Install the dependencies:

pip install -r requirements.txt

▶️ Usage

First, collect and store the news:

python main.py

Then start the dashboard:

streamlit run dashboard.py

Open the URL provided by Streamlit in your browser.

📰 News Sources

The initial version uses cybersecurity RSS feeds such as:

- The Hacker News
- Krebs on Security

Additional sources can be added later in "scraper.py".

💾 Database

The project uses SQLite for local storage.

The database is automatically created at:

data/news.db

Articles are identified by their URL, which prevents duplicate entries.

🔮 Future Improvements

Planned improvements include:

- More cybersecurity news sources
- Automatic scheduled scraping
- News categories
- CVE-related news detection
- Advanced search
- Date filtering
- Better dashboard statistics
- Export news to JSON/CSV
- Threat-level classification

⚠️ Disclaimer

This project is intended for educational and defensive cybersecurity purposes.

Always respect the terms of service and access policies of the websites and feeds you interact with.

📜 License

MIT License
