import requests
import feedparser
from datetime import datetime


RSS_FEEDS = {
    "The Hacker News": "https://feeds.feedburner.com/TheHackersNews",
    "Krebs on Security": "https://krebsonsecurity.com/feed/",
}


def scrape_feed(source, url):
    """Scrape les articles d'un flux RSS."""

    try:
        response = requests.get(
            url,
            timeout=10,
            headers={
                "User-Agent": "SecurityNewsDashboard/1.0"
            }
        )
        response.raise_for_status()

        feed = feedparser.parse(response.content)

        articles = []

        for entry in feed.entries:
            article = {
                "title": entry.get("title", "No title"),
                "source": source,
                "url": entry.get("link", ""),
                "published": entry.get(
                    "published",
                    datetime.now().isoformat()
                ),
                "summary": entry.get("summary", ""),
            }

            articles.append(article)

        return articles

    except requests.RequestException as error:
        print(f"[!] Error scraping {source}: {error}")
        return []


def scrape_all():
    """Scrape toutes les sources configurées."""

    all_articles = []

    for source, url in RSS_FEEDS.items():
        print(f"[*] Scraping {source}...")

        articles = scrape_feed(source, url)
        all_articles.extend(articles)

        print(f"[+] {len(articles)} articles found")

    return all_articles


if __name__ == "__main__":
    articles = scrape_all()

    print(f"\n[+] Total articles: {len(articles)}")

    for article in articles[:5]:
        print(f"\n{article['title']}")
        print(article["url"])
