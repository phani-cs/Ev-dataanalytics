"""Worksheet: Price vs Range (Cheapest EV database)"""
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from utils import load_cheapest_ev

df = load_cheapest_ev().dropna(subset=["Range_Km", "Price_Germany"])

plt.figure(figsize=(10, 6))
sns.regplot(data=df, x="Range_Km", y="Price_Germany", scatter_kws={"alpha": 0.6}, line_kws={"color": "red"})
plt.title("Price vs Range (Cheapest EV DB)")
plt.xlabel("Range (Km)")
plt.ylabel("Price Germany (EUR)")
plt.tight_layout()
plt.show()
