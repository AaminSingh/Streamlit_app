import streamlit as st
import base64

# ==========================
# Background Image Function
# ==========================

def get_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_base64("backgroundimage.jpg")

# ==========================
# CSS Styling
# ==========================

page_bg = f"""
<style>

/* Background Image */

.stApp {{
    background:
    linear-gradient(
        rgba(0,0,0,0.60),
        rgba(0,0,0,0.60)
    ),
    url("data:image/jpg;base64,{img}");

    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

/* Main Heading */

h1 {{
    color: white !important;
    text-align: center;
    font-size: 48px;
}}

/* Sub Heading */

h2 {{
    color: white !important;
}}

/* Labels */

label {{
    color: white !important;
    font-weight: bold;
}}

/* Paragraphs */

p {{
    color: white !important;
}}

/* Markdown text */

div[data-testid="stMarkdownContainer"] {{
    color: white !important;
}}

/* Success box text */

div[data-testid="stAlert"] {{
    color: white !important;
}}


</style>
"""

st.markdown("""
<style>

/* Button */

div.stButton > button:first-child{
    background-color:#ff4b4b;
    color:white !important;
    border:none;
    border-radius:10px;
    padding:10px 24px;
    font-size:17px;
    font-weight:bold;
    transition:0.3s;
}

div.stButton > button:first-child:hover{
    background-color:#d63d3d;
    color:white !important;
}

</style>
""", unsafe_allow_html=True)

st.markdown(page_bg, unsafe_allow_html=True)

# ==========================
# Title
# ==========================

st.title("🍎 Simple Diet Planner")

st.header("Enter your Details")

# ==========================
# Inputs
# ==========================

name = st.text_input("Enter your name:")

age = st.number_input(
    "Enter your age:",
    min_value=1,
    max_value=120
)

weight = st.number_input(
    "Enter your weight (in kg):",
    min_value=1.0,
    max_value=300.0
)

goal = st.selectbox(
    "Select your goal",
    [
        "Weight Loss",
        "Weight Gain",
        "Maintain Weight"
    ]
)

# ==========================
# Button
# ==========================

if st.button("Get Diet Plan"):

    st.subheader(f"Hello, {name} 👋")

    st.success("Recommended Diet Plan")

    if goal == "Weight Loss":

        st.write("🥣 **Breakfast:** Oats + Fruits")
        st.write("🥗 **Lunch:** Salad + Grilled Chicken")
        st.write("🥣 **Dinner:** Soup + Vegetables")

    elif goal == "Weight Gain":

        st.write("🥛 **Breakfast:** Milk + Eggs + Banana")
        st.write("🍗 **Lunch:** Rice + Chicken + Vegetables")
        st.write("🥜 **Dinner:** Paneer + Dry Fruits")

    else:

        st.write("🍞 **Breakfast:** Bread + Peanut Butter")
        st.write("🍛 **Lunch:** Balanced Meal")
        st.write("🥗 **Dinner:** Vegetables + Dal")