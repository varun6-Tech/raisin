import streamlit as st
import pickle
import pandas as pd

# ---------------- Page Configuration ----------------
st.set_page_config(
    page_title="🍇 Raisin Classifier",
    page_icon="🍇",
    layout="centered"
)

# ---------------- Load Model ----------------
with open("random_forest.pkl", "rb") as file:
    model = pickle.load(file)

# ---------------- Custom CSS ----------------
st.markdown("""
<style>
.main{
    background-color:#f5f7fa;
}
.title{
    text-align:center;
    color:#6a1b9a;
    font-size:38px;
    font-weight:bold;
}
.subtitle{
    text-align:center;
    color:gray;
    font-size:18px;
}
.stButton>button{
    width:100%;
    background-color:#6a1b9a;
    color:white;
    font-size:18px;
    border-radius:10px;
}
.stButton>button:hover{
    background-color:#8e24aa;
}
</style>
""", unsafe_allow_html=True)

# ---------------- Heading ----------------
st.markdown("<p class='title'>🍇 Raisin Classification App</p>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Predict whether the raisin is <b>Kecimen</b> or <b>Besni</b>.</p>", unsafe_allow_html=True)

st.divider()

# ---------------- Inputs ----------------
Area = st.number_input("Area", min_value=0.0, format="%.2f")
MajorAxisLength = st.number_input("MajorAxisLength", min_value=0.0, format="%.2f")
MinorAxisLength = st.number_input("MinorAxisLength", min_value=0.0, format="%.2f")
Eccentricity = st.number_input("Eccentricity", min_value=0.0, format="%.4f")
ConvexArea = st.number_input("ConvexArea", min_value=0.0, format="%.2f")
Extent = st.number_input("Extent", min_value=0.0, format="%.4f")
Perimeter = st.number_input("Perimeter", min_value=0.0, format="%.2f")

# ---------------- Prediction ----------------
if st.button("🔍 Predict"):

    input_data = pd.DataFrame({
        "Area":[Area],
        "MajorAxisLength":[MajorAxisLength],
        "MinorAxisLength":[MinorAxisLength],
        "Eccentricity":[Eccentricity],
        "ConvexArea":[ConvexArea],
        "Extent":[Extent],
        "Perimeter":[Perimeter]
    })

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("✅ Prediction: **Kecimen Raisin**")
        st.balloons()
    else:
        st.success("✅ Prediction: **Besni Raisin**")
        st.balloons()

st.divider()

st.info("Model: Random Forest Classifier")