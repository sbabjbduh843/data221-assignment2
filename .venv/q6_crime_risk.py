import pandas as pd

df = pd.read_csv("crime.csv")

df["risk"] = df["ViolentCrimesPerPop"].apply(
    lambda x: "HighCrime" if x >= 0.50 else "LowCrime"
)

avg_unemployment = df.groupby("risk")["PctUnemployed"].mean()

for risk, value in avg_unemployment.items():
    print(f"{risk}: {value:.2f}")
