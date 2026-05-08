import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="GlowCare Dashboard",
    page_icon="💄",
    layout="wide"
)

st.markdown("""
<style>
.main {
    background-color: #fff0f5;
}

h1 {
    color: #ff1493;
    text-align: center;
}

h2, h3 {
    color: #c71585;
}

.stMetric {
    background-color: #ffe4e1;
    padding: 15px;
    border-radius: 15px;
}
</style>
""", unsafe_allow_html=True)

st.title("💖 GlowCare Cosmetic Analytics Dashboard")

products = [
    "Cleanser",
    "Serum",
    "Moisturizer",
    "Sunscreen",
    "Face Wash"
]

ratings = []
sales = []

st.markdown("## 🌸 Product Ratings")

col1, col2 = st.columns(2)

with col1:
    for product in products[:3]:
        rating = st.slider(f"{product} Rating", 1, 10, 5)
        ratings.append(rating)

with col2:
    for product in products[3:]:
        rating = st.slider(f"{product} Rating", 1, 10, 5)
        ratings.append(rating)

st.markdown("## 💰 Monthly Sales")

for product in products:
    sale = st.slider(f"{product} Sales", 100, 1000, 500)
    sales.append(sale)

data = pd.DataFrame({
    "Products": products,
    "Ratings": ratings,
    "Sales": sales
})

average = sum(ratings) / len(ratings)

st.markdown("---")

m1, m2, m3 = st.columns(3)

m1.metric("⭐ Average Rating", round(average, 2))
m2.metric("🏆 Highest Rating", max(ratings))
m3.metric("💰 Total Sales", sum(sales))

st.markdown("---")

c1, c2 = st.columns(2)

with c1:
    st.subheader("📋 Product Data")
    st.dataframe(data)

with c2:
    st.subheader("📊 Ratings Bar Chart")
    st.bar_chart(data.set_index("Products")["Ratings"])

st.subheader("📈 Sales Line Chart")
st.line_chart(data.set_index("Products")["Sales"])

st.subheader("📉 Ratings Area Chart")
st.area_chart(data.set_index("Products")["Ratings"])

st.subheader("🥧 Product Comparison")
st.bar_chart(data.set_index("Products"))

st.subheader("🧴 Skin Type Recommendation")

skin = st.selectbox(
    "Choose Skin Type",
    ["Dry Skin", "Oily Skin", "Combination Skin", "Sensitive Skin"]
)

if skin == "Dry Skin":
    st.success("💧 Recommended: Hydrating Moisturizer")
elif skin == "Oily Skin":
    st.success("✨ Recommended: Oil-free Cleanser")
elif skin == "Combination Skin":
    st.success("🌼 Recommended: Sunscreen + Serum")
else:
    st.success("🌸 Recommended: Gentle Face Wash")

st.snow()

st.markdown(
    "<h2 style='text-align:center; color:#ff69b4;'>✨ Glow Naturally with Confidence ✨</h2>",
    unsafe_allow_html=True
)
