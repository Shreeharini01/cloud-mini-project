import streamlit as st
import pandas as pd

st.set_page_config(page_title="Skincare Dashboard", layout="wide")

st.title("💄 Skincare Product Analysis Dashboard")

products = ["Cleanser", "Serum", "Moisturizer", "Sunscreen", "Face Wash"]

ratings = []

st.markdown("## Rate the skincare products")

col1, col2 = st.columns(2)

with col1:
    for product in products[:3]:
        rating = st.slider(f"{product} Rating", 1, 10, 5)
        ratings.append(rating)

with col2:
    for product in products[3:]:
        rating = st.slider(f"{product} Rating", 1, 10, 5)
        ratings.append(rating)

data = pd.DataFrame({
    "Products": products,
    "Ratings": ratings
})

average = sum(ratings) / len(ratings)

st.markdown("---")

c1, c2 = st.columns(2)

c1.metric("Average Rating", round(average, 2))
c2.metric("Top Rating", max(ratings))

st.markdown("---")

col3, col4 = st.columns(2)

with col3:
    st.subheader("📋 Product Ratings Table")
    st.dataframe(data)

with col4:
    st.subheader("📊 Ratings Bar Chart")
    st.bar_chart(data.set_index("Products"))

st.subheader("📈 Ratings Line Chart")
st.line_chart(data.set_index("Products"))

st.subheader("🧴 Skin Type Recommendation")

skin = st.selectbox(
    "Choose your skin type",
    ["Dry Skin", "Oily Skin", "Combination Skin", "Sensitive Skin"]
)

if skin == "Dry Skin":
    st.success("Recommended: Moisturizer and Hydrating Serum")
elif skin == "Oily Skin":
    st.success("Recommended: Oil-free Cleanser and Gel Moisturizer")
elif skin == "Combination Skin":
    st.success("Recommended: Balanced Face Wash and Sunscreen")
else:
    st.success("Recommended: Gentle Cleanser and Fragrance-free Products")

st.balloons()
