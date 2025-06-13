#1.单例模式：一种常见的软件设计模式，主要目的是确保某一个类只有一个实例存在，内存地址都一样
#优点：可以节省内存空间；缺点：多线程访问时容易引发线程安全问题
#(1)实现方式一：@classmethod
#(2)实现方式二：通过装饰器
#(3)实现方式三（重点）：通过重写__new__()
#<1>定义一个类属性，初始值为None，用来记录单例对象的引用
#<2>重写__new__()
#<3>进行判断，如果类属性是None，则保存__new__()返回的对象引用
#<4>返回类属性中记录的对象引用
class Singleton(object):
    _instance = None    #记录第一个被创建的对象的引用
    def __new__(cls, *args, **kwargs):
        print("这是__new__()方法")
        #判断类属性是否为空
        if cls._instance == None:
            cls._instance = super().__new__(cls)
        return cls._instance
    def __init__(self):
        print("这是__init__()方法")
s1=Singleton()
print("s1：",s1)
s2=Singleton()
print("s2：",s2)
#(4)实现方式四：通过导入模块；模块是天然的单例模式
from test2 import te as te01
print(te01,id(te01))

#应用场景：回收站对象、音乐播放器、（游戏）场景管理器、数据库配置/连接池