import streamlit as st
import pandas as pd
import numpy as np


# Load the LSTM model
#model = load_model('your_model.h5')
countries=pd.read_csv("country_list.csv")
Income_pred=pd.read_csv('Income_pred_hyperparamless.csv')
Education_pred=pd.read_csv('Education_pred_hyperparamless.csv')
Life_pred=pd.read_csv('Life_pred_hyperparamless.csv')
# Function to predict HDI for a given year and country
# HDI formula
def calculate_hdi(life_expectancy_index, education_index, income_index):
    hdi = (life_expectancy_index * education_index * income_index) ** (1/3)
    return hdi
def predict_hdi(country,year):
    #predicted data set
    time_point=(year-2024)*12
    i=Income_pred.loc[time_point,country]
    e=Education_pred.loc[time_point,country]
    l=Life_pred.loc[time_point,country]
    hdi=calculate_hdi(l,e,i)
    
    # Make prediction
    #predicted_hdi = model.predict(input_data)
    return hdi

# Function to check if the input year is within a certain range
def check_year_range(year):
    # Define your range (adjust as needed)
    start_year = 2024
    end_year = 2027
    
    return start_year <= year <= end_year

# Main Streamlit app
st.title('HDI Prediction App')

# Input form for user
st.sidebar.header('User Input')
year = st.sidebar.slider('Enter the year', min_value=2023, max_value=2027)


# Define a list of options for the dropdown
options = countries.values
op=[]
for i in options:
    op.append(i[0])
# Create the dropdown menu and get the selected option
country = st.sidebar.selectbox('Select a Country', op)
country_index=op.index(country)
# Display the selected option
st.write(f'You selected: {country}')

income_index = st.sidebar.slider('Enter the income index', min_value=0.0, max_value=1.0, step=0.01)
education_index = st.sidebar.slider('Enter the education index', min_value=0.0, max_value=1.0, step=0.01)
life_index = st.sidebar.slider('Enter the life index', min_value=0.0, max_value=1.0, step=0.01)

# Check if the input year is within the allowed range
if not check_year_range(year):
    st.warning(f'The year {year} is out of range. Please enter a year between 2024 and 2027.')
else:
    # Display HDI prediction
    predicted_hdi = predict_hdi(country,year)
    st.success(f'Predicted HDI for {country} in {year}: {predicted_hdi}')

# Display graph of HDI over the years
st.header('HDI Over the Years')
# Assuming you have a DataFrame 'df' with columns 'Year', 'Country', and 'HDI'
# Replace this with your actual data
# df = pd.read_csv('your_data.csv')
# st.line_chart(df[df['Country'] == country].set_index('Year')['HDI'])




    
    # Load the data from 'pred.csv'
pred_data_I = pd.read_csv('Income_pred_hyperparamless.csv')
pred_data_E = pd.read_csv('Education_pred_hyperparamless.csv')
pred_data_L = pd.read_csv('Life_pred_hyperparamless.csv')
pred_data=pd.DataFrame()

# Calculate the new attribute based on the existing ones
pred_data['HDI'] = (pred_data_I[country] * pred_data_E[country] * pred_data_L[country]) ** (1/3)
pred_data['User_HDI']=calculate_hdi(life_index,education_index,income_index)
graph_data = pred_data[['HDI', 'User_HDI']]
# Input form for predicting future HDI
graph_sec=pd.DataFrame([pred_data_I[country],pred_data_E[country],pred_data_L[country]],columns=["Income","Education","Life"])
graph_sec['edu']=pred_data_E[country]
graph_sec['inc']=pred_data_I[country]
graph_sec['life']=pred_data_L[country]
st.line_chart(graph_data)
#st.line_chart(graph_sec)