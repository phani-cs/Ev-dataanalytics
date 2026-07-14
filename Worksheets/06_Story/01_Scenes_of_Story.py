"""Story: Scenes of Story — run key worksheet insights in sequence."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from utils import load_global_ev, load_india_ev, load_charging_stations

global_ev = load_global_ev()
india = load_india_ev()
charging = load_charging_stations()

print("=" * 50)
print("SCENES OF STORY — EV Data Analytics")
print("=" * 50)

print("\n--- Scene 1: Global Market ---")
print(f"Models: {len(global_ev)} | Brands: {global_ev['Brand'].nunique()}")
print(f"Avg Price: €{global_ev['PriceEuro'].mean():,.0f} | Avg Range: {global_ev['Range_Km'].mean():.0f} Km")

print("\n--- Scene 2: Pricing Insight ---")
top_brand = global_ev.groupby("Brand")["PriceEuro"].mean().idxmax()
cheap_brand = global_ev.groupby("Brand")["PriceEuro"].mean().idxmin()
print(f"Most expensive brand (avg): {top_brand}")
print(f"Most affordable brand (avg): {cheap_brand}")

print("\n--- Scene 3: Performance ---")
fastest = global_ev.loc[global_ev["TopSpeed_KmH"].idxmax()]
print(f"Fastest: {fastest['Brand']} {fastest['Model']} — {fastest['TopSpeed_KmH']} Km/H")

print("\n--- Scene 4: India EV Market ---")
print(f"Models: {len(india)}")
print(f"Price range: {india['Price_Lakhs'].min()} – {india['Price_Lakhs'].max()} Lakhs")
print(f"Best range: {india.loc[india['Range_Km'].idxmax(), 'Car']} ({india['Range_Km'].max():.0f} Km)")

print("\n--- Scene 5: Charging Infrastructure ---")
print(f"Stations: {len(charging)} across {charging['Region'].nunique()} regions")
print("Top region:", charging.groupby("Region").size().idxmax())

print("\n--- End of Story ---")
