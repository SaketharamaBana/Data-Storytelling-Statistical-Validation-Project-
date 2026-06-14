import pandas as pd
from scipy.stats import ttest_ind

df = pd.read_csv("Cleaned_Sales_Dataset.csv")

male_sales = df[df['Gender']=='Male']['Total_Sales']
female_sales = df[df['Gender']=='Female']['Total_Sales']

t_stat, p_value = ttest_ind(
    male_sales,
    female_sales,
    equal_var=False
)

print("T Statistic:", t_stat)
print("P Value:", p_value)

if p_value < 0.05:
    print("Reject Null Hypothesis")
else:
    print("Fail to Reject Null Hypothesis")