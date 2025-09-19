import requests
# 1.用户代理：请求头中user-agent字段必不可少，表示客户端操作系统以及浏览器信息
url="https://www.baidu.com"
# (1)构建请求头，添加User-Agent的目的是为了让服务器认为是浏览器在发送请求，而不是爬虫程序发送请求
headers={
    'User-Agent':'Mozilla/5.0 (Linux; Android) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 CrKey/1.54.248666 Edg/138.0.0.0'
}
# (2)headers参数接收字典形式的请求头，请求头字段名为key，值为value
response=requests.get(url,headers=headers)
print(response.request.headers)
# print(response.content.decode())
print(len(response.content.decode()))   #响应内容的长度是221444
# (3)User-Agent请求池：防止反爬
import random
# 自定义User-Agent请求池
UAlist = [
    'Mozilla/5.0 (Linux; Android) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 CrKey/1.54.248666 Edg/138.0.0.0',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 Edg/138.0.0.0',
    'Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Mobile Safari/537.36 Edg/138.0.0.0'
]
print(random.choice(UAlist))   #随机选择一个User-Agent
# 引入UserAgent模块中包含的User-Agent请求池（可能会出现异常）
from fake_useragent import UserAgent
print(UserAgent().random)   #使用fake_useragent库随机生成一个User-Agent