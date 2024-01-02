import glassdoor_scraper as gs
import pandas as pd

path = "/Users/shalmolymondal/Library/CloudStorage/OneDrive-Personal/Projects/DataScienceProjects/datasci_salary_estimator"

df = gs.get_jobs("data scientist", 1000, False, path, 15)

df.to_csv("glassdoor_jobs.csv", index=False)
df
