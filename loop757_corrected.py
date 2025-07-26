import pandas as pd
import streamlit.components.v1 as components

data = {"Business Name": ["Pretty Strategic, LLC", "DaChef’s Catering & Co.", "Pretty Ambitious LLC", "BPRE", "The SnoBall Shop", "Carte Brunch", "House of Salvage", "Lady's Fingers Health Spa | Massage Therapy", "Hearts-N-Hones Home Care Agency", "Str8 Up Slushed", "I Got A Love Jones Events", "TaxGuru Financial & Public Services", "Tax Boss Academy", "Montego Island Grill", "Stivas Kitchen", "Admire Curves", "NailsbyKeandra", "Versus Salon", "The Happy Hour Hostess", "Desmond’s Island Soul Grill", "Made In Norfolk", "Author- I Remember When", "Bar 9", "Lookout4 1 Records LLC.", "Alodeuri Artisan Jewelry", "Desmond’s Island Soul Grill", "Earthy Child"],
"Category": ["Professional & Business Services", "Food & Beverage", "Retail & Product-Based", "Professional & Business Services", "Food & Beverage", "Food & Beverage", "Retail & Product-Based", "Health & Wellness", "Health & Wellness", "Food & Beverage", "Events & Experiences", "Professional & Business Services", "Career & Skill Services", "Food & Beverage", "Food & Beverage", "Fitness & Body", "Beauty & Grooming", "Beauty & Grooming", "Events & Experiences", "Food & Beverage", "Retail & Product-Based", "Retail & Product-Based", "Food & Beverage", "Events & Experiences", "Retail & Product-Based", "Food & Beverage", "Retail & Product-Based"],
"Subcategory": ["Consultant", "Private Chef", "Boutique / Apparel Store", "Consultant", "Restaurant", "Restaurant", "Boutique / Apparel Store", "Massage Therapist", "Home Health Aide", "Bartending Service", "Event Planner", "Financial Advisor / Tax Pro", "Career Coach", "Restaurant", "Catering Service", "Personal Trainer", "Nail Tech", "Hair Stylist", "Event Planner", "Restaurant", "Boutique / Apparel Store", "Online Store / E-commerce", "Restaurant", "DJ / Live Music", "Mobile Vending Retailer", "Restaurant", "Product Maker (Candles, Soaps, etc.)"],
"Zipcode": [23435, 23666, 23523, 23794, 23454, 23707, 23320, 23502, 22452, 23352, 23523, 23523, 23523, 23452, 23503, 23462, 23703, 23462, 23455, 23464, 23509, 23513, 23702, 23504, 23504, 23464, 23661],
"Instagram or Website": ["@prettystrategicllc", "Instagram.com/dachef", "@missprettyambitious_", "www.bpreal.estate", "@thesnoballshop", "www.cartebrunch.com", "HouseofSalvage", "Ladysfingers.info (website) and ladysfingersllc (IG)", "www.hearts-n-homes.com", "Str8upslushed", "Igotalovejonesevents.com", "www.taxguru4you.net", "www.mytaxboss.net", "montegogrill.com ", "www.StivasKitchen.com", "Admire Curves Body sculpting ", "https://nailsbykeandrasade.glossgenius.com/", "https://www.versussalon.com/", "https://thehappyhourhostess.com/", "https://desmonds-island-soul-grill.square.site/", "Www.madeinnorfolkapparel.com", "Moddagoat96", "Bar9 portsmouth Va", "@Lookout4_1", "www.alodeuri.com www.instagram.com/alodeuri", "IG/desmondsislandsoulgrill", "Instagram.com/the_earthy_child"],
"Black Owned": [1]*27, "Mobile": [1,1,1,0,1,0,1,0,0,1,1,0,0,0,1,0,0,0,0,0,1,1,1,1,1,0,0],
"Kid Friendly": [0,1,0,0,1,1,1,1,0,0,0,1,1,1,1,0,0,1,0,1,1,0,1,1,0,1,1],
"Vegan Friendly": [0,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,0,0,1,0,1,1,0],
"Women Owned": [1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,0,1,0,1,1,1],
"Search Corpus": ["" for _ in range(27)]
}
df = pd.DataFrame(data)
csv_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQKkIx5eUS4kACrfiO5_tsWwa0iGBq0GEfNxhdru1hAWWvCb3BxjiqwVeEIlZYEc0PmCUL-wuMDs3ob/pub?gid=0&single=true&output=csv"
st.experimental_set_query_params(refresh=int(pd.Timestamp.now().timestamp()))
df = pd.read_csv(csv_url)

# Rename columns to expected names (remove leading/trailing spaces)
df.columns = df.columns.str.strip()

# Create 'Subcategory' column if your data splits it by main category
if 'Subcategory – Beauty & Grooming' in df.columns:
    subcat_cols = [col for col in df.columns if 'Subcategory' in col]
    df['Subcategory'] = df[subcat_cols].bfill(axis=1).iloc[:, 0]

# Rename other key columns if necessary
df.rename(columns={
    "Business Category": "Category",
    "Zip code": "Zipcode",
    "Instagram or Website": "Instagram or Website",
    "Is this a Black-owned business or service?": "Black Owned",
    "Select all that apply.": "Mobile",
    "Select all that apply. (Kid-friendly)": "Kid Friendly",
    "Select all that apply. (Vegan-friendly)": "Vegan Friendly",
    "Select all that apply. (Woman-owned)": "Women Owned"
}, inplace=True)

# Normalize binary columns to 0/1
for col in ['Black Owned', 'Mobile', 'Kid Friendly', 'Vegan Friendly', 'Women Owned']:
    df[col] = df[col].astype(str).str.lower().isin(['1', 'yes', 'true', 'y', 't']).astype(int)


st.set_page_config(page_title='Loop757', layout='centered')
st.markdown("""<style>body {background: linear-gradient(135deg, #d4fc79 0%, #96e6a1 100%);font-family: 'Arial', sans-serif;} h1 {color: #3b3b3b;} .stTextInput input, .stButton>button {border-radius: 10px;} </style>""", unsafe_allow_html=True)

    else:
        st.warning('No results found. Try a different keyword or filter combination.')
else:
    st.info('Enter a keyword or apply filters to find businesses.')
    st.info('Enter a keyword or apply filters to find businesses.')
