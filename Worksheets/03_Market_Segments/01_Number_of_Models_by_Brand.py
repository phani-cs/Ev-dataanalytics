"""Worksheet: Number of Models by Brand"""
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from utils import load_global_ev

df = load_global_ev()
counts = df.groupby("Brand", as_index=False)["Model"].count().rename(columns={"Model": "Models"})
counts = counts.sort_values("Models", ascending=False)

plt.figure(figsize=(12, 6))
sns.barplot(data=counts, x="Brand", y="Models", color="#3498DB")
plt.xticks(rotation=45, ha="right")
plt.title("Number of Models by Brand")
plt.tight_layout()
plt.show()
