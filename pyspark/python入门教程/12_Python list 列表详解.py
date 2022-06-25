

if __name__ == '__main__':
    # 列表中同时包含字符串、整数、列表、浮点数这些数据类型

    mylist = ["http://c.biancheng.net/python/", 1, [2, 3, 4], 3.0]

    print(type(mylist))

    #  使用 list() 函数创建列表
    # 除了使用[ ]创建列表外，Python 还提供了一个内置的函数 list()，使用它可以将其它数据类型转换为列表类型。

    # 将字符串转换成列表
    list1 = list("hello")
    print(list1)

    # 将元组转换成列表
    tuple1 = ('Python', 'Java', 'C++', 'JavaScript')
    list2 = list(tuple1)
    print(list2)

    # 将字典转换成列表
    dict1 = {'a': 100, 'b': 42, 'c': 9}
    list3 = list(dict1)
    print(list3)

    # 将区间转换成列表
    range1 = range(1, 6)
    list4 = list(range1)
    print(list4)

    # 创建空列表
    print(list())

    """

    Python 删除列表
    对于已经创建的列表，如果不再使用，可以使用 del 关键字将其删除。
    实际开发中并不经常使用 del 来删除列表，因为 Python 自带的垃圾回收机制会自动销毁无用的列表，即使开
    发者不手动删除，Python 也会自动将其回收。

    """