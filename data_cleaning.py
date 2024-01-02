import pandas as pd

df = pd.read_csv("glassdoor_jobs.csv")


# Parse Salary
# Company name text only
# Split location
# Parse job description (Python, React, etc)

df.head(30)

# Removed -1 from salary estimate
df = df[df["Salary Estimate"] != "-1"]

# Removing text from salary column

# salary = df["Salary Estimate"].apply(lambda x: x.split("(")[0])
salary = df["Salary Estimate"].apply(lambda x: x.split("(")[0])
minus_Kd = salary.apply(lambda x: x.replace("K", "").replace("$", ""))
