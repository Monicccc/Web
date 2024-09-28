import requests
import argparse
import json

def send_request(key_name, questions, _id):
    url = "http://192.168.8.66:9999/process"
    data = {
        "key_name": key_name,
        "questions": questions,
        "_id": _id
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
    parser.add_argument('--key_name', required=True, help='The key name to process')
    parser.add_argument('--questions', required=True, help='The questions text to process')
    parser.add_argument('--_id', required=True, help='The questions text to process')

    args = parser.parse_args()
    result = send_request(args.key_name, args.questions, args._id)
    print(result)
