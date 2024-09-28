import streamlit as st
import asyncio
from gradio_client import Client
from concurrent.futures import ThreadPoolExecutor
import requests
import uuid
import subprocess
import requests
import time
import nest_asyncio
import json

# 初始化 session_state 中的必要属性
if 'user_id' not in st.session_state:
    st.session_state.user_id = '001'  # 或使用 uuid.uuid4() 生成唯一ID

if 'is_terminated' not in st.session_state:
    st.session_state.is_terminated = False


# 允许嵌套的事件循环
nest_asyncio.apply()

# 发送请求以终止生成教学互动的函数
def send_request(kill_id):
    url = "http://192.168.8.66:9998/process"
    data = {
        "kill_id": kill_id
    }
    response = requests.post(url, json=data)

    # 检查请求是否成功
    if response.status_code == 200:
        try:
            json_data = response.json()  # 解析为JSON对象
            print(json_data.get("response", "No response content found"))
        except json.JSONDecodeError as e:
            print(f"JSON解析错误: {e}")
            print(response.text)
    else:
        print(f"Error: {response.status_code}\n{response.text}")

# 发送请求以追加字符串的函数
def send_append_request(string_to_append):
    url = 'http://192.168.8.63:5000/append'
    data = {
        'string_to_append': string_to_append
    }
    response = requests.post(url, json=data)
    
    # 检查请求是否成功
    if response.status_code == 200:
        print(response.json().get('message'))
    else:
        print(f"Error: {response.json().get('error')}")

# 异步执行终止和追加操作的主函数
async def kill_function(kill_id):
    send_request(kill_id)  # 终止生成互动的请求
    send_append_request(kill_id)  # 追加字符串的请求




# 王明轩-拼接结果
def result_splice(result, output):
    return f"""  
            一、学情分析  
            （一）学生基本信息  
            {result[0]}  
            （二）教材分析  
            {result[1]}  
            （三）课标分析  
            {result[2]}  
            二、教学目标  
            {result[3]}  
            三、教学重难点  
            {result[4]}  
            四、教学活动  
            （一）真实情境创设  
            {result[5]}  
            （二）学习任务设置  
            {output}  
            五、教学方法  
            {result[7]}  
            六、作业设计  
            {result[8]}  
            """  



def get_streaming_output(lessonname, prompt, ID):
    url = f'http://192.168.8.63:5001/generate/{lessonname}/{prompt}/{ID}'  # 服务端地址
    response = requests.get(url, stream=True)  # 使用 stream=True 来处理流式响应
#     response = str(response.decode('utf-8'))
#     yield response
    # 检查响应状态
    if response.status_code == 200:
        # 逐行读取流式输出
        for line in response.iter_lines():
            if line:
                # 解码字节流为字符串并输出
                for data in line.decode('utf-8'):
                    yield data
                    time.sleep(0.05)
                yield '\n'
                time.sleep(0.05)
    else:
        print(f"请求失败，状态码: {response.status_code}")


    

# col_title, col_pj = st.columns(2)
# with col_title:
#     # 使用markdown将标题和按钮放在同一行
#     st.title("教学设计生成")
# with col_pj:
#     # 创建评价反馈按钮
#     if st.button("评价反馈"):
#         st.write("https://www.wjx.cn/vm/mGQw4Hg.aspx#")

st.title("教学设计生成")
prompt = st.selectbox("选择课文",(
                      "沁园春·长沙",
                      "短歌行",
                      "琵琶行",
                      "登高",
                      "念奴娇·赤壁怀古",
                      "劝学",
                      "拿来主义",
                      "故都的秋",
                      "我与地坛",
                      "百合花",
                      "烛之武退秦师",
                      "庖丁解牛",
                      "说木叶",
                      "青蒿素",
                      "祝福",
                      "林教头风雪山神庙",
                      "装在套子里的人",
                      "促织",
                      "阿房宫赋",
                      "谏太宗十思疏",
                      "荷塘月色",)
                      )
option = st.text_input("请输入你的教学设计生成要求:")
st.write(f'''你的教学设计生成要求为:
         {option}''')
# async def main():
#     if st.button("终止生成"):
#         st.session_state.is_terminated = True  # 设置终止标志位
#         await send_append_request(st.session_state.user_id)  # 调用终止生成的请求
#         await kill_function(st.session_state.user_id)  # 结束生成进程
#     if st.button("生成教学设计"):
#         st.session_state.is_terminated = False  # 重置终止标志位
# #         placeholder = st.empty()  # 用于流式显示生成内容的占位符
#         st.write('### 生成的教学设计如下：')
#         with st.spinner('正在生成内容，请稍候...'):
#             loop = asyncio.get_running_loop()
            
#             with ThreadPoolExecutor() as pool:
#                 all_content = ""  # 用于存储完整的生成内容
#                 if st.session_state.is_terminated:
#                     return  # 如果标志位设置为True，终止任务

#                 # 模拟流式获取结果
#                 result = await loop.run_in_executor(pool, lambda: get_streaming_output(lessonname=prompt, prompt=option, ID='001')) 
#                 # 流式输出
#                 st.write_stream(result)
# #                 for data in result:
# #                     all_content += data

# #                 placeholder.write(result)
#                 # bug所在地，无法保存数据

                    
                    
#                 if st.session_state.is_terminated:
#                     return  # 如果标志位设置为True，终止任务

#                 # 逐步更新生成的内容
#             if not st.session_state.is_terminated:  # 如果生成过程中没有终止
#                 st.session_state.generated_content = ''.join(result)
#                 st.success("生成完成！")
#                 st.session_state.show_buttons = True  # 表示可以显示按钮了

#     # 显示下载和修改按钮，只有在生成完成后才显示
#     if 'show_buttons' in st.session_state and st.session_state.show_buttons:
#         col1, col2, col3 = st.columns(3)

#         with col1:
#             selected = st.feedback("stars")

#         with col2:
#             # 确保下载的是完整生成的内容
#             st.download_button(
#                 label="下载",
#                 data=st.session_state.generated_content,  # 这里会是完整生成的内容
#                 file_name='generated_content.txt',
#                 mime='text/plain'
#             )

#         with col3:
#             if st.button("修改"):
#                 st.session_state.generated_content = None
#                 st.session_state.show_buttons = False
# # 使用 asyncio.run 来运行异步主函数
# asyncio.run(main())
import asyncio
from concurrent.futures import ThreadPoolExecutor
import streamlit as st

async def main():
    col_1, col_2 = st.columns(2)
    with col_1:
        if st.button("终止生成"):
            st.session_state.is_terminated = True  # 设置终止标志位
            await kill_function(st.session_state.user_id)
    with col_2:
        if st.button("评价反馈"):
            st.write("https://www.wjx.cn/vm/mGQw4Hg.aspx#")
    if st.button("生成教学设计"):
        st.session_state.is_terminated = False  # 重置终止标志位
        placeholder = st.empty()  # 用于流式显示生成内容的占位符

        with st.spinner('正在生成内容，请稍候...'):
            loop = asyncio.get_running_loop()
            with ThreadPoolExecutor() as pool:
                all_content = ""  # 用于存储完整的生成内容

                # 模拟流式获取结果
                result = await loop.run_in_executor(pool, lambda: get_streaming_output(lessonname=prompt, prompt=option, ID='001')) 
                # 遍历生成器逐步处理流式数据
                for data in result:
                    if st.session_state.is_terminated:
                        break  # 如果终止标志位被设置，停止获取数据

                    # 实时显示数据
                    placeholder.write(all_content)
                    # 逐步保存到 all_content
                    all_content += data

                # 如果任务被终止，直接返回
                if st.session_state.is_terminated:
                    return

                # 将最终生成的内容保存到 session_state 中
            st.session_state.generated_content = all_content
            st.success("生成完成！")
            st.session_state.show_buttons = True
            st.session_state.download_show_buttons = False# 表示可以显示按钮了

    # 显示下载和修改按钮，只有在生成完成后才显示
    if 'show_buttons' in st.session_state and st.session_state.show_buttons:
        col1, col2 = st.columns(2)
        with col1:
            selected = st.feedback("stars")

        with col2:
            # 确保下载的是完整生成的内容
            if st.download_button(
                label="下载",
                data=st.session_state.generated_content,  # 这里会是完整生成的内容
                file_name='generated_content.txt',
                mime='text/plain'
            ):
                st.session_state.download_show_buttons = True
        if st.session_state.download_show_buttons:
            st.write(st.session_state.generated_content)
#         with col3:
#             if st.button("评价反馈"):
#                 st.write("https://www.wjx.cn/vm/mGQw4Hg.aspx#")

# 使用 asyncio.run 来运行异步主函数
asyncio.run(main())
