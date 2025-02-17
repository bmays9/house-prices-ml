import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_house_sales_data, load_inherited_house_data, load_pkl_file
from src.machine_learning.predictive_analysis_ui import predict_sale_price
from datetime import date

def page3_predict_saleprice_body():
    
    # load predict sale_price files
    version = 'v1'
    sale_price_pipe = load_pkl_file(
        f"outputs/ml_pipeline/predict_saleprice/{version}/regressor_pipeline.pkl")
    sale_price_features = (
        pd.read_csv(f"outputs/ml_pipeline/predict_saleprice/{version}/X_train.csv")
        .columns
        .to_list())

    st.write("### Predict Sale Price of Inherited Houses")
    # display client's query and its data
    st.info(
        f"#### Business Requirement 2\n"
        f"* Firstly, the client is interested in the sale price prediction for "
        f"the 4 inherited houses.")
    st.write(f"###### Predicted sales price of the 4 inherited houses\n")
    
    
    st.write("### Predict Sale Price of Any House")
    # display client's query and its data
    st.info(
        f"#### Business Requirement 2\n"
        f"* Secondly, the client is interested in the sale price prediction for "
        f"any house in Ames, Iowa.")

    st.write("---")
    st.write("Please enter the known property information below. "
	"Any missing data will be set to the median value. ")

    # Generate Live Data
    X_live = DrawInputsWidgets()

    # predict using live data
    if st.button("Run Predictive Analysis"):
        prediction_value = predict_sale_price(
            X_live, sale_price_features, sale_price_pipe)


def DrawInputsWidgets():

    # load dataset
    df = load_house_sales_data()
    percentageMin, percentageMax = 0.4, 2.0

# we create input widgets only for our 6 features
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
    col5, col6 = st.columns(2)

    # We are using these features to feed the ML pipeline 
    # values copied from check_variables_for_UI() result

    # create an empty DataFrame, which will be the live data
    X_live = pd.DataFrame([], index=[0])

    # from here on we draw the widget based on the variable type (numerical or categorical)
    # and set initial values

# ['GrLivArea', 'GarageArea', 'TotalBsmtSF', '1stFlrSF','YearBuilt', 'OverallQual']
    with col1:
        feature = "OverallQual"
        st_widget = st.selectbox(
			label= feature,
			options=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
			index = int(df[feature].median())
        )
    X_live[feature] = st_widget

    with col2:
        feature = "GarageArea"
        st_widget = st.number_input(
            label=f"{feature} | Area of Garage in Sq.Feet",
            min_value= int(df[feature].min()*percentageMin), 
			max_value= int(df[feature].max()*percentageMax),
			value= int(df[feature].median()), 
            step= 50
        )
    X_live[feature] = st_widget

    with col3:
        feature = "TotalBsmtSF"
        st_widget = st.number_input(
            label=f"{feature} | Basement Area in Sq.Feet",
            min_value=int(df[feature].min()*percentageMin),
            max_value=int(df[feature].max()*percentageMax),
            value=int(df[feature].median()),
            step= 50
        )
    X_live[feature] = st_widget

    with col4:
        feature = "1stFlrSF"
        st_widget = st.number_input(
            label=f"{feature} | Area of 1st Floor in Sq.Feet",
            min_value=int(df[feature].min()*percentageMin),
            max_value=int(df[feature].max()*percentageMax),
            value=int(df[feature].median()),
            step= 50
        )
    X_live[feature] = st_widget

    with col5:
        feature = "YearBuilt"
        st_widget = st.number_input(
            label=f"{feature} | Year the house was built",
			min_value= int(df[feature].min()*percentageMin), 
			max_value= date.today().year,
			value= int(df[feature].median()), 
            step= 1
        )
    X_live[feature] = st_widget

    with col6:
        feature = "OverallQual"
        st_widget = st.number_input(
            label="{feature} | Overall material + finish rating",
            min_value= 0, 
			max_value= 10,
			value= int(df[feature].median()), 
            step= 1
        )
    X_live[feature] = st_widget

    return X_live

