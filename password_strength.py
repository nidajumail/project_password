import re
import streamlit as st
st.set_page_config(page_title="Password Strength Meter", page_icon="🔒", layout="centered")
# custom CSS
st.markdown("""
<style>
      .main{text-align: center; padding: 10px;}
      .stTextInput{width:60% !important; margin: auto;}
      .stButton button{width:60%; background-color: #4CAF50; color: white; font-weight: bold; margin: auto;}
      .stButton button:hover{background-color: #45a049;}       
</style>
""", unsafe_allow_html=True)

# page title and description
st.title("Password Strength Meter")
st.write("Enter your password below to check its strength.🔑")

# ✅ JUST THESE TWO LINES MOVED UP — nothing else changed
password = st.text_input("Enter your password", type="password", help="Ensure your password is strong🔏")
if st.button("Check Password Strength"):
    if password:
        check_password_strength(password)
    else:   
        st.warning("⚠️ Please enter a password to check its strength.")

# function to make password strength checker
def check_password_strength(password):  
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password must be at least 8 characters long.")
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password): 
        score += 1  
    else:
        feedback.append("❌ Password must contain **both uppercase and lowercase letters**.")
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password must contain **at least one number(0-9)**.")   
    # special characters
    if re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~"+r'"]', password):
        score += 1
    else:   
        feedback.append("❌ Include **at least one special character(!@#$%^&*)**.")
# display password strength result
    if score == 4:
        st.success("✅ Your password is **strong**.")
    elif score == 3:
        st.warning("⚠️ Your password is **moderate**.")   
    else:
        st.error("❌ Your password is **weak**.")
                                                    # feedback
    if feedback:
        with st.expander("Password Strength Feedback"):
             for item in feedback:
                 st.write(item)

