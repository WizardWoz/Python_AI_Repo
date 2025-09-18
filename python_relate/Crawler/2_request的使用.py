# 1.检查是否安装了requests库：pip list | grep requests
# 2.如果未安装，则安装requests库：pip install requests

# 3.运行过程
# (1)导入requests库
import requests
url="https://www.baidu.com"
# (2)发送GET请求并获取响应
response=requests.get(url)
print(response)
# print(response.text)    #响应内容有乱码，request模块会自动寻找一种解码方式，与原编码格式不对应
print(response.content.decode())    #以字节形式获取响应内容，再手动解码

# 使用requests库保存文件
url='https://qcloud.dpfile.com/pc/5Ct4AVJJv2aq5MjcUIeJ2STd0ZYkopTa4r99ekPIg6qMpU7jk1n9-dyjZitV3vvb.jpg'
response=requests.get(url)
with open('baidu.jpg','wb') as f:
    f.write(response.content)
url="https://www.baidu.com"
response=requests.get(url)
with open('baidu.html','w',encoding='utf-8') as f:
    f.write(response.content.decode())

# 4.其它属性
# response.text与response.content的区别：
# (1)response.text：为str类型，requests模块自动根据http头部对响应的编码作出有根据的推测
# (2)response.content：为bytes类型，表示原始的响应内容，可通过.decode()方法进行解码
url="https://www.baidu.com"
response=requests.get(url)
print(response.text)    #自动解码，可能会有乱码
response.encoding='utf-8'   #手动指定编码格式
print(response.text)    #指定编码格式后，解码正确
# 打印响应的URL
print(response.url)
# 打印响应对象的请求头，用户发给服务器
print(response.request.headers)
# 打印响应对象的响应头，服务器返回给用户
print(response.headers)
#推测的响应内容编码格式
print(response.apparent_encoding)