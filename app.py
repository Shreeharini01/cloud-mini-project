import streamlit as st
import pandas as pd
import plotly.express as px

# PAGE SETTINGS
st.set_page_config(
    page_title="GlowCare Beauty Analytics",
    page_icon="💄",
    layout="wide"
)

# CUSTOM CSS
st.markdown("""
<style>

/* BACKGROUND */
.stApp {
    background: linear-gradient(to right, #ffe0f7, #fff4b5, #e5ccff);
}

/* MAIN TEXT */
html, body, [class*="css"] {
    color: #4a004d !important;
    font-weight: bold;
}

/* HEADINGS */
h1 {
    text-align: center;
    color: #d1006f !important;
    font-size: 55px;
    font-weight: 900;
}

h2, h3 {
    color: #7b1fa2 !important;
    font-weight: bold;
}

/* PRODUCT TITLES */
h3 {
    font-size: 28px !important;
}

/* LABELS */
label, p, div, span {
    color: #5a005a !important;
    font-weight: bold !important;
}

/* METRICS */
[data-testid="metric-container"] {
    background-color: rgba(255,255,255,0.8);
    border: 3px solid #ff4da6;
    padding: 20px;
    border-radius: 20px;
    color: #4a004d !important;
}

/* DATAFRAME */
[data-testid="stDataFrame"] {
    background-color: white;
    border-radius: 15px;
    color: black !important;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background-color: #ffd6f6;
}

/* BUTTONS */
.stButton>button {
    background-color: #ff4da6;
    color: white !important;
    border-radius: 12px;
    font-weight: bold;
    border: none;
}

/* SLIDERS */
.stSlider label {
    color: #7a007a !important;
    font-size: 18px !important;
}

/* SLIDER NUMBERS */
[data-baseweb="slider"] {
    color: #4a004d !important;
}

</style>
""", unsafe_allow_html=True)

# TITLE
st.title("💖 GlowCare Beauty Analytics Dashboard")

st.markdown("## 🌸 Interactive Cosmetic Product Analysis")

# PRODUCTS
products = [
    "Cleanser",
    "Serum",
    "Moisturizer",
    "Sunscreen",
    "Face Wash"
]

ratings = []
sales = []
reviews = []

# INPUT SECTION
for product in products:

    st.subheader(f"✨ {product}")

    col1, col2, col3 = st.columns(3)

    with col1:
        rating = st.slider(
            f"{product} Rating",
            1,
            10,
            5,
            key=f"rating_{product}"
        )

    with col2:
        sale = st.slider(
            f"{product} Sales",
            100,
            5000,
            1500,
            key=f"sales_{product}"
        )

    with col3:
        review = st.slider(
            f"{product} Reviews",
            10,
            1000,
            200,
            key=f"review_{product}"
        )

    ratings.append(rating)
    sales.append(sale)
    reviews.append(review)

# DATAFRAME
data = pd.DataFrame({
    "Products": products,
    "Ratings": ratings,
    "Sales": sales,
    "Reviews": reviews
})

# METRICS
avg_rating = round(sum(ratings) / len(ratings), 2)

st.markdown("---")

m1, m2, m3 = st.columns(3)

m1.metric("⭐ Average Rating", avg_rating)
m2.metric("💰 Total Sales", sum(sales))
m3.metric("📝 Total Reviews", sum(reviews))

st.markdown("---")

# BAR CHART
st.subheader("📊 Product Ratings")

fig1 = px.bar(
    data,
    x="Products",
    y="Ratings",
    color="Products",
    text="Ratings",
    color_discrete_sequence=[
        "#ff4da6",
        "#ffcc00",
        "#cc66ff",
        "#ff6699",
        "#ff9933"
    ]
)

fig1.update_layout(
    plot_bgcolor="#fff5fd",
    paper_bgcolor="#fff5fd",
    font_color="#4a004d"
)

st.plotly_chart(fig1, use_container_width=True)

# LINE CHART
st.subheader("📈 Monthly Sales Analysis")

fig2 = px.line(
    data,
    x="Products",
    y="Sales",
    markers=True
)

fig2.update_traces(
    line=dict(color="#ff1493", width=5)
)

fig2.update_layout(
    plot_bgcolor="#fff8dc",
    paper_bgcolor="#fff8dc",
    font_color="#4a004d"
)

st.plotly_chart(fig2, use_container_width=True)

# PIE CHART
st.subheader("🥧 Customer Review Distribution")

fig3 = px.pie(
    data,
    names="Products",
    values="Reviews",
    color_discrete_sequence=[
        "#ff66c4",
        "#ffd54f",
        "#ba68c8",
        "#f06292",
        "#ffb74d"
    ],
    hole=0.4
)

fig3.update_layout(
    paper_bgcolor="#fef6ff",
    font_color="#4a004d"
)

st.plotly_chart(fig3, use_container_width=True)

# SCATTER CHART
st.subheader("🔥 Product Performance Comparison")

fig4 = px.scatter(
    data,
    x="Ratings",
    y="Sales",
    size="Reviews",
    color="Products",
    size_max=60,
    color_discrete_sequence=[
        "#ff1493",
        "#ffcc00",
        "#ba68c8",
        "#ff7043",
        "#ab47bc"
    ]
)

fig4.update_layout(
    plot_bgcolor="#fff0f5",
    paper_bgcolor="#fff0f5",
    font_color="#4a004d"
)

st.plotly_chart(fig4, use_container_width=True)

# RECOMMENDATION SECTION
st.markdown("---")

st.subheader("🧴 Personalized Skincare Recommendation")

skin = st.selectbox(
    "Choose Your Skin Type",
    [
        "Dry Skin",
        "Oily Skin",
        "Combination Skin",
        "Sensitive Skin"
    ]
)

if skin == "Dry Skin":
    st.success("💧 Recommended: Hyaluronic Serum & Moisturizer")

elif skin == "Oily Skin":
    st.success("✨ Recommended: Oil-Free Cleanser & Gel Sunscreen")

elif skin == "Combination Skin":
    st.success("🌼 Recommended: Vitamin C Serum & Face Wash")

else:
    st.success("🌸 Recommended: Gentle Cleanser & Fragrance-Free Cream")

# TABLE
st.markdown("---")

st.subheader("📋 Product Dataset")

st.dataframe(data)

# ANIMATION
st.balloons()
