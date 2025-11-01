import streamlit as st
import requests

# Google Apps Script Web App URL
WEB_APP_URL = "https://script.google.com/macros/s/AKfycbwNuBVelTCDpEbq6SPp79oYGq8HXM346s4vSBTswxxX12khG_5MFz7JPNBGOuJsLjp-WA/exec"

st.set_page_config(page_title="Mini Project Members", page_icon="🎓", layout="centered")
st.title("🎓 K-R-R Mini Project Members Form")
st.write("Each row represents one team of one or two students. Please ensure no duplicates.")

with st.form("student_form"):
    st.subheader("👤 Student 1 (Required)")
    last1 = st.text_input("Last Name (Student 1):").strip()
    first1 = st.text_input("First Name (Student 1):").strip()

    st.subheader("👥 Student 2 (Optional)")
    last2 = st.text_input("Last Name (Student 2):").strip()
    first2 = st.text_input("First Name (Student 2):").strip()

    submitted = st.form_submit_button("Submit")

if submitted:
    # Validation
    if not (first1 and last1):
        st.warning("⚠️ Please fill in at least Student 1 information.")
    elif (first2 and not last2) or (last2 and not first2):
        st.warning("⚠️ Please fill in all fields before submitting.")  # ✅ your line
    else:
        data = {
            "first1": first1,
            "last1": last1,
            "first2": first2,
            "last2": last2
        }

        try:
            res = requests.post(WEB_APP_URL, json=data)
            result = res.text.strip().upper()

            if result == "SUCCESS":
                st.success("✅ Team successfully added!")
            elif result == "DUPLICATE":
                st.warning("⚠️ One or both students already exist in another team!")
            else:
                st.error(f"❌ Unexpected error: {res.text}")

        except Exception as e:
            st.error(f"🚫 Failed to submit. Error: {e}")
