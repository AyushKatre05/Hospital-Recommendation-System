import pandas as pd
import streamlit as st

def load_dataset():
    hospital_data = pd.read_csv('Hospitals.csv', encoding='utf-8')
    return hospital_data

def recommend_hospitals(city, data):
    recommended_hospitals = data[data['District'] == city]
    return recommended_hospitals

def main():
    st.title("Hospital Recommendation System")
    st.sidebar.header('User Input')
    
    city = st.sidebar.text_input('Enter District')  # Text input for city
    enter_button = st.sidebar.button('Enter')  # Button widget
    
    data = load_dataset()

    if enter_button:  # If Enter button is clicked
        recommended_hospitals = recommend_hospitals(city, data)

        st.subheader('Recommended Hospitals')

        if recommended_hospitals.empty:
            st.write('No hospitals found in the specified district')
        else:
            st.table(recommended_hospitals[['Hospital_Name', 'Address_Original_First_Line','District','Mobile_Number','Telephone','Emergency_Num','Hospital_Primary_Email_Id']])
            st.write('|Above are some Hospitals/Clinics based on your provided location.|')        
        

if __name__ == "__main__":
    main()
