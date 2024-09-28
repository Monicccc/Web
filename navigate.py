import streamlit as st

# 定义页面函数
def page1():
   # st.title("操作指南")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("单篇教学设计"):
            page1()

    with col2:
        if st.button("群文教学设计"):
            page2()

    with col1:
        if st.button("自由对话"):
            page3()

    with col2:
        if st.button("提示词对话"):
            page4()
    prompt1=st.chat_input("Enter")
    if prompt1:
        pass#输入后的处理
def page2():
    st.title("文本优化处理")


def page3():
   # st.title("新建对话")
  # 用于存储聊天记录
   if 'messages' not in st.session_state:
       st.session_state.messages = []

   # 聊天界面展示
   for msg in st.session_state.messages:
       with st.chat_message(msg['name'], ):
           st.write(msg['text'])

   # 聊天输入框
   prompt = st.chat_input("Enter")

   # 如果有输入，更新聊天记录
   if prompt:
       # 添加用户消息到聊天记录
       st.session_state.messages.append({"name": "user", "avatar": "🧑‍", "text": prompt})

       # 模拟助手回应，可以在这里添加实际的对话逻辑
       response = f"Echo: {prompt}"
       st.session_state.messages.append({"name": "assistant", "avatar": ":material/robot:", "text": response})

       # 重新显示更新后的聊天记录
       st.rerun()


def page4():
    st.title("历史对话")
    st.write("这是历史对话的内容。")

# 使用st.navigation定义导航
def show_navigation():
    pages = [
        #st.Page(page1, title="操作指南"),
        st.Page("textprocess.py", title="教学设计生成"),
#         st.Page("textprocess_asynchronous.py", title="教学设计生成"),
        st.Page("manage.py",title="知识库管理")
        #st.Page("chat.py", title="新建对话"),
        #st.Page(page4, title="历史对话"),
        #st.Page("test.py", title="测试页面")  # 确认test.py存在并正确定义了页面内容
    ]

    pg = st.navigation(pages)
    pg.run()
