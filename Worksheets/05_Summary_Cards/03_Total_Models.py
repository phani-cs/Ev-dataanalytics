"""Worksheet: Total Models"""
import sys
from pathlib import Path

import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from utils import load_global_ev

df = load_global_ev()
total = len(df)

fig, ax = plt.subplots(figsize=(5, 4))
ax.text(0.5, 0.55, str(total), fontsize=72, ha="center", va="center", fontweight="bold", color="#2E86C1")
ax.text(0.5, 0.22, "Total EV Models", fontsize=16, ha="center", va="center")
ax.axis("off")
plt.title("Total Models", fontsize=14)
plt.tight_layout()
plt.show()
