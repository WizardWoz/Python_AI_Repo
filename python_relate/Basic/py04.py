#1.文件：长期存储在外存设备上的一段数据
#(1)文件操作
#<1>open()：打开文件（相对路径/绝对路径），创建一个file对象，默认以只读模式'r'打开
f=open('test.txt')
print(f.name)
print(f.mode)
print(f.closed)
f.close()
#<2>read(n)：n表示从文件中读取的数据的长度，没有传n值/n取负值默认一次性读取文件的所有内容
f=open('test.txt')
# print(f.read())
# print(f.read(5))
f.close()
#<3>readline()：一次读取一行内容，方法执行完会把文件指针移到下一行，准备再次读取
f=open('test.txt',encoding='utf-8')
# print(f.readline())
# print(f.readline())
while True:
    text=f.readline()
    #读取不到内容则退出循环
    if not text:
        break
f.close()
#<4>readlines()：按行将文件一次性全部读取，返回的是一个列表，每一行数据就是列表中的一个元素
f=open('test.txt',encoding='utf-8')
text=f.readlines()
for i in text:
    print(i)
print(text)     #返回列表
f.close()
#<3>write()：将指定内容写入文件
#'r'：只读模式（默认模式），文件必须存在，不存在就会报错
#'w'：只写模式，若文件不存在则先创建；文件存在就会先清空文件内容，再写入新内容
#'+'：表示可以同时读写某个文件，但会影响文件读写效率；实际开发更多是使用只读、只写模式
#'r+'：可读写文件，文件不存在就会报错
#'w+'：先写再读，文件存在就重新编辑文件，不存在就创建文件
#'a'：追加模式，不存在则创建文件再写入，若存在就在原有内容基础上追加新内容
f=open('test.txt',"w")
f.write('...')
f.close()
f=open('test1.txt','w+')
f.write('bingbing')     #写完后，文件指针在字符串bingbing末尾
print(f.read())    #不加'+'会报错
f.close()
f=open('test.txt','a+')
print(f.read())    #不加'+'会报错
f.write("\ntest is being written.")
print(f.read())
f.close()
#<4>文件指针：标记从哪个位置开始读取数据
#<5>文件定位操作：tell()和seek()
#tell()：显示文件内当前位置（即文件指针当前位置）
#seek(offset,whence)：移动文件读取指针到指定位置
#cookie：偏移量，表示移动字节数
#whence：起始位置，表示移动字节参考位置，默认是0，0代表文件开头作为参考位置，1代表当前位置作为参考位置，2代表文件结尾作为参考位置
#seek(0,0)会将文件指针移到文件开头
f=open('test.txt','w+')
f.write("Hello Python!")
print("当前文件指针所在位置：",f.tell())   #文件内容长度：13
f.seek(0,0)
print("移动后文件指针所在位置：",f.tell())
print(f.read())
f.close()
#<6>with open
#作用：代码执行完，系统会自动调用f.close()，可以省略文件关闭步骤
with open('test.txt','r+',encoding='utf-8') as f:
    print(f.read())
    f.seek(0,0)
    f.write("emmmmm......")
    f.seek(0,0)
    print(f.read())

#<7>案例：读取图片
"""
1.读取图片：二进制文件读入操作
2.写入图片：二进制文件写入操作
"""
# with open('F:\\pic1.jpg','rb') as f:
#     img=f.read()
#     print(img)
# with open('F:\\pic2.jpg','wb') as f:
#     f.write(img)
#(2)文件属性
#<1>文件名.name：要打开文件的文件名，可以包含文件的绝对路径
#<2>文件名.mode：返回文件的访问模式
#<3>文件名.closed：检测文件是否关闭，关闭就返回True

#2.编码格式，open()的encoding参数默认值与平台有关，Windows上的默认字符编码是GBK，实际UTF-8更多被使用
# with open('test.txt','w',encoding='UTF-8') as f:    #写入中文时记得encoding='UTF-8'
#     f.write("早上好！")
#     f.close()
with open('test.txt','r') as f:
    print(f.read())

#2.文件/目录操作相关模块
import os
#(1)文件重命名 os.rename(旧名字,新名字)
# os.rename('test.txt','testpy.txt')
#(2)删除文件 os.remove(路径名)
# os.remove('test.txt')
#(3)创建文件夹 os.mkdir(路径名)
os.mkdir('hello')
#(4)删除文件夹 os.rmdir(路径名)
os.rmdir('hello')
#(5)获取当前目录 os.getcwd()
print(os.getcwd())
#(6)获取目录列表 os.listdir()
print(os.listdir())