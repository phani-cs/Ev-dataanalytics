"""Worksheet: Top Speed"""
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from utils import load_global_ev

df = load_global_ev().nlargest(15, "TopSpeed_KmH").copy()
df["Label"] = df["Brand"] + " " + df["Model"]

plt.figure(figsize=(10, 7))
sns.barplot(data=df, y="Label", x="TopSpeed_KmH", color="#8E44AD", orient="h")
plt.title("Top Speed — Fastest 15 Models")
plt.xlabel("Top Speed (Km/H)")
plt.ylabel("")
plt.tight_layout()
plt.show()
