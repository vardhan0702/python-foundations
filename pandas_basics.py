import pandas as pd
df = pd.read_csv("testdata.txt")
print(df)
print(df.head())
print(df.tail())
print(df.describe())


passed_only = df[df["status"]=="Passed"]
print(passed_only)
print("----------------------")
print(df["status"]=="Passed")
print("----------------------")
print(df[df["status"]=="Passed"])

#use the pandas library for counting passed, failed, total, percentage from test data file without using loops.
print("use the pandas library for counting passed, failed, total, percentage from test data file without using loops.")
df= pd.read_csv("testdata.txt")
passed = len(df[df["status"]=="Passed"])
failed = len(df[df["status"]=="Failed"])
total = len(df)
percentage_passed = (passed / total) * 100

print("Passed:", passed, "Failed:", failed, "Total:", total, "Percentage Passed:", percentage_passed)