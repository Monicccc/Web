import streamlit as st
import base64

# Function to set background image
def set_background(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/png;base64,{encoded});
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Define the login UI
def show_register():
    # Set the background image
    set_background("../design_generate/background.jpeg")

    # Create the login interface
    st.title("注册界面")

    username = st.text_input("用户名")
    password = st.text_input("密码", type="password")

    # Create two columns for buttons
    col1, col2 = st.columns(2)
    register=st.button("提交")
    if register:
        st.session_state['current_page']="login"
        st.rerun()

