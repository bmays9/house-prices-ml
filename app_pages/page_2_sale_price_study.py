import streamlit as st
from src.data_management import load_house_sales_data
from src.data_management import load_correlation_data
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
    df_results = load_correlation_data()

    # From CorrelationStudy notebook
    vars_to_study = ['GrLivArea', 'GarageArea', 'TotalBsmtSF',
                     '1stFlrSF','YearBuilt', 'OverallQual']
    
    st.write("## Sale Price Correlation Study | Business Requirement 1")
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
    st.subheader(f"**Conclusions from the Study**")
    st.info(
        f"- Typically, larger houses have a higher sale price.\n"
        f"- Typically, newer houses have a higher sale price.\n"
        f"- The quality of the house correlates positively with the sale " 
        f"price.\n"
        f"- An overall condition rating of at least 5 is required to achieve "
        f"the highest sale prices.\n"
    )

    # Correlation Results
    if st.checkbox("Correlation Results: Target variable = SalePrice"):
        display_correlation_results(df_results) 

    # Variables v Sale Price
    df_eda = df[vars_to_study + ['SalePrice']]
    boxplot_var = ['OverallQual']
    if st.checkbox("SalePrice correlation per variable"):
        target_var = 'SalePrice'
        plot_per_variable(df_eda, boxplot_var, target_var)

     

def plot_per_variable(df_eda, boxplot_var, target_var):
    for col in df_eda.drop([target_var], axis=1).columns.to_list():
        plot_scatter(df_eda, col, target_var)
        if col in boxplot_var:
            plot_boxplot(df_eda, col, target_var)

def plot_scatter(df, col, target_var):
    """
    Generate a scatter plot.
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.regplot(data=df, x=col, y=target_var, ci=None, line_kws={"color": "green"})
    plt.title(f"Scatter plot of {target_var} vs {col}", fontsize=20)
    st.pyplot(fig)

def plot_boxplot(df, col, target_var):
    """
    Generate a box plot.
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.boxplot(data=df, x=col, y=target_var)
    plt.title(f"Scatter plot of {target_var} vs {col}", fontsize=20)
    st.pyplot(fig)


def display_correlation_results(df):
    """
    Generate a bar chart.
    """

    # Set up figure
    fig, ax = plt.subplots(figsize=(10, 6))

    # Get y positions
    y_positions = np.arange(len(df))

    # Plot stacked horizontal bars
    ax.barh(df['Feature'], df['Spearman'], color='blue', label='Spearman')
    ax.barh(df['Feature'], df['Pearson'], color='green', left=df['Spearman'], label='Pearson')

    # Threshold Line 
    ax.axvline(x=1.15, color='red', linestyle='--',
               linewidth=2, alpha= 0.7, label="Threshold = 1.15")
    
    # Labels & Title
    ax.set_xlabel("Correlation Value")
    ax.set_ylabel("Feature")
    ax.set_title("Stacked Correlation Values (Spearman + Pearson)")
    ax.legend()

    # Display in Streamlit
    st.pyplot(fig)