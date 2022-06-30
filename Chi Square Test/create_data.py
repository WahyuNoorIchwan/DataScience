import numpy as np
import pandas as pd

cat_a = ["15-19", "20-25", "26-30", "31-40"]
cat_b = ["Single", "Married", "Divorced"]

data = []
data += [[cat_a[0], cat_b[0]]]*40
data += [[cat_a[1], cat_b[0]]]*20
data += [[cat_a[1], cat_b[1]]]*40
data += [[cat_a[2], cat_b[1]]]*40
data += [[cat_a[3], cat_b[2]]]*10

data = pd.DataFrame(data, columns=["Age", "Status"])
data.to_csv("dummy_data.csv")