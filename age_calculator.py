import streamlit as st
from datetime import date


# ---------------- Header ---------------- #

st.markdown(
    "<h1 style='text-align:center; color:red;'>Age Calculator</h1>",
    unsafe_allow_html=True
)

st.markdown("---")

# ---------------- Inputs ---------------- #

name = st.text_input("Enter your name:")

dob = st.date_input(
    "Select your Date of Birth",
    value=date(2000, 1, 1),      # Default selected date
    min_value=date(1970, 1, 1),  # Earliest allowed date
    max_value=date.today()       # Latest allowed date
)
# ---------------- Button ---------------- #

if st.button("Calculate age"):

    today = date.today()

    age = today.year - dob.year

    # Check whether birthday has occurred this year
    if (today.month, today.day) < (dob.month, dob.day):
        age -= 1

    st.success(f"Hello {name}!")
    st.write(f"Your age is **{age}** years.")

# ---------------- Footer ---------------- #

st.markdown("---")

st.markdown(
    "<p style='text-align:center;'>© 2026 Built with Streamlit</p>",
    unsafe_allow_html=True
)

