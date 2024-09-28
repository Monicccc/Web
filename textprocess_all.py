# import streamlit as st
# import asyncio
# from gradio_client import Client
# from concurrent.futures import ThreadPoolExecutor
# import requests
# import uuid
# import subprocess

# # # 初始化 session_state 中的必要属性
# # if 'user_id' not in st.session_state:
# #     st.session_state.user_id = '001'  # 或使用 uuid.uuid4() 生成唯一ID

# # 阮旺-杀进程代码
# async def send_append_request(string_to_append):
#     loop = asyncio.get_running_loop()
#     with ThreadPoolExecutor() as pool:
#         response = await loop.run_in_executor(
#             pool, 
#             lambda: requests.post('http://192.168.8.62:5000/append', json={'string_to_append': string_to_append})
#         )
#     if response.status_code == 200:
#         print(response.json().get('message'))
#     else:
#         print(f"Error: {response.json().get('error')}")

# # 王旭-生成教学互动的客户端调用代码
# async def function(key_name, questions, _id):
#     questions = (questions
#                  .replace("['", "")
#                  .replace("问题：", "")
#                  .replace("学习任务1\n", "任务1：")
#                  .replace("学习任务2\n", "任务2：")
#                  .replace("学习任务3\n", "任务3：")
#                  .replace("', '", "\n")
#                  .replace("']", ""))

#     # 调用客户端脚本来发送请求
#     command = [
#         "python3", "./生成教学互动.py",  # 假设你的客户端脚本命名为client_script.py
#         "--key_name", key_name,
#         "--questions", questions,
#         "--_id", _id
#     ]

#     # 异步执行命令并捕获输出
#     process = await asyncio.create_subprocess_exec(
#         *command,
#         stdout=asyncio.subprocess.PIPE,
#         stderr=asyncio.subprocess.PIPE
#     )
#     stdout, stderr = await process.communicate()

#     # 打印服务器端的输出，而不仅仅是状态码
#     if process.returncode == 0:
#         return stdout.decode().strip()  # 确保返回标准输出的内容
#     else:
#         return f"Error: {process.returncode}\n{stderr.decode()}"  # 返回错误信息

# # 王旭-终止生成教学互动
# async def kill_function(kill_id):
#     command = [
#         "python3", "./终止生成教学互动.py",
#         "--kill_id", kill_id
#     ]
#     process = await asyncio.create_subprocess_exec(
#         *command,
#         stdout=asyncio.subprocess.PIPE,
#         stderr=asyncio.subprocess.PIPE
#     )
#     stdout, stderr = await process.communicate()

#     if process.returncode == 0:
#         return stdout.decode().strip()
#     else:
#         return f"Error: {process.returncode}\n{stderr.decode()}"

# # 王明轩-拼接结果
# def result_splice(result, output):
#     return f"""  
#             一、学情分析  
#             （一）学生基本信息  
#             {result[0]}  
#             （二）教材分析  
#             {result[1]}  
#             （三）课标分析  
#             {result[2]}  
#             二、教学目标  
#             {result[3]}  
#             三、教学重难点  
#             {result[4]}  
#             四、教学活动  
#             （一）真实情境创设  
#             {result[5]}  
#             （二）学习任务设置  
#             {output}  
#             五、教学方法  
#             {result[7]}  
#             六、作业设计  
#             {result[8]}  
#             """  

# client = Client("http://192.168.8.62:7890/")

# st.title("教学设计生成")

# prompt = st.selectbox("选择课文",(
#                       "沁园春·长沙",
#                       "短歌行",
#                       "琵琶行",
#                       "登高",
#                       "念奴娇·赤壁怀古",
#                       "劝学",
#                       "拿来主义",
#                       "故都的秋",
#                       "我与地坛",
#                       "百合花",
#                       "烛之武退秦师",
#                       "庖丁解牛",
#                       "说木叶",
#                       "青蒿素",
#                       "祝福",
#                       "林教头风雪山神庙",
#                       "装在套子里的人",
#                       "促织",
#                       "阿房宫赋",
#                       "谏太宗十思疏",)
#                       )
# type = st.selectbox("选择教学设计类型",("主题导向","情境导向","任务导向","育人导向","实践导向","能力导向","活动导向","评价导向"))

# if type == "主题导向":
#     option = st.selectbox("",["该教案需要以理解这篇课文的主题和思想情感为核心教学目标，并设置典型的学习任务促进教学目标的实现。"])
# elif type == "情境导向":
#     option = st.selectbox("",[
#                    "(通用)该教案需要依据教学目标和课文内容特点创设真实的社会生活情境或者个人体验情境，并且所创设的情境能够与所设置的学习任务紧密融合。",
#                    "(中等生)该教案需要依据教学目标和课文内容特点创设真实的社会生活情境或者个人体验情境，并且所创设的情境能够与所设置的学习任务紧密融合；该教案面向的是高一年级学生，这部分学生学习成绩较好，理解能力较强，学习基础较好。",
#                    "(学困生)该教案需要依据教学目标和课文内容特点创设真实的社会生活情境或者个人体验情境，并且所创设的情境能够与所设置的学习任务紧密融合；该教案面向的是高一年级学生，这部分学生学习成绩一般，理解能力一般，学习基础一般。",
#                    "(学优生)该教案需要依据教学目标和课文内容特点创设真实的社会生活情境或者个人体验情境，并且所创设的情境能够与所设置的学习任务紧密融合；该教案面向的是高一年级学生，这部分学生学习成绩极好，理解能力极强，学习基础极好。"
#               ])
# elif type == "任务导向":
#     option = st.selectbox("", ["该教案应立足于新课标’学习任务群’的教学理念，设计不同类型的学习任务，依托学习任务整合学习情境、学习内容、学习方法和学习资源，安排连贯的语文实践活动。"])
# elif type == "育人导向":
#     option = st.selectbox("", ["该教案应立足于新课标’以文化人的育人导向’的教学理念，突出文以载道、以文化人，把立德树人作为语文教学的根本任务，清晰、明确地体现教学目标的育人立意。"])
# elif type == "实践导向":
#     option = st.selectbox("", ["该教案应立足于新课标’创设真实而富有意义的学习情境，凸显语文学习的实践性’的教学理念，通过真实情境创设，引导学生关注家庭生活、校园生活、社会生活等相关经验，增强在各种场合学语文、用语文的意识，建设开放的语文学习空间，激发学生探究问题、解决问题的兴趣和热情，引导学生在多样的日常生活场景和社会实践活动中学习语言文字运用。"])
# elif type == "能力导向":
#     option = st.selectbox("", ["该教案应立足于新课标’教一学一评’一体化的教学理念，应重点关注学生知识基础、认知过程、思维方式、态度情感等方面的表现，深入分析这些表现及其影响因素，并以此为基础制定教学目标，设计教学活动。"])
# elif type == "活动导向":
#     option = st.selectbox("", ["该教案应立足于新课标’关注互联网时代语文生活的变化，探索语文教与学方式的变革’的教学理念，在教学活动中整合多种媒介的学习内容，为学生提供多层面、多角度的阅读、表达和交流的机会，促进师生在语文学习中的多元互动。"])
# else:
#     option = st.selectbox("", [
#         "(作业)该教案应立足于新课标’作业设计是作业评价的关键’的作业设计理念，在作业任务设计中，增强作业的可选择性，除写字、阅读、日记、习作等作业外，可紧密结合课堂所学，关注学生校内外个人生活和社会发展中的热点问题，设计主题考察、跨媒介创意表达等多种类型的作业，培养学生自主学习和综合学习的能力。",
#         "(通用)该教案应立足于新课标’倡导课程评价的过程性和整体性，重视评价的导向作用’的教学设计理念，根据不同年龄学生的学习特点和不同学段的学习目标，选用恰当的评价方式，加强语文教学评价的整体性和综合性。"
#     ])

# async def main():
#     if st.button("生成教学设计"):

#         with st.spinner('正在生成内容，请稍候...'):
#             loop = asyncio.get_running_loop()
#             with ThreadPoolExecutor() as pool:
#                 result = await loop.run_in_executor(pool, lambda: client.predict(prompt, option, '001'))
#                 output = await function(prompt, result[6], _id= '001')
# #                 output = await loop.run_in_executor(pool, lambda: function(prompt, result[6], _id= '001'))

#             ID = output.splitlines()[0]
#             output = output.replace(f"{ID}","")
#             generated_content = result_splice(result, output)

#             st.session_state.generated_content = generated_content
#             st.session_state.show_buttons = True

#     if st.button("终止生成"): 
#         await send_append_request(st.session_state.user_id)
#         await kill_function(st.session_state.user_id)

#     if 'generated_content' in st.session_state:
#         st.subheader("生成内容:")
#         st.write(st.session_state.generated_content)
        
#     if 'show_buttons' in st.session_state and st.session_state.show_buttons:
#         col1, col2, col3 = st.columns(3)

#         with col1:
#             selected = st.feedback("stars")

#         with col2:
#             st.download_button(
#                 label="下载",
#                 data=st.session_state.generated_content,
#                 file_name='generated_content.txt',
#                 mime='text/plain'
#             )

#         with col3:
#             if st.button("修改"):
#                 st.session_state.generated_content = None
#                 st.session_state.show_buttons = False

# # 使用 asyncio.run 来运行异步主函数
# asyncio.run(main())

import streamlit as st
import asyncio
from gradio_client import Client
from concurrent.futures import ThreadPoolExecutor
import requests
import uuid
import subprocess
import requests

# 初始化 session_state 中的必要属性
if 'user_id' not in st.session_state:
    st.session_state.user_id = '001'  # 或使用 uuid.uuid4() 生成唯一ID

if 'is_terminated' not in st.session_state:
    st.session_state.is_terminated = False

# 阮旺-杀进程代码
async def send_append_request(string_to_append):
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        response = await loop.run_in_executor(
            pool, 
            lambda: requests.post('http://192.168.8.63:5000/append', json={'string_to_append': string_to_append})
        )
    if response.status_code == 200:
        print(response.json().get('message'))
    else:
        print(f"Error: {response.json().get('error')}")

# 王旭-生成教学互动的客户端调用代码
async def function(key_name, questions, _id):
    questions = (questions
                 .replace("['", "")
                 .replace("问题：", "")
                 .replace("学习任务1\n", "\n任务1：")
                 .replace("学习任务2\n", "\n任务2：")
                 .replace("学习任务3\n", "\n任务3：")
                 .replace("', '", "\n")
                 .replace("']", ""))

    # 调用客户端脚本来发送请求
    command = [
        "python3", "./生成教学互动.py",  # 假设你的客户端脚本命名为client_script.py
        "--key_name", key_name,
        "--questions", questions,
        "--_id", _id
    ]

    # 异步执行命令并捕获输出
    process = await asyncio.create_subprocess_exec(
        *command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()

    # 打印服务器端的输出，而不仅仅是状态码
    if process.returncode == 0:
        return stdout.decode().strip()  # 确保返回标准输出的内容
    else:
        return f"Error: {process.returncode}\n{stderr.decode()}"  # 返回错误信息

# 王旭-终止生成教学互动
async def kill_function(kill_id):
    command = [
        "python3", "./终止生成教学互动.py",
        "--kill_id", kill_id
    ]
    process = await asyncio.create_subprocess_exec(
        *command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()

    if process.returncode == 0:
        return stdout.decode().strip()
    else:
        return f"Error: {process.returncode}\n{stderr.decode()}"

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
    
    # 检查响应状态
    if response.status_code == 200:
        # 逐行读取流式输出
        for line in response.iter_lines():
            if line:
                # 解码字节流为字符串并输出
                yield line.decode('utf-8')
    else:
        print(f"请求失败，状态码: {response.status_code}")


    



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
type = st.selectbox("选择教学设计类型",("主题导向","情境导向","任务导向","育人导向","实践导向","能力导向","活动导向","评价导向"))

if type == "主题导向":
    option = st.selectbox("",["该教案需要以理解这篇课文的主题和思想情感为核心教学目标，并设置典型的学习任务促进教学目标的实现。"])
elif type == "情境导向":
    option = st.selectbox("",[
                   "(通用)该教案需要依据教学目标和课文内容特点创设真实的社会生活情境或者个人体验情境，并且所创设的情境能够与所设置的学习任务紧密融合。",
                   "(中等生)该教案需要依据教学目标和课文内容特点创设真实的社会生活情境或者个人体验情境，并且所创设的情境能够与所设置的学习任务紧密融合；该教案面向的是高一年级学生，这部分学生学习成绩较好，理解能力较强，学习基础较好。",
                   "(学困生)该教案需要依据教学目标和课文内容特点创设真实的社会生活情境或者个人体验情境，并且所创设的情境能够与所设置的学习任务紧密融合；该教案面向的是高一年级学生，这部分学生学习成绩一般，理解能力一般，学习基础一般。",
                   "(学优生)该教案需要依据教学目标和课文内容特点创设真实的社会生活情境或者个人体验情境，并且所创设的情境能够与所设置的学习任务紧密融合；该教案面向的是高一年级学生，这部分学生学习成绩极好，理解能力极强，学习基础极好。"
              ])
elif type == "任务导向":
    option = st.selectbox("", ["该教案应立足于新课标’学习任务群’的教学理念，设计不同类型的学习任务，依托学习任务整合学习情境、学习内容、学习方法和学习资源，安排连贯的语文实践活动。"])
elif type == "育人导向":
    option = st.selectbox("", ["该教案应立足于新课标’以文化人的育人导向’的教学理念，突出文以载道、以文化人，把立德树人作为语文教学的根本任务，清晰、明确地体现教学目标的育人立意。"])
elif type == "实践导向":
    option = st.selectbox("", ["该教案应立足于新课标’创设真实而富有意义的学习情境，凸显语文学习的实践性’的教学理念，通过真实情境创设，引导学生关注家庭生活、校园生活、社会生活等相关经验，增强在各种场合学语文、用语文的意识，建设开放的语文学习空间，激发学生探究问题、解决问题的兴趣和热情，引导学生在多样的日常生活场景和社会实践活动中学习语言文字运用。"])
elif type == "能力导向":
    option = st.selectbox("", ["该教案应立足于新课标’教一学一评’一体化的教学理念，应重点关注学生知识基础、认知过程、思维方式、态度情感等方面的表现，深入分析这些表现及其影响因素，并以此为基础制定教学目标，设计教学活动。"])
elif type == "活动导向":
    option = st.selectbox("", ["该教案应立足于新课标’关注互联网时代语文生活的变化，探索语文教与学方式的变革’的教学理念，在教学活动中整合多种媒介的学习内容，为学生提供多层面、多角度的阅读、表达和交流的机会，促进师生在语文学习中的多元互动。"])
else:
    option = st.selectbox("", [
        "(作业)该教案应立足于新课标’作业设计是作业评价的关键’的作业设计理念，在作业任务设计中，增强作业的可选择性，除写字、阅读、日记、习作等作业外，可紧密结合课堂所学，关注学生校内外个人生活和社会发展中的热点问题，设计主题考察、跨媒介创意表达等多种类型的作业，培养学生自主学习和综合学习的能力。",
        "(通用)该教案应立足于新课标’倡导课程评价的过程性和整体性，重视评价的导向作用’的教学设计理念，根据不同年龄学生的学习特点和不同学段的学习目标，选用恰当的评价方式，加强语文教学评价的整体性和综合性。"
    ])


# 可以执行的函数，但是没有下载功能
# async def main():
#     if st.button("终止生成"):
#         st.session_state.is_terminated = True  # 设置终止标志位
#         await send_append_request(st.session_state.user_id)  # 调用终止生成的请求
#         await kill_function(st.session_state.user_id)  # 结束生成进程
#     if st.button("生成教学设计"):
#         st.session_state.is_terminated = False  # 重置终止标志位
#         placeholder = st.empty()  # 用于流式显示生成内容的占位符

#         with st.spinner('正在生成内容，请稍候...'):
#             loop = asyncio.get_running_loop()
#             with ThreadPoolExecutor() as pool:
#                 all_content = ""  # 用于存储完整的生成内容
#                 if st.session_state.is_terminated:
#                     return  # 如果标志位设置为True，终止任务

#                 # 模拟流式获取结果
#                 result = await loop.run_in_executor(pool, lambda: get_streaming_output(lessonname=prompt, prompt=option, ID='001'))
#                 placeholder.write(result)
#                 if st.session_state.is_terminated:
#                     return  # 如果标志位设置为True，终止任务

# #                     逐步更新生成的内容
# #                     generated_content = result
# #                     if not st.session_state.is_terminated:  # 如果生成过程中没有终止
# #                         all_content += generated_content + "\n"  # 累积内容
# #                         st.session_state.generated_content = all_content
# #                         placeholder.write(st.session_state.generated_content)  # 动态更新内容


#         st.success("生成完成！")
#         st.session_state.show_buttons = True  # 表示可以显示按钮了

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
async def main():
    if st.button("终止生成"):
        st.session_state.is_terminated = True  # 设置终止标志位
        await send_append_request(st.session_state.user_id)  # 调用终止生成的请求
        await kill_function(st.session_state.user_id)  # 结束生成进程
    if st.button("生成教学设计"):
        st.session_state.is_terminated = False  # 重置终止标志位
        with st.spinner('正在生成内容，请稍候...'):
            loop = asyncio.get_running_loop()
            with ThreadPoolExecutor() as pool:
                all_content = ""  # 用于存储完整的生成内容
                if st.session_state.is_terminated:
                    return  # 如果标志位设置为True，终止任务

                # 模拟流式获取结果
                result = await loop.run_in_executor(pool, lambda: get_streaming_output(lessonname=prompt, prompt=option, ID='001'))
                # 流式输出
                st.write_stream(result)
                # bug所在地，无法保存数据
                for data in result:
                    print(data)
                    all_content += data
                    
                    
                if st.session_state.is_terminated:
                    return  # 如果标志位设置为True，终止任务

                # 逐步更新生成的内容
            if not st.session_state.is_terminated:  # 如果生成过程中没有终止
                st.session_state.generated_content = all_content
                st.success("生成完成！")
                st.session_state.show_buttons = True  # 表示可以显示按钮了

    # 显示下载和修改按钮，只有在生成完成后才显示
    if 'show_buttons' in st.session_state and st.session_state.show_buttons:
        col1, col2, col3 = st.columns(3)

        with col1:
            selected = st.feedback("stars")

        with col2:
            # 确保下载的是完整生成的内容
            st.download_button(
                label="下载",
                data=st.session_state.generated_content,  # 这里会是完整生成的内容
                file_name='generated_content.txt',
                mime='text/plain'
            )

        with col3:
            if st.button("修改"):
                st.session_state.generated_content = None
                st.session_state.show_buttons = False
# 使用 asyncio.run 来运行异步主函数
asyncio.run(main())
