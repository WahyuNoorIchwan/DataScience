import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_csv("dummy_data.csv")

# Separate Categories
cat_1 = df["Age"]
cat_2 = df["Status"]

# Cross Tabulation of Categories Pair
ctab = pd.crosstab(cat_1, cat_2, margins=True, margins_name="Total")

# Calculate Chi Square
row, col = ctab.shape
chi = 0

for i in range(row-1):
    for j in range(col-1):
        E = ctab.iloc[i, -1]*ctab.iloc[-1, j]/ctab.iloc[-1, -1]
        chi += (ctab.iloc[i, j] - E)**2 / E

# Calculate p-value from  Chi Square Value
p = 1 - stats.chi2.cdf(chi, (row-1)*(col-1))

treshold = 0.05
if p < 0.05:
    print("{} and {} are related".format("Age", "Status"))
else:
    print("{} and {} are not related")