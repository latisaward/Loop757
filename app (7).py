
import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

data = {"Business Name": ["Pretty Strategic, LLC", "DaChef\u2019s Catering & Co.", "Pretty Ambitious LLC", "BPRE", "The SnoBall Shop", "Carte Brunch", "House of Salvage", "Lady's Fingers Health Spa | Massage Therapy", "Hearts-N-Hones Home Care Agency", "Str8 Up Slushed", "I Got A Love Jones Events", "TaxGuru Financial & Public Services", "Tax Boss Academy", "Montego Island Grill", "Stivas Kitchen", "Admire Curves", "NailsbyKeandra", "Versus Salon", "The Happy Hour Hostess", "Desmond\u2019s Island Soul Grill", "Made In Norfolk", "Author- I Remember When", "Bar 9", "Lookout4 1 Records LLC.", "Alodeuri Artisan Jewelry", "Desmond\u2019s Island Soul Grill", "Earthy Child"], "Category": ["Professional & Business Services", "Food & Beverage", "Retail & Product-Based", "Professional & Business Services", "Food & Beverage", "Food & Beverage", "Retail & Product-Based", "Health & Wellness", "Health & Wellness", "Food & Beverage", "Events & Experiences", "Professional & Business Services", "Career & Skill Services", "Food & Beverage", "Food & Beverage", "Fitness & Body", "Beauty & Grooming", "Beauty & Grooming", "Events & Experiences", "Food & Beverage", "Retail & Product-Based", "Retail & Product-Based", "Food & Beverage", "Events & Experiences", "Retail & Product-Based", "Food & Beverage", "Retail & Product-Based"], "Subcategory": ["Consultant", "Private Chef", "Boutique / Apparel Store", "Consultant", "Restaurant", "Restaurant", "Boutique / Apparel Store", "Massage Therapist", "Home Health Aide", "Bartending Service", "Event Planner", "Financial Advisor / Tax Pro", "Career Coach", "Restaurant", "Catering Service", "Personal Trainer", "Nail Tech", "Hair Stylist", "Event Planner", "Restaurant", "Boutique / Apparel Store", "Online Store / E-commerce", "Restaurant", "DJ / Live Music", "Mobile Vending Retailer", "Restaurant", "Product Maker (Candles, Soaps, etc.)"], "Zipcode": [23435, 23666, 23523, 23794, 23454, 23707, 23320, 23502, 22452, 23352, 23523, 23523, 23523, 23452, 23503, 23462, 23703, 23462, 23455, 23464, 23509, 23513, 23702, 23504, 23504, 23464, 23661], "Instagram or Website": ["@prettystrategicllc", "Instagram.com/dachef", "@missprettyambitious_", "www.bpreal.estate", "@thesnoballshop", "www.cartebrunch.com", "HouseofSalvage", "Ladysfingers.info (website) and ladysfingersllc (IG)", "www.hearts-n-homes.com", "Str8upslushed", "Igotalovejonesevents.com", "www.taxguru4you.net", "www.mytaxboss.net", "montegogrill.com ", "www.StivasKitchen.com", "Admire Curves Body sculpting ", "https://nailsbykeandrasade.glossgenius.com/", "https://www.versussalon.com/", "https://thehappyhourhostess.com/", "https://desmonds-island-soul-grill.square.site/", "Www.madeinnorfolkapparel.com", "Moddagoat96", "Bar9 portsmouth Va", "@Lookout4_1", "www.alodeuri.com www.instagram.com/alodeuri", "IG/desmondsislandsoulgrill", "Instagram.com/the_earthy_child"], "Black Owned": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1], "Mobile": [1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0], "Kid Friendly": [0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1], "Vegan Friendly": [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0], "Women Owned": [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1], "Search Corpus": ["pretty strategic, llc professional & business services consultant", "dachef\u2019s catering & co. food & beverage private chef", "pretty ambitious llc retail & product-based boutique / apparel store", "bpre professional & business services consultant", "the snoball shop food & beverage restaurant", "carte brunch food & beverage restaurant", "house of salvage retail & product-based boutique / apparel store", "lady's fingers health spa | massage therapy health & wellness massage therapist", "hearts-n-hones home care agency health & wellness home health aide", "str8 up slushed food & beverage bartending service", "i got a love jones events events & experiences event planner", "taxguru financial & public services professional & business services financial advisor / tax pro", "tax boss academy career & skill services career coach", "montego island grill food & beverage restaurant", "stivas kitchen food & beverage catering service", "admire curves fitness & body personal trainer", "nailsbykeandra beauty & grooming nail tech", "versus salon beauty & grooming hair stylist", "the happy hour hostess events & experiences event planner", "desmond\u2019s island soul grill food & beverage restaurant", "made in norfolk retail & product-based boutique / apparel store", "author- i remember when retail & product-based online store / e-commerce", "bar 9 food & beverage restaurant", "lookout4 1 records llc. events & experiences dj / live music", "alodeuri artisan jewelry retail & product-based mobile vending retailer", "desmond\u2019s island soul grill food & beverage restaurant", "earthy child retail & product-based product maker (candles, soaps, etc.)"]}
df = pd.DataFrame(data)

st.set_page_config(page_title="Loop757", layout="centered")

st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #d4fc79 0%, #96e6a1 100%);
    font-family: 'Arial', sans-serif;
}
h1 {
    color: #3b3b3b;
}
.stTextInput input, .stButton>button {
    border-radius: 10px;
}
.card {
    background-color: #ffffffdd;
    padding: 1rem;
    margin-bottom: 1rem;
    border-left: 6px solid #f85a8b;
    border-radius: 12px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.05);
}
</style>
""", unsafe_allow_html=True)

st.title("❤️ Loop757: Discover Local Gems")
st.caption("Your go-to guide for finding local, Black-owned, women-led, mobile, vegan, and kid-friendly businesses in the 757.")

# Inject JS for location prompt
components.html("""
<script>
navigator.geolocation.getCurrentPosition(
    function(pos) {
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
    }
);
</script>
""", height=0)

# User ZIP + checkbox under input
user_zip = st.text_input("Enter ZIP code")
search_all = st.checkbox("Search all ZIP codes", value=(user_zip.strip() == ""))

# Search query
st.subheader("🔍 What are you looking for?")
query = st.text_input("Type a keyword like 'vegan food', 'private chef', or 'home health aide'")

# Filters
st.subheader("🎯 Filter Your Preferences")
black_owned = st.checkbox("Black-owned")
women_owned = st.checkbox("Women-owned")
mobile = st.checkbox("Mobile")
kid_friendly = st.checkbox("Kid-friendly")
vegan_friendly = st.checkbox("Vegan-friendly")

# Begin filtering logic
results = df.copy()

if query.strip():
    query_lower = query.lower()
    results = results[
        df['Business Name'].str.lower().str.contains(query_lower, na=False) |
        df['Category'].str.lower().str.contains(query_lower, na=False) |
        df['Subcategory'].str.lower().str.contains(query_lower, na=False)
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

# Show results
if query or black_owned or women_owned or mobile or kid_friendly or vegan_friendly or (not search_all and user_zip.strip()):
    st.subheader("📋 Your Recommendations")
    if not results.empty:
        for _, row in results.iterrows():
            st.markdown(f"""
<div class='card'>
    <h4 style='margin-bottom: 5px;'>💼 <strong>{{row['Business Name']}}</strong></h4>
    <p style='margin: 0;'>📂 {{row['Category']}} > {{row['Subcategory']}}</p>
    <p style='margin: 0;'>📍 ZIP: {{row['Zipcode']}}</p>
    <p style='margin: 0;'>🔗 <a href='{{row['Instagram or Website']}}' target='_blank'>{{row['Instagram or Website']}}</a></p>
    <p style='margin: 0;'>🖤 Black Owned: {{'✅' if row['Black Owned'] else '❌'}} | 👩 Women-Owned: {{'✅' if row['Women Owned'] else '❌'}}</p>
    <p style='margin: 0;'>🌱 Vegan: {{'✅' if row['Vegan Friendly'] else '❌'}} | 🚗 Mobile: {{'✅' if row['Mobile'] else '❌'}} | 👶 Kid-Friendly: {{'✅' if row['Kid Friendly'] else '❌'}}</p>
</div>
""", unsafe_allow_html=True)
    else:
        st.warning("No matches found. Try different keywords or filters.")
else:
    st.info("Use the search box or filters above to discover great local spots!")
