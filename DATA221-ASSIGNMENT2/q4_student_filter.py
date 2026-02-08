import pandas as pd

df = pd.read_csv("student.csv")

filtered = df[(df["studytime"] >= 3) & (df["internet"] == 1) & (df["absences"] <= 5)]

filtered.to_csv("high_engagement.csv", index=False)

print(len(filtered))
print(filtered["grade"].mean())
