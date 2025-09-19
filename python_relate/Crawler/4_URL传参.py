import requests
# 1.浏览器发送请求原理
# (1)构建请求:浏览器会向服务器服务器发送请求行,包括了请求方法、请求URL、HTTP协议版本
# (2)查找缓存
# (3)准备IP地址和端口
# (4)等待TCP队列
# (5)建立TCP连接
# (6)发送HTTP请求

# 2.URL传参：字符串被当作URL提交时，会被自动进行URL编码处理
# 例如：百度中搜索“学习”字符串（明文），在URL中会被编码成“%E5%AD%A6%E4%B9%A0”（密文）
from urllib.parse import quote,unquote
# quote()：对字符串进行URL编码，明文转密文；unquote()：对URL编码进行解码，密文转明文
print(quote('参数'))    # %E5%8F%82%E6%95%B0
print(unquote('%E5%8F%82%E6%95%B0'))

# 3.发送带参数的请求
name=input('请输入关键字：')
url='https://www.baidu.com/s?wd={name}'
headers={
    'User-Agent':'Mozilla/5.0 (Linux; Android) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 CrKey/1.54.248666 Edg/138.0.0.0'
}
res=requests.get(url,headers=headers)
print(res.content.decode())

# 4.通过params携带参数字典
# (1)构建请求参数字典
name=input('请输入关键字：')
kw={'wd':f'{name}'}   #wd是百度搜索的请求参数
# (2)发送请求的时候带上请求参数字典
res2=requests.get(url,headers=headers,params=kw)   #params参数接收字典形式的请求参数
print(res2.content.decode())