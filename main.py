import streamlit as st
import pandas as pd

df = pd.read_csv("CPA.csv")

st.title("College Predictor - MK97")
st.write("This is a simple college predictor app Based on MHTCET marks.")
st.subheader("Enter your MHTCET Percentile")
mhtcet_percentile = st.number_input("MHTCET Percentile", min_value=0.0, max_value=100.0, step=0.01, format="%.2f")
category = st.selectbox("Category", ["General", "OBC", "SC", "ST", "EWS"])
preferred_branch = st.selectbox("Preferred Branch", ["Computer Engineering","IOT & Cyber Security Including Blockchain", "Information Technology", "Electronics & Telecommunication Eng.", "Mechanical Engineering", "Civil Engineering","Electronics and Computer Engineering","Artificial Intelligence and Data Science"])
if st.button("Predict College"):
    
    filtered = df[(df['Percentile'] <= mhtcet_percentile) & (df['Branch'] == preferred_branch) & (df['Category'] == category)]
    if preferred_branch:
        filtered = filtered[filtered['Branch'].str.contains(preferred_branch, case=False)]
    if not filtered.empty:
        st.success(f"Based on your MHTCET percentile of {mhtcet_percentile} and preferred branch '{preferred_branch}', you can consider the following colleges:{len(filtered)}")
        st.dataframe(filtered.sort_values(by='Percentile', ascending=False))
    else:
        st.error("No colleges found matching your criteria. Please try different inputs.")
        