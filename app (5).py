import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

# Load your live Google Sheet
sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQKkIx5eUS4kACrfiO5_tsWwa0iGBq0GEfNxhdru1hAWWvCb3BxjiqwVeEIlZYEc0PmCUL-wuMDs3ob/pub?output=csv"
df = pd.read_csv(sheet_url)

st.set_page_config(page_title='Loop757', layout='centered')
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #d4fc79 0%, #96e6a1 100%);
    font-family: 'Arial', sans-serif;
}
h1 { color: #3b3b3b; }
.stTextInput input, .stButton>button { border-radius: 10px; }
</style>
""", unsafe_allow_html=True)

st.title('❤️ Loop757: Discover Local Gems')
st.caption("Love where you live. Discover the best of the 757 — from beauty and bites to pop-ups and parties.")

# Enable ZIP auto-detection
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

# Inputs
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

# Filtering
results = df.copy()
if query.strip():
    q = query.lower()
    results = results[
        df['Business Name'].str.lower().str.contains(q, na=False) |
        df['Category'].str.lower().str.contains(q, na=False) |
        df['Subcategory'].str.lower().str.contains(q, na=False)
    ]

if black_owned:
    results = results[results['Black Owned'] == 1]
if women_owned:
    results = results[results['Women Owned'] == 1]
if mobile:
    results = results[results['Mobile'] == 1]
if kid_friendly:
    results = results[results['Kid Friendly'] == 1]
if vegan_friendly:
    results = results[results['Vegan Friendly'] == 1]
if not search_all and user_zip.strip():
    results = results[results['Zipcode'].astype(str).str.contains(user_zip.strip(), case=False)]

# Output
if query or black_owned or women_owned or mobile or kid_friendly or vegan_friendly or (not search_all and user_zip.strip()):
    st.subheader('📋 Matching Recommendations')
    if not results.empty:
        for _, row in results.iterrows():
            st.markdown(f"### {row['Business Name']}")
            st.markdown(f"📂 **{row['Category']} > {row['Subcategory']}**")
            st.markdown(f"📍 ZIP: {row['Zipcode']}")

            # Format IG or website field
            link = str(row['Instagram or Website']).strip()
            if link:
                if "instagram.com" in link.lower():
                    if not link.lower().startswith("http"):
                        link = "https://" + link
                elif link.startswith("@"):
                    link = "https://www.instagram.com/" + link[1:]
                elif not link.startswith("http"):
                    link = "https://" + link
                st.markdown(f"🔗 [Visit Website or Instagram]({link})", unsafe_allow_html=True)

            tags = []
            if row['Black Owned']: tags.append('🖤 Black-Owned')
            if row['Women Owned']: tags.append('👩 Women-Owned')
            if row['Mobile']: tags.append('🚗 Mobile')
            if row['Vegan Friendly']: tags.append('🌱 Vegan-Friendly')
            if row['Kid Friendly']: tags.append('👶 Kid-Friendly')
            if tags: st.markdown(' | '.join(tags))
            st.markdown('---')
    else:
        st.warning('No results found. Try a different keyword or filter combination.')
else:
    st.info('Enter a keyword or apply filters to find businesses.')

