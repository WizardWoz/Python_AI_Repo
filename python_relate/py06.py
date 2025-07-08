# 1.多线程：同时运行多个线程
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
def wdata(q1):
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
