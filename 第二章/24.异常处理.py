# try:
#     print("===========================")
#     print(my_name)
#     print("===========================")
# except NameError as e:
#     print("出错了~:异常现象",e
#
# try:
#     print("===========================")
#     # print(1/0)
#     #print("abc"[10])
#     print("abc".hello)
#     print("===========================")
# except NameError as e:
#     print("出错了~:,请检查函数名字异常现象",e)
# except ZeroDivisionError as e:
#     print("0不能被出，异常现象:",e)
# except IndexError as e:
#     print("数组越界:",e)
# except :
#     print("出差了，类型管理")
# finally:
#     print("释放")

def fun1():
    print("fun1......running")
    fun2()
def fun2():
    print("fun2......running")
    fun3()
def fun3():
    print("fun3......running")


if __name__ == "__main__":
    try:
        fun1()
    except Exception as e:
        print("EROO",e)



