"""Worksheet: Global Summary Card"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from utils import load_global_ev

df = load_global_ev()

print("=== Global EV Summary ===")
print(f"Total Models      : {len(df)}")
print(f"Total Brands      : {df['Brand'].nunique()}")
print(f"Avg Price (EUR)   : {df['PriceEuro'].mean():,.0f}")
print(f"Avg Range (Km)    : {df['Range_Km'].mean():.0f}")
print(f"Avg Top Speed     : {df['TopSpeed_KmH'].mean():.0f} Km/H")
print(f"Avg Efficiency    : {df['Efficiency_WhKm'].mean():.0f} Wh/Km")
print(f"Rapid Charge Yes  : {(df['RapidCharge'] == 'Yes').sum()}")
