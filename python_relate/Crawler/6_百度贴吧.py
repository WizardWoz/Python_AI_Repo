import requests
# 1.获取百度贴吧单页
# url='https://tieba.baidu.com/f?ie=utf-8&kw=%E6%9D%8E%E6%AF%85&fr=search'
# headers={
#     'User-Agent':'Mozilla/5.0 (Linux; Android) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 CrKey/1.54.248666 Edg/138.0.0.0'
# }
# res=requests.get(url,headers=headers)
# print(res.text)
# with open("tieba.html",'wb') as f:
#     f.write(res.content)

# 2.获取百度贴吧多页
# url='http://tieba.baidu.com/f?'
# headers={
#     'User-Agent':'Mozilla/5.0 (Linux; Android) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 CrKey/1.54.248666 Edg/138.0.0.0'
# }
# cookies={
#     'BAIDUID':'F3C4D1E3E2A5D1B6C3F2E8D4B7A5C6E3:FG=1',
#     'BIDUPSID':'F3C4D1E3E2A5D1B6C3F2E8D4B7A5C6E3',
#     'PSTM':'1695223030',
#     'BDUSS':'VZfXlYbEZiMWx3Z1p5Yl9mZzZkR2x1TVRFeWFXVjNRV1E2TURBd0NnWUVBdXlLQUFBJCQAAAAAAAAAAAEAAABJ6c7h0dW5nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHg3aF4d4Nhe',
#     'TIEBAUID':'d5f5f0e5b1f6c8b7f0e5b1f6c8b7f0e5b1f6c8b7f0e5b1f6c8b7f0e5b1f6c8b7f0e5b1f6'
# }
# word=input("请输入贴吧名称：")
# page=int(input("请输入爬取页数："))
# for i in range(page):
#     params={
#         'kw':word,
#         'pn':i*50,
#     }
#     response=requests.get(url,headers=headers,params=params,cookies=cookies)
#     with open(f'{word}{i+1}.html','wb') as f:
#         f.write(response.content)
# # pn：第一页0，第二页50，第三页100，第四页150
# for i in range(4):
#     print(50*i)
    
# https://tieba.baidu.com/f?kw=%E6%9D%8E%E6%AF%85&ie=utf-8&pn=0
# https://tieba.baidu.com/f?kw=%E6%9D%8E%E6%AF%85&ie=utf-8&pn=50
# https://tieba.baidu.com/f?kw=%E6%9D%8E%E6%AF%85&ie=utf-8&pn=100
# https://tieba.baidu.com/f?kw=%E6%9D%8E%E6%AF%85&ie=utf-8&pn=150

# 3.改写为面向对象的形式
class TiebaSpider:
    def __init__(self):
        self.url='https://tieba.baidu.com/f?'
        self.headers={
            'User-Agent':'Mozilla/5.0 (Linux; Android) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 CrKey/1.54.248666 Edg/138.0.0.0'
        }
    # 发送请求
    def send_request(self,params):
        response=requests.get(self.url,headers=self.headers,params=params)
        return response.text
    # 保存数据
    def save_html(self,page,content):
        with open(f'{page}.html','w',encoding='utf-8') as f:
            f.write(content)
    def run(self):
        word=input("请输入贴吧名称：")
        pages=int(input("请输入爬取页数："))
        for page in range(pages):
            params={
                'kw':word,
                'pn':page*50,
            }
            data=self.send_request(params)
            self.save_html(page,data)
te=TiebaSpider()
te.run()