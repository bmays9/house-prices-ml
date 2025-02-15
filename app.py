import streamlit as st
from app_pages.multipage import MultiPage

from app_pages.page_1_project_summary import page1_body
from app_pages.page_2_sale_price_study import page2_sale_price_study_body
from app_pages.page_3 import page3_body
from app_pages.page_4 import page4_body
from app_pages.page_5 import page5_body

app = MultiPage(app_name="House Price Predict") 

app.app_page("Page 1 - Project Summary", page1_body)
app.app_page("Page 2 - Sale Price Study", page2_sale_price_study_body)
app.app_page("Page 3 - ", page3_body)
app.app_page("Page 4 - ", page4_body)
app.app_page("Page 5 - ", page5_body)

app.run()