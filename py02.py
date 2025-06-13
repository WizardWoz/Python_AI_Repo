#Python面向对象基础
class MyClass:  #类名遵循大驼峰命名法（见名知义），符合标识符规定
    """这是一个示例类，为后文的各种类或实例的特性服务"""
    height=800  #类属性：类所拥有的属性，既可以使用类名，也可以使用self调用；类似C++类的静态成员变量
    __hide='隐藏属性'
    _private='私有属性'
    @staticmethod   #静态方法既可以用类名访问，也可以用对象名访问
    def show():
        """定义静态方法"""
        print("staticmethod静态方法")
        print(f"我的高度为：{MyClass.height}")    #可以访问类属性，但是没有意义
        # self.width=100  #不能访问对象的实例成员
    @classmethod    #类方法，方法内部可以访问类属性，或者调用其它类方法
    def ClassMethod(cls):   #参数列表第一个参数则是类本身（名字不一定是cls）
        """定义类方法"""
        print(cls)
        print("classmethod类方法")
        # self.width=100  #不能访问对象的实例成员
        print(f"通过类名访问类属性：{MyClass.height}")
    def __new__(cls, *args, **kwargs):  #由object基类提供的内置静态方法
        # __new__先于__init__执行，必须要返回一个实例对象，才会执行__init__，所以这里要用super()
        res=super().__new__(cls)    #对父类方法进行扩展，__new__()是静态方法，形参有cls实参则必须传cls
        print("这是__new__()方法")
        return res  #一定要返回super().__new__(cls)的对象引用
    def __init__(self,name,age):     #初始化方法,类似C++的默认构造函数
        print("这是__init__()方法")
        self.name='洗衣机'
        self.age=10
        self.width=200      #实例属性，对象私有
    def __str__(self):  #__str__()没有返回或者返回的不是字符串则报错
        return "这里是__str__()的返回值"
        # return 1
        # pass
    def __call__(self):
        print("这是__call__()方法")
    def __hidefun(self):        #隐藏方法，可以通过公有方法调用
        """定义隐藏方法"""
        print("这是隐藏方法__hidefun()")
        # self.name='123'     #可以成功修改公有成员
    def wash(self): #self参数名并不是硬性规定，可以是其他的名称
        """定义公有实例方法"""
        print("我会洗衣服")
        print("wash()成员方法里的self地址：",self)
    def introduce(self):        #公有实例方法
        #如果使用类名调用类属性，则用对象无法成功修改该属性
        print(f"{self.name}的高度：{MyClass.height}，年龄：{self.age}，属性：{MyClass.__hide}")
        # MyClass.__hidefun(self) #通过introduce()公有方法调用__hidefun()隐藏方法
    def __del__(self):      #析构函数，程序结束/删除某个对象时都会调用
        print("这是__del__()方法")

#1.查看类属性：类名.属性名
print(MyClass.height)

#2.新增类属性
MyClass.width=450
print(MyClass.width)

#3.创建对象（实例化对象）：对象名=类名()
wa=MyClass('123',2)
print(wa)   #输出对象在内存中的地址；<__main__.MyClass object at 64位虚拟地址>
wa2=MyClass('456',1)
print(wa2)  #与wa的内存地址不一样，说明是不同对象，可以实例化多个对象

#4.实例方法、属性：由对象调用，至少有一个self参数，执行实例方法时将调用该方法的对象赋值给self
#方法内部可以访问实例属性，也可通过类名.类属性名访问类属性
wa3=MyClass('789',3)
print("wa对象的地址：",wa)    #class类中self的地址和该类实例化对象的地址相同
wa3.wash()
#类属性是公共的，有类名访问，实例属性是私有的，由对象名访问，不同对象可以有自己的实例属性
wa3.name='洗衣机'   #实例属性，只能使用对象名调用，无法使用类名调用；类似C++类的非静态成员变量
wa3.height=600     #通过对象名、类名均可访问&修改类属性
wa3.introduce()
#每实例化一次对象就需要添加相对应的方法和属性，效率不高

#5.构造函数__init__()：通常用来做属性初始化和赋值操作
#如果没有显式定义__init__()，则每次实例化对象调用MyClass()就不需要传参了
te=MyClass('bingbing',18)
te.introduce()

#6.析构函数__del__()：对象被垃圾回收时调用的一个方法，意味着一个对象不能再被调用并回收内存
#正常运行时不会调用__del__()，对象执行结束后系统会自动调用__del__()
#删除对象的时候，解释器会默认调用__del__()
print("这是最后一句代码")
del te  #删除te这个对象，会立即执行对象本身的__del__()

#7.封装
#面向对象的三大特性：封装、继承、多态
#封装：隐藏对象中一些不希望被外部访问到的属性和方法
#(1)隐藏成员（私有权限）：__属性名/方法名；只允许在类内部使用，无法通过对象访问，相当于C++类的private
#一般是Python中的魔法属性/方法，有特殊含义和功能，不要轻易自行定义
te=MyClass('bingbing',18)
# print(te.__hide)    #通过对象访问不到
#访问隐藏属性的一些方法
#<1>隐藏属性实际上是将名字修改为：_类名__属性名，不推荐使用了解即可
print(te._MyClass__hide)
te._MyClass__hide='访问隐藏属性方法一成功'
print(te._MyClass__hide)
#<2>使用类方法访问
te.introduce()

#(2)私有成员：_属性名/方法名；定义在类中则外部可以使用，子类也可以继承；但是在另一个.py文件
#通过from xxx import *导入时却无法导入，相当于C++类的protect；一般是为了避免与Python的关键字冲突而采用
te=MyClass('bingbing',18)
print("MyClass()类的私有成员private：",te._private)
# te.__play()
te.introduce()

#8.继承：类和类之间转变为父子关系，子类默认继承父类的属性和方法
#(1)单继承
class MySonClass(MyClass):
    def warm(self):
        print("可以烘干")
#(2)多重继承：继承的传递，子类默认继承所有层次父类的属性和方法
class MySonClass2(MySonClass):
    pass    #占位符，类没有内容时会自动跳过，也可以写None；空类不写pass/None会报缩进错误
    # None    #同样是占位符
msc=MySonClass2('123',12)
msc.warm()
#(3)父类方法重写
class SonClass(MyClass):
    def introduce(self):
        print("SonClass子类覆盖了父类MyClass的introduce()方法")
sc=SonClass('123',10)
sc.introduce()
#(4)父类方法扩展：继承父类方法，子类也可增加自己的功能
class SonClass2(MyClass):
    def introduce(self):
        MyClass.introduce(self)     #<1>父类名.方法名(self)
        super().introduce()         #<2>（推荐）super().方法名()；super()使用super类创建出来的对象
        super(SonClass2, self).introduce()  #<3>super(子类名,self).方法名()
        print("SonClass2子类覆盖了父类MyClass的introduce()方法")
sc=SonClass2('123',10)
sc.introduce()

#9.新式类：继承了object类（孙子辈）或者object类的子类都是新式类
#经典类（仅限Python 2；因为Python 3一个类默认继承object类，不用显式写出）：不由任意内置类型派生出的类
class Animal:
    def walk(self):
        print("我会走路")
#派生类：有不同于父类的属性和方法
class Dog(Animal):
    name='富贵'
    def bite(self):
        print("我会咬人")
#object类：Python为所有类提供的父类（顶级），提供了一些内置的属性和方法，可通过dir()查看
print(dir(object))

#10.多继承
class Father(object):
    def money(self):
        print("爸爸的100万需要被继承")
class Mother(object):
    def money(self):
        print("妈妈的120万需要被继承")
    def appearance(self):
        print("绝世容颜需要被继承")
#(1)不同的父类存在同名方法，类似C++的菱形继承；需要尽量避免该情况
#会依据就近原则调用：调用括号内父类列表最前面的父类属性/方法，object类总是在最后
#方法的搜索顺序：Python中内置的属性__mro__可以查看方法搜索顺序（自左向右）
#如果在当前类中找到同名方法，则直接执行不用搜索__mro__
class Son(Father, Mother):
    pass
son=Son()
son.money()
son.appearance()
print(Son.__mro__)
#(2)弊端：容易引发冲突，增加代码设计的复杂度

#11.多态：同一种行为具有不同的表现形式
#前提：基于继承关系，子类重写父类方法
#特点：
#(1)不关注对象的类型，只关注对象的实例方法是否重名
#(2)增加代码的外部调用灵活度，代码更加通用、兼容性更强
#(3)不同的子类对象调用相同的父类方法，会产生不同的执行结果
print(10+10)        #算术运算符：实现两个整型数相加
print('10'+'10')    #字符串拼接：实现字符串之间的拼接操作
class Animal(object):
    """父类：动物类"""
    def shout(self):
        print("动物会叫")
class Cat(Animal):
    """子类一：猫类"""
    def shout(self):
        print("小猫喵喵喵")
class Dog(Animal):
    """子类二：狗类"""
    def shout(self):
        print("小狗汪汪汪")
cat=Cat()
cat.shout()
dog = Dog()
dog.shout()
#定义一个统一的接口，一个接口多种实现
def test(obj):
    obj.shout()
animal = Animal()
test(dog)
test(cat)

#12.静态方法：使用@staticmethod进行修饰，没有self、cls等参数的限制
#(1)与类、对象无关，可以被转换成函数使用
#(2)取消不必要的参数传递，有利于减少不必要的内存占用和性能消耗
#(3)可以访问类属性：类名.类属性名；不能访问实例属性
mc=MyClass('456',1)
mc.show()
MyClass.show()

#13.类方法：使用@classmethod进行修饰，第一个参数必须是类对象（一般是cls），一般配合类属性使用
#(1)方法内部一般只需要访问类属性，不能访问实例属性
print(MyClass)      #cls参数即为当前类
MyClass.ClassMethod()

#14.魔术属性/方法
#(1)__new__()：由object基类提供的内置静态方法，不能被重写，不然会导致创建对象错误
#<1>在内存中为对象分配空间
#<2>返回对象的引用，然后对象才能调用__init__()

#(2)__init__()：实例级别的方法，初始化对象，定义实例属性

#(3)__doc__：类或方法的描述信息，只能使用多行注释""""""
print(MyClass.__doc__)
print(MyClass.ClassMethod.__doc__)
print(MyClass.show.__doc__)
print(MyClass.wash.__doc__)

#(4)__module__：表示当前操作对象所在模块；__class__：表示当前操作对象所在类
import test2
b=test2.B()
print(b.__module__)
print(b.__class__)

#(5)__str__()：对象的描述信息，打印对象时默认输出该方法的返回值，也就是打印方法中返回的数据
#该方法必须返回一个字符串
mc=MyClass('456',1)
print(mc)

#(6)__call__()：使一个实例对象成为一个可调用对象，就像函数那样可调用
#可调用对象：（内置）函数和类都是可调用对象，凡是可以把一对()应用到某个对象身上的均可称为可调用对象
#callable()：判断一个对象是否是可调用对象
print(callable(MyClass))
print(callable(MyClass.ClassMethod))
mc=MyClass('456',1)
print(callable(mc))     #MyClass类中重写__call__()方法后返回True
mc()    #调用一个可调用的实例对象，其实就是在调用它的__call__()方法