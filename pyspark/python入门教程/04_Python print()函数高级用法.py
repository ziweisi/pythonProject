#打开文件以便写入
f = open("01.txt","a")
print('沧海月明珠有泪',file=f)
print('蓝回日暖玉生烟',file=f)
f.close()