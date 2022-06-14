str1 = "Oct: \061\062\063"
str2 = "Hex: \x31\x32\x33\x78\x79\x7A"
print(str1)
print(str2)


#使用\t 排版
str1 = '网站\t\t 域名\t\t\t 年龄\t\t 价值'
str2 = 'C 语言中文网\tc.biancheng.net\t\t8\t\t500W'
str3 = '百度\t\twww.baidu.com\t\t20\t\t500000W'
print(str1)
print(str2)
print(str3)
print("--------------------")

# \n 在输出时换行，\在书写字符串时换行
info = "Python 教程：http://c.biancheng.net/python/\n\
C++教程：http://c.biancheng.net/cplus/\n\
Linux 教程：http://c.biancheng.net/linux_tutorial/"
print(info)