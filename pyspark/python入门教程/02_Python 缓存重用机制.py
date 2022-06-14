#范围在 [-5, 256] 之间的小整数
int1 = -5
int2 = -5
print("[-5, 256] 情况下的两个变量：", id(int1), id(int2))
#bool 类型
bool1 = True
bool2 = True
print("bool 类型情况下的两个变量：",id(bool1),id(bool2))
#对于字符串
s1 = "3344"
s2 = "3344"
print("字符串情况下的两个交量", id(s1), id(s2))