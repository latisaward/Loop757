import streamlit as st
import pandas as pd

# Auto-refresh every 60 seconds
st.experimental_rerun_interval = 60

# Google Sheet CSV link
csv_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQKkIx5eUS4kACrfiO5_tsWwa0iGBq0GEfNxhdru1hAWWvCb3BxjiqwVeEIlZYEc0PmCUL-wuMDs3ob/pub?gid=0&single=true&output=csv"

# Load and clean data
@st.cache_data(ttl=60)
def load_data():
    df = pd.read_csv(csv_url)
    df.columns = df.columns.str.strip().str.replace(r'\s+', ' ', regex=True).str.replace('"', '').str.replace('\n', '').str.strip()
    return df

df = load_data()

st.title("Loop757: Small Biz Recommender")

# Smart search bar
q = st.text_input("Search by business name, category, or subcategory").strip().lower()

if q:
    results = df[
        df['Business Name'].str.lower().str.contains(q, na=False) |
        df['Business Category'].str.lower().str.contains(q, na=False) |
        df.filter(like='Subcategory').apply(lambda x: x.str.lower().str.contains(q, na=False)).any(axis=1)
    ]
else:
    results = df

st.write(f"Showing {len(results)} businesses")

# Show selected results in a cleaner format
for _, row in results.iterrows():
    st.markdown(f"""
    ### {row['Business Name']}
    **Category:** {row.get('Business Category', 'N/A')}  
    **Subcategory:** {', '.join([str(row[c]) for c in df.columns if 'Subcategory' in c and pd.notnull(row[c])])}  
    **Zip Code:** {row.get('Zip code', 'N/A')}  
    **Black-owned:** {row.get('Is this a Black-owned business or service?', 'N/A')}  
    **Instagram/Website:** {row.get('Instagram or Website', 'N/A')}
    ---
    """)

