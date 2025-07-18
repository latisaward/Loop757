
import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

# Load business data
data = {"Business Name": ["Pretty Strategic, LLC", "DaChef\u2019s Catering & Co.", "Pretty Ambitious LLC", "BPRE", "The SnoBall Shop", "Carte Brunch", "House of Salvage", "Lady's Fingers Health Spa | Massage Therapy", "Hearts-N-Hones Home Care Agency", "Str8 Up Slushed", "I Got A Love Jones Events", "TaxGuru Financial & Public Services", "Tax Boss Academy", "Montego Island Grill", "Stivas Kitchen", "Admire Curves", "NailsbyKeandra", "Versus Salon", "The Happy Hour Hostess", "Desmond\u2019s Island Soul Grill", "Made In Norfolk", "Author- I Remember When", "Bar 9", "Lookout4 1 Records LLC.", "Alodeuri Artisan Jewelry", "Desmond\u2019s Island Soul Grill", "Earthy Child"], "Category": ["Professional & Business Services", "Food & Beverage", "Retail & Product-Based", "Professional & Business Services", "Food & Beverage", "Food & Beverage", "Retail & Product-Based", "Health & Wellness", "Health & Wellness", "Food & Beverage", "Events & Experiences", "Professional & Business Services", "Career & Skill Services", "Food & Beverage", "Food & Beverage", "Fitness & Body", "Beauty & Grooming", "Beauty & Grooming", "Events & Experiences", "Food & Beverage", "Retail & Product-Based", "Retail & Product-Based", "Food & Beverage", "Events & Experiences", "Retail & Product-Based", "Food & Beverage", "Retail & Product-Based"], "Subcategory": ["Consultant", "Private Chef", "Boutique / Apparel Store", "Consultant", "Restaurant", "Restaurant", "Boutique / Apparel Store", "Massage Therapist", "Home Health Aide", "Bartending Service", "Event Planner", "Financial Advisor / Tax Pro", "Career Coach", "Restaurant", "Catering Service", "Personal Trainer", "Nail Tech", "Hair Stylist", "Event Planner", "Restaurant", "Boutique / Apparel Store", "Online Store / E-commerce", "Restaurant", "DJ / Live Music", "Mobile Vending Retailer", "Restaurant", "Product Maker (Candles, Soaps, etc.)"], "Zipcode": [23435, 23666, 23523, 23794, 23454, 23707, 23320, 23502, 22452, 23352, 23523, 23523, 23523, 23452, 23503, 23462, 23703, 23462, 23455, 23464, 23509, 23513, 23702, 23504, 23504, 23464, 23661], "Instagram or Website": ["@prettystrategicllc", "Instagram.com/dachef", "@missprettyambitious_", "www.bpreal.estate", "@thesnoballshop", "www.cartebrunch.com", "HouseofSalvage", "Ladysfingers.info (website) and ladysfingersllc (IG)", "www.hearts-n-homes.com", "Str8upslushed", "Igotalovejonesevents.com", "www.taxguru4you.net", "www.mytaxboss.net", "montegogrill.com ", "www.StivasKitchen.com", "Admire Curves Body sculpting ", "https://nailsbykeandrasade.glossgenius.com/", "https://www.versussalon.com/", "https://thehappyhourhostess.com/", "https://desmonds-island-soul-grill.square.site/", "Www.madeinnorfolkapparel.com", "Moddagoat96", "Bar9 portsmouth Va", "@Lookout4_1", "www.alodeuri.com www.instagram.com/alodeuri", "IG/desmondsislandsoulgrill", "Instagram.com/the_earthy_child"], "Black Owned": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1], "Mobile": [1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0], "Kid Friendly": [0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1], "Vegan Friendly": [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0], "Women Owned": [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1], "Search Corpus": ["pretty strategic, llc professional & business services consultant", "dachef\u2019s catering & co. food & beverage private chef", "pretty ambitious llc retail & product-based boutique / apparel store", "bpre professional & business services consultant", "the snoball shop food & beverage restaurant", "carte brunch food & beverage restaurant", "house of salvage retail & product-based boutique / apparel store", "lady's fingers health spa | massage therapy health & wellness massage therapist", "hearts-n-hones home care agency health & wellness home health aide", "str8 up slushed food & beverage bartending service", "i got a love jones events events & experiences event planner", "taxguru financial & public services professional & business services financial advisor / tax pro", "tax boss academy career & skill services career coach", "montego island grill food & beverage restaurant", "stivas kitchen food & beverage catering service", "admire curves fitness & body personal trainer", "nailsbykeandra beauty & grooming nail tech", "versus salon beauty & grooming hair stylist", "the happy hour hostess events & experiences event planner", "desmond\u2019s island soul grill food & beverage restaurant", "made in norfolk retail & product-based boutique / apparel store", "author- i remember when retail & product-based online store / e-commerce", "bar 9 food & beverage restaurant", "lookout4 1 records llc. events & experiences dj / live music", "alodeuri artisan jewelry retail & product-based mobile vending retailer", "desmond\u2019s island soul grill food & beverage restaurant", "earthy child retail & product-based product maker (candles, soaps, etc.)"]}
df = pd.DataFrame(data)

st.set_page_config(page_title="Loop757", layout="centered")

# --- THEME / STYLING ---
st.markdown("""
<style>
body {
    background: linear-gradient(120deg, #fceabb 0%, #f8b500 100%);
    font-family: 'Helvetica', sans-serif;
}

h1, h2, h3 {
    color: #073763 !important;
}

input[type="text"], .stTextInput input {
    border-radius: 10px;
    padding: 0.5rem;
    border: 2px solid #f8b500;
}

.stButton>button {
    background-color: #f85a8b;
    color: white;
    border-radius: 12px;
    padding: 0.5rem 1rem;
    font-weight: bold;
}

.block-container {
    padding-top: 2rem;
}
</style>
""", unsafe_allow_html=True)

st.title("❤️ Loop757: Discover Local Gems")
st.caption("Powered by love for the 757. Discover Black-owned, women-led, mobile, vegan-friendly, and family-friendly businesses around you.")

# Location note
st.markdown("📍 We can auto-detect your location (if allowed), or you can enter a ZIP code manually.")

# Auto-location via JavaScript
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

# --- ZIP Input and Search-All Toggle ---
user_zip = st.text_input("Enter ZIP code")
search_all = st.checkbox("Search all ZIP codes", value=(user_zip.strip() == ""))

# --- Search Input ---
st.subheader("🔍 What are you looking for?")
query = st.text_input("Try 'vegan food', 'private chef', 'home health aide', etc.")

# --- Filter Toggles ---
st.subheader("🎯 Filter Your Preferences")
black_owned = st.checkbox("Black-owned")
women_owned = st.checkbox("Women-owned")
mobile = st.checkbox("Mobile")
kid_friendly = st.checkbox("Kid-friendly")
vegan_friendly = st.checkbox("Vegan-friendly")

# --- Filter Logic ---
results = df.copy()

# Better keyword matching using .str.contains across multiple fields
if query.strip():
    query_lower = query.lower()
    mask = (
        df['Business Name'].str.lower().str.contains(query_lower, na=False) |
        df['Category'].str.lower().str.contains(query_lower, na=False) |
        df['Subcategory'].str.lower().str.contains(query_lower, na=False)
    )
    results = results[mask]

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

# Filter by ZIP unless search_all is checked
if not search_all and user_zip.strip():
    results = results[results['Zipcode'].astype(str).str.contains(user_zip.strip(), case=False)]

# --- Display Results ---
if query or black_owned or women_owned or mobile or kid_friendly or vegan_friendly or (not search_all and user_zip.strip()):
    st.subheader("📋 Recommendations")
    if not results.empty:
        for _, row in results.iterrows():
            st.markdown(f"""
**{row['Business Name']}**  
📂 {row['Category']} > {row['Subcategory']}  
📍 ZIP: {row['Zipcode']}  
🔗 Website/IG: {row['Instagram or Website']}  
🖤 Black Owned: {'✅' if row['Black Owned'] else '❌'}  
🌱 Vegan Friendly: {'✅' if row['Vegan Friendly'] else '❌'}  
🚗 Mobile: {'✅' if row['Mobile'] else '❌'}
--- 
""")
    else:
        st.warning("No matches found. Try adjusting your filters or keywords.")
else:
    st.info("Use the search box or filters above to find local businesses.")
