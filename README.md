# House Prices ML
![](media/amiresponsive.png)

Click [here](https://house-prices-ml.onrender.com/) to view the live site.

# Overview

This House-Price project utilises machine learning to build a functional data app for predicting the Sale Price of a house, presented on an interactive Streamlit dashboard, hosted on Rendor. The project is for educational purposes only and includes usage of Machine Learning Python Packages, Data analysis, Data visualisation tools, and Streamlit. 

The project was designed to help a client maximise the sale prices of houses they have inherited in Ames, Iowa. To achieve this, the client has provided a dataset that contains historical house sale prices and associated features of each property. The project goals are to identify the expected sale price for these homes and to analyse how specific property features influence the price. 

To ensure a structured and systematic approach, the project follows the Cross Industry Standard Process for Data Mining (CRISP-DM). This six-phase methodology provides a comprehensive framework for navigating the data science life cycle, from understanding the business problem to delivering actionable insights.

This was my fifth Milestone project with Code Institute and focusses not only on the code and presentation of the application, but the logic behind the analysis and interpretation of the data.

## Dataset Content

* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data). 
* The dataset has almost 1.5 thousand rows and represents housing records from Ames, Iowa, indicating house profile (Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built) and its respective sale price for houses built between 1872 and 2010.

|Variable|Meaning|Units|
|:----|:----|:----|
|1stFlrSF|First Floor square feet|334 - 4692|
|2ndFlrSF|Second-floor square feet|0 - 2065|
|BedroomAbvGr|Bedrooms above grade (does NOT include basement bedrooms)|0 - 8|
|BsmtExposure|Refers to walkout or garden level walls|Gd: Good Exposure; Av: Average Exposure; Mn: Minimum Exposure; No: No Exposure; None: No Basement|
|BsmtFinType1|Rating of basement finished area|GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinshed; None: No Basement|
|BsmtFinSF1|Type 1 finished square feet|0 - 5644|
|BsmtUnfSF|Unfinished square feet of basement area|0 - 2336|
|TotalBsmtSF|Total square feet of basement area|0 - 6110|
|GarageArea|Size of garage in square feet|0 - 1418|
|GarageFinish|Interior finish of the garage|Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage|
|GarageYrBlt|Year garage was built|1900 - 2010|
|GrLivArea|Above grade (ground) living area square feet|334 - 5642|
|KitchenQual|Kitchen quality|Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor|
|LotArea| Lot size in square feet|1300 - 215245|
|LotFrontage| Linear feet of street connected to property|21 - 313|
|MasVnrArea|Masonry veneer area in square feet|0 - 1600|
|EnclosedPorch|Enclosed porch area in square feet|0 - 286|
|OpenPorchSF|Open porch area in square feet|0 - 547|
|OverallCond|Rates the overall condition of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|OverallQual|Rates the overall material and finish of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|WoodDeckSF|Wood deck area in square feet|0 - 736|
|YearBuilt|Original construction date|1872 - 2010|
|YearRemodAdd|Remodel date (same as construction date if no remodelling or additions)|1950 - 2010|
|SalePrice|Sale Price|34900 - 755000|

## Business Requirements

You are requested by your friend, who has received an inheritance from a deceased great-grandfather located in Ames, Iowa, to  help in maximising the sales price for the inherited properties.

Although your friend has an excellent understanding of property prices in her own state and residential area, she fears that basing her estimates for property worth on her current knowledge might lead to inaccurate appraisals. What makes a house desirable and valuable where she comes from might not be the same in Ames, Iowa. She found a public dataset with house prices for Ames, Iowa, and will provide you with that.

* 1 - The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualisations of the correlated variables against the sale price to show that.
* 2 - The client is interested in predicting the house sale price from her four inherited houses and any other house in Ames, Iowa.

## Hypothesis and how to validate?

### Hypothesis 1

Larger houses have a higher sale price than smaller houses (area).
* A correlation study is required to test this hypothesis

### Hypothesis 2

Newer houses, or recently remodelled houses are more expensive than older 
houses.
* A correlation study is required to test this hypothesis

### Hypothesis 3

Houses in the best condition command the highest prices.
* A correlation study is required to test this hypothesis

## Rationale to map the business requirements to the data visualizations and Machine Learning task

### Business Requirement 1: Data Visualization and Correlation Study
  - We will load, inspect, evaluate, clean and feature engineer the data related to the houses provided by the client.
  - We will conduct a correlation study to understand how each variable correlates with Sale Price of a house.
  - We will use the visual representations of the data to test our hypotheses and fulfill the business requirements.
For more information, please visit the "CorrelationStudy" notebook.

### Business Requirement 2: Regression Pipeline
  - We want to be able to predict the sale price of the 4 inherited houses for our client, and any other house in Ames, Iowa.
  - We will identify the data variables (property attributes) necessary to make a prediction about the sale price.
  - We will run a regression model to predict the sale price from the selected variables.
  - We will clean and feature engineer the data to prepare it for machine learning. 
  - We obtain the R2 score and Mean Absolute Error.

## ML Business Case
  - We need to implement an ML model to predict the sale price of a house. Data analytics alone will not be sufficient to meet the business requirements. As the target variable (SalePrice) is a continuous numeric value, we will use a Regression Model.
  - The target variable is already identified so the model will be supervised.
  - As agreed with the client, model success will be defined by an R2 score of at least 0.7 on the Train and Test Set.
  - The ML model will be considered expired if after a period of 12 months the models predictions are more than 40% different from the actual sale price, on more than 30% of predictions.
  - The ML model should predict the sale price in USD if all necessary input variables (house attributes) are provided.
  - The client will be provided with an interactive dashboard which will faciliate the sale pice predictions of all houses in Ames, Iowa (including the inherited ones).

___________________________
  

## Dashboard Design

### Page 1 | Project Summary
* Explain the project, terms & jargon
* Describe Project Dataset
* State Business Requirements

### Page 2 | Sale Price Study
* Satisfy Business Requirement 1

### Page 3 | Sale Price Predictor
* Satisfy Business Requirement 2
* Display predicted `SalePrice` for the 4 inherited houses.
* Allow user to input property data to predict `SalePrice' of any house.
* "Run Predictive Analysis" button passes user data into the ML pipeline
* Predicted `SalePrice` is displayed to the user.

### Page 4 | Hypothesesis - Testing and Validation

### Page 5 | ML Pipeline


## Deployment

### Rendor



### Forking the GitHub Repository

By forking the GitHub Repository you will be able to make a copy of the original repository on your own GitHub account allowing you to view and/or make changes without affecting the original repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](repo here???)
2. At the top of the Repository (not top of page) just above the "Settings" button on the menu, locate the "Fork" button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/Code-Institute-Solutions/milestone-project-heritage-housing-issues)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open commandline interface on your computer
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

## Main Data Analysis and Machine Learning Libraries

* Here you should list the libraries you used in the project and provide example(s) of how you used these libraries.

## Credits

* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism.
* You can break the credits section up into Content and Media, depending on what you have included in your project.

### Content

* The text for the Home page was taken from Wikipedia Article A
* Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
* The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

* The photos used on the home and sign-up page are from This Open Source site
* The images used for the gallery page were taken from this other open-source site

## Acknowledgements (optional)


* In case you would like to thank the people that provided support through this project.

