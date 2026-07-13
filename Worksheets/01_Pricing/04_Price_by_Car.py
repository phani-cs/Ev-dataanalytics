"""Worksheet: Price by Car (India EVs)"""
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from utils import load_india_ev

df = load_india_ev().sort_values("Price_Lakhs", ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(data=df, y="Car", x="Price_Lakhs", color="#E67E22", orient="h")
plt.title("Price by Car (India EV — Lakhs)")
plt.xlabel("Price Range (Lakhs)")
plt.ylabel("")
plt.tight_layout()
plt.show()
