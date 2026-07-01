import streamlit as st
import pickle
import pandas as pd

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="🍇 AI Raisin Classifier",
    page_icon="🍇",
    layout="wide"
)

# -----------------------------
# Load Model
# -----------------------------
with open("random_forest.pkl", "rb") as file:
    model = pickle.load(file)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

/* Background */
.stApp{
    background: linear-gradient(135deg,#0f172a,#1e3a8a,#7c3aed);
    background-size: cover;
}

/* Hide Streamlit Menu */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* Title */
.title{
    text-align:center;
    font-size:52px;
    font-weight:800;
    color:white;
}

.subtitle{
    text-align:center;
    font-size:20px;
    color:#e2e8f0;
    margin-bottom:25px;
}

/* Glass Card */

.glass{
    background: rgba(255,255,255,0.12);
    backdrop-filter: blur(18px);
    border-radius:20px;
    padding:25px;
    border:1px solid rgba(255,255,255,0.2);
    box-shadow:0px 8px 30px rgba(0,0,0,0.4);
}

/* Input */

.stNumberInput label{
    color:white;
    font-weight:bold;
}

/* Button */

.stButton>button{
    width:100%;
    height:60px;
    font-size:22px;
    border-radius:15px;
    border:none;
    color:white;
    background:linear-gradient(90deg,#ff512f,#dd2476);
    transition:0.4s;
    font-weight:bold;
}

.stButton>button:hover{
    transform:scale(1.03);
    background:linear-gradient(90deg,#dd2476,#ff512f);
}

/* Prediction Card */

.result{
    text-align:center;
    padding:25px;
    border-radius:15px;
    background:#ffffff;
    color:#111827;
    font-size:28px;
    font-weight:bold;
}

/* Sidebar */

section[data-testid="stSidebar"]{
    background:#111827;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------
st.markdown("<div class='title'>🍇 AI Raisin Classification</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Random Forest Machine Learning Model</div>", unsafe_allow_html=True)

st.write("")

# -----------------------------
# Layout
# -----------------------------
left,right=st.columns([2,1])

with left:

    st.markdown("<div class='glass'>",unsafe_allow_html=True)

    st.subheader("📊 Enter Raisin Features")

    col1,col2=st.columns(2)

    with col1:
        Area=st.number_input("Area",0.0,format="%.2f")
        MajorAxisLength=st.number_input("Major Axis Length",0.0,format="%.2f")
        MinorAxisLength=st.number_input("Minor Axis Length",0.0,format="%.2f")
        Eccentricity=st.number_input("Eccentricity",0.0,format="%.4f")

    with col2:
        ConvexArea=st.number_input("Convex Area",0.0,format="%.2f")
        Extent=st.number_input("Extent",0.0,format="%.4f")
        Perimeter=st.number_input("Perimeter",0.0,format="%.2f")

    st.write("")

    predict=st.button("🚀 Predict Raisin Type")

    st.markdown("</div>",unsafe_allow_html=True)

with right:

    st.markdown("<div class='glass'>",unsafe_allow_html=True)

    st.metric("🌟 Model","Random Forest")

    st.metric("📈 Accuracy","97%")

    st.metric("🍇 Classes","2")

    st.metric("🤖 Status","Ready")

    st.markdown("</div>",unsafe_allow_html=True)

# -----------------------------
# Prediction
# -----------------------------
if predict:

    df=pd.DataFrame({

        "Area":[Area],
        "MajorAxisLength":[MajorAxisLength],
        "MinorAxisLength":[MinorAxisLength],
        "Eccentricity":[Eccentricity],
        "ConvexArea":[ConvexArea],
        "Extent":[Extent],
        "Perimeter":[Perimeter]

    })

    prediction=model.predict(df)[0]

    st.write("")

    if prediction==1:

        st.markdown("""
        <div class='result'>
        🍇 KECIMEN RAISIN
        </div>
        """,unsafe_allow_html=True)

        st.balloons()

    else:

        st.markdown("""
        <div class='result'>
        🍇 BESNI RAISIN
        </div>
        """,unsafe_allow_html=True)

        st.balloons()

# -----------------------------
# Footer
# -----------------------------
st.write("")
st.markdown(
"""
<center style='color:white'>
Made with ❤️ using Streamlit & Random Forest
</center>
""",
unsafe_allow_html=True
)