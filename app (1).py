
import streamlit as st
import pandas as pd
from difflib import get_close_matches

# Load cleaned data
data = {'Business Name': ['Pretty Strategic, LLC', 'DaChef’s Catering & Co.', 'Pretty Ambitious LLC', 'BPRE', 'The SnoBall Shop', 'Carte Brunch', 'House of Salvage', "Lady's Fingers Health Spa | Massage Therapy", 'Hearts-N-Hones Home Care Agency', 'Str8 Up Slushed', 'I Got A Love Jones Events', 'TaxGuru Financial & Public Services', 'Tax Boss Academy', 'Montego Island Grill', 'Stivas Kitchen', 'Admire Curves', 'NailsbyKeandra', 'Versus Salon', 'The Happy Hour Hostess', 'Desmond’s Island Soul Grill', 'Made In Norfolk', 'Author- I Remember When', 'Bar 9', 'Lookout4 1 Records LLC.', 'Alodeuri Artisan Jewelry', 'Desmond’s Island Soul Grill', 'Earthy Child'], 'Category': ['Professional & Business Services', 'Food & Beverage', 'Retail & Product-Based', 'Professional & Business Services', 'Food & Beverage', 'Food & Beverage', 'Retail & Product-Based', 'Health & Wellness', 'Health & Wellness', 'Food & Beverage', 'Events & Experiences', 'Professional & Business Services', 'Career & Skill Services', 'Food & Beverage', 'Food & Beverage', 'Fitness & Body', 'Beauty & Grooming', 'Beauty & Grooming', 'Events & Experiences', 'Food & Beverage', 'Retail & Product-Based', 'Retail & Product-Based', 'Food & Beverage', 'Events & Experiences', 'Retail & Product-Based', 'Food & Beverage', 'Retail & Product-Based'], 'Subcategory': ['Consultant', 'Private Chef', 'Boutique / Apparel Store', 'Consultant', 'Restaurant', 'Restaurant', 'Boutique / Apparel Store', 'Massage Therapist', 'Home Health Aide', 'Bartending Service', 'Event Planner', 'Financial Advisor / Tax Pro', 'Career Coach', 'Restaurant', 'Catering Service', 'Personal Trainer', 'Nail Tech', 'Hair Stylist', 'Event Planner', 'Restaurant', 'Boutique / Apparel Store', 'Online Store / E-commerce', 'Restaurant', 'DJ / Live Music', 'Mobile Vending Retailer', 'Restaurant', 'Product Maker (Candles, Soaps, etc.)'], 'Zipcode': [23435, 23666, 23523, 23794, 23454, 23707, 23320, 23502, 22452, 23352, 23523, 23523, 23523, 23452, 23503, 23462, 23703, 23462, 23455, 23464, 23509, 23513, 23702, 23504, 23504, 23464, 23661], 'Instagram or Website': ['@prettystrategicllc', 'Instagram.com/dachef', '@missprettyambitious_', 'www.bpreal.estate', '@thesnoballshop', 'www.cartebrunch.com', 'HouseofSalvage', 'Ladysfingers.info (website) and ladysfingersllc (IG)', 'www.hearts-n-homes.com', 'Str8upslushed', 'Igotalovejonesevents.com', 'www.taxguru4you.net', 'www.mytaxboss.net', 'montegogrill.com ', 'www.StivasKitchen.com', 'Admire Curves Body sculpting ', 'https://nailsbykeandrasade.glossgenius.com/', 'https://www.versussalon.com/', 'https://thehappyhourhostess.com/', 'https://desmonds-island-soul-grill.square.site/', 'Www.madeinnorfolkapparel.com', 'Moddagoat96', 'Bar9 portsmouth Va', '@Lookout4_1', 'www.alodeuri.com www.instagram.com/alodeuri', 'IG/desmondsislandsoulgrill', 'Instagram.com/the_earthy_child'], 'Black Owned': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1], 'Mobile': [1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0], 'Kid Friendly': [0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1], 'Vegan Friendly': [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0], 'Women Owned': [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1], 'Search Corpus': ['pretty strategic, llc professional & business services consultant', 'dachef’s catering & co. food & beverage private chef', 'pretty ambitious llc retail & product-based boutique / apparel store', 'bpre professional & business services consultant', 'the snoball shop food & beverage restaurant', 'carte brunch food & beverage restaurant', 'house of salvage retail & product-based boutique / apparel store', "lady's fingers health spa | massage therapy health & wellness massage therapist", 'hearts-n-hones home care agency health & wellness home health aide', 'str8 up slushed food & beverage bartending service', 'i got a love jones events events & experiences event planner', 'taxguru financial & public services professional & business services financial advisor / tax pro', 'tax boss academy career & skill services career coach', 'montego island grill food & beverage restaurant', 'stivas kitchen food & beverage catering service', 'admire curves fitness & body personal trainer', 'nailsbykeandra beauty & grooming nail tech', 'versus salon beauty & grooming hair stylist', 'the happy hour hostess events & experiences event planner', 'desmond’s island soul grill food & beverage restaurant', 'made in norfolk retail & product-based boutique / apparel store', 'author- i remember when retail & product-based online store / e-commerce', 'bar 9 food & beverage restaurant', 'lookout4 1 records llc. events & experiences dj / live music', 'alodeuri artisan jewelry retail & product-based mobile vending retailer', 'desmond’s island soul grill food & beverage restaurant', 'earthy child retail & product-based product maker (candles, soaps, etc.)']}
df = pd.DataFrame(data)

st.set_page_config(page_title="Loop757", layout="centered")
st.title("Loop757: Discover Local Gems")
st.caption("Smart local business recommendations powered by community data and filters.")

# User ZIP code input
st.subheader("Your Location")
user_zip = st.text_input("Enter your ZIP code (optional if searching all)", max_chars=10)
search_all = st.checkbox("Search all ZIP codes", value=True)

# Search box
st.subheader("What are you looking for?")
query = st.text_input("Type keywords like 'private chef', 'consultant', or 'vegan'")

# Search logic
results = df.copy()
if query:
    matches = get_close_matches(query.lower(), df['Search Corpus'], n=10, cutoff=0.3)
    results = results[results['Search Corpus'].isin(matches)]

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

if not search_all and user_zip:
    results = results[results['Zipcode'].astype(str).str.strip() == user_zip.strip()]


# Filter toggles
st.subheader("Filter Your Preferences")
black_owned = st.checkbox("Black-owned")
women_owned = st.checkbox("Women-owned")
mobile = st.checkbox("Mobile")
kid_friendly = st.checkbox("Kid-friendly")
vegan_friendly = st.checkbox("Vegan-friendly")

# Display results
if query or black_owned or women_owned or mobile or kid_friendly or vegan_friendly or (not search_all and user_zip):
    st.subheader("Recommendations")
    if not results.empty:
        for _, row in results.iterrows():
            st.markdown(f"""
**{row['Business Name']}**  
Category: {row['Category']} > {row['Subcategory']}  
Zip Code: {row['Zipcode']}  
Website/IG: {row['Instagram or Website']}  
Black Owned: {'Yes' if row['Black Owned'] else 'No'}  
Vegan Friendly: {'Yes' if row['Vegan Friendly'] else 'No'}  
Mobile: {'Yes' if row['Mobile'] else 'No'}
""")
    else:
        st.info("No matches found. Try different filters or search terms.")
else:
    st.info("Use the search box or filters above to find local businesses.")
