"""Worksheet: Average Price by Brand"""
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from utils import load_global_ev

df = load_global_ev()
avg = df.groupby("Brand", as_index=False)["PriceEuro"].mean().sort_values("PriceEuro", ascending=False)

plt.figure(figsize=(12, 6))
sns.barplot(data=avg, x="Brand", y="PriceEuro", color="#2E86C1")
plt.xticks(rotation=45, ha="right")
plt.title("Average Price by Brand (€)")
plt.xlabel("Brand")
plt.ylabel("Average Price (EUR)")
plt.tight_layout()
plt.show()
