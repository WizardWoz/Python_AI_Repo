# 1.多线程：同时运行多个线程（适合IO密集型操作：文件操作、爬虫）
# 进程：操作系统进行资源分配的基本单位，每打开一个程序至少有一个进程
# 线程：CPU调度的基本单位，每个进程至少有一个线程，该线程即为主线程；一个进程默认拥有一个线程，且可以创建多个线程，线程是依附于进程的
# 需要先导入线程模块import threading
import os
import threading,time

def sing(name):
    print(f'sing子进程编号：{os.getpid()}，父进程id：{os.getppid()}')     # 获取当前进程编号，当前父进程的编号
    print(f"{name}在唱歌")
    time.sleep(2)   # 延迟2秒
    print(f"{name}唱完歌了")
def dance(name):
    print(f'dance子进程编号：{os.getpid()}，父进程id：{os.getppid()}')     # 获取当前进程编号，当前父进程的编号
    print(f"{name}在跳舞")
    time.sleep(2)   # 延迟2秒
    print(f"{name}跳完舞了")

# 2.多线程特点：线程间执行是无序的，线程间共享资源，并引发资源竞争问题
# 线程执行是根据CPU调度决定的
def task():
    time.sleep(1)
    print("当前线程是：",threading.current_thread().name)   #显示当前线程对象名

# 3.线程之间共享资源；进程间不共享全局变量
li=['张三','李四','王五','赵六']   # 定义全局变量li
# 为li写入数据的方法
def wdata():
    for i in range(5):
        li.append(i)
        time.sleep(1)
    print("写入的数据是：",li)
# 读取li中数据的方法
def rdata():
    print("读取的数据是：",li)

# 4.线程之间资源竞争：可共享资源（全局变量...）
# 5.线程同步：主线程和创建的子线程之间，各自执行完自己的代码直至结束
# (1)线程等待：join()阻塞线程
# (2)互斥锁：对共享数据进行锁定，保证多个线程访问共享数据不会出现数据错误；保证同一时刻只能有一个线程进行操作
# acquire()：上锁；release()：释放锁；两方法必须成对出现，否则会形成死锁（一直等待对方释放锁的情景）
# 互斥锁的缺点：会影响代码的执行效率
# 死锁会造成应用程序停止响应，不能处理其它任务
# 使用互斥锁前需导入模块from threading import Lock
from threading import Lock,Thread
# (1)创建全局互斥锁
lock=Lock()
a=0
b=1000000
def add1():
    # (2)使用共享数据前必须先上锁
    lock.acquire()
    for i in range(b):
        # 可以读取全局变量，但是修改全局变量必须先用global声明
        global a    # 声明a是在函数外定义的局部变量
        a+=1
    print("第一次累加：",a)
    # (3)共享数据使用完成必须释放锁
    lock.release()
def add2():
    # (2)使用共享数据前必须先上锁
    lock.acquire()
    for i in range(b):
        # 可以读取全局变量，但是修改全局变量必须先用global声明
        global a    # 声明a是在函数外定义的局部变量
        a+=1
    print("第二次累加：",a)
    # (3)共享数据使用完成必须释放锁
    lock.release()

# 6.进程：操作系统进行资源分配的基本单位，一个正在运行的程序/软件就是一个进程；多进程也可实现多任务
# 多进程适合CPU密集型操作（例：科学计算、视频高清解码）
# 进程的状态：
# (1)就绪状态：运行条件均满足，等待被CPU调度执行
# (2)运行状态：CPU正在执行
# (3)等待（阻塞）状态：等待某些条件满足后（例：请求临界资源）
print("我是bingbing")   # 程序开始，处于执行状态
sex=input("输入性别：")     # 光标闪烁等待用户输入，处于等待状态
print(sex)      # 执行状态
time.sleep(1)   # 等待状态

# 进程语法结构：multiprocessing模块，是一个跨平台的多进程模块，提供了Process类代表进程对象
# multiprocessing的Queue是进程安全队列，支持跨进程通信
from multiprocessing import Process
from multiprocessing import Queue

# Process类参数：
# (1)target：执行的目标任务名，即子进程要执行的任务
# (2)args：以元组的形式传参
# (3)kwargs：以字典形式传参
# Process类方法：
# (1)start()：开启子进程
# (2)is_alive()：判断子进程是否存活，若存活则返回True，否则返回False
# (3)join()：主进程等待子进程执行结束
# Process常用属性：
# (1)name：当前进程的别名，默认Process-N
# (2)pid：当前进程的进程编号

# 7.进程间通信（利用线程安全队列Queue，仅适用于单进程的多线程）；需导入模块from queue import Queue（严格区分大小写）
# q.put()：放入单条消息
# q.get()：获取单条消息，然后将其从队列中移除
# q.empty()：判断队列是否为空
# q.qsize()：返回队列包含的消息数量
# q.full()：判断消息队列是否已满
from queue import Queue
q=Queue(3)      # 队列q最多只能接收3条消息，为空或者负值则代表没有上限，直到内存的上限
q.put('Message1')
q.put('Message2')
q.put('Message3')
# q.put('Message4')   # 不允许再插入消息（主进程会被阻塞）
print(q.qsize())
print(q.full())
print(q.get())
print(q.get())
print(q.empty())
print(q.get())
print(q.empty())
print(q.qsize())

# 8.协程（微线程/纤程）：Python中实现多任务的方式，比线程更小、占用资源更少；自带CPU上下文，协程切换过程中要保存/恢复
# 是在单线程下的开发；线程&进程的操作是由程序触发系统接口，最后的执行者是系统；协程的操作则是由程序员触发
# 应用场景：一个线程内部IO操作较多；适合高并发处理
# 以下是协程的简单实现
def task1():
    while True:
        yield 'a'
        time.sleep(1)
def task2():
    while True:
        yield 'b'
        time.sleep(1)

# 9.greenlet模块：为更好使用协程完成多任务。Python中的greenlet模块对其封装，使切换任务更加简单
# 由C语言实现的协程模块；通过设置switch()来实现任意函数之间的切换
# 注意：greenlet属于手动切换，当遇到IO操作程序会阻塞，而不能进行自动切换
from greenlet import greenlet
def sing1():
    print("sing1在唱歌")
    g2.switch()
    print("sing1唱完歌了")
def dance1():
    print("dance1在跳舞")
    print("dance1跳完舞了")
    g1.switch()

# 10.gevent：当遇到IO操作程序会自动切换，属于主动切换，相较于greenlet更好；但是底层实现仍基于greenlet
import gevent       # 导入gevent模块
# gevent.spawn(函数名)    # 创建协程对象
# gevent.sleep()      # 睡眠操作
# gevent.join()：     # 阻塞，等待某个协程执行结束
# gevent.joinall()：  # 等待所有协程对象都执行结束再退出，参数是一个协程对象列表
def sing2():
    print("sing2在唱歌")
    gevent.sleep(3)
    print("sing2唱完歌了")
def dance2():
    print("dance2在跳舞")
    gevent.sleep(2)
    print("dance2跳完舞了")

def sing3(name):
    for i in range(3):
        gevent.sleep(1)     # 注意，不能使用time.sleep()
        print(f"{name}在唱歌")
    
# 11.monkey补丁：拥有在模块运行时替换的功能
from gevent import monkey
# monkey.patch_all()必须放在被打补丁的函数前
monkey.patch_all()      # 将用到的time.sleep(1)替换为gevent.sleep(1)
def sing4(name):
    for i in range(3):
        time.sleep(1)     # 注意，不能使用time.sleep()
        print(f"{name}在唱歌")

# Thread线程类参数：
# (1)target：执行的任务名
# (2)args：以元组的形式给任务传参（即方法参数列表）
# (3)kwargs：以字典的形式给任务传参（即方法参数列表）
# 代码主程序入口：__name__=="__main__"；
# (1)防止别人导入文件的时候执行main里面的方法
# (2)防止Windows系统递归创建子进程
if __name__=="__main__":
    # 创建子线程
    t1=threading.Thread(target=sing,args=('bingbing',))     # 元组只有一个参数时，后面要用 ,
    print(t1)
    t2=threading.Thread(target=dance,args=('bingbing',))
    # 守护线程，必须放在start()方法前，主线程执行结束，子线程也会跟着结束
    t1.daemon=True
    t2.setDaemon(True)      # Python弃用的方法会在终端输出DeprecationWarning弃用警告
    # 开启子线程
    t1.start()
    t2.start()
    # 子线程使用join()阻塞主线程，等待子线程结束后，主线程才结束；必须放在start()之后
    # 实际作用与守护进程类似
    t1.join()
    t2.join()
    # 获取线程名字
    print(t1.getName())
    print(t2.name)
    # 更改线程名字
    t1.setName('子线程1')
    t2.name='子线程2'
    print(t1.getName())
    print(t2.name)
    print("完美谢幕")
    
    for i in range(5):
        # 每循环一次就创建一个子线程
        t=threading.Thread(target=task)
        # 启动子线程
        t.start()

    wt=threading.Thread(target=wdata)
    rt=threading.Thread(target=rdata)
    wt.start()
    wt.join()   # 等待wt线程执行结束后，代码才往下执行
    rt.start()

    a1=threading.Thread(target=add1)
    a2=threading.Thread(target=add2)
    a1.start()
    # 线程同步方法(1)：join()
    # a1.join()   # 等待a1线程执行结束后，代码才往下执行
    # 线程同步方法(2)：互斥锁
    a2.start()

    # 创建子进程
    # 修改子进程名的第一种方式：创建时修改name属性
    p1=Process(target=sing,args=('bingbing',),name='子进程1')
    p2=Process(target=dance,args=('bingbing',),name='子进程2')
    # 访问name属性
    print('p1:',p1.name)
    print('p2:',p2.name)
    # 开启子进程
    p1.start()
    p1.join()       # 主进程处于等待状态，p1是运行状态
    p2.start()
    # 修改子进程名的第二种方式：p1.name='新名字'3
    p1.name='p1'
    p2.name='p2'
    # 访问name属性
    print('p1:',p1.name)
    print('p2:',p2.name)
    # 查看子进程的进程编号
    print("p1.pid：",p1.pid)
    print("p2.pid：",p2.pid)
    print(f"主进程pid：{os.getpid()}；主进程的父进程pid：{os.getppid()}")
    # 查看各子进程的存活状态
    print("p1存活状态：",p1.is_alive())     # 因为之前p1.join()加入运行，并运行完毕，所以存活状态是False
    print("p2存活状态：",p2.is_alive())     # 因为p2一直没有join()加入运行，所以存活状态是True

    # 创建子进程，测试子进程与全局变量的关系
    p3=Process(target=wdata)
    p4=Process(target=rdata)
    # 开启子进程
    p3.start()      # 写进程已经将新数据写入共享数组了
    p4.start()      # 可读进程的读取共享数组一直是空的

    # 创建协程方法一：手动实现
    # t1=task1()
    # t2=task2()
    # while True:
    #     print(next(t1))
    #     print(next(t2))
    # 创建协程方法二：greenlet模块
    g1=greenlet(sing1)
    g2=greenlet(dance1)
    g1.switch()     # 切换到g1中去运行
    g2.switch()     # 切换到g2中去运行
    # 创建协程方法三：gevent模块
    g3=gevent.spawn(sing2)
    g4=gevent.spawn(dance2)
    g3.join()       # 主线程要先等待g3协程对象执行结束后才结束
    g4.join()       # 主线程要先等待g4协程对象执行结束后才结束
    gevent.joinall([    # 主线程等待所有协程对象执行完才退出
        gevent.spawn(sing3,'bingbing'),
        gevent.spawn(sing3,'冰冰')
    ])
    gevent.joinall([    # 主线程等待所有协程对象执行完才退出
        gevent.spawn(sing4,'我'),
        gevent.spawn(sing4,'你')
    ])