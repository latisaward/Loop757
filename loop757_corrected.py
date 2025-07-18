import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

data = {"Business Name": ["Pretty Strategic, LLC", "DaChef’s Catering & Co.", "Pretty Ambitious LLC", "BPRE", "The SnoBall Shop", "Carte Brunch", "House of Salvage", "Lady's Fingers Health Spa | Massage Therapy", "Hearts-N-Hones Home Care Agency", "Str8 Up Slushed", "I Got A Love Jones Events", "TaxGuru Financial & Public Services", "Tax Boss Academy", "Montego Island Grill", "Stivas Kitchen", "Admire Curves", "NailsbyKeandra", "Versus Salon", "The Happy Hour Hostess", "Desmond’s Island Soul Grill", "Made In Norfolk", "Author- I Remember When", "Bar 9", "Lookout4 1 Records LLC.", "Alodeuri Artisan Jewelry", "Desmond’s Island Soul Grill", "Earthy Child"],
"Category": ["Professional & Business Services", "Food & Beverage", "Retail & Product-Based", "Professional & Business Services", "Food & Beverage", "Food & Beverage", "Retail & Product-Based", "Health & Wellness", "Health & Wellness", "Food & Beverage", "Events & Experiences", "Professional & Business Services", "Career & Skill Services", "Food & Beverage", "Food & Beverage", "Fitness & Body", "Beauty & Grooming", "Beauty & Grooming", "Events & Experiences", "Food & Beverage", "Retail & Product-Based", "Retail & Product-Based", "Food & Beverage", "Events & Experiences", "Retail & Product-Based", "Food & Beverage", "Retail & Product-Based"],
"Subcategory": ["Consultant", "Private Chef", "Boutique / Apparel Store", "Consultant", "Restaurant", "Restaurant", "Boutique / Apparel Store", "Massage Therapist", "Home Health Aide", "Bartending Service", "Event Planner", "Financial Advisor / Tax Pro", "Career Coach", "Restaurant", "Catering Service", "Personal Trainer", "Nail Tech", "Hair Stylist", "Event Planner", "Restaurant", "Boutique / Apparel Store", "Online Store / E-commerce", "Restaurant", "DJ / Live Music", "Mobile Vending Retailer", "Restaurant", "Product Maker (Candles, Soaps, etc.)"],
"Zipcode": [23435, 23666, 23523, 23794, 23454, 23707, 23320, 23502, 22452, 23352, 23523, 23523, 23523, 23452, 23503, 23462, 23703, 23462, 23455, 23464, 23509, 23513, 23702, 23504, 23504, 23464, 23661],
"Instagram or Website": ["@prettystrategicllc", "Instagram.com/dachef", "@missprettyambitious_", "www.bpreal.estate", "@thesnoballshop", "www.cartebrunch.com", "@HouseofSalvage", "@ladysfingersllc", "www.hearts-n-homes.com", "@Str8_up_slushed", "Igotalovejonesevents.com", "www.taxguru4you.net", "www.mytaxboss.net", "montegogrill.com ", "www.StivasKitchen.com", "@AdmireCurvesBodysculpting ", "https://nailsbykeandrasade.glossgenius.com/", "https://www.versussalon.com/", "https://thehappyhourhostess.com/", "https://desmonds-island-soul-grill.square.site/", "Www.madeinnorfolkapparel.com", "@Moddagoat96", "@Bar9portsmouthVa", "@Lookout4_1", "www.instagram.com/alodeuri", "@desmondsislandsoulgrill", "Instagram.com/the_earthy_child"],
"Black Owned": [1]*27, "Mobile": [1,1,1,0,1,0,1,0,0,1,1,0,0,0,1,0,0,0,0,0,1,1,1,1,1,0,0],
"Kid Friendly": [0,1,0,0,1,1,1,1,0,0,0,1,1,1,1,0,0,1,0,1,1,0,1,1,0,1,1],
"Vegan Friendly": [0,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,0,0,1,0,1,1,0],
"Women Owned": [1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,0,1,0,1,1,1],
"Search Corpus": ["" for _ in range(27)]
}
df = pd.DataFrame(data)

# Load live Google Sheet with refresh cache
@st.cache_data(ttl=60)  # refresh every 60 seconds
def load_data():
    url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQKkIx5eUS4kACrfiO5_tsWwa0iGBq0GEfNxhdru1hAWWvCb3BxjiqwVeEIlZYEc0PmCUL-wuMDs3ob/pubhtml?gid=0&single=true"
    return pd.read_csv(url)

df = load_data()

st.set_page_config(page_title='Loop757', layout='centered')
st.markdown("""<style>body {background: linear-gradient(135deg, #d4fc79 0%, #96e6a1 100%);font-family: 'Arial', sans-serif;} h1 {color: #3b3b3b;} .stTextInput input, .stButton>button {border-radius: 10px;} </style>""", unsafe_allow_html=True)
st.title('❤️ Loop757: Discover Local Gems')
st.caption('Your guide to the 757’s Black-owned, women-led, mobile, vegan, and family-friendly businesses.')

components.html("""<script>navigator.geolocation.getCurrentPosition(function(pos) {var lat = pos.coords.latitude;var lon = pos.coords.longitude;fetch(`https://nominatim.openstreetmap.org/reverse?format=json&lat=${lat}&lon=${lon}`).then(res => res.json()).then(data => {const zip = data.address.postcode;const input = window.parent.document.querySelector('input[type=text]');if (zip && input && !input.value) {input.value = zip;const event = new Event('input', { bubbles: true });input.dispatchEvent(event);}});});</script>""", height=0)

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

results = df.copy()
if query.strip():
    q = query.lower()
    results = results[df['Business Name'].str.lower().str.contains(q, na=False) | df['Category'].str.lower().str.contains(q, na=False) | df['Subcategory'].str.lower().str.contains(q, na=False)]
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

if query or black_owned or women_owned or mobile or kid_friendly or vegan_friendly or (not search_all and user_zip.strip()):
    st.subheader('📋 Matching Recommendations')
    if not results.empty:
        for _, row in results.iterrows():
            st.markdown(f"### {row['Business Name']}")
            st.markdown(f"📂 **{row['Category']} > {row['Subcategory']}**")
            st.markdown(f"📍 ZIP: {row['Zipcode']}")
            link = str(row['Instagram or Website']).strip()
            if link:
                if link.startswith("@" or ""):
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
