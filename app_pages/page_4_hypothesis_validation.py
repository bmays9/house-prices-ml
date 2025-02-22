import streamlit as st

def page4_hypothesis_validation_body():
    st.write("### Project Hypotheses and Validation")
	
    st.write(
        f"For the detailed validation of each Hypothesis, please "
        f"visit the CorrelationStudy Notebook."
    )

    st.info(
        f"#1: Larger houses have a higher sale price than smaller houses "
        f"(area)\n"
    )

    st.success(
        f"**True**. \n"
        f"The hypothesis is proved to be valid - larger houses do command \n"
        f"higher sale prices.\n"
        f"`GarageArea` `GrLivArea`, `TotalBsmtSF` all correlate positively "
        f"with the sale price."
)
    
    st.info(
        f"#2: Newer houses and recently remodelled / improved houses are "
        f"more expensive than older houses.\n"
        )

    st.success(
        f"**True**. \n"
        f"There is a positive correlation between `SalePrice` and each "
        f"of the variables `YearBuilt` and `YearRemodAdd`. There is a "
        f"noticable correlation between both variables that prove the "
        f"hypothesis is true."
)
    
    st.info(
        f"3: Houses in the best condition command the highest prices.\n"
    )

    st.error(f"**False**. \n"
        f"Our study showed that the houses with the highest sale prices are not "
        f"those in the best condition. \n"
        f"Houses with the best rating for `OverallCond` have not sold for "
        f"over 500,000 USD. Many houses with an `OverallCond` rating of 5 have "
        f"a sale price in excess of 500,000 USD more expensive than older "
        f"houses.\n"
)


