import streamlit as st

# Title and Header
st.title("Retail Business Dashboard")
st.header("Manager Input Selection")



# Instruction
st.write("Please enter the monthly sales target and select the region")



# Number input for sales target
monthly_target = st.number_input("Enter monthly sales target in USD:",
                      min_value=0,
                      max_value=1000000,
                      value=25)



# Dropdown for region selection
option = st.selectbox("Choose your favorite color:",
                      ["Asian", "Europe", "NA", "Africa"])
st.write(f"You selected: {option}")


# Submit button
if st.button("Submit"):
    # Display entered values
  st.write(f"Your monthly sales target is {monthly_target}")


    # Success message
st.success("Operation completed successfully!")


    # Extra message for ambitious target



