"""Worksheet: Charging Summary Card"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from utils import load_sample_charging

df = load_sample_charging()

print("=== Charging Network Summary ===")
print(f"Total Stations    : {len(df)}")
print(f"Regions           : {df['Region'].nunique()}")
print(f"Charger Types     : {df['ChargerType'].nunique()}")
print(f"Avg Power (kW)    : {df['Power_kW'].mean():.0f}")
print(f"Max Power (kW)    : {df['Power_kW'].max()}")
print(f"Min Power (kW)    : {df['Power_kW'].min()}")
