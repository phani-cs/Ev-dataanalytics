"""Worksheet: Top Speed (Cheapest EV database)"""
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from utils import load_cheapest_ev

df = load_cheapest_ev().dropna(subset=["TopSpeed_KmH"]).nlargest(15, "TopSpeed_KmH")

plt.figure(figsize=(10, 7))
sns.barplot(data=df, y="Name", x="TopSpeed_KmH", color="#8E44AD", orient="h")
plt.title("Top Speed — Fastest 15 Models")
plt.xlabel("Top Speed (Km/H)")
plt.ylabel("")
plt.tight_layout()
plt.show()
