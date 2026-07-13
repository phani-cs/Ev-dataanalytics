"""Worksheet: Boot Space (India EVs)"""
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from utils import load_india_ev

df = load_india_ev().sort_values("BootSpace_L", ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(data=df, y="Car", x="BootSpace_L", color="#9B59B6", orient="h")
plt.title("Boot Space — India EVs")
plt.xlabel("Boot Space (Litres)")
plt.ylabel("")
plt.tight_layout()
plt.show()
