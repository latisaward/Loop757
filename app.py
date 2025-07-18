
import streamlit as st
import pandas as pd
from difflib import get_close_matches
from geopy.distance import geodesic

# --- Streamlit Setup ---
st.set_page_config(page_title="Loop757", layout="centered")

st.markdown("""
<style>
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        font-weight: bold;
        border-radius: 8px;
    }
    .stTextInput>div>input {
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

# --- Sample Data ---
data = {
    'Business Name': ['Taste of Soul', 'Glow Hair Studio', 'Vegan Vibes Café', 'Kidz Kare Mobile Cuts'],
    'Category': ['Food & Beverage', 'Beauty & Grooming', 'Food & Beverage', 'Beauty & Grooming'],
    'Subcategory': ['Restaurant', 'Hair Stylist', 'Vegan', 'Mobile Barber'],
    'Zipcode': ['23504', '23462', '23456', '23320'],
    'Latitude': [36.851, 36.837, 36.794, 36.761],
    'Longitude': [-76.285, -76.133, -76.071, -76.231],
    'Black Owned': ['Yes', 'Yes', 'No', 'Yes'],
    'Women Owned': ['No', 'Yes', 'Yes', 'No'],
    'Mobile': ['No', 'No', 'No', 'Yes'],
    'Kid Friendly': ['Yes', 'Yes', 'Yes', 'Yes'],
    'Vegan Friendly': ['No', 'No', 'Yes', 'No']
}
df = pd.DataFrame(data)

binary_cols = ['Black Owned', 'Women Owned', 'Mobile', 'Kid Friendly', 'Vegan Friendly']
df[binary_cols] = df[binary_cols].applymap(lambda x: 1 if x == 'Yes' else 0)
df['Search Corpus'] = (df['Business Name'] + ' ' + df['Category'] + ' ' + df['Subcategory']).str.lower()

# --- App UI ---
st.title("📍 Loop757: Discover Local Gems")
st.caption("Smart local business recommendations based on your vibe and location.")

# --- Location ---
st.subheader("📌 Set Your Location")
user_lat = st.number_input("Latitude", value=36.85, step=0.001)
user_lon = st.number_input("Longitude", value=-76.29, step=0.001)
radius = st.slider("Search Radius (miles)", 0, 50, 10)
search_all = st.checkbox("Search all across the 757", value=False)

# --- Smart Search ---
st.subheader("🔍 What are you looking for?")
query = st.text_input("Try keywords like 'vegan food', 'barber', or 'soul food'")

# --- Logic ---
def is_within_radius(row, user_loc, r):
    return geodesic(user_loc, (row['Latitude'], row['Longitude'])).miles <= r

if query:
    matches = get_close_matches(query.lower(), df['Search Corpus'], n=5, cutoff=0.3)
    results = df[df['Search Corpus'].isin(matches)]
else:
    results = df.copy()

if not search_all:
    user_location = (user_lat, user_lon)
    results = results[results.apply(lambda row: is_within_radius(row, user_location, radius), axis=1)]

# --- Results ---
st.subheader("📋 Recommendations")
if not results.empty:
    for _, row in results.iterrows():
        st.markdown(f'''
**{row["Business Name"]}**  
🏷️ {row["Category"]} > {row["Subcategory"]}  
📍 Zip: {row["Zipcode"]}  
🖤 Black Owned: {'✅' if row["Black Owned"] else '❌'}  
🌱 Vegan Friendly: {'✅' if row["Vegan Friendly"] else '❌'}  
🚗 Mobile: {'✅' if row["Mobile"] else '❌'}
''')
else:
    st.info("No matches found. Try a different keyword or adjust your filters.")
