import streamlit as st


def predict_sale_price(X_live, house_features, sale_price_pipeline):

    # Code inspired by the Churnometer walkthrough project.
    # from live data, subset features related to this pipeline
    X_live_sale_price = X_live.filter(house_features)

    # predict
    sale_price_prediction_proba = sale_price_pipeline.predict(X_live_sale_price)

    # create logic to display the results
    proba = sale_price_prediction_proba
    value = float(proba[0].round(1))
    amount = '${:,.2f}'.format(value)

    st.write(f"The predicted Sale Price for this property is: **{amount}**")
    