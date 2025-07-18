
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Loop757", layout="wide")

# Load live Google Sheet
csv_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQKkIx5eUS4kACrfiO5_tsWwa0iGBq0GEfNxhdru1hAWWvCb3BxjiqwVeEIlZYEc0PmCUL-wuMDs3ob/pub?output=csv"
try:
    df = pd.read_csv(csv_url)
except Exception as e:
    st.error("⚠️ Could not load data from Google Sheets.")
    st.stop()

st.title("Loop757")
st.subheader("Your guide to the 757’s Black-owned, women-led, mobile, vegan, family-friendly businesses — and events too!")

# --- Filters ---
st.sidebar.header("Search & Filters")
search_input = st.sidebar.text_input("What are you looking for?")
zip_code = st.sidebar.text_input("ZIP Code")
search_all_zip = st.sidebar.checkbox("Search all ZIP codes")
black_owned = st.sidebar.checkbox("Black-owned only")
women_owned = st.sidebar.checkbox("Women-owned only")
mobile = st.sidebar.checkbox("Mobile business")
vegan = st.sidebar.checkbox("Vegan-friendly")
kid_friendly = st.sidebar.checkbox("Kid-friendly")

# --- Filtering Logic ---
def matches_filters(business):
    if black_owned and not str(business.get("Black Owned", "")).strip().lower() == "yes":
        return False
    if women_owned and not str(business.get("Women Owned", "")).strip().lower() == "yes":
        return False
    if mobile and not str(business.get("Mobile", "")).strip().lower() == "yes":
        return False
    if vegan and not str(business.get("Vegan Friendly", "")).strip().lower() == "yes":
        return False
    if kid_friendly and not str(business.get("Kid Friendly", "")).strip().lower() == "yes":
        return False
    if not search_all_zip and zip_code and str(business.get("ZIP Code", "")).strip() != zip_code:
        return False
    if search_input:
        query = search_input.lower()
        fields = [
            "Business Name", "Category", "Subcategory", "Description",
            "Instagram or Website"
        ]
        if not any(query in str(business.get(field, "")).lower() for field in fields):
            return False
    return True

# --- Display Results ---
results = df[df.apply(matches_filters, axis=1)]

if not results.empty:
    for _, business in results.iterrows():
        st.markdown("---")
        st.subheader(business.get("Business Name", "Unnamed"))
        st.write(f"📍 ZIP Code: {business.get('ZIP Code', 'N/A')}")
        st.write(f"📂 Category: {business.get('Category', '')} → {business.get('Subcategory', '')}")
        st.write(f"📝 Description: {business.get('Description', '')}")

        # Format and display website/Instagram link
        link = str(business.get("Instagram or Website", "")).strip()
        if link:
            if link.startswith("@"):
                link = "https://www.instagram.com/" + link[1:]
            elif not link.startswith("http"):
                link = "https://" + link
            st.markdown(f"[Visit Website or Instagram]({link})", unsafe_allow_html=True)
else:
    st.warning("No matching results found.")
