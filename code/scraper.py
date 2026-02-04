import requests 
from bs4 import BeautifulSoup 
import csv  

url = "https://www.usa.gov"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X)"
}

response = requests.get(url, headers=headers, timeout=10)
response.raise_for_status()

soup = BeautifulSoup(response.text, "lxml")

links = soup.find_all("a")

for link in links:
    text = link.text.strip()
    href = link.get("href")
    print(text, href)
print(soup.title.text)

with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["text", "url"])
    for link in links:
        writer.writerow([link.text.strip(), link.get("href")])