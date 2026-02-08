import string
from collections import defaultdict

def normalize_line(line: str) -> str:
    line = line.lower()
    remove_chars = set(string.whitespace) | set(string.punctuation)
    return "".join(ch for ch in line if ch not in remove_chars)

with open("sample-file.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

groups = defaultdict(list)

for idx, line in enumerate(lines, start=1):
    norm = normalize_line(line)
    groups[norm].append((idx, line.rstrip("\n")))

duplicate_sets = [items for items in groups.values() if len(items) >= 2]

print(len(duplicate_sets))

for set_idx, items in enumerate(duplicate_sets[:2], start=1):
    print(f"\nSet {set_idx}:")
    for line_no, original in items:
        print(f"{line_no}: {original}")
