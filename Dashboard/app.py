import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from pathlib import Path

# ── PAGE CONFIG ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Consumer Dynamics Analytics",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── DESIGN TOKENS ─────────────────────────────────────────────────────────────
SIDEBAR_BG  = "#FFFFFF"   # clean white sidebar
ACCENT      = "#DC2626"   # enterprise red
ACCENT_DARK = "#991B1B"
ACCENT_SOFT = "#FEF2F2"
BG          = "#F9FAFB"   # near-white page
CARD_BG     = "#FFFFFF"
BORDER      = "#E5E7EB"
BORDER_MED  = "#D1D5DB"
TEXT_PRI    = "#111827"
TEXT_SEC    = "#6B7280"
TEXT_MUTED  = "#9CA3AF"
CHART_H     = 400

# ── GLOBAL CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"], .stApp {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
}

/* ── SIDEBAR ── */
[data-testid="stSidebar"] {
    background-color: #FFFFFF !important;
    border-right: 1px solid #E5E7EB !important;
}
[data-testid="stSidebar"] * {
    color: #374151 !important;
}
[data-testid="stSidebar"] .stMarkdown h1,
[data-testid="stSidebar"] .stMarkdown h2,
[data-testid="stSidebar"] .stMarkdown h3 {
    color: #111827 !important;
}
[data-testid="stSidebar"] hr {
    border-color: #E5E7EB !important;
}
[data-testid="stSidebar"] .stCheckbox label {
    color: #4B5563 !important;
    font-size: 0.85rem !important;
    font-weight: 500 !important;
}
[data-testid="stSidebar"] .stCheckbox label:hover {
    color: #DC2626 !important;
}

/* ── MAIN PAGE ── */
[data-testid="stAppViewContainer"] {
    background-color: #F9FAFB !important;
}
[data-testid="stHeader"] {
    background-color: #FFFFFF !important;
    border-bottom: 1px solid #E5E7EB !important;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05) !important;
}

/* ── KPI METRIC CARDS ── */
div[data-testid="stMetric"] {
    background: #FFFFFF;
    border: 1px solid #E5E7EB;
    border-radius: 12px;
    padding: 20px 24px;
    box-shadow: 0 1px 4px rgba(0,0,0,0.06);
    position: relative;
    overflow: hidden;
}
div[data-testid="stMetric"]::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: #DC2626;
}
[data-testid="stMetricLabel"] p {
    font-size: 0.72rem !important;
    font-weight: 600 !important;
    color: #6B7280 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.6px !important;
    margin-bottom: 6px !important;
}
[data-testid="stMetricValue"] {
    font-size: 1.75rem !important;
    font-weight: 800 !important;
    color: #111827 !important;
    line-height: 1.1 !important;
}
[data-testid="stMetricDelta"] {
    font-size: 0.78rem !important;
    font-weight: 500 !important;
}

/* ── TABS ── */
.stTabs [data-baseweb="tab-list"] {
    gap: 16px;
    background: #FFFFFF;
    border-bottom: 1px solid #E5E7EB;
    padding: 0 4px;
}
.stTabs [data-baseweb="tab"] {
    background: transparent !important;
    border: none !important;
    color: #6B7280 !important;
    font-size: 0.85rem !important;
    font-weight: 500 !important;
    padding: 12px 18px !important;
    border-radius: 0 !important;
    border-bottom: 2px solid transparent !important;
}
.stTabs [aria-selected="true"] {
    color: #DC2626 !important;
    border-bottom: 2px solid #DC2626 !important;
    font-weight: 600 !important;
    background: transparent !important;
}
.stTabs [data-baseweb="tab-panel"] {
    padding: 24px 0 !important;
}

/* ── CHAPTER HEADER ── */
.chapter-header {
    font-size: 1.35rem;
    font-weight: 700;
    color: #111827;
    margin: 0 0 20px 0;
    padding: 0 0 14px 0;
    border-bottom: 2px solid #F3F4F6;
    display: flex;
    align-items: center;
    gap: 10px;
}
.chapter-header::before {
    content: '';
    display: inline-block;
    width: 4px;
    height: 22px;
    background: #DC2626;
    border-radius: 2px;
    flex-shrink: 0;
}

/* ── CARD ── */
.card {
    background: #FFFFFF;
    border: 1px solid #E5E7EB;
    border-radius: 12px;
    padding: 20px;
    box-shadow: 0 1px 4px rgba(0,0,0,0.05);
    margin-bottom: 16px;
}

/* ── SECTION TITLE ── */
.section-title {
    font-size: 0.78rem;
    font-weight: 700;
    color: #6B7280;
    text-transform: uppercase;
    letter-spacing: 0.7px;
    margin-bottom: 12px;
    padding-bottom: 8px;
    border-bottom: 1px solid #F3F4F6;
}

/* ── OBSERVATION BOX ── */
.insight-narrative {
    background: #FEF2F2;
    border: 1px solid #FECACA;
    border-left: 4px solid #DC2626;
    border-radius: 8px;
    padding: 16px 20px;
    margin: 20px 0 4px 0;
    font-size: 0.88rem;
    line-height: 1.65;
    color: #374151;
}
.insight-narrative b {
    color: #111827;
    font-weight: 700;
}

/* ── DATAFRAME ── */
[data-testid="stDataFrame"] {
    border: 1px solid #E5E7EB !important;
    border-radius: 10px !important;
    overflow: hidden !important;
    font-size: 0.82rem !important;
}

/* ── DOWNLOAD BTN ── */
.stDownloadButton > button {
    background: #FFFFFF !important;
    color: #DC2626 !important;
    border: 1px solid #DC2626 !important;
    border-radius: 8px !important;
    font-size: 0.82rem !important;
    font-weight: 600 !important;
    padding: 10px 18px !important;
    letter-spacing: 0.2px !important;
    transition: all .15s ease !important;
}
.stDownloadButton > button:hover {
    background: #DC2626 !important;
    color: #FFFFFF !important;
}

/* ── DIVIDER ── */
hr {
    border: none !important;
    border-top: 1px solid #E5E7EB !important;
    margin: 24px 0 !important;
}

h1, h2, h3 {
    color: #111827 !important;
    font-weight: 700 !important;
}

/* ── SIDEBAR LABELS ── */
.filter-group-title {
    font-size: 0.68rem;
    font-weight: 700;
    color: #4B5563;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    margin: 16px 0 6px 0;
    display: block;
}

/* ── FOOTER ── */
.footer-bar {
    font-size: 0.75rem;
    color: #9CA3AF;
    display: flex;
    align-items: center;
    gap: 8px;
}
.footer-dot {
    width: 4px; height: 4px;
    background: #DC2626;
    border-radius: 50%;
    display: inline-block;
}
</style>
""", unsafe_allow_html=True)


# ── CHART HELPER ─────────────────────────────────────────────────────────────
def apply_chart_style(fig, height=CHART_H, showscale=False, legend_h=False):
    """Apply unified professional chart styling."""
    fig.update_layout(
        height=height,
        font=dict(family="Inter, Segoe UI, sans-serif", size=11.5, color="#374151"),
        paper_bgcolor="#FFFFFF",
        plot_bgcolor="#FFFFFF",
        margin=dict(l=16, r=16, t=44, b=16),
        title_font=dict(size=14, color="#111827", family="Inter, Segoe UI, sans-serif"),
        title_x=0,
        coloraxis=dict(
            colorbar=dict(title=None, thickness=10, len=0.65, bgcolor="#FFFFFF",
                         borderwidth=0, tickfont=dict(size=10)),
            showscale=showscale
        ),
        xaxis=dict(showgrid=False, zeroline=False, linecolor="#E5E7EB",
                   tickfont=dict(size=11, color="#6B7280"), title_font=dict(color="#6B7280")),
        yaxis=dict(showgrid=True, gridcolor="#F3F4F6", zeroline=False,
                   linecolor="#E5E7EB", tickfont=dict(size=11, color="#6B7280"),
                   title_font=dict(color="#6B7280")),
    )
    if legend_h:
        fig.update_layout(
            legend=dict(orientation="h", yanchor="bottom", y=1.02,
                        xanchor="right", x=1, font=dict(size=10.5),
                        bgcolor="rgba(0,0,0,0)", borderwidth=0)
        )
    fig.update_traces(marker_line_width=0)
    return fig

# ── DATA ENGINE ───────────────────────────────────────────────────────────────
@st.cache_data
def load_and_process_data():
    data_path = Path(__file__).parent.parent / "shopping_trends.csv"
    
    if not data_path.exists():
        data_path = Path("shopping_trends.csv")
        
    df = pd.read_csv(data_path)

    freq_values = {
        "Weekly": 52, "Fortnightly": 26, "Bi-Weekly": 26,
        "Monthly": 12, "Every 3 Months": 4, "Quarterly": 4, "Annually": 1
    }
    df["Freq_Num"]       = df["Frequency of Purchases"].map(freq_values)
    df["Annual Revenue"] = df["Freq_Num"] * df["Purchase Amount (USD)"]

    state_to_code = {
        'Alabama':'AL','Alaska':'AK','Arizona':'AZ','Arkansas':'AR','California':'CA',
        'Colorado':'CO','Connecticut':'CT','Delaware':'DE','Florida':'FL','Georgia':'GA',
        'Hawaii':'HI','Idaho':'ID','Illinois':'IL','Indiana':'IN','Iowa':'IA',
        'Kansas':'KS','Kentucky':'KY','Louisiana':'LA','Maine':'ME','Maryland':'MD',
        'Massachusetts':'MA','Michigan':'MI','Minnesota':'MN','Mississippi':'MS','Missouri':'MO',
        'Montana':'MT','Nebraska':'NE','Nevada':'NV','New Hampshire':'NH','New Jersey':'NJ',
        'New Mexico':'NM','New York':'NY','North Carolina':'NC','North Dakota':'ND','Ohio':'OH',
        'Oklahoma':'OK','Oregon':'OR','Pennsylvania':'PA','Rhode Island':'RI','South Carolina':'SC',
        'South Dakota':'SD','Tennessee':'TN','Texas':'TX','Utah':'UT','Vermont':'VT',
        'Virginia':'VA','Washington':'WA','West Virginia':'WV','Wisconsin':'WI','Wyoming':'WY'
    }
    df["State_Code"] = df["Location"].map(state_to_code)

    sub_map = {"Yes": 1, "No": 0}
    df["Sub_Binary"] = df["Subscription Status"].map(sub_map)
    conditions = [
        (df["Sub_Binary"] == 1) | (df["Previous Purchases"] > 25),
        (df["Promo Code Used"] == "Yes") | (df["Previous Purchases"] < 10)
    ]
    df["Segment"]    = np.select(conditions, ["Loyal", "Deal Hunter"], default="Regular")
    vip_thr          = df["Annual Revenue"].quantile(0.9)
    df["VIP_Status"] = (df["Annual Revenue"] > vip_thr).map({True: "VIP", False: "Standard"})
    df["Age Group"]  = pd.cut(df["Age"], bins=[0, 30, 60, 100], labels=["Youth", "Adult", "Senior"])
    return df

try:
    df_raw = load_and_process_data()
except Exception as e:
    st.error(f"Data Engine Error: {e}")
    st.stop()


# ── SIDEBAR ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='padding: 8px 0 20px 0;'>
        <div style='font-size:1.05rem;font-weight:800;color:#111827;letter-spacing:-0.3px;'>
            Strategic Control Center
        </div>
        <div style='font-size:0.72rem;color:#6B7280;margin-top:4px;font-weight:500;'>
            Consumer Dynamics Analytics
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")

    st.markdown('<span class="filter-group-title">Season</span>', unsafe_allow_html=True)
    all_seasons = sorted(df_raw["Season"].unique())
    sel_season  = [s for s in all_seasons if st.checkbox(s, value=True, key=f"s_{s}")]

    st.markdown('<span class="filter-group-title">Category</span>', unsafe_allow_html=True)
    all_cats = sorted(df_raw["Category"].unique())
    sel_cat  = [c for c in all_cats if st.checkbox(c, value=True, key=f"c_{c}")]

    st.markdown('<span class="filter-group-title">Shipping Type</span>', unsafe_allow_html=True)
    all_ships = sorted(df_raw["Shipping Type"].unique())
    sel_ship  = [sh for sh in all_ships if st.checkbox(sh, value=True, key=f"sh_{sh}")]

    st.markdown("---")


# ── FILTER DATA ───────────────────────────────────────────────────────────────
df = df_raw[
    df_raw["Season"].isin(sel_season) &
    df_raw["Category"].isin(sel_cat) &
    df_raw["Shipping Type"].isin(sel_ship)
]

if df.empty:
    st.warning("No records match the current filters. Adjust your selections to continue.")
    st.stop()


# ── HEADER ────────────────────────────────────────────────────────────────────
st.markdown("""
<div style='padding: 8px 0 20px 0; text-align: center;'>
    <div style='font-size:1.8rem;font-weight:800;color:#111827;letter-spacing:-0.5px;'>
        Consumer Dynamics &amp; Market Performance Analytics
    </div>
    <div style='font-size:0.9rem;color:#6B7280;margin-top:6px;font-weight:400;'>
        Executive Production
    </div>
</div>
""", unsafe_allow_html=True)
st.markdown("---")


# ── TABS ──────────────────────────────────────────────────────────────────────
tabs = st.tabs([
    "Market Velocity",
    "Ecosystem & Logistics",
    "Segment Archetypes",
    "Demographic Yield",
])


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CHAPTER 1 — MARKET VELOCITY
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tabs[0]:
    st.markdown('<p class="chapter-header">Market Velocity</p>', unsafe_allow_html=True)

    # KPI Row
    k1, k2, k3, k4 = st.columns(4)
    total_rev  = df["Purchase Amount (USD)"].sum()
    annual_val = df["Annual Revenue"].sum()
    avg_rating = df["Review Rating"].mean()
    vip_pct    = (df["VIP_Status"] == "VIP").mean() * 100
    k1.metric("Transaction Revenue", f"${total_rev:,.0f}")
    k2.metric("Annual Portfolio Value", f"${annual_val:,.0f}")
    k3.metric("Brand Satisfaction", f"{avg_rating:.2f} / 5.0")
    k4.metric("VIP Penetration", f"{vip_pct:.1f}%")

    st.markdown("<br>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<p class="section-title">Portfolio Segment Performance</p>', unsafe_allow_html=True)
        pivot_df = df.groupby("Segment")["Purchase Amount (USD)"].agg(["count","mean","sum"]).reset_index()
        pivot_df.columns = ["Segment", "Orders", "Avg Ticket (USD)", "Revenue (USD)"]
        pivot_df["Avg Ticket (USD)"] = pivot_df["Avg Ticket (USD)"].round(2)
        pivot_df["Revenue (USD)"]    = pivot_df["Revenue (USD)"].astype(int)
        pivot_df = pivot_df.sort_values("Revenue (USD)", ascending=False)
        st.dataframe(pivot_df, use_container_width=True, hide_index=True)

    with c2:
        st.markdown('<p class="section-title">Top 3 VIP Accounts</p>', unsafe_allow_html=True)
        top_vips = (
            df.sort_values("Annual Revenue", ascending=False)
            .head(3)[["Customer ID", "Annual Revenue", "Segment", "Location"]]
            .assign(**{"Annual Revenue": lambda x: x["Annual Revenue"].astype(int)})
        )
        st.dataframe(top_vips, use_container_width=True, hide_index=True)

    top_seg = pivot_df.iloc[0]["Segment"]
    st.markdown(f"""
    <div class="insight-narrative">
        <b>Observation:</b> Portfolio analysis shows a total transaction revenue of <b>${total_rev:,.0f}</b>
        across <b>{len(df):,}</b> transactions. The <b>{top_seg}</b> customer archetype leads in revenue
        contribution, with a VIP penetration rate of <b>{vip_pct:.1f}%</b> indicating strong high-value
        customer retention.
    </div>
    """, unsafe_allow_html=True)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CHAPTER 2 — ECOSYSTEM & LOGISTICS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tabs[1]:
    st.markdown('<p class="chapter-header">Ecosystem & Logistics</p>', unsafe_allow_html=True)

    state_revenue = df.groupby(["State_Code","Location"])["Purchase Amount (USD)"].sum().reset_index()
    top_state     = state_revenue.sort_values("Purchase Amount (USD)").iloc[-1]["Location"]
    best_ship     = df.groupby("Shipping Type")["Review Rating"].mean().idxmax()

    c3, c4 = st.columns([3, 2])
    with c3:
        st.markdown('<p class="section-title">Geospatial Revenue Contribution</p>', unsafe_allow_html=True)
        fig_map = px.choropleth(
            state_revenue, locations="State_Code", locationmode="USA-states",
            color="Purchase Amount (USD)", scope="usa",
            hover_name="Location",
            title="Geospatial Revenue Heatmap",
            color_continuous_scale="Reds",
            labels={"Purchase Amount (USD)": "Revenue (USD)"},
        )
        fig_map.update_layout(
            height=CHART_H,
            margin=dict(l=0, r=0, t=40, b=0),
            paper_bgcolor="#FFFFFF",
            geo=dict(bgcolor="#FFFFFF", lakecolor="#F9FAFB",
                     showlakes=True, showframe=False),
            font=dict(family="Inter, Segoe UI, sans-serif"),
            coloraxis=dict(colorbar=dict(title=None, thickness=10, len=0.65, bgcolor="#FFFFFF",
                                        borderwidth=0, tickfont=dict(size=10))),
        )
        fig_map.update_traces(marker_line_color="#FFFFFF", marker_line_width=0.5)
        st.plotly_chart(fig_map, use_container_width=True)

    with c4:
        st.markdown('<p class="section-title">Shipment Rating Matrix — Top 10</p>', unsafe_allow_html=True)
        ship_matrix = (
            df.pivot_table(index="Location", columns="Shipping Type",
                           values="Review Rating", aggfunc="mean")
            .reset_index()
        )
        if "Express" in ship_matrix.columns:
            ship_matrix = ship_matrix.sort_values("Express", ascending=False).head(10)
        st.dataframe(ship_matrix.round(2), use_container_width=True, hide_index=True)

    st.markdown("---")
    st.markdown('<p class="section-title">Logistic Impact — Shipping Method vs Customer Rating</p>', unsafe_allow_html=True)
    ship_rating = df.groupby(["Review Rating","Shipping Type"]).size().reset_index(name="Orders")
    fig_impact = px.bar(
        ship_rating, x="Review Rating", y="Orders", color="Shipping Type", barmode="group",
        title="Fulfillment Method Impact on Satisfaction Ratings",
        color_discrete_sequence=["#DC2626","#B91C1C","#7F1D1D","#FCA5A5","#FEE2E2","#991B1B"],
        labels={"Orders": "No. of Orders", "Review Rating": "Customer Rating (1–5)"},
    )
    apply_chart_style(fig_impact, height=360, legend_h=True)
    st.plotly_chart(fig_impact, use_container_width=True)

    st.markdown(f"""
    <div class="insight-narrative">
        <b>Observation:</b> <b>{top_state}</b> leads all states in revenue contribution.
        The <b>{best_ship}</b> shipping method delivers the highest average customer satisfaction score,
        making it the preferred fulfillment channel for high-value customer segments.
    </div>
    """, unsafe_allow_html=True)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CHAPTER 3 — SEGMENT ARCHETYPES
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tabs[2]:
    st.markdown('<p class="chapter-header">Segment Archetypes & Style Cycles</p>', unsafe_allow_html=True)

    vips     = df[df["VIP_Status"] == "VIP"]
    vip_cats = vips["Category"].value_counts().reset_index()
    top_vip_cat = vips["Category"].value_counts().idxmax()

    seasonal_trend        = df.groupby(["Season","Color"]).size().reset_index(name="Count")
    most_color_per_season = (
        seasonal_trend.sort_values(["Season","Count"], ascending=[True,False])
        .groupby("Season").head(1)
        .copy()
    )
    most_color_per_season.columns = ["Season","Most Color","Volume"]
    top_color  = most_color_per_season.iloc[0]["Most Color"]
    top_season = most_color_per_season.iloc[0]["Season"]

    c5, c6 = st.columns(2)
    with c5:
        st.markdown('<p class="section-title">VIP Category Preference</p>', unsafe_allow_html=True)
        fig5 = px.bar(
            vip_cats, x="count", y="Category", orientation="h",
            title="Dominant Product Categories Among VIPs",
            color="count", color_continuous_scale="Reds",
            labels={"count": "VIP Customers"},
        )
        apply_chart_style(fig5, showscale=False)
        st.plotly_chart(fig5, use_container_width=True)

    with c6:
        st.markdown('<p class="section-title">Peak Style Selection by Season</p>', unsafe_allow_html=True)
        fig6 = px.bar(
            most_color_per_season, x="Season", y="Volume",
            title="Seasonal Color Trend Dominance",
            color="Volume", hover_data={"Most Color": True, "Volume": True},
            color_continuous_scale="Reds",
            labels={"Volume": "Purchase Volume"},
        )
        apply_chart_style(fig6, showscale=False)
        st.plotly_chart(fig6, use_container_width=True)

    st.markdown('<p class="section-title">Dominant Color by Season</p>', unsafe_allow_html=True)
    st.dataframe(most_color_per_season, use_container_width=True, hide_index=True)

    st.markdown(f"""
    <div class="insight-narrative">
        <b>Observation:</b> VIP customers exhibit a strong preference for the <b>{top_vip_cat}</b> category.
        The style trend analysis confirms <b>{top_color}</b> as the leading color choice
        in the <b>{top_season}</b> period — a key signal for inventory planning and targeted promotions.
    </div>
    """, unsafe_allow_html=True)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CHAPTER 4 — DEMOGRAPHIC YIELD
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tabs[3]:
    st.markdown('<p class="chapter-header">Demographic Yield & Senior Insights</p>', unsafe_allow_html=True)

    age_yield     = df.groupby("Age Group", observed=False)["Purchase Amount (USD)"].sum().reset_index()
    top_age_group = age_yield.sort_values("Purchase Amount (USD)").iloc[-1]["Age Group"]
    seniors       = df[df["Age Group"] == "Senior"]
    senior_trends = seniors.groupby(["Season","Category"]).size().reset_index(name="Count")
    senior_top_cat    = seniors["Category"].value_counts().idxmax()
    senior_top_season = seniors["Season"].value_counts().idxmax()

    c7, c8 = st.columns(2)
    with c7:
        st.markdown('<p class="section-title">Revenue Yield by Demographic Cluster</p>', unsafe_allow_html=True)
        fig7 = px.bar(
            age_yield, x="Age Group", y="Purchase Amount (USD)",
            title="Total Revenue by Demographic Cohort",
            color="Purchase Amount (USD)", color_continuous_scale="Reds",
            labels={"Purchase Amount (USD)": "Total Revenue (USD)"},
        )
        apply_chart_style(fig7, showscale=False)
        st.plotly_chart(fig7, use_container_width=True)

    with c8:
        st.markdown('<p class="section-title">Senior Consumer — Seasonal Category Trends</p>', unsafe_allow_html=True)
        fig8 = px.bar(
            senior_trends, x="Season", y="Count", color="Category", barmode="group",
            title="Category Preferences by Season (Senior Segment)",
            color_discrete_sequence=["#DC2626","#B91C1C","#7F1D1D","#FCA5A5"],
            labels={"Count": "No. of Purchases"},
        )
        apply_chart_style(fig8, legend_h=True)
        st.plotly_chart(fig8, use_container_width=True)

    st.markdown(f"""
    <div class="insight-narrative">
        <b>Observation:</b> The <b>{top_age_group}</b> demographic cluster generates the highest revenue yield.
        Among Senior consumers, <b>{senior_top_cat}</b> is the most purchased category,
        with peak activity in the <b>{senior_top_season}</b> season —
        presenting a clear opportunity for targeted seasonal campaigns.
    </div>
    """, unsafe_allow_html=True)


# ── FOOTER ────────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #6B7280; font-size: 0.85rem; padding: 20px 0;">
    Consumer Dynamics & Market Performance Analytics&nbsp;&nbsp;|&nbsp;&nbsp;Executive Production&nbsp;&nbsp;|&nbsp;&nbsp;Developed by <strong style="color: #DC2626;">Adel Badran</strong> — AI Engineer
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
col_fl, col_fm, col_fr = st.columns([2, 1, 2])
with col_fm:
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("Export Report", csv, "consumer_dynamics_report.csv", "text/csv", use_container_width=True)
