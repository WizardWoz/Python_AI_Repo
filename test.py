print("这是test模块")
#变量
test_name='bingbing'
#函数
def funa():
    print("这是test模块中的funa()")
def funb():
    print("这是test模块中的funb()")

def test():
    print("哈哈哈")
#在test.py中执行会显示，test.py作为模块被其他.py文件import之后不会被执行
if __name__ == '__main__':
    print("这是test模块中的test()")