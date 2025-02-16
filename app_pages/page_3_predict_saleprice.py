import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_house_sales_data, load_inherited_house_data, load_pkl_file
# from src.machine_learning.predictive_analysis_ui import predict_sale_price
from datetime import date

def page3_predict_saleprice_body():
    
    version = 'v1'
