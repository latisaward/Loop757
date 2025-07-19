
import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import streamlit.components.v1 as components

# Google Sheets setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scope)
client = gspread.authorize(creds)
sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1vQKkIx5eUS4kACrfiO5_tsWwa0iGBq0GEfNxhdru1hAWWvCb3BxjiqwVeEIlZYEc0PmCUL-wuMDs3ob/edit")
worksheet = sheet.sheet1
data = worksheet.get_all_records()
df = pd.DataFrame(data)

# Streamlit config and styling
st.set_page_config(page_title='Loop757', layout='centered')
st.markdown("""<style>body {background: linear-gradient(135deg, #d4fc79 0%, #96e6a1 100%);font-family: 'Arial', sans-serif;} h1 {color: #3b3b3b;} .stTextInput input, .stButton>button {border-radius: 10px;} </style>""", unsafe_allow_html=True)
st.title('❤️ Loop757: Discover Local Gems')
st.caption('Your guide to the 757’s Black-owned, women-led, mobile, vegan, and family-friendly businesses.')

# Auto ZIP from geolocation
components.html("""
<script>
navigator.geolocation.getCurrentPosition(function(pos) {
    var lat = pos.coords.latitude;
    var lon = pos.coords.longitude;
    fetch(`https://nominatim.openstreetmap.org/reverse?format=json&lat=${lat}&lon=${lon}`)
        .then(res => res.json())
        .then(data => {
            const zip = data.address.postcode;
            const input = window.parent.document.querySelector('input[type=text]');
            if (zip && input && !input.value) {
                input.value = zip;
                const event = new Event('input', { bubbles: true });
                input.dispatchEvent(event);
            }
        });
});
</script>
""", height=0)

user_zip = st.text_input('Enter ZIP code')
search_all = st.checkbox('Search all ZIP codes', value=(user_zip.strip() == ''))
st.subheader('🔍 What are you looking for?')
query = st.text_input('Search by keyword (e.g. "vegan", "chef", "barber")')

st.subheader('🎯 Filter Your Preferences')
black_owned = st.checkbox('Black-owned')
women_owned = st.checkbox('Women-owned')
mobile = st.checkbox('Mobile')
kid_friendly = st.checkbox('Kid-friendly')
vegan_friendly = st.checkbox('Vegan-friendly')

# Normalize column headers
df.columns = df.columns.str.strip()

# Apply filters
results = df.copy()
if query.strip():
    q = query.lower()
    results = results[
        results['Business Name'].str.lower().str.contains(q, na=False) |
        results['Business Category'].str.lower().str.contains(q, na=False) |
        results['Instagram or Website'].str.lower().str.contains(q, na=False)
    ]
if black_owned:
    results = results[results['Is this a Black-owned business or service?'].str.lower() == 'yes']
if women_owned:
    results = results[results['Select all that apply. (Woman-owned)'] == True]
if mobile:
    results = results[results['Select all that apply. (Mobile)'] == True]
if kid_friendly:
    results = results[results['Select all that apply. (Kid-friendly)'] == True]
if vegan_friendly:
    results = results[results['Select all that apply. (Vegan-friendly)'] == True]
if not search_all and user_zip.strip():
    results = results[results['Zip code'].astype(str).str.contains(user_zip.strip(), case=False)]

# Display results
if query or black_owned or women_owned or mobile or kid_friendly or vegan_friendly or (not search_all and user_zip.strip()):
    st.subheader('📋 Matching Recommendations')
    if not results.empty:
        for _, row in results.iterrows():
            st.markdown(f"### {row['Business Name']}")
            st.markdown(f"📂 **{row['Business Category']}**")
            st.markdown(f"📍 ZIP: {row['Zip code']}")
            link = str(row['Instagram or Website']).strip()
            if link:
                if link.startswith('@'):
                    link = "https://www.instagram.com/" + link[1:]
                elif not link.startswith("http"):
                    link = "https://" + link
                st.markdown(f"🔗 [Visit Website or Instagram]({link})", unsafe_allow_html=True)
            tags = []
            if row['Is this a Black-owned business or service?'].lower() == 'yes': tags.append('🖤 Black-Owned')
            if row['Select all that apply. (Woman-owned)']: tags.append('👩 Women-Owned')
            if row['Select all that apply. (Mobile)']: tags.append('🚗 Mobile')
            if row['Select all that apply. (Vegan-friendly)']: tags.append('🌱 Vegan-Friendly')
            if row['Select all that apply. (Kid-friendly)']: tags.append('👶 Kid-Friendly')
            if tags: st.markdown(' | '.join(tags))
            st.markdown('---')
    else:
        st.warning('No results found. Try a different keyword or filter combination.')
else:
    st.info('Enter a keyword or apply filters to find businesses.')
