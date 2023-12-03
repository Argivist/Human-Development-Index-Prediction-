# HDI Prediction Project

## Overview

This project involves predicting the Human Development Index (HDI) for different countries based on income, education, and life indices. It encompasses various components such as data preprocessing, feature engineering, model training, and a Streamlit app for user interaction.


## Dataset Information

The dataset utilized in this project is sourced from the World Development Indicators database, last updated on October 26, 2023. It encompasses a range of indicators related to economic, health, education, and demographic aspects, providing valuable insights into various facets of development.

### Key Indicators and Definitions

1. **GNI (current US$)**
   - Definition: Sum of value added by all resident producers plus any product taxes (less subsidies) in current U.S. dollars.
   - Source: World Bank national accounts data and OECD National Accounts data files.
   - [More Info](https://datacatalog.worldbank.org/public-licenses#cc-by)

2. **GNI per capita, PPP (current international $)**
   - Definition: GNI per capita expressed in current international dollars converted by purchasing power parity (PPP) conversion factor.
   - Source: Economic Policy & Debt: Purchasing power parity.
   - [More Info](https://datacatalog.worldbank.org/public-licenses#cc-by)

3. **Life expectancy at birth, total (years)**
   - Definition: Number of years a newborn infant would live if prevailing mortality patterns at its birth remained constant.
   - Source: United Nations Population Division and various statistical publications.
   - [More Info](https://datacatalog.worldbank.org/public-licenses#cc-by)

4. **GNI per capita, PPP (constant 2017 international $)**
   - Definition: GNI per capita based on purchasing power parity rates in constant 2017 international dollars.
   - Source: International Comparison Program, World Bank | World Development Indicators database.
   - [More Info](https://datacatalog.worldbank.org/public-licenses#cc-by)

5. **Education Duration**
   - Primary, preprimary, and secondary education duration measured in years.
   - Source: UNESCO Institute for Statistics.
   - [More Info](https://datacatalog.worldbank.org/public-licenses#cc-by)

6. **Total Population**
   - Definition: Total population based on the de facto definition, regardless of legal status or citizenship.
   - Source: United Nations Population Division and various statistical publications.
   - [More Info](https://datacatalog.worldbank.org/public-licenses#cc-by)
### Notes and Considerations

- The dataset covers economic, health, education, and demographic indicators from diverse sources such as national accounts data, statistical publications, and international organizations.
- Data quality and reliability, especially in demographic statistics, may vary due to limitations in resources and collection methods, particularly in developing countries.
- The included license URLs provide information regarding usage rights and permissions for this dataset.

Understanding these indicators and their sources is crucial for comprehensive analysis and interpretation within the context of economic, health, education, and population trends.

## Files

- **App.py**: Streamlit app allowing users to input country, indices, and year to predict HDI.
- **country_list.csv**: CSV file containing a list of country names.
- **FeatureEngineering.py**: Python script for feature engineering on World Development Indicators data.
- **Income_pred_hyperparamless.csv**: Predicted income index data.
- **Education_pred_hyperparamless.csv**: Predicted education index data.
- **Life_pred_hyperparamless.csv**: Predicted life expectancy index data.
- **best_model_hyperless.pkl (not provided)**: The trained LSTM models used for predictions.
- **000_Original_.csv**: World Development Indicators dataset.
- **HDI_Model_Training.ipynb**: Jupyter Notebook for training the LSTM models.

## Description

### App.py
- Utilizes Streamlit for a user-friendly interface.
- Loads predicted index data for countries and predicts HDI based on user inputs.
- Visualizes HDI trends over the years for selected countries.

### FeatureEngineering.py
- Preprocesses the '000_Original_.csv' dataset.
- Calculates Life Expectancy, Education, and Income Indices for each country.
- Saves individual country data after interpolation and resampling.

### HDI_Model_Training.ipynb
- Jupyter Notebook containing the code for training LSTM models on the prepared data.
- Includes data splitting, scaling, model building, and evaluation.

### Models
- Trained LSTM models (not provided) used for predicting future index values.

## Usage

1. **Feature Engineering**: Run FeatureEngineering.py to preprocess and engineer features.
2. **Model Training**: Utilize HDI_Model_Training.ipynb to train your LSTM models and save them as 'YourModel.h5'.
3. **App Execution**: Run App.py to interact with the HDI prediction interface.
4. **Data Files**: Ensure 'Income_pred_hyperparamless.csv', 'Education_pred_hyperparamless.csv', and 'Life_pred_hyperparamless.csv' exist for predictions.

## Additional Notes

- Ensure you have the necessary dependencies installed (Streamlit, pandas, numpy, etc.).
- Modify file paths and update 'YourModel.h5' with your trained models for the app to function properly.
- Adjust the range for the year input in the Streamlit app as needed.

## Video Demo

For a video demonstration of the app, check [here](https://youtu.be/Or3Q9MA9Dw0).
