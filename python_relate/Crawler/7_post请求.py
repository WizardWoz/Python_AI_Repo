import requests
# 1.post请求：比get请求更安全，对数据长度无要求，适合传输大文本
# requests.post(url,data)
# data参数：接受一个字典或字符串，表示要传递的数据
# get请求：使用较多，直接向服务器发送请求；携带参数params
# post请求：使用较少，先给服务器一些数据，然后再获取响应；携带参数data

# 2.cookie模拟登录
# 找到登录后的url
url='https://renren.com/'
headers={
    'User-Agent':'Mozilla/5.0 (Linux; Android) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 CrKey/1.54.248666 Edg/138.0.0.0',
    'cookie':'anonymousUser=0; depovince=GW; _r01_=1; JSESSIONID=abcW6x3KxwQ3vXvB7tfxw; first_login_flag=1; ick=; _ga=GA1.2.2006489735.1695883293'
}
response=requests.get(url,headers=headers)
print(response.text)

# 3.post请求举例（金山翻译）

# 4.session：自动处理cookie
# (1)对登录后才能访问的页面进行抓包
# (2)分析登录请求，找到url、请求方式、请求参数
# (3)确定登录才能访问的页面url和请求方法
# (4)利用requests.session()模拟登录
session=requests.session()
response=session.post(url,data=data,headers=headers)
session.get(url.text)

# 5.cookie池：每一个cookie代表一个账号；通过代理ip和cookie池实现高效爬取；
# (1)cookie有有效期，session无有效期
# (2)cookie数据放在客户浏览器上，别人可以分析本地cookie并进行cookie欺骗；session数据放在服务器上，别人无法分析
# (3)session会在一定时间内保存于服务器上，占用服务器资源，影响性能；考虑到减轻服务器负载，应当使用cookie
# (4)session存放登录帐号密码等敏感信息，安全性更高；cookie则存放其它信息