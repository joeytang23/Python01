#全局变量局部变量 global关键字，可以修改全局变量和使用
# num = 100
#
# def circle_area(r):
#     pi = 3.14
#     area = pi * r * r
#     global num
#     num = 10000
#     print("num = ",num)
#     return area
#
# c_area = circle_area(10)
# print(c_area)
#
# print("num = ",num)

# def reg_stu(name,age,gender,city):
#     print(f"注册成功,姓名:{name},年龄:{age},性别:{gender},城市:{city}")
#     return {"name":name,"age":age,"gender":gender,"city":city}
#
# #位置参数
# stu = reg_stu("张三",18,"男","北京")
# print(stu)
#
# #关键字参数
# stu = reg_stu(name="王林",age=18,gender="男",city="北京")
# print(stu)

#混用的时候，关键字参数在后
#-------------------------------------------#
#默认参数
# def reg_stu(name,age,gender="男",city="北京"):
#     print(f"注册成功,姓名:{name},年龄:{age},性别:{gender},城市:{city}")
#     return {"name":name,"age":age,"gender":gender,"city":city}
#
# stu = reg_stu("李幕婉",18,"女")
# print(stu)

#----rgs):-----------------------------不定长参数(位置参数)---------------------------------
# def calc_data(*args):
#     min_data = min(args)
#     max_data = max(args)
#     avg_data = sum(args) / len(args)
#     return min_data, max_data, round(avg_data,1)
#
# print(calc_data(1,2,3,4,5,6,7,8,9))

#关键字参数，不定长
def calc_data(*args,**kwargs):
    """
    :param args:
    :param kwargs:
    round:小数位个数
         print:是否打印
    :return:
    """
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args)/len(args)
    if kwargs.get("round") is not None:
        avg_data = round(avg_data,kwargs.get("round"))
    if kwargs.get("print"):
        print(f"计算出的最小:{min_data},最大{max_data},平均{avg_data}")
    return min_data, max_data, avg_data

# print(calc_data(1,2,3,4,5,6,7,8,9))
print(calc_data(1,2,3,4,5,6,7,8,9,round=3,print=True))
