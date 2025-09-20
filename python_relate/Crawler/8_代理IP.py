# 1.代理IP：指通过中间服务器转发请求的IP地址，可以隐藏真实IP，保护用户隐私。
# (1)代理IP的类型
# - <1>透明代理：不隐藏用户真实IP，主要用于缓存加速。
# - <2>匿名代理：隐藏用户真实IP，但仍然可以被识别为代理IP。
# - <3>高匿代理：完全隐藏用户真实IP，无法被识别。
# (2)代理IP的获取
# - <1>免费代理IP：通过爬虫等方式获取，稳定性差，容易失效。
# - <2>付费代理IP：通过购买获得，稳定性高，速度快。
# (3)代理IP的使用
# - <1>设置代理IP：在请求中添加代理IP信息。
# - <2>切换代理IP：定期更换代理IP，避免被封禁。
# (4)代理IP的注意事项
# - <1>合法合规：使用代理IP时，遵守相关法律法规。
# - <2>风险控制：避免频繁切换代理IP，降低被封禁风险。

# 2.代理：分为透明代理、正向代理和反向代理；
# (1)透明代理：服务器知道用户使用了代理，也知道真实IP
# (2)匿名代理：服务器知道用户使用了代理，但不知道真实IP
# (3)高匿代理：服务器既不知道用户使用了代理，也不知道真实IP
# (4)正向代理：给客户端作代理，让服务器不知道客户端的真实身份，保护客户端
# (5)反向代理：给服务器作代理，让客户端不知道服务器的真实身份，保护服务端

# 3.proxies代理参数：传入一个字典，指定不同协议的代理IP；键值对形式 IP地址:端口号
# proxies={
#     'http':'http://<proxy_ip>:<proxy_port>',
#     'https':'https://<proxy_ip>:<proxy_port>'
# }
# 如果代理IP无效，则使用本机的真实IP访问
import requests
url='https://www.baidu.com/'
headers={
    'User-Agent':'Mozilla/5.0 (Linux; Android) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 CrKey/1.54.248666 Edg/138.0.0.0'
}
proxies={
    # 'http':'http://<proxy_ip>:<proxy_port>',
    # 'https':'https://<proxy_ip>:<proxy_port>'
}
res=requests.get(url,headers=headers,proxies=proxies)
print(res.content.decode())