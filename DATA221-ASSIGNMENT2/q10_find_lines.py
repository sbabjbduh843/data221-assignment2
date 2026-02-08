def find_lines_containing(filename, keyword):

    results = []
    keyword_lower = keyword.lower()

    with open(filename, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            if keyword_lower in line.lower():
                results.append((i, line.rstrip("\n")))

    return results


matches = find_lines_containing("sample-file.txt", "lorem")

print(len(matches))

for line_no, text in matches[:3]:
    print(f"{line_no}: {text}")
