import streamlit as st
import pandas as pd

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Afficionado Coffee Analytics",
    page_icon="☕",
    layout="wide"
)

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("outputs/processed_coffee_data.csv")
    return df

df = load_data()

# --------------------------------------------------
# TITLE
# --------------------------------------------------
st.title("☕ Afficionado Coffee Analytics")
st.markdown(
    "### Sales Trends, Store Performance & Time-Based Demand Analysis"
)

st.divider()

# --------------------------------------------------
# SIDEBAR FILTERS
# --------------------------------------------------
st.sidebar.header("🔎 Dashboard Filters")

stores = ["All"] + sorted(df["store_location"].dropna().unique().tolist())
categories = ["All"] + sorted(df["product_category"].dropna().unique().tolist())

selected_store = st.sidebar.selectbox(
    "Store Location",
    stores
)

selected_category = st.sidebar.selectbox(
    "Product Category",
    categories
)

filtered_df = df.copy()

if selected_store != "All":
    filtered_df = filtered_df[
        filtered_df["store_location"] == selected_store
    ]

if selected_category != "All":
    filtered_df = filtered_df[
        filtered_df["product_category"] == selected_category
    ]

# --------------------------------------------------
# KPI CALCULATIONS
# --------------------------------------------------
total_revenue = filtered_df["revenue"].sum()
total_transactions = filtered_df["transaction_id"].nunique()
total_units = filtered_df["transaction_qty"].sum()

avg_transaction = (
    total_revenue / total_transactions
    if total_transactions > 0
    else 0
)

# --------------------------------------------------
# KPI CARDS
# --------------------------------------------------
st.subheader("📌 Business Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "💰 Total Revenue",
    f"${total_revenue:,.2f}"
)

col2.metric(
    "🧾 Transactions",
    f"{total_transactions:,}"
)

col3.metric(
    "📦 Units Sold",
    f"{total_units:,}"
)

col4.metric(
    "💵 Avg Transaction",
    f"${avg_transaction:,.2f}"
)

st.divider()

# --------------------------------------------------
# STORE PERFORMANCE
# --------------------------------------------------
st.subheader("🏪 Store Performance")

store_performance = (
    filtered_df.groupby("store_location")
    .agg(
        Revenue=("revenue", "sum"),
        Units=("transaction_qty", "sum")
    )
    .sort_values("Revenue", ascending=False)
)

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Revenue by Store**")
    st.bar_chart(store_performance["Revenue"])

with col2:
    st.markdown("**Units Sold by Store**")
    st.bar_chart(store_performance["Units"])

st.divider()

# --------------------------------------------------
# CATEGORY PERFORMANCE
# --------------------------------------------------
st.subheader("☕ Product Category Performance")

category_performance = (
    filtered_df.groupby("product_category")
    .agg(
        Revenue=("revenue", "sum"),
        Units=("transaction_qty", "sum")
    )
    .sort_values("Revenue", ascending=False)
)

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Revenue by Category**")
    st.bar_chart(category_performance["Revenue"])

with col2:
    st.markdown("**Units Sold by Category**")
    st.bar_chart(category_performance["Units"])

st.divider()

# --------------------------------------------------
# HOURLY DEMAND
# --------------------------------------------------
st.subheader("⏰ Hourly Demand Analysis")

hourly_sales = (
    filtered_df.groupby("hour")
    .agg(
        Revenue=("revenue", "sum"),
        Transactions=("transaction_id", "nunique")
    )
    .sort_index()
)

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Revenue by Hour**")
    st.line_chart(hourly_sales["Revenue"])

with col2:
    st.markdown("**Transactions by Hour**")
    st.line_chart(hourly_sales["Transactions"])

st.divider()

# --------------------------------------------------
# TOP PRODUCTS
# --------------------------------------------------
st.subheader("🏆 Top 10 Products by Revenue")

top_products = (
    filtered_df.groupby("product_detail")
    .agg(
        Revenue=("revenue", "sum"),
        Units=("transaction_qty", "sum")
    )
    .sort_values("Revenue", ascending=False)
    .head(10)
)

st.dataframe(
    top_products,
    use_container_width=True
)

st.divider()

# --------------------------------------------------
# BUSINESS INSIGHTS
# --------------------------------------------------
st.subheader("💡 Business Insights")

if not filtered_df.empty:

    top_store = (
        filtered_df.groupby("store_location")["revenue"]
        .sum()
        .idxmax()
    )

    top_category = (
        filtered_df.groupby("product_category")["revenue"]
        .sum()
        .idxmax()
    )

    peak_hour = (
        filtered_df.groupby("hour")["transaction_id"]
        .nunique()
        .idxmax()
    )

    st.info(
        f"""
        **Key Findings**

        • 🏪 Highest revenue store: **{top_store}**

        • ☕ Highest revenue category: **{top_category}**

        • ⏰ Peak transaction hour: **{peak_hour}:00**

        • 💰 Total revenue for selected filters:
        **${total_revenue:,.2f}**
        """
    )

st.divider()

# --------------------------------------------------
# RAW DATA
# --------------------------------------------------
with st.expander("📊 View Raw Sales Data"):

    st.dataframe(
        filtered_df,
        use_container_width=True,
        height=500
    )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.caption(
    "Afficionado Coffee Analysis | Data Analytics Project | By Dilip Marella"
)