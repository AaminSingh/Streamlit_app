import streamlit as st

st.title("Simple Diet Planner")

st.header("Enter your Details")

name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=1, max_value=120)
weight = st.number_input("Enter your weight (in kg):", min_value=1.0, max_value=300.0)


goal = st.selectbox(
    "Select your goal",
      ["Weight loss","Weight gain","Maintain Weight"]
)


if st.button("Get Diet Plan"):
    st.subheader(f"Hello,{name}")

    if goal == "Weight Loss":
        st.success("Diet Plan")
        st.write("Breakfast:Oats+Fruits")
        st.write("Lunck:Salad+Chicken")
        st.write("Dinner: Soup + Vegetables")
    elif goal == "Weight Gain":
        st.success("Diet Plan")
        st.write("Breakfast:Oats +Fruits")
        st.write("Lunch: Salad + Chicken ") 
        st.write("Dinner: Soup + Vegetables")
    else:
        st.success("Diet Plan")
        st.write("Breakfast:Oats + Fruits")
        st.write("Lunch: Salad + Chicken") 
        st.write("Dinner: Soup + Vegetables")          