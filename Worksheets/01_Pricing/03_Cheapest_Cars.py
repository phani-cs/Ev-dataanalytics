"""Worksheet: Cheapest Cars (uses global EV data ranked by price)"""
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from utils import load_global_ev

df = load_global_ev()
cheap = df.nsmallest(10, "PriceEuro").copy()
cheap["Label"] = cheap["Brand"] + " " + cheap["Model"]

plt.figure(figsize=(10, 6))
sns.barplot(data=cheap, y="Label", x="PriceEuro", color="#27AE60", orient="h")
plt.title("Cheapest Cars (Top 10)")
plt.xlabel("Price (EUR)")
plt.ylabel("")
plt.tight_layout()
plt.show()
