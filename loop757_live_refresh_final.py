import streamlit as st
import pandas as pd
import requests
from io import StringIO

# --- Auto-refresh every 60 seconds ---
st.experimental_rerun()

# --- Load CSV from Google Sheets ---
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQKkIx5eUS4kACrfiO5_tsWwa0iGBq0GEfNxhdru1hAWWvCb3BxjiqwVeEIlZYEc0PmCUL-wuMDs3ob/pub?gid=0&single=true&output=csv"
response = requests.get(url)
data = StringIO(response.text)
df = pd.read_csv(data)

# --- Clean column names ---
df.columns = df.columns.str.strip().str.replace('\n', ' ').str.replace(r'\s+', ' ', regex=True)

# --- Combine all subcategory columns into one 'Subcategory' column ---
subcategory_cols = [col for col in df.columns if col.startswith("Subcategory")]
df["Subcategory"] = df[subcategory_cols].bfill(axis=1).iloc[:, 0]

# --- Format Instagram or Website field ---
def format_link(x):
    x = str(x).strip()
    if x.startswith("@"):
        return f"https://instagram.com/{x[1:]}"
    elif "instagram.com" in x or "http" in x:
        return x if x.startswith("http") else f"https://{x}"
    elif "." in x:
        return f"https://{x}"
    return x

df["Formatted Link"] = df["Instagram or Website"].apply(format_link)

# --- Search Box ---
q = st.text_input("Search businesses by name, category, or subcategory").strip().lower()

# --- Filter based on query ---
if q:
    results = df[
        df['Business Name'].str.lower().str.contains(q, na=False) |
        df['Business Category'].str.lower().str.contains(q, na=False) |
        df['Subcategory'].str.lower().str.contains(q, na=False)
    ]
else:
    results = df.copy()

# --- Display results ---
for _, row in results.iterrows():
    st.markdown(f"### {row['Business Name']}")
    st.markdown(f"**Category:** {row['Business Category']}")
    st.markdown(f"**Subcategory:** {row['Subcategory']}")
    st.markdown(f"**ZIP Code:** {row['Zip code']}")
    st.markdown(f"[Visit Business]({row['Formatted Link']})")
    st.markdown("---")
