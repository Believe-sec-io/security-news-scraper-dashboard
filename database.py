import sqlite3
from pathlib import Path


DATABASE_DIR = Path("data")
DATABASE_FILE = DATABASE_DIR / "news.db"


def connect():
    DATABASE_DIR.mkdir(exist_ok=True)
    return sqlite3.connect(DATABASE_FILE)


def create_table():
    with connect() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS news (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                source TEXT NOT NULL,
                url TEXT UNIQUE NOT NULL,
                published TEXT,
                summary TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        conn.commit()


def save_article(article):
    """Save an article if it does not already exist."""

    with connect() as conn:
        cursor = conn.execute("""
            INSERT OR IGNORE INTO news
            (title, source, url, published, summary)
            VALUES (?, ?, ?, ?, ?)
        """, (
            article["title"],
            article["source"],
            article["url"],
            article["published"],
            article["summary"],
        ))

        conn.commit()

        return cursor.rowcount > 0


def save_articles(articles):
    """Save multiple articles."""

    saved = 0

    for article in articles:
        if save_article(article):
            saved += 1

    return saved


def get_articles(limit=100):
    """Return stored articles."""

    with connect() as conn:
        cursor = conn.execute("""
            SELECT id, title, source, url, published, summary
            FROM news
            ORDER BY id DESC
            LIMIT ?
        """, (limit,))

        return cursor.fetchall()


if __name__ == "__main__":
    create_table()
    print("[+] Database initialized")
