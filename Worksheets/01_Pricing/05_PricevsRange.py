"""Worksheet: Price vs Range (alternate view)"""
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from utils import load_global_ev

df = load_global_ev()

plt.figure(figsize=(10, 6))
sns.regplot(data=df, x="Range_Km", y="PriceEuro", scatter_kws={"alpha": 0.6}, line_kws={"color": "red"})
plt.title("Price vs Range (with trend)")
plt.xlabel("Range (Km)")
plt.ylabel("Price (EUR)")
plt.tight_layout()
plt.show()
