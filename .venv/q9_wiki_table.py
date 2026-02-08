import csv
import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Machine_learning"
headers = {"User-Agent": "Mozilla/5.0"}

resp = requests.get(url, headers=headers, timeout=10)
resp.raise_for_status()

soup = BeautifulSoup(resp.text, "html.parser")

content = soup.find("div", id="mw-content-text")
if not content:
    raise SystemExit("Could not find mw-content-text")

tables = content.find_all("table")

def get_cell_text(cell):
    return cell.get_text(" ", strip=True)

chosen_table = None
chosen_rows = None

for table in tables:
    rows = table.find_all("tr")
    data_rows = []
    for r in rows:
        if r.find_all("td"):
            data_rows.append(r)
    if len(data_rows) >= 3:
        chosen_table = table
        chosen_rows = rows
        break

headers_row = None
for r in chosen_rows:
    ths = r.find_all("th")
    tds = r.find_all("td")
    if ths and not tds:
        headers_row = r
        break

if headers_row:
    headers = [get_cell_text(th) for th in headers_row.find_all("th")]
else:
    max_cols = 0
    for r in chosen_table.find_all("tr"):
        cols = r.find_all(["th", "td"])
        max_cols = max(max_cols, len(cols))
    headers = [f"col{i}" for i in range(1, max_cols + 1)]

data = []
max_len = len(headers)

for r in chosen_table.find_all("tr"):
    tds = r.find_all("td")
    if not tds:
        continue
    row_vals = [get_cell_text(td) for td in tds]
    if len(row_vals) < max_len:
        row_vals += [""] * (max_len - len(row_vals))
    elif len(row_vals) > max_len:
        row_vals = row_vals[:max_len]
    data.append(row_vals)

with open("wiki_table.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(data)
