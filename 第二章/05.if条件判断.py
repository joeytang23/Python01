# score = 700
# score -=50
# if score > 680:
#     print("清华我来了")
#     print("大学生我是")
#---------------------------
# ok_account = 1888888888
# ok_password = 666888
# accout = int(input("请输入账号:"))
# password = int(input("请输入密码:"))
# if accout == ok_account and password == ok_password :
#     print("登陆成功")
# else:
#     print("账号或密码错误")


#闰年 整百年份被400整除，非整百被4整除
# year = int(input("请输入年份"))
#
# if (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0 ):
#     print(f"{year}是闰年")
# else:
#     print("平年")

# num = int(input("请输入数字:"))
#
# if num > 0:
#     print(f"{num}是整数")
# elif num < 0 :
#     print(f"{num}是复数")
# else:
#     print(f"{num}是0")
"""password = input("请输入密码：")

if username == "admin" and password == "666888":
    print("登陆成功")
"""

#三角形类型判断:
#
# a = int(input("请输入第一个边长"))
# b = int(input("请输入二个边长"))
# c = int(input("请输入第三个边长"))
#
# if a + b > c and a + c > b and b + c > a:
#     if a == b and b == c:
#         print("等边三角形")
#     elif a == b or a == c or b == c:
#         print("等腰三角形")
#     else:
#         print("普通三角形")
# else:
#     print(f"{a}{b}{c}构不成三角形！！！")

#阶梯水价
degree = float(input("请输入用电度数："))
level_first = 0.4883
level_second = 0.5383
level_third = 0.7883
if degree > 0 and degree <=2880:
    print(f"{degree}度电,花费{degree * level_first}元")
elif degree > 2800 and degree <=4800:
    print(f"{degree}度电，花费,{2880*level_first+(degree - 2880)*level_second}")
elif degree > 4800:
    print(f"{degree}度电，花费 {2880 * level_first + (4800 - 2800) * level_second+(degree - 4800)*level_third}")

