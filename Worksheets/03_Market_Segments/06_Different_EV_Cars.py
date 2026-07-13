"""Worksheet: Different EV Cars (India catalogue)"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from utils import load_india_ev

df = load_india_ev()[["Car", "Style", "VehicleType", "Range", "PriceRange(Lakhs)", "Capacity", "BootSpace"]]
print("Different EV Cars — India\n")
print(df.to_string(index=False))
