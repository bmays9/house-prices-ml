import streamlit as st
from src.data_management import load_house_sales_data
import matplotlib.pyplot as plt
import numpy as np
import ppscore as pps
from feature_engine.discretisation import ArbitraryDiscretiser
import seaborn as sns
sns.set_style("whitegrid")

def page2_sale_price_study_body():
    """
    Use data visualistions to display correlated feature study
    """
    
    # Load data
    df = load_house_sales_data()

    # From CorrelationStudy notebook
    vars_to_study = ['OverallQual', 'GrLivArea', 'GarageArea',
                     'TotalBsmtSF', '1stFlrSF','YearBuilt']
    
    st.write("## Housing Price Correlation Study | Business Requirement 1")
    st.info(
        f"* **Business Requirement** - The client is interested in discovering "
        f"how house attributes correlate with sale prices. Therefore, the "
        f"client expects data visualizations of the correlated variables "
        f"against the sale price.")


    # inspect data
    if st.checkbox("Inspect House Data"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns."
            f"An example of the data is displayed below."
            f"10 rows of data is displayed, with each row representing one "
            f"property.")

        st.write(df.head(10))
        
        st.write("---")

    # Correlation Study Summary

    st.write(
        f"* A correlation study was conducted in the notebook to better "
        f"understand how the variables are correlated to our target variable, "
        f"the Sale Price. \n"
        f"Our analysis revealed the most correlated variables are: \n"
        f"**{vars_to_study}**")

# Text based on "04 - CorrelationStudy" notebook - "Conclusions" section
    st.info(
        f"Conclusions"
    )