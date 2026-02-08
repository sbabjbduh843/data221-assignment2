import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Data_science"
headers = {"User-Agent": "Mozilla/5.0"}

resp = requests.get(url, headers=headers, timeout=10)
resp.raise_for_status()

soup = BeautifulSoup(resp.text, "html.parser")

content = soup.find("div", id="mw-content-text")
if not content:
    raise SystemExit("Could not find mw-content-text")

banned = {"references", "external links", "see also", "notes"}

headings = []
for h2 in content.find_all("h2"):
    text = h2.get_text(" ", strip=True)
    text = text.replace("[edit]", "").strip()

    lower = text.lower()
    if any(b in lower for b in banned):
        continue

    if text:
        headings.append(text)

with open("headings.txt", "w", encoding="utf-8") as f:
    for h in headings:
        f.write(h + "\n")
