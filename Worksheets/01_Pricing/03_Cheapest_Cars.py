"""Worksheet: Cheapest Cars (Cheapestelectriccars-EVDatabase)"""
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from utils import load_cheapest_ev

df = load_cheapest_ev().dropna(subset=["Price_Germany"]).nsmallest(10, "Price_Germany")

plt.figure(figsize=(10, 6))
sns.barplot(data=df, y="Name", x="Price_Germany", color="#27AE60", orient="h")
plt.title("Cheapest Cars (Top 10 — Germany €)")
plt.xlabel("Price (EUR)")
plt.ylabel("")
plt.tight_layout()
plt.show()
