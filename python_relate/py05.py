# 1.可迭代对象Iterable：实现了Python迭代协议，可通过for...in...遍历的对象
# (1)对象实现了__iter__()方法
# (2)__iter__()方法返回了迭代器对象
# 遍历（迭代）：依次从对象中把单个元素取出来的过程
# 数据类型：str、list、tuple、dict、set等均属于可迭代对象

# 2.迭代器Iterator：是一个可以记住遍历位置的对象；在上次停留的位置继续做一些事情，只能往前不能往后
# 同一个可迭代对象可通过多次调用iter()/__iter__()获取不同的迭代器，每个迭代器保存自身状态不会互相干扰
li=[1,2,3,4,5]
for i in li:
    print(i)
# iter()：调用list对象的__iter__()，并把__iter__()的返回结果作为自己的返回值（可迭代对象的迭代器）；
# next()：调用Iterator对象的__next__()，一个个地取元素，取完元素后会引发一个StopIteration异常
li=[1,2,3,4,5]
print(dir(li))
# (1)创建可迭代对象
li2=iter(li)
print(dir(li2))
print('li2:',li2)
li3=li.__iter__()
print(dir(li3))
print('li3:',li3)
# (2)获取下一条数据
print(next(li2))
print(next(li2))
print(next(li2))
print(next(li2))
print(next(li2))

print(li3.__next__())
print(li3.__next__())
print(li3.__next__())
print(li3.__next__())
print(li3.__next__())
# (3)取完元素后，再使用next()或__next__()会引发StopIteration异常
# print(next(li2))
# print(li3.__next__())

# 3.isinstance(o,t)：o是对象；t是类型（可以是类型元组）
# 判断一个对象是否是可迭代对象，或者是一个已知的数据类型；使用前要导入模块
# from collections import Iterable    #Python 3.3版本之前这样导入
from collections.abc import Iterable,Iterator
st='123'
# 可迭代对象不一定是迭代器对象
print(isinstance(st,Iterable))      # 是可迭代对象
print(isinstance(st,Iterator))      # 但不是迭代器对象
# 迭代器对象一定是可迭代对象
st1=iter(st)    # 可迭代对象通过iter()强制类型转换为迭代器对象
print(isinstance(st1,Iterator))      # 此时转为迭代器对象
print(isinstance(st1,Iterable))      # 是可迭代对象
print(isinstance(123,Iterable))
print(isinstance(123,(dict,Iterable)))
print(isinstance(123,(dict,int)))
# 可迭代对象：拥有__iter__()
# 迭代器对象：拥有__iter__()、__next__()

# 4.迭代器协议：迭代器对象都是实现了该协议的对象；必须提供一个next()方法，
# 执行该方法要么返回迭代中的下一项，要么就引发StopIteration异常来终止迭代
# 自定义迭代器类：__iter__()和__next__()
class MyIterator(object):
    def __init__(self):
        self.num=0
    def __iter__(self):
        return self     # 返回当前迭代器类的实例对象
    def __next__(self):
        # 加上判断结束的条件
        if self.num==10:
            raise StopIteration("终止迭代，数据已经被取完了")   # 抛出StopIteration异常
        self.num+=1
        return self.num
mi=MyIterator()
print(isinstance(mi,Iterator))
print(next(mi))

# 5.for循环工作原理：
# (1)先通过__iter__()获取可迭代对象的迭代器
# (2)对获取到的迭代器不断调用__next__()方法来获取下一个值并将其赋值给临时变量i
for i in mi:
    print(i)

# 6.生成器generator：使用了yield()方法的迭代器Iterator；本质仍是迭代器（可迭代对象），一边循环、一边计算的机制
# (1)生成器表达式：类似列表推导式；列表推导式的[]改成()就成了生成器表达式
li=[i*5 for i in range(5)]      # 列表推导式
print(li)

gen=(i*5 for i in range(5))     # 生成器表达式
print(gen)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen))

# (2)生成器函数：使用了yield关键字的函数
# yield的作用：类似return，将指定值或多个值返回给调用者；一次返回一个结果，在每个结果中间挂起函数，执行__next__()，再重新从挂起点继续向下执行
# 是函数中断并保存中断的状态
def gen(n):
    li=[]
    for i in range(n):
        yield i     # 返回一个i并暂停函数，在此挂起，下一次再从此处恢复执行
        li.append(i)
    print("li:",li)
gen_01=gen(5)
print(gen_01)
for i in gen(5):
    print(i)
# print(next(gen_01))