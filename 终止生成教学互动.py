import requests
import argparse
import json

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
            # 只返回response对应的内容
            return json_data.get("response", "No response content found")
        except json.JSONDecodeError as e:
            print(f"JSON解析错误: {e}")
            return response.text  # 返回未解码的文本内容
    else:
        return f"Error: {response.status_code}\n{response.text}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process key_name and questions.")
    parser.add_argument('--kill_id', required=True, help='The key name to process')

    args = parser.parse_args()
    result = send_request(args.kill_id)
    print(result)
