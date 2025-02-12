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
st.sidebar.title("GNN Output Area Analysis Toolkit")
# st.sidebar.header("Select Options")

# Display welcome text and images in the main area
st.write("Welcome to the toolkit. Select options on the side to explore.")

# Paths to the images
uk_image_path = "img/uk.png"
me_national_average_image_path = "img/me_national_average.png"

# Display images if they exist
if os.path.exists(uk_image_path):
    st.image(uk_image_path, caption="UK Image", width=500)

# if os.path.exists(me_national_average_image_path):
#     st.image(me_national_average_image_path, caption="ME National Average Image")




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
    
    # col1, col2 = st.columns(2)
    
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