import streamlit as st
import pandas as pd
from src.data_management import load_house_sales_data, load_inherited_house_data, load_pkl_file
from src.machine_learning.evaluate_regression import regression_performance
import matplotlib.pyplot as plt

def page_5_ml_predict_body():

    version = 'v1'
    # load needed files

    sale_price_pipe = load_pkl_file(
        f'outputs/ml_pipeline/predict_saleprice/{version}/regressor_pipeline.pkl')
    sale_price_feat_importance = plt.imread(
        f"outputs/ml_pipeline/predict_saleprice/{version}/features_importance.png")
    
    X_train = pd.read_csv(f"outputs/ml_pipeline/predict_saleprice/{version}/X_train.csv")
    X_test = pd.read_csv(f"outputs/ml_pipeline/predict_saleprice/{version}/X_test.csv")
    y_train = pd.read_csv(f"outputs/ml_pipeline/predict_saleprice/{version}/y_train.csv")
    y_test = pd.read_csv(f"outputs/ml_pipeline/predict_saleprice/{version}/y_test.csv")

    st.write("### ML Pipeline: Predict Sale Price")

    # display pipeline training summary conclusions
    st.info(
        f"* The pipeline was created to satisfy Business Requirement 2 for our "
        f"client. Please see Page 1 of the dashboard as a reminder."
        f"A regressor model was chosen to predict the **Sale Price. Data "
        f"cleaing and feature engineering steps have been taken to optimise "
        f"our model."
        f"In agreement with the client, we have set the following targets as a "
        f"measurement of success.")
    st.info(
        f"- Target R2 score: 0.75 on both Train and Test sets"
    )
    st.success(
        f"- TrainSet: R2 score achieved: 0.946 \n"
        f"- TestSet: R2 score achieved: 0.835 \n"
        )

    st.write("---")

    # Display pipeline details
    st.write("* ML pipeline used for predicting Sale Price")
    st.write(sale_price_pipe)
    st.write("---")

    # Display feature importance 
    st.write("---")
    st.write("* The features the model was trained and their importance.")
    st.write(X_train.columns.to_list())
    st.image(sale_price_feat_importance)

    # Evaluate performance of TrainSet and TestSets
    st.write("## Pipeline Performance")
    regression_performance(X_train=X_train, y_train=y_train,
                        X_test=X_test, y_test=y_test,
                        pipeline=sale_price_pipe)

# The Churnometer Project from Code Institute was the basis for the above code,
# with some modifications to adapt to this project.