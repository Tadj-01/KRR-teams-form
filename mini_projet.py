import streamlit as st
import requests

# Google Apps Script Web App URL
WEB_APP_URL = "https://script.google.com/macros/s/AKfycbwxOK8vFy1PtkvhqBFjonjgrBAIGXOOedolvH1b8MqOpOG9gW4Iab1b0UPBxzTDSCAE/exec"

st.set_page_config(page_title="Presentation Members Form")
st.title("🎓 A.I Presentation Members Form")
st.write("Each row represents one team of three students. Please fill all fields. No duplicates allowed.")

with st.form("student_form"):
    st.subheader("👤 Student 1 (Required)")
    last1 = st.text_input("Last Name (Student 1):").strip()
    first1 = st.text_input("First Name (Student 1):").strip()

    st.subheader("👥 Student 2 (Required)")
    last2 = st.text_input("Last Name (Student 2):").strip()
    first2 = st.text_input("First Name (Student 2):").strip()

    st.subheader("👥 Student 3 (Required)")
    last3 = st.text_input("Last Name (Student 3):").strip()
    first3 = st.text_input("First Name (Student 3):").strip()

    submitted = st.form_submit_button("Submit")

if submitted:
    # Check all fields are filled
    if not all([first1, last1, first2, last2, first3, last3]):
        st.error("⚠️ Please fill in all fields for all three students.")
    else:
        data = {
            "first1": first1,
            "last1": last1,
            "first2": first2,
            "last2": last2,
            "first3": first3,
            "last3": last3,
        }

        try:
            res = requests.post(WEB_APP_URL, json=data)
            result = res.text.strip().upper()

            if result == "SUCCESS":
                st.success("✅ Team successfully added!")
            elif result == "DUPLICATE":
                st.warning("⚠️ One or more students already exist in another team!")
            else:
                st.error(f"❌ Unexpected error: {res.text}")

        except Exception as e:
            st.error(f"🚫 Failed to submit. Error: {e}")
