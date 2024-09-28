import streamlit as st


import os

# 模拟的文件存储路径
if st.session_state['user_role']=='teacher':
    UPLOAD_FOLDER = "uploads_users/"
else:
    UPLOAD_FOLDER = "uploads_admin/"

# 确保上传文件夹存在
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


st.title("知识库管理")

# 文件管理部分
st.subheader("文件管理")
prompt = st.selectbox("选择语料类型",
                      ( "教学设计","赏析文本"))
uploaded_file = st.file_uploader("上传文件", type=["txt", "pdf", "docx"])
if uploaded_file :
    file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.write(f"文件已上传")
    st.rerun()  # 页面刷新，避免上传控件显示已上传文件

# 显示已上传文件列表
st.write("已上传文件：")
for filename in os.listdir(UPLOAD_FOLDER):
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    col1, col2, col3, col4 = st.columns([5, 1, 1, 1])
    with col1:
        st.write(filename)
    with col3:
        st.download_button(
            label="下载",
            data=open(file_path, "rb").read(),
            file_name=filename,
            mime="application/octet-stream",
            key=f"download_{filename}"
        )
    with col4:
        if st.button(f"删除", key=f"delete_{filename}"):
            os.remove(file_path)
            st.success(f"文件 {filename} 已删除")
            st.rerun()  # 页面刷新，更新文件列表


return_button = st.button("返回")

if return_button:
    st.session_state['current_page'] = "login"


