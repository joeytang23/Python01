#函数定义

# def out_line():
#     print("------------------------------")
#
# out_line()

#函数参数与返回值
# def circle_area(r):
#     area = 3.14 * r**2
#     return area
# circle = circle_area(10)
# print(circle)

#长方形
def rectangle_area(l,w):
    """
    该函数根据长方形长度和宽度计算面积
    :param l: 长度
    :param w: 宽度
    :return: 面积
    """
#     area = l*w
#     return area
# print(rectangle_area(20,10))
#
# #多个返回值
# def circle_area_len(r):
#    return 3.14 *r**2,round(2*3.14*r,1) #多个返回值,分隔
#
# al = circle_area_len(10)
# print(al)
# print(type(al))
# area,len = circle_area_len(5)
# print(area)
# print(len)

def function_a():
    print("a...before")
    function_b()
    print("a...after")

def function_b():
    print("b...before")
    function_c()
    print("b...after")

def function_c():
    print("c...")
    
function_a()
print("函数调用完毕")