import streamlit as st

# 用于存储聊天记录和生成内容
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'generated_content' not in st.session_state:
    st.session_state.generated_content = ""
if 'rating' not in st.session_state:
    st.session_state.rating = None

# 聊天界面展示
st.title("对话界面")

for msg in st.session_state.messages:
    with st.chat_message(msg['name'], ):
        st.write(msg['text'])

# 聊天输入框
prompt = st.chat_input("enter")

# 如果有输入，更新聊天记录并生成内容
if prompt:
    # 添加用户消息到聊天记录
    st.session_state.messages.append({"name": "user", "avatar": "🧑‍", "text": prompt})

    # 模拟助手回应，可以在这里添加实际的对话逻辑
    response = f"HAHAHA: {prompt}"
    st.session_state.messages.append({"name": "assistant", "avatar": ":material/robot:", "text": response})

    # 更新生成的内容
    st.session_state.generated_content = response


    # 重新显示更新后的聊天记录
    st.rerun()

# 显示生成的内容



# 评分、下载和修改按钮

col1, col2, col3 = st.columns(3)

with col1:
    st.session_state.rating = st.feedback("stars")
    if st.session_state.rating is not None:
        pass

with col2:
    if st.button("下载"):
        pass

with col3:
    if st.button("修改"):
        pass


