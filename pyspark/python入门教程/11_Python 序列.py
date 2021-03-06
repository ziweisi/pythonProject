str="C语言中文网"
print(str[0],"==",str[-6])
print(str[5],"==",str[-1])
"""

序列切片
切片操作是访问序列中元素的另一种方法，它可以访问一定范围内的元素，通过切片操作，可以生成一个新的
序列。
序列实现切片操作的语法格式如下
sname[start : end : step]
其中，各个参数的含义分别是：
• sname：表示序列的名称；
• start：表示切片的开始索引位置（包括该位置），此参数也可以不指定，会默认为 0，也就是从序列的开头进
行切片；
• end：表示切片的结束索引位置（不包括该位置），如果不指定，则默认为序列的长度；
• step：表示在切片过程中，隔几个存储位置（包含当前位置）取一次元素，也就是说，如果 step 的值大于 1，
则在进行切片去序列元素时，会“跳跃式”的取元素。如果省略设置 step 的值，则最后一个冒号就可以省略

"""

str="C语言中文网"
# 取索引区间为[0,2]之间（不包括索引 2 处的字符）的字符串
print(str[:2])
#隔 1 个字符取一个字符，区间是整个字符串
print(str[::2])
#取整个字符串，此时 [] 中只需一个冒号即可
print(str[:])

str="c.biancheng.net"
print('c'in str)
print('c'not in str)

str="c.biancheng.net"
#找出最大的字符
print(max(str))
#找出最小的字符
print(min(str))
#对字符串中的元素进行排序
print(sorted(str))


