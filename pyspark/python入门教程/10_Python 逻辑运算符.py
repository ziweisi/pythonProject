print(100 and 200)
print(45 and 0)
print("" or "http://c.biancheng.net/python/")
print(18.5 or "http://c.biancheng.net/python/")

"""
Python 按照下面的规则执行 and 运算:
• 如果左边表达式的值为假，那么就不用计算右边表达式的值了，因为不管右边表达式的值是什么，都不会影响
最终结果，最终结果都是假，此时 and 会把左边表达式的值作为最终结果。
• 如果左边表达式的值为真，那么最终值是不能确定的，and 会继续计算右边表达式的值，并将右边表达式的值
作为最终结果。

对于 or 运算符，情况是类似的，两边的值都为假时最终结果才为假，只要其中有一个值为真，那么最终结果就
是真，所以 Python 按照下面的规则执行 or 运算：
• 如果左边表达式的值为真，那么就不用计算右边表达式的值了，因为不管右边表达式的值是什么，都不会影响
最终结果，最终结果都是真，此时 or 会把左边表达式的值作为最终结果。
• 如果左边表达式的值为假，那么最终值是不能确定的，or 会继续计算右边表达式的值，并将右边表达式的值作
为最终结果。
"""

# 180页 学习结束！