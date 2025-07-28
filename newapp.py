import streamlit as st
import pandas as pd
import numpy as np

# --- Load Data ---
@st.cache_data
def load_data():
    url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQKkIx5eUS4kACrfiO5_tsWwa0iGBq0GEfNxhdru1hAWWvCb3BxjiqwVeEIlZYEc0PmCUL-wuMDs3ob/pub?gid=0&single=true&output=csv"
    df = pd.read_csv(url)
    df = df.dropna(subset=['Business Name', 'Category', 'Subcategory', 'Zip Code'])
    return df

data = load_data()

# --- Page Setup ---
st.set_page_config(page_title="Loop757", layout="centered")
st.title("🔁 Loop757: Discover Local Gems in the 757")
st.caption("A data-powered tool to close the loop and keep dollars circulating in our community.")

# --- Filter Sidebar ---
st.sidebar.header("📍 Filters")
zip_input = st.sidebar.text_input("Enter ZIP code (optional):")
search_all_zips = st.sidebar.checkbox("Search All ZIP Codes")
category_filter = st.sidebar.selectbox("Select Category", ["All"] + sorted(data["Category"].dropna().unique()))
subcategory_filter = st.sidebar.selectbox("Select Subcategory", ["All"] + sorted(data["Subcategory"].dropna().unique()))
black_owned = st.sidebar.checkbox("Black-Owned Only")
women_owned = st.sidebar.checkbox("Women-Owned Only")
keyword_input = st.sidebar.text_input("🔍 Smart Search (e.g., 'vegan', 'barber', 'mobile')")

# --- Filter Logic ---
filtered_data = data.copy()

if not search_all_zips and zip_input:
    filtered_data = filtered_data[filtered_data["Zip Code"].astype(str).str.contains(zip_input)]

if category_filter != "All":
    filtered_data = filtered_data[filtered_data["Category"] == category_filter]

if subcategory_filter != "All":
    filtered_data = filtered_data[filtered_data["Subcategory"] == subcategory_filter]

if black_owned:
    filtered_data = filtered_data[filtered_data["Black Owned"].str.lower() == "yes"]

if women_owned:
    filtered_data = filtered_data[filtered_data["Women Owned"].str.lower() == "yes"]

if keyword_input:
    keyword = keyword_input.lower()
    mask = (
        data["Business Name"].str.lower().str.contains(keyword)
        | data["Category"].str.lower().str.contains(keyword)
        | data["Subcategory"].str.lower().str.contains(keyword)
        | data.get("Description", pd.Series("")).fillna("").str.lower().str.contains(keyword)
    )
    filtered_data = filtered_data[mask]

# --- Results Display ---
st.markdown("### 💼 Recommended Businesses")
if filtered_data.empty:
    st.warning("No businesses found with the selected filters. Try adjusting your search.")
else:
    for _, row in filtered_data.iterrows():
        st.markdown(f"""
        **{row['Business Name']}**  
        *{row['Category']} — {row['Subcategory']}*  
        ZIP: {row['Zip Code']}  
        {"🖤 Black-Owned" if str(row.get("Black Owned", "")).lower() == "yes" else ""}
        {"🌸 Women-Owned" if str(row.get("Women Owned", "")).lower() == "yes" else ""}
        """)
        st.markdown("---")
