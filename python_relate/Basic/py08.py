# 1.OS模块：用于和操作系统进行交互
# 通用操作：(1)获取平台信息；(2)对目录的操作；(3)判断操作
import os
# (1)os.name()：指示正在使用的工作平台，返回操作系统类型
# Windows返回nt；Linux返回posix
# NT：New Technology；POSIX：Portable Operating System Interface of the Unix
print(os.name)
# (2)os.getenv(环境变量名称)：读取环境变量
print(os.getenv('PATH'))
# (3)os.path.split()：分割路径，把目录名和文件名分离，以元组的形式接收，第一个元素是目录路径，第二个元素是文件名
# 如果是Windows的文件路径（包含反斜杠），则在字符串前需要加上'r'变成原生字符串，防止路径内部出现转义字符影响分割
print(os.path.split(r"/home/george/Codes/Python_AI_Repo/python_relate/py08.py"))
o=os.path.split(r"/home/george/Codes/Python_AI_Repo/python_relate/py08.py")
print(o[0])
# (4)os.path.dirname()：显示split分割的第一个元素，即目录路径
print(os.path.dirname("/home/george/Codes/Python_AI_Repo/python_relate/py08.py"))
# (5)os.path.basename()：显示split分割的第二个元素，即文件名
print(os.path.basename("/home/george/Codes/Python_AI_Repo/python_relate/py08.py"))
# (6)os.path.exists()：判断路径是否存在，存在返回True，不存在返回False
print(os.path.exists("/home/george/Codes/Python_AI_Repo/python_relate/py08.py"))
print(os.path.exists("/home/george/Codes/Python_AI_Repo/python_relate/py80.py"))
# (7)os.path.isfile()：判断路径是否是一个文件，存在且是文件返回True，否则返回False
print(os.path.isfile("/home/george/Codes/Python_AI_Repo/python_relate/py08.py"))
# (8)os.path.isdir()：判断路径是否是一个目录，存在且是目录返回True，否则返回False
print(os.path.isdir("/home/george/Codes/Python_AI_Repo/python_relate/py08.py"))
print(os.path.isdir("/home/george/Codes/Python_AI_Repo/python_relate"))
# (9)os.path.abspath()：返回当前路径的绝对路径
print(os.path.abspath("."))
print(os.path.abspath("py08.py"))

# 2.sys模块：负责程序与Python解释器之间的交互，用于访问和操作Python运行时环境的变量和功能
import sys
# (1)sys.getdefaultencoding()：获取当前默认的字符串编码方式
print(sys.getdefaultencoding())
# (2)sys.path：一个列表，包含了Python解释器的模块搜索路径，可通过此路径获取环境变量、导入模块等
print(sys.path)
print(sys.path[0])  # 第一个元素通常是当前脚本所在的目录
print(sys.path[-1])  # 最后一个元素通常是Python安装目录
# (3) sys.platform：获取当前操作系统平台的名称；与os.name()区别
print(sys.platform)  # 输出操作系统平台名称，如'win32'或'linux'等
# (4) sys.version：获取Python解释器的版本信息
print(sys.version)  # 输出Python版本信息，如'3.8.5 (default, Jul 20 2020, 08:00:00) \n[GCC 7.5.0]'

# 3.time模块：用于处理时间相关的任务
import time
# 三种时间表示：(1)时间戳(timestamp)；(2)格式化时间字符串(format time)；(3)结构化时间元组(struct_time)
# (1)time.time()：获取当前时间戳（从1970年1月1日0时0分0秒到现在所经过的秒数），是浮点型数据
print(time.time(),type(time.time()))  # 输出当前时间戳及其类型
# (2)time.sleep(秒数)：使程序暂停指定的秒数
print("程序暂停前的时间戳:", time.time())
time.sleep(3)  # 暂停3秒
print("程序暂停后的时间戳:", time.time())
# (3)格式化时间字符串：将时间戳转换为可读性较强的时间格式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# (4)结构化时间元组：将时间戳转换为结构化时间元组time.struct_time，含有九个元素
print(time.localtime(),type(time.localtime()))  # 输出当前时间的结构化时间元组及其类型
print(time.localtime().tm_year)  # 输出当前年份
# (5)time.asctime()：将结构化时间元组time.struct_time转换为可读性较强的字符串格式
print(time.asctime(time.localtime()))  # 输出当前时间
t=time.time()
# print(time.asctime(t))  # 会报错，不能直接将时间戳传入asctime函数
print(time.asctime(time.localtime(t)))  # 将时间戳转换为结构化时间元组后再传入asctime函数
# (6)time.ctime()：将时间戳转换为可读性较强的字符串格式，等同于asctime(time.localtime())
print(time.ctime(t))  # 输出当前时间
# (7)time.strftime(格式化字符串,struct_time)：将结构化时间元组转换为指定格式的字符串
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  # 输出当前时间
# (8)time.strptime(时间字符串,格式化字符串)：将时间字符串转换为结构化时间元组
print(time.strptime("2023-10-01 12:00:00", "%Y-%m-%d %H:%M:%S"))  # 输出结构化时间元组

# 4.logging模块：用于记录程序运行时的日志信息，便于调试和追踪问题
# 日志的作用：了解程序运行情况是否正常；记录程序运行中的重要信息、错误信息和调试信息，便于后续分析和问题定位
# 级别排序（从高到低）：CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET
import logging
# (1)logging日志记录的级别
logging.debug("This is a debug message")  # 调试信息
logging.info("This is an info message")  # 一般信息
# logging默认level就是WARNING，只会显示级别大于等于WARNING的日志信息，所以debug和info不会输出
logging.warning("This is a warning message")  # 警告信息
logging.error("This is an error message")  # 错误信息
logging.critical("This is a critical message")  # 严重错误信息
# (2)logging.basicConfig(filename,filemode)：配置日志记录的基本设置，如日志级别
# filename指定日志文件的文件名，所有会显示的日志信息都会写入该文件
# filemode='w'表示每次运行程序时都会覆盖之前的日志文件，'a'表示追加到日志文件末尾
# level：指定日志显示级别，默认是警告信息warning
# format：指定日志信息的输出格式
logging.basicConfig(filename='./testlog.log',filemode='a',level=logging.NOTSET,
format='%(levelname)s:%(asctime)s\t%(message)s')
logging.debug("debug")  # 调试信息
logging.info("info")  # 一般信息
# logging默认level就是WARNING，只会显示级别大于等于WARNING的日志信息，所以debug和info不会输出
logging.warning("warning")  # 警告信息
logging.error("error")  # 错误信息
logging.critical("critical")  # 严重错误信息

# 5.random模块：用于生成随机数，可实现各种概率分布
import random
# (1)random.random()：生成一个[0.0, 1.0)范围内的随机浮点数
print(random.random())
# (2)random.uniform(a, b)：生成一个[a, b]范围内的随机浮点数
print(random.uniform(1, 10))
# (3)random.randint(a, b)：生成一个[a, b]范围内的随机整数
print(random.randint(1, 10))
# (4)random.randrange(start, stop[, step])：生成一个[start, stop)范围内的随机整数，步长为step
print(random.randrange(1, 10, 2))  # 从1到9之间的奇数中随机选择一个