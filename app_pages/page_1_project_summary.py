import streamlit as st

def page1_body():
    # Renders summary page.
    st.header("**Project Summary**")

    st.success(
        f"House Price Predict is a project designed to predict sales prices "
        f"for houses in Ames, Iowa. Our client has inherited four properties "
        f"and asked us to maximise the sale price of these houses. We also "
        f"have to show which house properties correlate most strongly with the "
        f"sale price. The client has provided a publicly available dataset "
        f"which we will use to conduct our study." 
    )

    # Dataset
    st.subheader(f"**Datasets**")
    st.write(
        f"The dataset has 1460 rows and represents housing records from Ames,"
        f"Iowa. Each row indicates the house profile (Floor Area, Basement,"
        f"Garage, Kitchen, Lot, Porch, Wood Deck, Year Built etc. ) and its"
        f"respective sale price, for houses built between 1872 and 2010."
        f"The data set has been uploaded to kaggle and dowloaded to this"
        f"project for study."
        )

    st.write(f"The data set is available here: "
             f"[kaggle](\
        https://www.kaggle.com/datasets/codeinstitute/housing-prices-data).")


    # Business Requirements
    st.subheader(f"**Business Requirements**")
    st.write(f"The project has two business requirements:")
    st.write(f"1: The client is interested in discovering how the house "
             f"attributes correlate with the sale price. Therefore, "
             f"the client expects data visualisations of the correlated "
             f"variables against the sale price to demonstrate our findings.")
    st.write(f"2: The client is interested in predicting the house sale price "
             f"from her four inherited houses and any other house in Ames, "
             f"Iowa.")

 

    # Project terminology
    st.subheader(f"**Project Terms & Jargon**")
    st.info(f"* **Features / Attributes**: The individual characteristics of a "
            f"house.\n"
            f"* **Target**: The characteristic we are interested in predicting."
            f"In this project, the target is Sale Price.\n"
            f"* **Saleprice**: The price at which a house has been sold in "
            f"USD.\n"           
            f"* **Inherited house**: A house the client has inherited and "
            f"wishes to sell. Property information has been provided.\n")


    # Link to project README file on GitHub. 
    st.write(
        f"* For full information, please visit the "
        f"[Project README file](\
        https://github.com/bmays9/house-prices-ml/blob/main/README.md)."
        )
