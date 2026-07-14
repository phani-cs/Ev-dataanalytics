"""
EV Data Analytics — interactive website
Run:  streamlit run app.py
"""
from pathlib import Path
import sys

import pandas as pd
import plotly.express as px
import streamlit as st

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "Worksheets"))
from utils import (  # noqa: E402
    load_global_ev,
    load_india_ev,
    load_cheapest_ev,
    load_charging_stations,
)

st.set_page_config(
    page_title="EV Data Analytics",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---- theme polish ----
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;600;700&family=Space+Grotesk:wght@500;700&display=swap');
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
h1, h2, h3 { font-family: 'Space Grotesk', sans-serif !important; }
.block-container { padding-top: 1.5rem; }
div[data-testid="stMetricValue"] { font-size: 1.6rem; }
</style>
""",
    unsafe_allow_html=True,
)


@st.cache_data
def get_data():
    return {
        "global": load_global_ev(),
        "india": load_india_ev(),
        "cheap": load_cheapest_ev(),
        "charging": load_charging_stations(),
    }


data = get_data()
global_ev = data["global"]
india = data["india"]
cheap = data["cheap"]
charging = data["charging"]

# ---- sidebar ----
st.sidebar.title("⚡ EV Analytics")
page = st.sidebar.radio(
    "Navigate",
    [
        "Home",
        "Datasets",
        "Pricing",
        "Performance",
        "Market & Segments",
        "Charging",
        "India EVs",
        "Story",
    ],
)
st.sidebar.markdown("---")
st.sidebar.caption("4 datasets · interactive charts · publishable web app")

# ============================================================
if page == "Home":
    st.title("EV Data Analytics")
    st.markdown("Interactive analytics for electric vehicles — pricing, performance, market segments, and charging infrastructure.")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Global EV models", len(global_ev))
    c2.metric("India EV models", len(india))
    c3.metric("Cheapest EV DB", len(cheap))
    c4.metric("Charging stations", len(charging))

    st.markdown("### Datasets overview")
    d1, d2 = st.columns(2)
    with d1:
        st.info("**1. ElectricCarData_Clean** — 103 global models with price, range, efficiency, powertrain")
        st.info("**2. EVIndia** — 12 India EV models with price (Lakhs), range, boot space")
    with d2:
        st.info("**3. Cheapestelectriccars-EVDatabase** — ~180 EVs with UK/Germany pricing & drive type")
        st.info("**4. electric_vehicle_charging_station_list** — 50 stations across Indian regions")

    st.markdown("### Quick insight")
    fig = px.scatter(
        global_ev,
        x="Range_Km",
        y="PriceEuro",
        color="Brand",
        hover_data=["Model"],
        title="Price vs Range (Global EVs)",
        labels={"Range_Km": "Range (Km)", "PriceEuro": "Price (EUR)"},
    )
    fig.update_layout(height=420, showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

# ============================================================
elif page == "Datasets":
    st.title("All 4 Datasets")
    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "1 · ElectricCarData_Clean",
            "2 · EVIndia",
            "3 · Cheapest EVs",
            "4 · Charging Stations",
        ]
    )
    with tab1:
        st.caption(f"{len(global_ev)} rows · Data/ElectricCarData_Clean.csv")
        st.dataframe(global_ev, use_container_width=True, height=420)
    with tab2:
        st.caption(f"{len(india)} rows · Data/EVIndia.csv")
        st.dataframe(india, use_container_width=True, height=420)
    with tab3:
        st.caption(f"{len(cheap)} rows · Data/Cheapestelectriccars-EVDatabase.csv")
        st.dataframe(cheap, use_container_width=True, height=420)
    with tab4:
        st.caption(f"{len(charging)} rows · Data/electric_vehicle_charging_station_list.csv")
        st.dataframe(charging, use_container_width=True, height=420)

# ============================================================
elif page == "Pricing":
    st.title("Pricing")
    col1, col2 = st.columns(2)

    with col1:
        avg = global_ev.groupby("Brand", as_index=False)["PriceEuro"].mean().sort_values("PriceEuro", ascending=False)
        fig = px.bar(avg, x="Brand", y="PriceEuro", title="Average Price by Brand (€)", color="PriceEuro", color_continuous_scale="Blues")
        fig.update_layout(xaxis_tickangle=-45, showlegend=False, height=400)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = px.scatter(global_ev, x="Range_Km", y="PriceEuro", color="Segment", hover_name="Model",
                         title="Price vs Range", labels={"Range_Km": "Range (Km)", "PriceEuro": "Price (EUR)"})
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)

    col3, col4 = st.columns(2)
    with col3:
        cheapest = cheap.dropna(subset=["Price_Germany"]).nsmallest(12, "Price_Germany")
        fig = px.bar(cheapest, x="Price_Germany", y="Name", orientation="h", title="Cheapest Cars (Germany €)",
                     labels={"Price_Germany": "Price (EUR)", "Name": ""})
        fig.update_layout(height=450, yaxis={"categoryorder": "total ascending"})
        st.plotly_chart(fig, use_container_width=True)

    with col4:
        fig = px.bar(india.sort_values("Price_Lakhs"), x="Price_Lakhs", y="Car", orientation="h",
                     title="Price by Car — India (Lakhs)", labels={"Price_Lakhs": "Price (Lakhs)", "Car": ""},
                     color="Price_Lakhs", color_continuous_scale="Oranges")
        fig.update_layout(height=450, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

# ============================================================
elif page == "Performance":
    st.title("Performance")
    col1, col2 = st.columns(2)

    with col1:
        top = global_ev.nlargest(15, "TopSpeed_KmH").copy()
        top["Label"] = top["Brand"] + " " + top["Model"]
        fig = px.bar(top, x="TopSpeed_KmH", y="Label", orientation="h", title="Top Speed — Fastest 15",
                     labels={"TopSpeed_KmH": "Km/H", "Label": ""})
        fig.update_layout(height=450, yaxis={"categoryorder": "total ascending"})
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        speed = global_ev.groupby("Brand", as_index=False)["TopSpeed_KmH"].max().sort_values("TopSpeed_KmH", ascending=False)
        fig = px.bar(speed, x="Brand", y="TopSpeed_KmH", title="Max Top Speed by Brand", labels={"TopSpeed_KmH": "Km/H"})
        fig.update_layout(xaxis_tickangle=-45, height=450)
        st.plotly_chart(fig, use_container_width=True)

    col3, col4 = st.columns(2)
    with col3:
        fig = px.scatter(global_ev, x="Efficiency_WhKm", y="Range_Km", color="Segment", hover_name="Model",
                         title="Range vs Efficiency", labels={"Efficiency_WhKm": "Wh/Km", "Range_Km": "Range (Km)"})
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)

    with col4:
        fc = global_ev.dropna(subset=["FastCharge_KmH"]).nlargest(12, "FastCharge_KmH").copy()
        fc["Label"] = fc["Brand"] + " " + fc["Model"]
        fig = px.bar(fc, x="FastCharge_KmH", y="Label", orientation="h", title="Fast Charging — Top 12",
                     labels={"FastCharge_KmH": "Km/H equiv.", "Label": ""})
        fig.update_layout(height=400, yaxis={"categoryorder": "total ascending"})
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Drive type (Cheapest EV database)")
    drive = cheap["Drive"].value_counts().reset_index()
    drive.columns = ["Drive", "Count"]
    fig = px.pie(drive, names="Drive", values="Count", title="Drive Type Distribution", hole=0.35)
    st.plotly_chart(fig, use_container_width=True)

# ============================================================
elif page == "Market & Segments":
    st.title("Market & Segments")
    col1, col2 = st.columns(2)

    with col1:
        counts = global_ev.groupby("Brand", as_index=False)["Model"].count().rename(columns={"Model": "Models"})
        counts = counts.sort_values("Models", ascending=False)
        fig = px.bar(counts, x="Brand", y="Models", title="Number of Models by Brand")
        fig.update_layout(xaxis_tickangle=-45, height=400)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        seg = global_ev["Segment"].value_counts().reset_index()
        seg.columns = ["Segment", "Count"]
        fig = px.pie(seg, names="Segment", values="Count", title="Segment Distribution", hole=0.35)
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)

    col3, col4 = st.columns(2)
    with col3:
        body = global_ev.groupby(["Brand", "BodyStyle"]).size().reset_index(name="Count")
        fig = px.bar(body, x="Brand", y="Count", color="BodyStyle", title="Brand by BodyStyle")
        fig.update_layout(xaxis_tickangle=-45, height=420)
        st.plotly_chart(fig, use_container_width=True)

    with col4:
        pt = global_ev.groupby(["Brand", "PowerTrain"]).size().reset_index(name="Count")
        fig = px.bar(pt, x="Brand", y="Count", color="PowerTrain", title="Brand by PowerTrain")
        fig.update_layout(xaxis_tickangle=-45, height=420)
        st.plotly_chart(fig, use_container_width=True)

    eff = global_ev.groupby("Brand", as_index=False)["Efficiency_WhKm"].mean().nsmallest(10, "Efficiency_WhKm")
    fig = px.bar(eff, x="Efficiency_WhKm", y="Brand", orientation="h",
                 title="Top 10 Most Efficient Brands (lower Wh/Km = better)",
                 labels={"Efficiency_WhKm": "Avg Wh/Km", "Brand": ""})
    fig.update_layout(height=400, yaxis={"categoryorder": "total descending"})
    st.plotly_chart(fig, use_container_width=True)

# ============================================================
elif page == "Charging":
    st.title("Charging Infrastructure")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Stations", len(charging))
    c2.metric("Regions", charging["Region"].nunique())
    c3.metric("Charger types", charging["Charger_Type"].nunique())
    c4.metric("Avg power (kW)", f"{charging['Power_kW'].mean():.0f}")

    col1, col2 = st.columns(2)
    with col1:
        by_region = charging.groupby("Region", as_index=False).size().rename(columns={"size": "Stations"})
        fig = px.bar(by_region, x="Region", y="Stations", title="Charging Stations by Region", color="Stations",
                     color_continuous_scale="Oranges")
        fig.update_layout(showlegend=False, height=380)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        by_type = charging["Charger_Type"].value_counts().reset_index()
        by_type.columns = ["Charger_Type", "Count"]
        fig = px.pie(by_type, names="Charger_Type", values="Count", title="Stations by Charger Type", hole=0.35)
        fig.update_layout(height=380)
        st.plotly_chart(fig, use_container_width=True)

    col3, col4 = st.columns(2)
    with col3:
        mix = charging.groupby(["Region", "Charger_Type"]).size().reset_index(name="Count")
        fig = px.bar(mix, x="Region", y="Count", color="Charger_Type", title="Charger Type by Region")
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)

    with col4:
        fig = px.histogram(charging, x="Power_kW", nbins=10, title="Charging Power Distribution",
                           labels={"Power_kW": "Power (kW)"})
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("EV Charging Stations Map")
    fig = px.scatter_mapbox(
        charging,
        lat="Latitude",
        lon="Longitude",
        color="Region",
        size="Power_kW",
        hover_name="Station_Name",
        hover_data=["City", "Charger_Type", "Power_kW", "Operator"],
        zoom=4,
        height=520,
        mapbox_style="open-street-map",
        title="Charging stations across India",
    )
    st.plotly_chart(fig, use_container_width=True)

    st.dataframe(charging, use_container_width=True, height=280)

# ============================================================
elif page == "India EVs":
    st.title("India EV Market")
    col1, col2 = st.columns(2)
    with col1:
        fig = px.bar(india.sort_values("Range_Km"), x="Range_Km", y="Car", orientation="h",
                     title="Range Comparison", labels={"Range_Km": "Range (Km)", "Car": ""}, color="Range_Km",
                     color_continuous_scale="Teal")
        fig.update_layout(height=420, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        fig = px.bar(india.sort_values("BootSpace_L"), x="BootSpace_L", y="Car", orientation="h",
                     title="Boot Space", labels={"BootSpace_L": "Litres", "Car": ""}, color="BootSpace_L",
                     color_continuous_scale="Purples")
        fig.update_layout(height=420, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Catalogue")
    st.dataframe(
        india[["Car", "Style", "VehicleType", "Range", "PriceRange(Lakhs)", "Capacity", "BootSpace", "BaseModel", "TopModel"]],
        use_container_width=True,
    )

# ============================================================
elif page == "Story":
    st.title("Scenes of Story")
    st.markdown("A guided walkthrough of the key EV insights.")

    with st.expander("Scene 1 — Global Market", expanded=True):
        st.write(
            f"**{len(global_ev)} models** across **{global_ev['Brand'].nunique()} brands**. "
            f"Average price **€{global_ev['PriceEuro'].mean():,.0f}**, average range "
            f"**{global_ev['Range_Km'].mean():.0f} km**."
        )

    with st.expander("Scene 2 — Pricing Insight", expanded=True):
        top_brand = global_ev.groupby("Brand")["PriceEuro"].mean().idxmax()
        cheap_brand = global_ev.groupby("Brand")["PriceEuro"].mean().idxmin()
        st.write(f"Most expensive brand (avg): **{top_brand}**. Most affordable (avg): **{cheap_brand}**.")

    with st.expander("Scene 3 — Performance", expanded=True):
        fastest = global_ev.loc[global_ev["TopSpeed_KmH"].idxmax()]
        st.write(f"Fastest model: **{fastest['Brand']} {fastest['Model']}** — {fastest['TopSpeed_KmH']} km/h.")

    with st.expander("Scene 4 — India EV Market", expanded=True):
        best = india.loc[india["Range_Km"].idxmax()]
        st.write(
            f"**{len(india)} India EVs**, priced **{india['Price_Lakhs'].min()}–{india['Price_Lakhs'].max()} Lakhs**. "
            f"Best range: **{best['Car']}** ({best['Range_Km']:.0f} km)."
        )

    with st.expander("Scene 5 — Charging Infrastructure", expanded=True):
        top_region = charging.groupby("Region").size().idxmax()
        st.write(
            f"**{len(charging)} stations** across **{charging['Region'].nunique()} regions**. "
            f"Leading region: **{top_region}**."
        )
