import os
import pandas as pd
import csv
import math
import numpy as np

#Doc info
#Data from database: World Development Indicators
#Last Updated: 10/26/2023


missing_limit=0.5;
df=pd.read_csv("000_Original_.csv")# https://databank.worldbank.org/source/world-development-indicators# 

def check_file_exists(filename):
    return os.path.isfile(filename)

def add_noise(series, noise_level):
    return series + noise_level * np.random.randn(len(series))
#life expectancy index
def LifeExpectancyIndex(l):
    l=l
    return (l-20)/(85-20)   #https://www.azcalculator.com/  https://ourworldindata.org/life-expectancy 



#income index
def IncomeIndex(i):
    return (math.log(i)-math.log(100))/(math.log(75000)-math.log(100))
    
country_list=[]
# Assuming df is your DataFrame
countries = df['Country Name'].unique()

for country in countries:
    
    # Filter the DataFrame for each country
    df_country = df[df['Country Name'] == country]
    
    # Drop the 'Country Name' column as it's no longer needed
    df_country = df_country.drop(columns=['Country Name'])
    
    # Set 'Series Name' as the index
    df_country = df_country.set_index('Series Name')
    

    # Transpose the DataFrame so that the features become columns
    df_country = df_country.transpose()

    # Extract the year part from the index
    df_country.index     = df_country.index.str.extract('(\d{4})').squeeze()
    
    # Convert the index to a DatetimeIndex
    df_country.index = pd.to_datetime(df_country.index , errors='coerce')
    
    # Drop rows where the year couldn't be extracted
    df_country = df_country[df_country.index.notna()]
    
    #interpolating missing data
    for cols in df_country.columns:
        df_country[cols] = df_country[cols].interpolate(method='time')
    
    # Calculate indices and add them to the DataFrame
    if 'Preprimary education, duration (years)' in df_country.columns:
        df_country['Expected Years of Schooling'] = df_country['Preprimary education, duration (years)']+df_country['Primary education, duration (years)'] + df_country['Secondary education, duration (years)'] +4
    else:
        print("Column 'Preprimary education, duration (years)' does not exist in df_country")
    df_country['GNI per capital']=df_country['GNI (current US$)']/df_country['Population, total']
    # Calculate indexis
    
 

    df_country['Life Expectancy Index'] = df_country['Life expectancy at birth, total (years)'].apply(LifeExpectancyIndex)
    df_country['Education Index'] = df_country['Expected Years of Schooling'] / 18
    df_country['Income Index'] = df_country['GNI per capital'].apply(IncomeIndex)
    
    df_country['Life Expectancy Index'] = df_country['Life Expectancy Index'].astype(float)
    df_country['Income Index'] = df_country['Income Index'].astype(float)
    df_country['Education Index'] = df_country['Education Index'].astype(float)

    df_country['Human Development Index'] = (df_country['Life Expectancy Index']*df_country['Income Index']*df_country['Education Index'])**(1/3)

    key_Cols=['Life Expectancy Index','Education Index','Income Index']
    
    if ((df_country[key_Cols[0]].isnull().sum()/len(df_country[key_Cols[0]]) > missing_limit) or 
    (df_country[key_Cols[1]].isnull().sum()/len(df_country[key_Cols[1]]) > missing_limit) or 
    (df_country[key_Cols[2]].isnull().sum()/len(df_country[key_Cols[2]]) > missing_limit)):
            pass
    else:
        for cols in df_country.columns:
            df_country[cols] = df_country[cols].interpolate(method='time',limit_direction='both')
        df_country['Year'] = pd.to_datetime(df_country.index)
        # Set 'Year' as the index
        df_country.set_index('Year', inplace=True)
        df_country_ = df_country.resample('MS').interpolate(method='linear')
        df_country_=df_country_.apply(add_noise,noise_level=0)
        df_country_.to_csv(f'data//{country}.csv')
        print(f'data//{country}.csv saved')
        country_list.append(country)

# Assuming country_list is your list of country names
with open('country_list.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Country Name'])
    for country in country_list:
        writer.writerow([country])