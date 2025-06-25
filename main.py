import streamlit as st
import pandas as pd

df = pd.read_csv("CPA.csv")

st.title("College Predictor - MK97")
st.write("This is a simple college predictor app Based on MHTCET marks.")
st.subheader("Enter your MHTCET Percentile")
mhtcet_percentile = st.number_input("MHTCET Percentile", min_value=0.0, max_value=100.0, step=0.01, format="%.2f")
category = st.selectbox("Category", ['GOPENS', 'GSCS', 'GSTS', 'GVJS', 'GNT1S', 'GNT2S', 'GNT3S', 'GOBCS', 'LOPENS', 'LSCS', 'LSTS', 'LVJS', 'LNT1S', 'LNT2S', 'LNT3S', 'LOBCS', 'PWDOPENS', 'DEFOPENS', 'TFWS', 'EWS', 'PWDROBC', 'SDEFROBCS', 'PWDRSCS', 'DEFROBCS', 'PWDOBCS', 'DEFOBCS', 'S', 'DEFRSCS', 'ORPHAN', 'MI', 'DEFRNT3S', 'SDEFRSCS', 'SDEFRNT2S', 'DEFRNT2S', 'SDEFRVJS', 'PWDRNT2S', 'PWDSCS', 'DEFSCS', 'DEFRNT1S', 'PWDRNT1S', 'PWDRSTS', 'PWDRNT3S', 'DEFRVJS', 'SDEFRNT3S', 'GOPENH', 'GSCH', 'GVJH', 'GNT1H', 'GOBCH', 'LOPENH', 'LOBCH', 'LSCH', 'GNT2H', 'GNT3H', 'LNT1H', 'GSTH', 'LSTH', 'LNT3H', 'PWDOPENH', 'LNT2H', 'LVJH', 'H', 'PWDSCH', 'PWDOBCH', 'PWDRNT1H', 'PWDRSTH', 'GOPENO', 'GSCO', 'GNT3O', 'GOBCO', 'LOPENO', 'GNT2O', 'LSTO', 'LOBCO', 'GSTO', 'GVJO', 'LSCO', 'LNT2O', 'LVJO', 'LNT3O', 'LNT1O', 'GNT1O', 'PWDRSCH', 'PWDRNT2H', 'PWDRVJH'])
preferred_branch = st.selectbox("Preferred Branch", ['Civil Engineering', 'Computer Science and Engineering', 'Information Technology', 'Electrical Engineering', 'Electronics and Telecommunication Engg', 'Instrumentation Engineering', 'Mechanical Engineering', 'Artificial Intelligence (AI) and Data Science', 'Industrial IoT', 'Chemical Engineering', 'Production Engineering', 'Textile Technology', 'Agricultural Engineering', 'Computer Science and Design', 'Plastic and Polymer Engineering', 'Electronics and Computer Engineering', 'Computer Engineering', 'Electronics Engineering', 'Production Engineering[Sandwich]', '303319113K - Civil Engineering', 'Electronics Engineering ( VLSI Design and Technology)', 'Petro Chemical Engineering', 'Dyestuff Technology', 'Oil,Oleochemicals and Surfactants Technology', 'Pharmaceuticals Chemistry and Technology', 'Fibres and Textile Processing Technology', 'Polymer Engineering and Technology', 'Food Engineering and Technology', 'Surface Coating Technology', 'Bio Medical Engineering', 'Electronics and Computer Science'])
if st.button("Predict College"):
    
    filtered = df[(df['Percentile'] <= mhtcet_percentile) & (df['Branch'] == preferred_branch) & (df['Category'] == category)]
    if preferred_branch:
        filtered = filtered[filtered['Branch'].str.contains(preferred_branch, case=False)]
    if not filtered.empty:
        st.success(f"Based on your MHTCET percentile of {mhtcet_percentile} and preferred branch '{preferred_branch}', you can consider the following colleges:{len(filtered)}")
        st.dataframe(filtered.sort_values(by='Percentile', ascending=False))
    else:
        st.error("No colleges found matching your criteria. Please try different inputs.")
        