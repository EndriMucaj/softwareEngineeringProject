import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.bbc.com/news"

def scrape_news():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    articles = []

    for item in soup.select("h2"):
        title = item.get_text(strip=True)
        if title:
            articles.append(title)

    return articles


def save_to_csv(data, filename="data/news.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["title"])
        for title in data:
            writer.writerow([title])


if __name__ == "__main__":
    news = scrape_news()
    save_to_csv(news)
