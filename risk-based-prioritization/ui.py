import streamlit as st
from classification import classify_risk
from priority import priority_score, adjusted_score
from risk_keywords import calculate_keyword_risk

st.set_page_config(page_title="QA Risk Prioritization", page_icon="⚠️")

st.title("⚠️ AI QA Risk-Based Prioritization")

st.write("Enter a requirement to analyze risk level and testing priority.")

module = st.text_input("Module Name")
requirement = st.text_area("Requirement Description")

if st.button("Analyze Risk"):

    keyword_score = calculate_keyword_risk(requirement)
    final_score = adjusted_score(module, keyword_score)
    risk = classify_risk(final_score)
    priority = priority_score(risk)

    st.subheader("Analysis Result")

    # Progress bar
    risk_meter = min(final_score * 10, 100)
    st.progress(risk_meter)

    # Risk level display
    if risk == "High":
        st.markdown("<h3 style='color:red;'>Risk Level: HIGH</h3>", unsafe_allow_html=True)
    elif risk == "Medium":
        st.markdown("<h3 style='color:orange;'>Risk Level: MEDIUM</h3>", unsafe_allow_html=True)
    else:
        st.markdown("<h3 style='color:green;'>Risk Level: LOW</h3>", unsafe_allow_html=True)

    st.write("Keyword Risk Score:", keyword_score)
    st.write("Adjusted Risk Score:", final_score)

    # Priority display
    if priority == "Test First":
        st.markdown("<h3 style='color:red;'>Priority: Test First</h3>", unsafe_allow_html=True)
    elif priority == "Test Soon":
        st.markdown("<h3 style='color:orange;'>Priority: Test Soon</h3>", unsafe_allow_html=True)
    else:
        st.markdown("<h3 style='color:green;'>Priority: Test Later</h3>", unsafe_allow_html=True)