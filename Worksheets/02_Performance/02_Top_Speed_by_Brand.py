"""Worksheet: Top Speed by Brand"""
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from utils import load_global_ev

df = load_global_ev()
speed = df.groupby("Brand", as_index=False)["TopSpeed_KmH"].max().sort_values("TopSpeed_KmH", ascending=False)

plt.figure(figsize=(12, 6))
sns.barplot(data=speed, x="Brand", y="TopSpeed_KmH", color="#2980B9")
plt.xticks(rotation=45, ha="right")
plt.title("Top Speed by Brand (Max)")
plt.xlabel("Brand")
plt.ylabel("Top Speed (Km/H)")
plt.tight_layout()
plt.show()
