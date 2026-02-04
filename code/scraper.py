import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.usa.gov/"

headers = {
    "User-Agent": "Mozilla/5.0 (compatible; MyScraper/1.0)"
}

response = requests.get(URL, headers=headers, timeout=10)
response.raise_for_status()

soup = BeautifulSoup(response.text, "lxml")

links = []

for a in soup.find_all("a"):
    text = a.get_text(strip=True)
    href = a.get("href")
    if href:
        links.append({"text": text, "url": href})

with open("usa_gov_links.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["text", "url"])
    writer.writeheader()
    writer.writerows(links)

print(f"Saved {len(links)} links to usa_gov_links.csv")
