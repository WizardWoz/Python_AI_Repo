#import导入包时，首先执行__init.py__文件内的代码，不建议在__init.py__内写过多代码
#主要作用是导入所属包内的其他模块，相当于C的头文件
#__init__.py是把你其他所有地方写的文件收集在一起，最后只运行该文件就可以调用其他地方的文件
print("这是__init.py__")
#(1)导包方式一
# from pack_01 import register
# register.reg()

#__all__：本质上是一个列表，列表中的元素代表要导入的模块
#1.如果一个模块定义了__all__，那么from module import *只会导入__all__中列出的名称
#2.如果没有定义__all__，那么from module import *会导入所有不以下划线_开头的全局名称
#3.__all__应该是一个字符串列表list of strings，每个字符串代表一个可导出的名称
#4.__all__只影响import *的行为，不影响显式导入，比如import module或from module import name
__all__ = ["register"]  #相当于导入中括号内定义的模块