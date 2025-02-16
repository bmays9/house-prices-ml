import streamlit as st
from app_pages.multipage import MultiPage

from app_pages.page_1_project_summary import page1_body
from app_pages.page_2_sale_price_study import page2_sale_price_study_body
from app_pages.page_3_predict_saleprice import page3_predict_saleprice_body
from app_pages.page_4 import page4_body
from app_pages.page_5_ml_predict import page_5_ml_predict_body

app = MultiPage(app_name="House Price Predict") 

app.app_page("P1 - Project Summary", page1_body)
app.app_page("P2 - Sale Price Study", page2_sale_price_study_body)
app.app_page("P3 - Predict Sale Price", page3_predict_saleprice_body)
app.app_page("P4 - ", page4_body)
app.app_page("P5 - ML | Predict Sale Price", page_5_ml_predict_body)

app.run()