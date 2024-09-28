import streamlit as st
from navigate import show_navigation
from login import show_login
from register import show_register
# 检查用户是否登录
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# 初始化当前页面状态
if 'current_page' not in st.session_state:
    st.session_state['current_page'] = "login"  # 默认页面为登录页面

# 页面导航逻辑
if st.session_state['current_page']=="register":
    show_register()
elif st.session_state['current_page']=="navigation" and st.session_state['logged_in']==True:
    show_navigation()

else:
    show_login()
