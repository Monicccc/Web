import requests
from tqdm import tqdm
import time
import threading
import io
import sys

def app(Prompt):
    result = io.StringIO()  # 创建一个 StringIO 对象，用来捕获输出

    # 指定服务端 URL，使用服务端提供的 IP 地址和端口
    url = 'http://172.28.52.179:5000/api/process'

    # 准备要发送的数据，这里的 'prompt' 是你的函数期待的参数
    data = {
        'prompt': Prompt
    }

    # 模拟进度条的总时间（秒）
    total_time = 6 * 60  # 6分钟

    def fetch_data():
        try:
            # 使用 POST 方法发送请求，并设置超时时间为5分钟
            response = requests.post(url, json=data, timeout=total_time)
            # 将服务器的响应内容写入 result
            result.write("教学设计生成完毕！\n")
            result.write(str(response.json()) + "\n")
        except requests.exceptions.Timeout:
            result.write("\n请求超时，服务器未在6分钟内响应，请再次尝试。\n")
        except requests.exceptions.RequestException as e:
            result.write(f"\n请求失败: {e}\n")

    # 创建并启动线程以运行 fetch_data
    fetch_thread = threading.Thread(target=fetch_data)
    fetch_thread.start()

    # 模拟进度条
    for i in tqdm(range(total_time), desc="教学设计生成中，请耐心等待。。。", unit="秒", ncols=100):
        time.sleep(1)
        # 检查 fetch_thread 是否仍然在运行
        if not fetch_thread.is_alive():
            break

    # 确保 fetch_thread 在进度条结束后也完成
    fetch_thread.join()

    # 获取并返回 result 中的内容
    return result.getvalue()

prompt = "请生成一个关于红楼梦的教学设计"
output = app(prompt)
print(output)  # 输出 result 中的内容

