import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Data_science"
headers = {"User-Agent": "Mozilla/5.0"}

resp = requests.get(url, headers=headers, timeout=10)
resp.raise_for_status()

soup = BeautifulSoup(resp.text, "html.parser")

title_tag = soup.find("title")
print(title_tag.get_text(strip=True) if title_tag else "")

content = soup.find("div", id="mw-content-text")
if not content:
    print("Could not find mw-content-text")
    raise SystemExit

for p in content.find_all("p"):
    text = p.get_text(strip=True)
    if len(text) >= 50:
        print(text)
        break
text = p.get_text(" ", strip=True)
