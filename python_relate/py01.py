#1.Python是什么？
#Python是面向对象的高级解释型语言；是强类型的动态脚本语言

#2.编写第一个程序
# print("hello world")    #这是Python注释

#3.bug与debug
#(1)输入错误，检查所有拼写
# print（"hello world"）  #使用了中文括号
#注意：Python中的符号都是英文模式下的
#(2)缩进错误，语句必须顶格写
  # print(123)
#(3)语法错误，同一行若要写多个语句则之间要加;或,
# print("hello world"), print(123)

#4.命名错误
# helloworld=1
# print(helloworld)     #不加引号（单引号或双引号）即为变量，要先声明并定义（赋值）后才能使用
# print(123)
# print(123)
# print(123)

#debug中蓝色代码行表示即将要运行的代码

'''
    我是多行注释
'''
# from idlelib.grep import findfiles    #从idlelib.grep包中引入模块findfiles

"""
    我也是多行注释
"""

#5.输出函数print()
#输出多个值之间应该使用,分隔
#每个输出之间可以使用sep='分隔符'进行分开，但是一个print函数只能包含一个分隔符
#end='...'用于设定结尾的符号，默认使用\n换行符
# print("哈哈哈","123",'456',sep=',',end='\t')
# print("789")

#6.变量
#变量只有声明并定义后才会被创建，所以使用变量前要赋值
# num1=3;num2=2
# total=num1+num2
# print(total,num1,num2,sep=',')
# a=666
# b=a
# a=999
# print(a,b,sep=',')
#同一个变量可以被反复赋值，并且可以是不同的数据类型
# a='haha'
# b=1.4
# print(a,b,sep=',')

#7.标识符
#只能由数字、字母、下划线_组成（Python 3支持中文作为变量名但是不推荐使用）
_ad=123;ad=123;a123=123;我=1
print(我,sep=',')
(a)=1
print((a))
#不能以数字开头
# 1_ad=123
#不能是关键字（Python已经使用的标识符，具有特殊的含义，不允许用户使用）
# False=1
#严格区分大小写

#8.数值类型
#int整型：任意大小的整数
num1=-1
print(type(num1))    #type函数：检测变量数据类型
#float浮点数：任意大小的小数
num2=1.2
print(type(num2))    #type函数：检测变量数据类型
#bool布尔型：有固定写法，一个为真True，一个为假False；可以当作整型对待：True=1；False=0
print(type(True))    #type函数：检测变量数据类型
print(type(False))    #type函数：检测变量数据类型
print(False+True)
#complex复数型：z=a+bj；a是实部，b是虚部，j是虚数单位（只能是j，不能改成其他的）
print(type(2+3j))    #type函数：检测变量数据类型
ma1=1+2j
ma2=2+3j
print(ma1+ma2)
#字符串类型：单行字符串用""或''；多行字符串用""""""或''''''；没有引号将会识别成变量名
name='你hao呀'
str1="""
    123
    456
    789
"""
str2='''
    123
    456
    789
'''
print(type(name))    #type函数：检测变量数据类型
print(name)
print(type(str1))
print(str1)
print(type(str2))
print(str2)

#9.格式化输出
#占位符：生成一定格式的字符串，只是占据位置不会被输出
#%s：字符串；%d：整数；%nd：n位整数，预留位数n>源数据位数前面留空白；预留位数n<=源数据位数按原样输出
#%f：浮点数；%.nf，n位小数，预留位数n>源数据位数后面补0；预留位数n<=源数据位数则四舍五入；%%
name='bingbing'
age=18
a=123
b=1.666666666
print("我的名字是：%s，我的年龄是：%d" %(name,age))
print("%2d" %a)
print("%06d" %a)        #预留位数n>源数据位数前面用字符'0'补全
print("%f" %b)          #默认六位小数，源数据位数不够后面补0，源数据长度>6则四舍五入
print("%.3f" %b)
print("%.9f" %b)
#f格式化：f"{表达式}"
print(f"我的名字是：{name}，我的年龄是：{age}")

#10.算术运算符
print(1+1)
print(1/2)      #商一定是浮点数，且除数不能为0
a=0/1
print(type(a))
#取整除//，向下取整，不管四舍五入的原则，只要后面有小数就忽略小数
a=5
b=2
print(a//b)
#取余数%，只取余数部分
print(a%b)
#幂运算**：m**n代表m的n次方
m=2
n=1.5
print(m**n)

#11.input()函数，输入内容被看作字符串
# name=input("请输入姓名：")     #参数__prompt是提示语句
# print(name)
# score=int(input("请输入成绩："))   #使用int()函数将输入的字符串转换成整数

#12.转义字符
#\t制表符：通常表示四个空格字符
print("123\t45\t678")
print("姓名\t年龄\t电话")
#\n换行符：将当前位置移到下一行开头
print("haha\nxixi")
#\r回车符：将当前位置移到本行开头
print("hahaha\rxixi")
#\\直接输出一个'\'
print("123\\t45\t678")
print("\\\\")

#13.if、if-else、if-elif、if-elif-else判断
score=input("请输入成绩：")
if score=='100':
    print("你真棒")
if score=="60":
    print("还需加油")

a=666
if a==666:
    print("OK")
else:       #else后面无需添加任何东西
    print("NOT OK")

score=120
if 85<=score<=100:
    print("成绩优秀")
elif 60<=score<85:
    print("成绩及格")
elif 0<=score<60:
    print("成绩及格")
else:
    print("分数无效")

#嵌套if：内层if判断和外层if判断，可以是不同或相同结构
ticket=True
temp=38.5
if ticket==True:
    print("可以进站")
    if 36.5<=temp<=37.2:
        print("体温正常")
    else:
        print("体温异常")

#14.运算符
#比较（关系）运算符
a=666
b=999
print(a==b)     #相等返回True，不相等返回False
print(a!=b)     #不相等返回True，相等返回False
#逻辑运算符
a='哈哈'
b='嘿嘿'
if a=='哈哈' and b=='嘿嘿':
    print("a和b都在笑")
fruit='西瓜'
if fruit=='苹果' or fruit=='水蜜桃':
    print("带回了水果")
print(not 3>9)      #也可写成print(not (3>9))

#15.循环
i=1     #i记录循环的次数
s=0     #s记录相加的和
while i<=100:
    s=s+i
    i+=1
print(s)
#条件只要不为False，即不为0，则一定是死循环
# while True:
#     print("123")      #死循环里可以嵌套条件，当满足条件时，break可以就能结束循环了
while False:
    print("123")
#多层循环
i=1     #i记录外层循环次数
while i<=3:
    print(f"外循环{i}次")
    j=1     #j记录内层循环次数
    while j<=5:
        print(f"内循环{j}次")
        j+=1
    i=i+1
#for循环
st="hello world"
for i in st:       #i是临时变量，可以随便取，i只是常规写法
    print(i)
#range()函数：range(start,stop,step)，start起始下标；stop终止下标；step步长（默认为1）
#从1开始，11结束，遵循包前不包后原则（即[左闭右开)）；所以1<=i<11
#range()括号内只写一个数，就是循环的次数，默认从0开始
s=0
for i in range(1,101):
    s+=i
print(s)    #没有大括号，靠缩进体现层级
#break和continue只能放在循环内
i=1
while i<=5:
    print(f"在吃第{i}个苹果")
    if i==3:
        print("吃饱了")
        break
    i+=1
i=1
while i<=5:
    print(f"在吃第{i}个苹果")
    if i==3:
        print(f"第{i}个苹果有虫子")
        i+=1        #continue前一定要修改计数器变量
        continue
    i+=1

#16.字符串
#编解码
a='hello'
print(a,type(a))    #类型是str，以字符为单位
a1=a.encode()       #字符串a编码
print("编码后：",a1)
print(type(a1))     #类型是bytes，以字节为单位
a2=a1.decode()      #字节流a1解码
print(a2,type(a2))
st="中文字符串"
st1=st.encode("utf-8")
print("编码后：",st1)
st2=st1.decode("utf-8")
print("解码后：",st2)
#字符串拼接
print("10"+'10')    #字符串拼接'+'号
name1="你好"
name2="世界"
print(name1,name2,sep='')   #等同于字符串拼接'+'号
print("你好"*5)       #字符串重复输出'*'号
#成员运算符
name="bingbing"
print('b' in name)
print('a' in name)
print('bin' in name)
print('binb' in name)
name="冰冰"
print('冰' in name)
#下标，Python下标自左向右从0开始；自左向右从-1开始
name='sixstar'
print(name[0])
# print(name[7])      #数组越界
print(name[-1])
# print(name[-8])       #数组越界
#切片：对操作的对象截取其中一部分[start:stop:step]
#start起始下标（默认为0）；stop终止下标（默认为最后下标+1）；step步长（默认为1）；遵循包前不包后原则（即[左闭右开)）
#start>=stop，无论是自左向右还是自右向左；步长正负号决定切取方向，绝对值大小决定切取间隔
st="asdfghjkl"
print(st[0:3])
print(st[4:7])
print(st[3:])
print(st[:5])
print(st[0:-2])     #结束下标也可以是尾部开始的负数
# print(st[-2:3])     #无效的下标范围
print(st[-4:])
print(st[-4:-1])
print(st[-1::1])    #只切取到l
print(st[-1::-1])   #切取到lkjhgfdsa
print(st[0:9:2])    #切取到adgjl
#字符串查找
#find()：检查某个字符串是否被包含在另一字符串中，若包含则返回所在下标，若不存在返回-1
#find(子字符串,开始位置下标start（默认为0），结束位置下标stop（默认为最后字符的下标）)
#遵循包前不包后原则（即[左闭右开)）
name="bingbing"
print(name.find('g'))
print(name.find('b',3)) #返回4
print(name.find('b',5)) #返回-1
print(name.find('b',3,4))   #返回-1，包前不包后

#index()：检查某个字符串是否被包含在另一字符串中，若包含则返回所在下标，若不存在则抛出异常
#index(子字符串,开始位置下标start（默认为0），结束位置下标stop（默认为最后字符的下标）)
#遵循包前不包后原则（即[左闭右开)）
name="我是谁？"
print(name.index('？'))
# print(name.index('我',3))    #直接抛出异常

#count()：返回某个字符串在整个字符串中出现的次数，没有就返回0
#count(子字符串,开始位置下标start（默认为0），结束位置下标stop（默认为最后字符的下标）)
#遵循包前不包后原则（即[左闭右开)）
name="bingbing"
print(name.count('b'))      #返回值为2
print(name.count('a'))      #返回值为0
print(name.count('b',1))    #返回值为1
print(name.count('b',1,4))  #返回值为0

#startswith()：是否以某个字符串开头，是的话返回True，不是的话返回False
#startswith(子字符串,开始位置下标start（默认为0），结束位置下标stop（默认为最后字符的下标）)
st="sixstar"
print(st.startswith('s'))
print(st.startswith('s',4))

#endswith()：是否以某个字符串结尾，是的话返回True，不是的话返回False
st="sixstar"
print(st.endswith('r'))

#isupper()：检测字符串中所有字母是否均为大写，是的话就返回True
st="sixstar"
print(st.isupper())

#修改元素
#replace(旧内容,新内容,替换次数)
st="好好学习，天天向上"
print(st.replace("天","时"))

#split()：指定分隔符来切割字符串
st="Hello,Python"
print(st.split(','))#以列表的形式返回切割结果['Hello', 'Python']
print(st.split('a'))#如果字符串不包含分隔符，则源字符串作为一个整体出现['Hello,Python']
print(st.split('o'))#可以分割多次
print(st.split('o',1))#可设置最大分割次数

#capitalize()：第一个字符大写，其他字符小写
st="bingBing"
print(st.capitalize())

#lower()：大写字母转为小写字母
st="bIngBinG"
print(st.lower())

#upper()：小写字母转为大写字母
st="bIngBinG"
print(st.upper())

#17.列表
#列表名=[元素1,元素2,元素3......]，可以有无限个元素，元素之间的数据类型可互不相同
li=[1,2,'3',4]
print(li,type(li))
print(li[0],li[2])
print(li[0:3])      #列表也可进行切片操作
#列表是可迭代对象，可以for循环遍历取值
for i in li:
    print(i)
#列表添加元素
#append()：整体添加
li=['one','two','three']
li.append('four')
print(li)
#extend()：分散添加，参数必须是可迭代对象（字符串、另一个列表...）
li.extend('five')
print(li)
#insert()：在指定位置插入元素，原有元素会后移
li.insert(1,'six')
# li.insert("hello")  #必须指定位置，不然会报错
print(li)
li=[1,2,3]
li.append(4)
print(li)
# li.extend(4)    #4为整型变量，不是可迭代变量，所以不行
li.extend([5])
print(li)

#列表修改元素：直接通过下标修改
li[2]='a'
print(li)

#列表查找元素：in，not in类似字符串操作
li=['a','b','c','d']
print('a' in li)
print('e' in li)
#用户输入昵称，昵称重复则不可使用
name_list=['bingbing','susu','ziyi']
name=input('请输入昵称：')
while True:
    if name in name_list:
        print(f"您输入的昵称{name}已经存在")
    else:
        print(f"昵称{name}已经被您使用")
        name_list.append(name)
        break
print(name_list)

#index()：检查某个字符串是否被包含在另一字符串中，若包含则返回所在下标，若不存在则抛出异常
#index(子字符串,开始位置下标start（默认为0），结束位置下标stop（默认为最后字符的下标）)
#遵循包前不包后原则（即[左闭右开)），和字符串中的用法相同

#count()：返回某个字符串在整个字符串中出现的次数，没有就返回0
#count(子字符串,开始位置下标start（默认为0），结束位置下标stop（默认为最后字符的下标）)
#遵循包前不包后原则（即[左闭右开)），和字符串中的用法相同

#删除元素
#del
li=['a','b','c','d']
# del li      #删除整个列表，之后的print会报错
del li[0]       #根据下标删除
del li[-1]
print(li)
#pop()：删除指定下标的数据，Python 3版本默认删除最后的元素
li=['a','b','c','d']
li.pop()    #默认删除最后的元素
print(li)
li.pop(0)   #删除下标为2的元素
li.pop(0)   #被删除元素下标不能超出范围
print(li)
#remove():根据元素的值删除
li=['a','b','c','d','b']
li.remove('b')      #若有重复元素，则删除首先找到的
print(li)
# li.remove('t')      #报错，因为li列表中并不含有字符't'
# print(li)
#sort()：顺序排序，将列表按从小到大顺序重新排列
li=[1,4,63,7,4,9]
li.sort()
print(li)
#reverse()：将列表逆置（反过来），而不会排序
li.reverse()    #li.sort()+li.reverse()可以做到将列表逆序排序
print(li)

#列表推导式
#格式一：[表达式 for 变量 in 列表]；in后面可以放列表、range()、可迭代对象
li=[1,2,3,4,5,6]
#例如：[2*x for x in [1,2,3]] 相当于 {2x | x∈{1,2,3}} 。唯一区别就是列表有序，集合无序。
[print(i) for i in li]  #列表推导式相当于数学集合的描述法
#等价于
# for i in li
#     print(i)
li=[]
[li.append(i) for i in range(1,6)]
print(li)
#等价于
# for i in range(1,6):
#     li.append(i)

#格式二：[表达式 for 变量 in 列表 if 条件]
#把奇数放进列表内
li=[]
[li.append(i) for i in range(1,11) if i%2==1]
print(li)
#等价于
# for i in range(1,11):
#     if i%2==1:
#         li.append(i)
# print(li)

#列表嵌套（相当于C语言的二维数组）
li=[1,2,3,[4,5,6]]
print(li[3])        #取出里面的列表
print(li[3][0])     #取出里面的列表的某个元素

#18.元组（类似C语言的枚举类型enum）
#基本格式：元组名=(元素1,元素2,元素3......)，不同元素也可以是不同数据类型
tua=(1,2,3,4,1,'a',[6,7,8])
print(tua,type(tua))
tub=(1,)    #元组只有一个元素，末尾一定要加上','
print(tub,type(tub))
#元组只支持查询操作，不支持增删改操作；如果元组含有列表元素，则可以修改列表
tua[6].insert(3,9)
print(tua)
# tua[0]=7    #报错，不支持改变非列表类型的成员
# print(tua)
#count()、index()、len()、切片、in、not in等等，用法和列表相同
print(tua.count(1))
print(tua.index(3))
print(len(tua))
print(tua[1:])
#应用场景
#1.函数的参数和返回值
#2.格式化输出后面的%()本质上就是一个元组
name="bingbing"
age=18
print("%s的年龄是：%d" %(name,age))
#等价于
# info=("bingbing",18)
# print("%s的年龄是：%d" %info)

#19.字典dict：键值对形式保存，键和值之间用:隔开，每个键值对之间用,隔开
#基本格式：字典名={键1:值1,键2:值2,键3:值3,......}；无论键或者值，如果是字符串类型都要用""或''包裹
#键具备唯一性，值可以重复
dic={'name':'bingbing','age':18}
print(dic,type(dic))
#当键名重复时，以最后出现的键值对为准
dic1={'name':'bingbing','name':"susu"}
print(dic1)
dic2={'name1':'bingbing','name2':"bingbing"}
print(dic2)

#查看字典元素
dic={'name':'bingbing','age':18}
#方法一：通过字典名[键名]
# print(dic[0])         #字典中没有下标
print(dic['name'])      #查找元素需要根据键名
# print(dic['gender'])  #键名不存在也会报错
#方法二：通过字典名.get(键名)
print(dic.get('age'))
print(dic.get('gender'))#键名不存在，会返回None
print(dic.get("tel","不存在"))#键名不存在，返回信息"不存在"

#修改字典元素
dic={'name':'bingbing','age':18}
#方法一：通过字典名[键名]，注意键名存在就修改，不存在则新增
dic['age']=20
print(dic)

#添加字典元素
dic={'name':'bingbing','age':18}
#方法一：通过字典名[键名]，注意键名存在就修改，不存在则新增
dic['gender']="male"
print(dic)

#删除字典元素
dic={'name':'bingbing','age':18}
# del dic     #删除整个字典
# print(dic)  #报错，dic已经被删除，找不到该字典
del dic['age']
print(dic)
# del dic['gender']   #删除不存在的键值对也会报错

#clear()：清空字典保存的所有内容，但保留空字典
dic.clear()
print(dic)
dic['age']=18   #又能继续增删改查
print(dic)

#pop()：删除指定键值对，键不存在则报错
dic={'name':'bingbing','age':18}
dic.pop('age')
print(dic)
# dic.pop('gender')
# print(dic)

#len()：求字典长度（字符串、元组、列表、字典......）
dic={'name':'bingbing','age':18,'tel':"123"}
print(len(dic))

#keys()：返回字典里包含的所有键名
dic={'name':'bingbing','age':18,'tel':"123"}
print(dic.keys())
for i in dic.keys():    #只取出键名
    print(i)

#values()：返回字典里包含的所有值
dic={'name':'bingbing','age':18,'tel':"123"}
print(dic.values())
for i in dic.values():    #只取出值
    print(i)

#items()：返回字典里包含的所有键值对
dic={'name':'bingbing','age':18,'tel':"123"}
print(dic.items())  #返回的键值对是以元组形式存在
for i in dic.items():    #只取出键值对元组
    print(i)

#字典的应用场景
#1.使用键值对，存储描述一个物体的相关信息

#20.集合set：元素无序且唯一，可用于元组、列表去重
#基本格式：集合名={元素1,元素2,元素3,......}
# s1={}       #定义空字典
# s1=set()    #定义空集合
s1={1,2,3,4,5,6,7}
print(s1)       #存储整形数据的集合每次打印结果一样
s1={'a','b','c','d','e','f','g'}
print(s1)       #存储字符数据的集合每次打印结果不一样
#集合无序的实现方式涉及Hash表
#每次运行结果Hash值都不同，所以在Hash表中的位置也不同
print(hash('a'))
print(hash('b'))
print(hash('c'))
#每次运行结果Hash值都相同，所以在Hash表中的位置也相同
print(hash(1))
print(hash(2))
print(hash(3))

#集合唯一性可以使它自动去重
s1={1,2,3,2,4,2,5,2}
print(s1)

#集合添加元素
#add()：添加的是一个整体
s2={1,2,3,4}
print("add()原集合：",s2)
s2.add(5)
print("add()现集合：",s2)
#集合的唯一性：决定若集合已存在需要添加的元素，则不进行任何操作
# s2.add(5,6)     #一次只能添加一个元素，添加多个会报错

#update()：把传入的元素拆分，分别放入集合中
s2={1,2,3,4}
print("update()原集合：",s2)
# s2.update(567)    #整型会报错，因为update添加的元素必须是可迭代对象
s2.update((5,6,7))
print("update()现集合：",s2)

#remove()：删除元素
s2={1,2,3,4}
print("remove()原集合",s2)
s2.remove(3)
print("remove()现集合",s2)
# s2.remove(7)        #remove()删除集合中没有的元素会报错

#pop()：弹出元素，对集合无序排列，然后删除第一个元素（存整型数据的集合除外）
s2={1,2,3,4}
print("pop()原集合",s2)
s2.pop()        #默认弹出第一个元素1
print("pop()现集合",s2)

#discard()：选择要删除的元素，有则删除，没有则不会发生任何改变（不会进行任何操作）
s2={1,2,3,4}
print("discard()原集合",s2)
s2.discard(3)
print("discard()现集合",s2)
s2.discard(9)       #discard()删除集合中没有的元素

#交集和并集
a={1,2,3,4}
b={3,4,5,6}
print(a&b)          #求交集、求并集
print(a|b)
s1={'a','b'}
s2={'c','d','e'}
print(s1&s2)        #返回空集合set()

#21.类型转换
#int()：转换为一个整数，只能转换由纯数字构成的字符串
a=1.2
b=int(a)        #浮点型强转整型会去掉小数点以及后面的数值，只保留整数部分
print(a,type(a))
print(b,type(b))
#如果字符串中有数字和正负号之外的字符，则会报错
a="123"
print(a,type(a))
a='+10'
print(a,type(a))
a="-10"
print(a,type(a))

age=int(input("请输入年龄："))
# age=input("请输入年龄：")
if age>=18:
    print("成年了")

#float()：转换为一个小数
print(float(11))    #整型转为浮点型，会自动添加一位小数

#str()：可将任意数据类型转换为字符串类型
n1=100
n2=str(n1)
print(n1,n2,type(n1),type(n2))
n1=-1.3100
n2=str(n1)      #float转换成str会截取末尾为0的部分
print(n1,n2,type(n1),type(n2))
li=[1,2,3]
st=str(li)      #输出[1, 2, 3]，也即整个li列表被看作一个字符串
print(st)
#eval()：执行一个字符串表达式，并返回表达式的值
print(10+10)
print('10'+'10')
print('10+10')
print(eval('10+10'))

#可以实现tuple、list、dict、str之间的转换
st1="[[1,2],[3,4],[5,6]]"
print(type(st1))
li=eval(st1)
print(li,type(li))
st2="{'name':'bingbing','age':18}"
dic=eval(st2)
print(dic,type(dic))

#list()：将可迭代对象转换成列表，支持转换成列表的类型：str、tuple、dict、set
li=list('123')
print(li,type(li))
tu=list((1,2,3,4))
print(tu,type(tu))
dic=list({'name':'bingbing','age':18})  #只输出键名
print(dic,type(dic))    #字典转换成列表，会取键名作为列表的值
se=list({'1','2','3','4','2'})
print(se,type(se))      #集合转换成列表，会先去重再转换

#22.深拷贝、浅拷贝：实现数据赋值的两种方法，只针对可变对象，不可变对象没有拷贝的说法
li=[1,2,3,4]
print('新增前li',li)
#赋值，等于变量之间共享内存资源，会随着原对象一起变化
li2=li
print('新增前li2',li2)
li.append(5)
#li、li2本质上指向同一个物理地址的对象，只是贴上了不同的名称标签
print('新增后li',li)       #新增后li [1, 2, 3, 4, 5]
print('新增后li2',li2)     #新增后li2 [1, 2, 3, 4, 5]
#查看内存地址id()
print('li内存地址',id(li))
print('li2内存地址',id(li2))

#浅拷贝：会创建新的对象，拷贝第一层的数据，嵌套层会指向原来的内存地址
#写程序大多数情况下使用浅拷贝；拷贝速度快，占用空间少
import copy     #浅拷贝需要导入copy模块
li=[1,2,3,[4,5,6]]
li2=copy.copy(li)   #实现浅拷贝
print('li',li)
print('li2',li2)
#查看内存地址id()
print('li内存地址',id(li))
print('li2内存地址',id(li2))
li.append(7)
print('li',li)
print('li2',li2)
#外层内存地址不同，但是内层的内存地址相同
li[3].append(8)     #在内层嵌套列表添加元素
print("li[3]内存地址",id(li[3]))
print("li2[3]内存地址",id(li2[3]))

#深拷贝：数据完全不共享，外层的对象和内部的元素均拷贝了一遍
import copy     #深拷贝也需要导入copy模块
li=[1,2,3,[4,5,6]]
li2=copy.deepcopy(li)
print('li',li,id(li))
print('li2',li2,id(li2))
li.append(7)
print('li',li)
print('li2',li2)
li[3].append(8)     #在内层嵌套列表添加元素
print('li',li,id(li[3]))
print('li2',li2,id(li2[3]))
#深拷贝数据变化只影响自己本身，跟原来的对象没有关联

#23.可变对象：存储空间保存的数据允许被修改（变量对应的值可修改，但内存地址不能改变）
#例：列表list、字典dict、集合set
li=[1,2,3,4]
print('li的内存地址：',id(li))
li.append(5)
print('li',li)
print('li的现内存地址：',id(li))
dic={'name':'bingbing','age':18}
print(dic,id(dic))
dic['name']='susu'
print(dic,id(dic))
set={1,2,3,4,5}
print(set,id(set))
set.remove(5)
print(set,id(set))

#不可变对象：存储空间保存的数据不允许被修改，如果修改就会重新分配内存空间存储新的值
n=10
print(n,"n原地址：",id(n))
n=15
print(n,"n新地址：",id(n))      #验证内存地址不一样
st="hello"
print(st,"st原地址",id(st))
st='bingbing'
print(st,"st新地址",id(st))
tua=(1,2,3)
print(tua,id(tua))
tua=('a','b','c')
print(tua,id(tua))

#24.函数
#(1)定义函数：
# def 函数名()
#     函数体
#(2)函数名
def login():
    print("这是登录函数")
login()
login()

#(3)返回值：函数执行结束后return给调用者的一个结果
#作用：
#
def buy():
    #return返回多个值，是以元组类型返回给调用者
    # return "一桶水果茶",20      #return返回调用者后不再执行之后的代码
    # return 20
    return      #单独return语句返回None
buy()
print(buy())

def add(arg1,arg2):
    return arg1+arg2
print(add(1,2))

#函数参数
#(1)必备参数（位置参数）
#含义：传递和定义参数的顺序及个数必须一致
def funa(name,age,gender):
    print("姓名：",name)
    print("年龄：",age)
    print("性别：",gender)
funa('bingbing','18','女')
#(2)默认参数：为参数提供默认值，调用函数时可不传该默认参数的值
#注意：所有的位置参数必须出现在默认参数前，包括函数定义和调用
def func(a,b=8):
    print(a,b)
# func()         #报错，因为没有给位置参数传值
func(200)      #没有传值会根据默认值来执行代码
func(200,100)   #传了值会根据传入的值来执行代码
#(3)可变参数：传入的值的数量是可以改变的，可以传入多个，也可以不传
def fund(*args):
    print(args)
    print(args[1],args[2])
    print(type(args))   #可变参数是元组类型
fund(1,"你好",[1,2,3])
#(4)关键字参数：
def fune(**kwargs):
    print(kwargs)   #返回字典
fune()      #空字典
#使用给变量赋值的形式传值，采用键=值的形式
fune(name='bingbing',age=18)

#函数嵌套
#(1)嵌套调用：一个函数内调用另外一个函数
def study():
    print("晚上在学习")
def course():
    study()
    print("Python基础")
course()
#(2)嵌套定义：一个函数中定义另一个函数
def learn():
    print("晚上在学习")
    def subject():      #内函数没有被调用
        # learn()         #注意：不能在内函数中调用外函数，会陷入死循环，直至超出递归最大深度
        print("Python基础")
    subject()     #此处可调用内函数，定义和调用是同级的，调用如果在定义里面永远调用不到
# subject()       #内函数可见范围只有外函数，此处报错
learn()

#匿名函数（函数比较简单的情况下使用）
#函数名=lambda 形参:返回值(表达式)
#形参若是必备参数，调用时必须传递相应的值；最后一个形参也可以是默认参数
#调用：结果=函数名(形参)
add=lambda x,y:x+y  #x,y就是匿名函数形参，x+y是返回值表达式
#lambda不需要写return返回值，表达式本身结果就是返回值
print(add(1,3))
fun_1=lambda :"123"
print(fun_1())
add1=lambda x,y=1:x+y
print(add1(1))
fun_2=lambda **kwargs:kwargs
print(fun_2(name='bingbing',age=18))
#lambda结合if判断
comp=lambda a,b:"a比b小" if a<b else "a大于等于b"     #a，b是形参
print(comp(5,8))

#内置函数
import builtins
print(dir(builtins))
#大写字母开头一般是内置常量名，小写字母开头一般是内置函数名

#函数闭包（可以理解成返回值是指向内部函数的指针）
#(1)函数嵌套定义（函数里面再定义函数）
#(2)内层函数使用外层函数的局部变量
#(3)外层函数的返回值是内层函数的函数名
def outer(m):    #外层函数
    print("outer()函数中m的值：",m)
    def inner(n):#内层函数
        print("inner()函数中n的值：",n)
        return n+m
    # 返回inner而不是inner()，是因为inner函数里参数较多或者受到限制时，写法不太规范
    return inner
# print(outer())  #返回的是内层函数的内存地址
#调用方式一
# outer()()
#调用方式二
ot=outer(10)    #调用外函数
print(ot(20))   #调用内函数
print(ot(30))
#总结：使用闭包过程中，一旦外函数被调用一次，返回了内函数的引用；每次调用内函数会开启一个函数，执行后消亡
#但是闭包变量实际上只有一份，每次开启内函数都在使用同一份闭包变量

#应用：装饰器（以函数名为参数的闭包）
#(1)不修改源程序/函数的代码
#(2)不改变函数或程序的调用方法
def test02():
    print("发送信息给冰冰")
def test01(fn):
    print("开始注册")
    print("登录")
    fn()    #调用作为参数传入的参数
test01(test02)
#(3)语法糖
#格式：@装饰器名称
#outer()是装饰器函数
def outer(fn):
    def inner():
        print("登录...")
        #执行被装饰的函数
        fn()
    return inner
#注意：装饰器名称后面不要加()，前者是引用，后者是函数调用
@ outer
#send()是被装饰的函数
def send1():
    print("发送消息：笑死我了")
send1()
#@outer相当于outer(send1)()
@outer
def send2():
    print("发送消息：哈哈哈")
send2()
#(4)被装饰的函数有参数
def outer(fn):
    def inner(name):
        print(f"{name}是inner()函数的参数")
        print("哈哈")
        fn(name)
    return inner
@outer
def func(name):
    print("这是被装饰的函数")
func(name)
#(5)被装饰的函数有可变参数*args,**kwargs
def func(*args, **kwargs):
    print(args)
    print(kwargs)
func(name='bingbing')
#装饰器函数
def outer(fn):
    def inner(*args, **kwargs):
        print("登录...")
        fn(*args, **kwargs)
    return inner
ot=outer(func)
#'susu'以元组的形式传递给*args；name='bingbing'以键=值的形式传递给**kwargs
ot('susu','haha',name='bingbing',age=18)
#(6)多个装饰器
def deco1(fn):
    def inner():
        return "哈哈哈"+fn()+"呵呵呵"
    return inner
def deco2(fn):
    def inner():
        return "Nice"+fn()+"非常优秀"
    return inner
#多个装饰器的装饰过程：由内向外，离得近的先装饰
@deco1
@deco2
def test1():
    return "晚上在学习python基础"
# print(test1())  #输出：哈哈哈Nice晚上在学习python基础非常优秀呵呵呵
#相当于以下语句
# ot1=deco2(test1)    #ot1=deco2的inner指针
# ot2=deco1(ot1)      #ot2=deco1的inner指针
# ot2()

#函数引用
def test1():
    print("这是test1函数")
test1()
print(test1)    #test1()函数的内存地址（引用）
te=test1
te()        #通过函数引用调用函数

#(1)abs()：返回绝对值
print(abs(-10));print(abs(10))      #都是返回10

#(2)sum()：求和
# print(sum(123))     #报错，sum()参数是可迭代对象
# print(sum('abcd'))  #报错，字符串类型不能相加
# print(sum({'name':'bingbing','age':18}))    #报错，不支持字典
print(sum([1,2,3]))     #元组tuple (...)、列表list [...]、集合set {...}均可行
print(sum({1.5,2,3}))   #只要有一个运算对象是浮点数，则结果必定为浮点数

#(3)min()：求最小值；max()：求最大值
print(max(1,2,3))
print(min([4,2,8]))
print(min({4,2,8}))
print(max(-8,5,key=abs))    #参数传入求绝对值函数，则数值先会求绝对值，再取其中绝对值最大者

#(4)zip()：将可迭代对象作为参数，将对象中对应的元素打包成一个个对应的元组
li=[1,2,3]
li2=['a','b','c']
# li2=['a','b']           #如果个数不对应，则只配对个数一致的部分
print(zip(li,li2))      #输出<zip object at 64位虚拟线性地址>
#方式一：for循环打印
for i in zip(li,li2):
    print(i,type(i))
#方式二：转换成列表打印
print(list(zip(li,li2)))

#(5)map()：可对可迭代对象中的每一个元素进行映射，分别去执行
li=[1,2,3]
def funa(x):
    return x*5
mp=map(funa,li)     #只需写函数名，无需写括号()
print(mp)               #输出<map object at 64位虚拟线性地址>
#方式一：for循环打印
for i in mp:
    print(i,type(i))
#方式二：转换成列表打印
print(list(mp))

#(6)reduce()：先把对象中的两个元素取出，计算出一个值然后保存，接下来把计算值跟第三个元素进行计算
from functools import reduce
# reduce(function,sequence)     function：必须是有两个参数的函数；sequence：可迭代对象序列
li2=[1,2,3]
def add(x,y):
    return x+y
res=reduce(add,[1,2,3])
print(res)

#拆包：对于函数中多个返回数据，去掉元组、列表、集合、字典，获取里面元素的过程
tua=(1,2,3,4)
#方法一：元组内有多少个元素，就定义相对应个数的变量接收
a,b,c,d=tua
print(a,b,c,d)
#方法二：使用可变参数（*变量名）接收多个元素（一般在函数定义使用）
a,*b=tua
print(a,*b)
print(a,b)
def funa(a,b,*args):
    print(a,b)
    print(args,type(args))
funa(1,2,3,4,5,6,7)
arg=(1,2,3,4,5,6,7)
funa(*arg)

#25.作用域
a=100       #全局变量，在全体函数以外定义的变量
def test1():
    print("这是test1中全局变量a的值：",a)
def test2():
    global a  # global关键字：只声明全局变量（在函数顶部，所有全局变量使用前），变量赋值定义位于函数外部
    a=300     #相当于修改了全局变量a
    print("这是test2中全局变量a的值：",a)
print("调用函数前a的值：",a)
test1()
test2()
print("调用函数后a的值：",a)

def testa():
    arga=1
    print("arga：",arga)
    def testb():
        arga=2      #局部变量，在函数内部定义的变量，只能在该函数内部使用
        print("arga：",arga)
    testb()
testa()

def study():
    global name     #在局部作用域中声明全局变量，之后在函数外也可使用
    name = "Python基础"
    print(f"我们在学习{name}")
study()
print(name)
def work():
    print(name)
work()

#nonlocal：用来声明外层的局部变量，只能在嵌套函数中使用；外部函数先进行声明，内部函数进行nonlocal声明
a=10
def outer():
    a=5
    def inner1():
        # nonlocal声明的变量a，会导致外层函数同名变量a的值改变，但只会影响相邻的上一级
        # nonlocal a
        a=20
        def inner2():
            nonlocal a
            a=30
            print("inner2函数中a的值：", a)
        inner2()
        print("inner1函数中a的值：",a)
    inner1()
    print("outer函数中a的值：",a)
outer()

#26.异常：程序执行过程中出现的非正常流程的现象
#(1)异常处理
#方式一：根据控制台的错误提示找到出错点并分析改正
#Traceback：异常的追踪信息，可以追溯到程序异常的具体位置
#XXXError：异常类型，后面会包含异常具体信息

#方式二：对异常进行捕获处理
#注意：可以单独使用try...finally...；也可以配合except和else使用
#try：可能引发异常的代码块
try:
    print("abc")    #只有try内的代码发生异常了，才会进入except代码块
#except：发生异常时才会执行的代码块
except (TypeError,NameError):   #当要捕获多个异常时，可以把要捕获的异常类型名放到except后，并以元组的形式编写
    print("该行代码有错")
#else：没有发生异常才会执行的代码块
else:
    print("这里是else代码")
#finally：无论异常有没有发生，都会执行的代码块
finally:
    print("不管怎样finally里面的内容都会被执行")

def login():
    pwd=input("请输入你的密码：")
    if len(pwd) >= 6:
        return "密码输入成功"
    raise Exception("长度不足六位，密码输入失败")
# print(login())      #由系统自动捕获异常，控制台出现红色报错，出错了不能继续往下执行
try:        #自己实现异常捕获&异常处理，控制台不会出现红色报错，还可以继续往下执行
    print(login())  #一般try下面只放一行尝试代码
except Exception as e:  #万能的异常类（所有异常的父类），可以接受所有的异常类型
    print(e)    #as相当于取别名，Exception类的变量名是e，as e把异常信息保存到变量e中

#27.模块
#(1)内置模块，如：random、time、os、login，直接导入即可使用
#(2)第三方模块（第三方库），下载方式：cmd窗口输入pip install 模块名
#(3)自定义模块，自行在项目中定义的模块；命名遵循标识符规定以及变量命名规范，并且不要与内置模块起冲突

#导入方式
#<1>import 模块名；调用功能：模块名.函数名
#可以一个import语句导入多个模块，但最好是一个import单独导入一个模块
import test
print("test模块中的name变量：",test.test_name)
test.funa()
#<2>从模块中导入指定部分：from ... import ...
from test import funa,test_name
funa()      #不用写模块名了
print(test_name)    #没有导入test_name变量名，会报错
#<3>从模块中导入全部：from ... import *，不建议过多使用，有时候命名冲突会造成一些错误
#直接import要模块名.函数，from 模块名 import *可以直接使用函数
from test import *
from test1 import *     #后导入的会覆盖前面导入模块内的同名变量、函数
funa()
funb()
print("test模块中的name变量：",test_name)

#(1)as为模块起别名
#import 模块名 as 别名
import test as te
te.funa()
#(2)as给功能起别名
#from 模块名 import 功能 as 别名，可以为多个功能取别名
from test import funa as a,test_name,funb as b

#内置全局变量__name__：用来控制py文件在不同的应用场景执行不同的逻辑
#if __name__=="__main__":
#(1)文件在当前程序执行（即自己执行自己）__name__=="__main__"
#(2)文件当作模块被其他文件导入__name__=="模块名"
import test
test.test()

#28.包：项目结构中的文件夹/目录；将有联系的模块放到同一个文件夹下，并且文件夹中创建一个名为__init__.py的文件
#作用：可有效避免模块名称冲突问题，让结构更清晰
#与普通文件夹的区别：包是含有__init__.py的文件夹
import pack_01      #自动执行了__init.py__内的代码
#(1)导包方式一见__init__.py
#(2)导包方式二
from pack_01 import *
register.reg()

#29.递归：一个函数内部调用它本身
#(1)条件：
#<1>递归出口：必须有一个明确的结束条件
#<2>每进行更深一层的递归，问题规模相比上次递归都有所减少
#<3>相邻两次重复之间有紧密的联系
def add(n):     #要累加到第n项
    if n==0:
        return 0
    else:
        return n+add(n-1)
print(add(10))