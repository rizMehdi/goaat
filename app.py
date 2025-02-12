import streamlit as st
from PIL import Image
import os

def load_image(image_path):
    if os.path.exists(image_path):
        return Image.open(image_path)
    else:
        return None

# Streamlit App Configuration
st.set_page_config(page_title="Output Area Analysis", layout="centered")

# Display logos
logo_paths = ["img/logo1.png", "img/logo2.png", "img/logo3.png"]
st.image([img for img in logo_paths if os.path.exists(img)], width=100)

# Page Title
st.title("Output Area Analysis")

# Dropdown Options
cities = ["Birmingham", "Bradford", "York", "Bristol", "London", "Manchester", "Leeds", "Liverpool", "Sheffield", "Coventry", "Leicester", "Nottingham", "Newcastle", "Southampton", "Portsmouth", "Brighton", "Plymouth", "Derby", "Stoke-on-Trent", "Wolverhampton", "Norwich", "Oxford", "Cambridge", "Bath", "Exeter", "Durham", "Lancaster", "Chester", "Hull", "Sunderland", "Ipswich", "Reading", "Milton Keynes", "Northampton", "Luton", "Swindon", "Worcester", "Gloucester", "Carlisle", "Lincoln", "Chelmsford", "Preston", "Blackpool", "Bolton", "Stockport", "Warrington", "Rochdale", "Oldham", "Bournemouth", "Poole", "Worthing", "Basildon", "Southend-on-Sea", "Middlesbrough", "Blackburn", "Burnley", "Telford", "Slough", "Wakefield", "Doncaster", "Rotherham", "Huddersfield", "Southport", "Peterborough", "Guildford", "Basingstoke", "Woking"]

categories = ["Property", "Poverty", "Economic", "Health", "Eth", "Energy"]

classifications = [f"Class_{i}" for i in range(8)]

# Dropdown Selections
city = st.selectbox("Select a City", cities)
category = st.selectbox("Select a Category", categories)
classification = st.selectbox("Select a Classification", classifications)

# Show Images Button
if st.button("Show Images"):
    left_image_path = f"img/{city}.png"
    right_image_path = f"img/{city}_{category}_{classification}.png"
    
    left_image = load_image(left_image_path)
    right_image = load_image(right_image_path)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if left_image:
            st.image(left_image, caption=f"{city} Image")
        else:
            st.error("Left image not found")
    
    with col2:
        if right_image:
            st.image(right_image, caption=f"{city} {category} {classification} Image")
        else:
            st.error("Right image not found")
