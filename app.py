import streamlit as st
from PIL import Image
import os

def load_image(image_path):
    if os.path.exists(image_path):
        return Image.open(image_path)
    else:
        return None
    

# Streamlit App Configuration
st.set_page_config(page_title="GNN Output Area Analysis Toolkit", layout="wide", initial_sidebar_state="expanded")

applogo = "img/applogo.png" 

# Display images if they exist
if os.path.exists(applogo):
    st.sidebar.image(applogo, width=70)

# Sidebar for Dropdown Selections
st.sidebar.title("GNN Output Area Analysis Toolkit")

# Reset Button
# if st.sidebar.button("Restart"):
#     if st.sidebar.confirm("Are you sure you want to reset the selections?"):
#         st.experimental_rerun()

cities = ["Birmingham", "Bradford", "York", "Bristol", "London", "Manchester", "Leeds", "Liverpool", "Sheffield", "Coventry", "Leicester", "Nottingham", "Newcastle", "Southampton", "Portsmouth", "Brighton", "Plymouth", "Derby", "Stoke-on-Trent", "Wolverhampton", "Norwich", "Oxford", "Cambridge", "Bath", "Exeter", "Durham", "Lancaster", "Chester", "Hull", "Sunderland", "Ipswich", "Reading", "Milton Keynes", "Northampton", "Luton", "Swindon", "Worcester", "Gloucester", "Carlisle", "Lincoln", "Chelmsford", "Preston", "Blackpool", "Bolton", "Stockport", "Warrington", "Rochdale", "Oldham", "Bournemouth", "Poole", "Worthing", "Basildon", "Southend-on-Sea", "Middlesbrough", "Blackburn", "Burnley", "Telford", "Slough", "Wakefield", "Doncaster", "Rotherham", "Huddersfield", "Southport", "Peterborough", "Guildford", "Basingstoke", "Woking"]

category_mapping = {
    "House Ownership": "Property",
    "Occupation": "Economic",
    "Poverty": "Poverty",
    "Health": "Health",
    "Energy": "Energy"
}

categories = list(category_mapping.keys())
classifications = [f"Class_{i}" for i in range(8)]

city = st.sidebar.selectbox("Select a Location", [""] + cities)

if city:
    category = st.sidebar.selectbox("Select a Category", [""] + categories, key=f"category_{city}")
else:
    category = None

if category:
    classification = "Class_0"
else:
    classification = None

# Show Images Button
if city and category and st.sidebar.button("Show Results"):
    category_path = category_mapping[category]
    left_image_path = f"img/{city}.png"
    right_image_path = f"img/{city}_{category_path}_{classification}.png"
    
    left_image = load_image(left_image_path)
    right_image = load_image(right_image_path)
    
    if right_image:
        right_image = right_image.rotate(-90, expand=True)
    
    col0, col1 = st.columns(2)
        
    with col0:
        if left_image:
            st.image(left_image, caption=f"{city}")
        else:
            st.error("Data for this city is yet to be integrated.")
        
    
    with col1:

        tabs = st.tabs(classifications)
        
        for i, tab in enumerate(tabs):
            with tab:
                classification = classifications[i]
                right_image_path = f"img/{city}_{category_path}_{classification}.png"
                ethnicity_image_path = f"img/{city}_Eth_Class_{classification[-1]}.png"
                
                right_image = load_image(right_image_path)
                ethnicity_image = load_image(ethnicity_image_path)
                
                if right_image:
                    right_image = right_image.rotate(-90, expand=True)
                
                if right_image:
                    st.image(right_image, caption=f"{classification} for {category} in {city}. This graph shows different features for {city} as compared to the national average. Higher value means its above national average.", width=right_image.width // 3)
                else:
                    st.error("Data for this category/class is yet to be integrated.")
                
                if ethnicity_image:
                    st.image(ethnicity_image, caption=f"Ethnic distribution for {classification} in {city}", width=ethnicity_image.width // 3)
                else:
                    st.error("Ethnicity data for this city/class is yet to be integrated.")

# Display logos at the bottom of the sidebar
st.sidebar.markdown("---")  # Add a line above the logos

# logo_paths = ["img/prime.png", "img/hwu.png", "img/ukri.png"]
logo_paths = ["img/logos3.png"]
logos = [img for img in logo_paths if os.path.exists(img)]

for logo in logos:
    st.sidebar.image(logo)

# # Inject custom CSS to change the sidebar background color
# st.markdown(
#     """
#     <style>
#     .css-1d391kg {  /* This class name may change, inspect the sidebar element to get the correct class */
#         background-color: #506c8c !important;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )