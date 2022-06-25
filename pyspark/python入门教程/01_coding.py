import sys

if __name__ == '__main__':
    print(sys.getdefaultencoding())
    # utf-8

    b5 = "C 语言中文网 8 岁了".encode('UTF-8')
    print("b5: ", b5)
    str1 = b5.decode("UTF-8")
    print(str1)
