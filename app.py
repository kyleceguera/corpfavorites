import streamlit as st
import pandas as pd

# Load CSV data
@st.cache_data
def load_data():
    data = pd.read_csv('path/to/WW Res Numbers.csv')
    return data

# Streamlit app
def main():

    # Set the title of the tab and other configurations
    st.set_page_config(page_title="Corporate Favorite Lookup", page_icon="📒")
    st.title("Corporate Favorite Lookup")

    # Load data
    df = load_data()

    col1, col2 = st.columns(2)

    with col1:
        # Get unique values for picklists
        unique_brands = df['Brand'].unique().tolist()
        unique_countries = df['Country'].unique().tolist()
        unique_customer_types = df['Type'].unique().tolist()

        # Picklist with free text input ability
        brand = st.selectbox("Enter Brand", options=unique_brands)
        country = st.selectbox("Enter Country", options=unique_countries)
        customer_type = st.selectbox("Enter Customer Type", options=unique_customer_types)

        # Button to trigger the lookup
        if st.button("Return Phone Number"):
            filtered_data = df[
                (df['Brand'] == brand) & 
                (df['Country'] == country) & 
                (df['Type'] == customer_type)
            ]

            if not filtered_data.empty:
                matching_number = int(filtered_data['Number'].values[0])  # Convert to integer to remove trailing ".0"
                with col2:
                    st.markdown(
                        "<div style='text-align: center;'><h3>Number to Dial</h3></div>", 
                        unsafe_allow_html=True
                    )
                    st.markdown(
                        f"<div style='text-align: center;'>{matching_number}</div>",
                        unsafe_allow_html=True)
                    st.markdown("-------------------")
                    st.markdown("When transferring the call please be sure to include '0' before the phone number. WE CAN PUT ANYTHING WE WANT HERE")
            else:
                with col2:
                    st.markdown(
                        "<div style='text-align: center;'><h3>No matching data found.</h3></div>", 
                        unsafe_allow_html=True
                    )
                    

if __name__ == "__main__":
    main()
