import requests
# 1.获取单张图片
# (1)找到目标URL
url='https://p5.music.126.net/obj/wonDlsKUwrLClGjCm8Kx/62665941769/2b89/4cf3/5dea/d58c86253972a57f13d9bd72f8b244de.png?imageView&quality=89'
# (2)构建请求头字典
headers={
    'User-Agent':'Mozilla/5.0 (Linux; Android) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 CrKey/1.54.248666 Edg/138.0.0.0'
}
# (3)发送请求、获取响应
res=requests.get(url,headers=headers)
# print(res.content)
with open('wangyiyun.jpg','wb') as f:
    f.write(res.content)

# 2.获取单首歌曲
url='https://m804.music.126.net/20250920100423/2cadb2d61fc8c6a1897787d329ee979c/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/62181734471/a1a2/59d1/5a2d/75d713b80a51cacadf46626290b8d344.m4a?vuutv=3olYQ5a+3XhK5970w21gRpsJ6zm8JpvjI68JmeVVTZmScc6N7dWp2/twrl1pmZePwlFS9iCXms4f3YQIjIsCM3TX6G1wC07rzCc5MlmeCyg=&authSecret=0000019964c6a2a108670a30847c1d3b&cdntag=bWFyaz1vc193ZWIscXVhbGl0eV9leGhpZ2g'
res=requests.get(url)
# print(res.content)
with open('wangyiyun.mp3','wb') as f:
    f.write(res.content)

# 3.获取单个MV
url='https://vodkgeyttp8.vod.126.net/cloudmusic/obj/core/62362392631/e674931e23c1d88b243c5cbbd4e5ab2f.mp4?wsSecret=ca9a44d1c35a34af00b14f50e922a985&wsTime=1758333783'
res=requests.get(url)
# print(res.content)
with open('wangyiyun.mp4','wb') as f:
    f.write(res.content)