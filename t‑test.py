import pandas as pd
from scipy.stats import ttest_ind

df = pd.read_csv("test.csv")
d = df[["Sex", "Age"]].dropna()

stat, p_val = ttest_ind(
    d[d["Sex"] == "male"]["Age"],
    d[d["Sex"] == "female"]["Age"],
)

print(f"t = {stat:.4f}, p-value = {p_val:.4g}")
print("Разница значима" if p_val < 0.05 else "Значимой разницы нет")
