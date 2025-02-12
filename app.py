import streamlit as st
from PIL import Image
import os

def load_image(image_path):
    if os.path.exists(image_path):
        return Image.open(image_path)
    else:
        return None

# Streamlit App Configuration
st.set_page_config(page_title="GNN Output Area Analysis Toolkit", layout="centered")

# Sidebar for Dropdown Selections
st.sidebar.title("Output Area Analysis")
st.sidebar.header("Select Options")

cities = ["Birmingham", "Bradford", "York", "Bristol", "London", "Manchester", "Leeds", "Liverpool", "Sheffield", "Coventry", "Leicester", "Nottingham", "Newcastle", "Southampton", "Portsmouth", "Brighton", "Plymouth", "Derby", "Stoke-on-Trent", "Wolverhampton", "Norwich", "Oxford", "Cambridge", "Bath", "Exeter", "Durham", "Lancaster", "Chester", "Hull", "Sunderland", "Ipswich", "Reading", "Milton Keynes", "Northampton", "Luton", "Swindon", "Worcester", "Gloucester", "Carlisle", "Lincoln", "Chelmsford", "Preston", "Blackpool", "Bolton", "Stockport", "Warrington", "Rochdale", "Oldham", "Bournemouth", "Poole", "Worthing", "Basildon", "Southend-on-Sea", "Middlesbrough", "Blackburn", "Burnley", "Telford", "Slough", "Wakefield", "Doncaster", "Rotherham", "Huddersfield", "Southport", "Peterborough", "Guildford", "Basingstoke", "Woking"]

category_mapping = {
    "House Ownership": "Property",
    "Economic": "Economic",
    "Ethnicity": "Eth",
    "Poverty": "Poverty",
    "Health": "Health",
    "Energy": "Energy"
}

categories = list(category_mapping.keys())
classifications = [f"Class_{i}" for i in range(8)]

city = st.sidebar.selectbox("Select a City", cities)
category = st.sidebar.selectbox("Select a Category", categories)
classification = st.sidebar.selectbox("Select a Classification", classifications)

# Show Images Button
if st.sidebar.button("Show Results"):
    category_path = category_mapping[category]
    left_image_path = f"img/{city}.png"
    right_image_path = f"img/{city}_{category_path}_{classification}.png"
    
    left_image = load_image(left_image_path)
    right_image = load_image(right_image_path)
    
#     col1, col2 = st.columns(2)
    
#     with col1:
#         if left_image:
#             st.image(left_image, caption=f"{city} Image")
#         else:
#             st.error("Data for this city is yet to be integrated.")
    
#     with col2:
#         if right_image:
#             st.image(right_image, caption=f"{city} {category} {classification} Image")
#         else:
#             st.error("Data for this category/class is yet to be integrated.")

# # Display logos at the bottom of the sidebar
# logo_paths = ["img/prime.png", "img/hwu.png", "img/ukri.png"]
# st.sidebar.image([img for img in logo_paths if os.path.exists(img)], width=100)

col1, col2 = st.columns(2)
    
with col1:
    if left_image:
        st.image(left_image, caption=f"{city} Image")
    else:
        st.error("Data for this city is yet to be integrated.")
    
with col2:
    if right_image:
        st.image(right_image, caption=f"{city} {category} {classification} Image")
    else:
        st.error("Data for this category/class is yet to be integrated.")

# Display logos at the bottom of the sidebar
st.sidebar.markdown("---")  # Add a line above the logos

logo_paths = ["img/prime.png", "img/hwu.png", "img/ukri.png"]
logos = [img for img in logo_paths if os.path.exists(img)]

# Encase logos in a box with color #506c8c
st.sidebar.markdown(
    f"""
    <div style="background-color:#506c8c; padding:10px;">
        {"".join([f'<img src="{logo}" style="display:block; margin-bottom:10px; width:100px;" />' for logo in logos])}
    </div>
    """,
    unsafe_allow_html=True
)