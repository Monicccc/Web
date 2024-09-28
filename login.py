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
def show_login():
    # Set the background image
    set_background("./background.jpeg")

    # Create the login interface
    st.title("登录界面")

    username = st.text_input("用户名")
    password = st.text_input("密码", type="password")

    # Create two columns for buttons
    col1, col2 = st.columns(2)

    with col1:
        login_as_teacher = st.button("普通用户登录")
    with col2:
        login_as_admin = st.button("专家登录")
    register=st.button("注册")
    if register:
        st.session_state['current_page']="register"
        st.rerun()
    reset=st.button("忘记密码?")
    if login_as_teacher:
        st.session_state['logged_in'] = True
        st.session_state['user_role'] = 'teacher'
        st.session_state['current_page'] = "navigation"
        st.rerun()

        if username is None or password is None:
            st.error("请输入用户名和密码")
    if login_as_admin:
        st.session_state['logged_in'] = True
        st.session_state['user_role'] = 'admin'
        st.session_state['current_page'] = "navigation"
        st.rerun()

        if username is None or password is None:
            st.error("请输入用户名和密码")


