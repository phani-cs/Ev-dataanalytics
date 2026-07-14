"""Worksheet: Efficiency (Cheapest EV database)"""
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from utils import load_cheapest_ev

df = load_cheapest_ev().dropna(subset=["Efficiency_WhKm"]).nsmallest(15, "Efficiency_WhKm")

plt.figure(figsize=(10, 7))
sns.barplot(data=df, y="Name", x="Efficiency_WhKm", color="#1ABC9C", orient="h")
plt.title("Most Efficient EVs (Lowest Wh/Km)")
plt.xlabel("Efficiency (Wh/Km)")
plt.ylabel("")
plt.tight_layout()
plt.show()
