import streamlit as st
import requests

WEB_APP_URL = "https://script.google.com/macros/s/AKfycbwNuBVelTCDpEbq6SPp79oYGq8HXM346s4vSBTswxxX12khG_5MFz7JPNBGOuJsLjp-WA/exec"

st.set_page_config(page_title="Mini Project Members", page_icon="🎓", layout="centered")
st.title("🎓 K-R-R Mini Project Members Form")
st.write("Each row represents one team of two students. Please ensure no duplicates.")

with st.form("student_form :"):
    st.subheader("Student 1 :")
    last1 = st.text_input("Last Name (Student 1) :")
    first1 = st.text_input("First Name (Student 1) :")
    

    st.subheader("Student 2 :")
    last2 = st.text_input("Last Name (Student 2) :")
    first2 = st.text_input("First Name (Student 2) :")
    

    submitted = st.form_submit_button("Submit")

if submitted:
    if all([first1, last1, first2, last2]):
        data = {
            "first1": first1.strip(),
            "last1": last1.strip(),
            "first2": first2.strip(),
            "last2": last2.strip()
        }
        res = requests.post(WEB_APP_URL, json=data)
        if res.text.strip() == "SUCCESS":
            st.success("✅ Team successfully added !")
        elif res.text.strip() == "DUPLICATE":
            st.warning("⚠️ One or both students already exist in another team!")
        else:
            st.error(f"❌ Unexpected error: {res.text}")
    else:
        st.warning("⚠️ Please fill in all fields before submitting.")
