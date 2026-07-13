"""Worksheet: Price vs Range"""
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from utils import load_global_ev

df = load_global_ev()

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="Range_Km", y="PriceEuro", hue="Brand", legend=False)
plt.title("Price vs Range")
plt.xlabel("Range (Km)")
plt.ylabel("Price (EUR)")
plt.tight_layout()
plt.show()
