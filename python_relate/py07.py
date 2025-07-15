# 1.正则表达式：记录文本规则的代码，需要导入re模块
import re
# 字符串处理工具
# 特点：语法较复杂，可读性较差；通用性强，其他语言代码也使用这套规则
# (1)re.match(pattern,string,flags)：匹配出以xxx为开头的字符串；如果起始位置没有匹配成功，则返回None
# 参数：pattern匹配的正则表达式；string要匹配的字符串；flags：标志位，是否区分大小写、多行匹配等功能
res=re.match("冰",'冰冰永远18')     # 源字符串中包含多个相同的正则表达式，返回最开始出现的
print(res)
# (2)re.group()：如果上一步数据匹配成功，使用group()提取数据
print(res.group())
# 注意：match是从开始位置匹配，匹配不到就没有，且匹配的是表达式整理

# 2.匹配单个字符
# (1) . 匹配任意一个字符（除\n之外）    ---常用
res=re.match('.','hello')   # 匹配到首字符
print(res.group())
# (2) [] 匹配在[]中列举的字符   ---常用
res=re.match('[he]','hello')    # 匹配h或e开头的单个字符
print(res.group())
res=re.match('[he].','hello')    # 匹配h或e开头的单个字符，且后一个字符为任意字符的字符串
print(res.group())
# 匹配0-9的第一种写法
res=re.match('[0123456789]','978')
print(res.group())
# 匹配0-9的第二种写法
res=re.match('[0-9]','542')
print(res.group())
# 匹配所有大、小写英文字母
res=re.match('[a-zA-Z]','Hello')
print(res.group())
# (3) \d 匹配数字0-9    ---常用
res=re.match('\d\d','09Hello')
print(res.group())
# (4) \D 匹配非数字     ---常用
res=re.match('\D','，Hello')
print(res.group())
# (5) \w 匹配单词字符，即a-z，A-Z，0-9，_，汉字		---常用
res=re.match('\w','我爱Hello')
print(res.group())
res=re.match('\w','_我爱Hello')
print(res.group())
# (6) \W 匹配非单词字符
res=re.match('\W','#我爱Hello')
print(res.group())
# (7) \s 匹配空白，即空格和Tab
res=re.match('\s.',' ，Hello')
print(res.group())
res=re.match('\s.','	Hello')		# 需要设置代码编辑器使用制表符缩进
print(res.group())
# (8) \S 匹配非空白
res=re.match('\S','，Hello')
print(res.group())

# 3.匹配多个字符
# (1) * 匹配前一个字符出现0次或者无限次，即可有可无		---常用
res=re.match('\w*',"bingbing")
print(res.group())
res=re.match('\d*',"bingbing")		# 没有输出
print(res.group())
# (2) + 匹配前一个字符出现1次或者无限次，即至少一次		---常用
res=re.match('\d+',"1我爱你")
print(res.group())
res=re.match('.+',"~`!@#$%^&*()_+-=1我？")
print(res.group())
# (3) ? 匹配前一个字符出现0次或者1次	---常用
res=re.match('\d?',"~`!@#$%^&*()_+-=1我？")		# 没有输出
print(res.group())
res=re.match('\d?',"321我爱你")
print(res.group())
# (4) {m} 匹配前一个字符出现m次
# res=re.match('\d{3}',"12python")	# 报错，需要匹配3个数字
# print(res.group())
res=re.match('\w{3}',"python")
print(res.group())
# (5) {m,n} 匹配前一个字符出现从m次到n次，必须满足m<n
res=re.match('\w{1,3}',"_1*12python")
print(res.group())

# 4.匹配开头和结尾
# (1) ^ 表示以...开头，[^]表示对...取反
res=re.match('^py',"python")	# python的确是以py开头
print(res.group())
# res=re.match('[^py]',"python")	# [^py]会报错
# print(res.group())
# (2) $ 表示以...结尾
res=re.match('.*g$',"bingbing")		# 判断是否以字母g结尾
print(res.group())
# 因为re.match()从头开始匹配，所以$在match中只对完整字符串有效
# res=re.match('.*2$',"bingbing")		# 报错
# print(res.group())

# 5.匹配分组
# (1) | 匹配左右任意一个表达式	---常用
res=re.match('abc|def',"def")	
print(res.group())
res=re.match('.|\d',"abcd")		# 从左到右进行匹配，字符s与 . 匹配后不再匹配\d
print(res.group())
# res=re.match('abc|deg',"def")	# 报错
# print(res.group())
# res=re.match('\d|\S',"abcd")	# 报错
# print(res.group())
# (2) (ab) 将括号中字符作为一个分组		---常用
res=re.match('\w*@(163|qq|126).com',"123@163.com")
print(res.group())
res=re.match('\w*@(163|qq|126).com',"123@qq.com")
print(res.group())
res=re.match('\w*@(163|qq|126).com',"123@126.com")
print(res.group())
# (3) \num 匹配前面分组num匹配到的字符串	---常用
res=re.match('<\w*>\w*</\w*>',"<html>login</html>")
print(res.group())
res=re.match('<(\w*)>\w*</\\1>',"<html>login</html>")	# 1代替了第一个括号()里的内容
print(res.group())
# res=re.match('<(\w*)>\w*</\\1>',"<html>login</div>")	# 报错
# print(res.group())
# 从外到内排序，编号从1开始
res=re.match('<(\w*)><(\w*)>\w*</\\2></\\1>',"<html><body>login</body></html>")	# 1代替了第一个括号()里的内容
print(res.group())
# (4) (?P<name>) 分组起别名
# (5) (?P=name) 引用别名为name分组匹配到的字符串
res=re.match('<(?P<L1>\w*)><(?P<L2>\w*)>\w*</(?P=L2)></(?P=L1)>',"<html><body>login</body></html>")	# 1代替了第一个括号()里的内容
print(res.group())

# 6.匹配网址：前缀一般是www；后缀一般是：.com、.cn、.org
li=['www.baidu.com','www.python.org','http.jd.cn','www.abc.cn','www.py.en']
for i in li:
	res=re.match('www\.\w*\.(com|cn|org)',i)
	if res:
		print(res.group())
	else:
		print(f"{i}该网址有错误")

# 7.re.search()：从头到尾扫描整个字符串，并返回第一个成功匹配的对象；扫描整个字符串并返回第一个成功匹配的对象，如果匹配失败则返回None
res=re.search('th',"pythonth")	# 返回首先出现的th
# 如果上一部匹配成功，则使用group()提取数据
print(res.group())
res=re.search('\d',"py1tho2nth")	# 返回首先出现的1
print(res.group())
res=re.search('\s',"py1th o2nth")
print(res.group())

# 8.re.findall()：从头到尾匹配，找到所有匹配成功的数据，返回一个列表，无需使用group()提取数据
res=re.findall('th',"pythonth")
print(res,type(res))
res=re.findall('\d',"pyt123456honth")
print(res)

# 9.re.sub(pattern,repl,string,count)：字符串替换
# pattern：正则表达式（代表需要被替换的，字符串内的旧内容）；repl：新内容；string：原字符串；count：指定替换的次数
res=re.sub('python','bingbing','hellopython')	# 输出hellobingbing
print(res)
res=re.sub('bing','b','hellobingbing')		# 输出hellobb
print(res)
res=re.sub('\d','2','这是这个月的第30天',1)
print(res)

# 10.re.split(pattern,string,maxsplit)：字符串分割
# pattern：正则表达式（代表需要被替换的，字符串内的旧内容）；string：原字符串；maxsplit：指定最大分割次数
res=re.split('|',"hello,python")	# 分割成单个字符
print(res)
res=re.split(',',"hello,python")
print(res)
# 没有设置次数，默认全部分割
res=re.split(',',"hello,python,123,hahaha",maxsplit=2)
print(res)

# 11.贪婪与非贪婪匹配
# 贪婪匹配：在满足匹配时匹配尽可能长的字符串，默认情况下采用贪婪匹配
res=re.match('em*',"emmmmm......")		# 返回emmmmm
print(res.group())
# 非贪婪匹配：在满足匹配时匹配尽可能短的字符串，使用?来表示非贪婪匹配（匹配0次或者多次）
# *表示匹配0次或者多次，?表示匹配0次或者多次，交集为{0}，取最小值0
res=re.match('em*?',"emmmmm......")		# 返回e
print(res.group())
# +表示匹配1次或者多次，?表示匹配0次或者多次，交集为{1}，取最小值1
res=re.match('em+?',"emmmmm......")		# 返回em
print(res.group())
# {2,4}表示匹配2次~4次，?表示匹配0次或者多次，交集为{2,3,4}，取最小值2
res=re.match('m{2,4}?',"mmmmmm")		# 返回mm
print(res.group())

# 12.原生字符串：字符串前加上'r'表示
print(r'sixs\tar')		# 字符'r'取消转义
print('sixs\\tar')
# 正则表达式中，匹配字符串中的字符'\'需要四个'\\\\'
res=re.match('\\\\',"\game")		# 返回em
print(res.group())
# 使用原生字符串，则只需'\\'即可代表原字符串的'\'
res=re.match(r'\\',"\game")		# 返回em
print(res.group())