# i = 1
# while i<=5:
#     name = input("请输入名称")
#     password = input("请输入密码")
#     if name == "" or password == "":
#         print("不让为空")
#         continue#跳出该轮，进行下一轮
#     if name == "admin" and password == "666888":
#         print("Log in")
#         break
#     elif name == "bozai" and password == "888888":
#         print("Log in")
#         break
#     else:
#         print("包子你继续登录")
#         i+=1
#         if i == 6:
#             print(f"是人啊{i-1}次全错")

for i in range(5):
    username = input("请输入用户名: ")
    password = input("请输入密码: ")
    if username == "admin" and password == "666888":
        print("登录成功")
        break
    elif username == "zhangsan" and password == "123456":
        print("登录成功")
        break
    elif username == "taoge" and password == "888666":
        print("登录成功")
        break
    else:
        print("登录失败")
        if i == 4:
            print("输入错误五次，不允许再登录")
            break
