import pandas as pd

df = pd.read_csv("student.csv")

def grade_band(grade):
    if grade <= 9:
        return "Low"
    elif grade <= 14:
        return "Medium"
    else:
        return "High"

df["grade_band"] = df["grade"].apply(grade_band)

summary = df.groupby("grade_band").agg(
    number_of_students=("grade", "count"),
    average_absences=("absences", "mean"),
    internet_percentage=("internet", lambda x: x.mean() * 100)
)

summary.to_csv("student_bands.csv")
print(summary)