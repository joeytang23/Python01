#字典 -- key不能重复,否则后值覆盖前值，key是不可变类型(str,int,float,tuple)

# dict1 = {"王林":670,"李幕婉":608,"徐立国":580,"韩立":688}
#
# print(dict1)
# print(type(dict1))
#
# dict2 = {0:671,1.5:608,(1,2):580,("A","B"):688}
# print(dict2)
#
# print(dict1["王林"])
# dict1["王林"]=900
#
# print(dict1)

#---------------------常规操作
# dict1 = {"王林":670,"李幕婉":608,"徐立国":580,"韩立":688}
# print(dict1)
#
# dict1["博哥"] = 609
# print(dict1)
#
# print(dict1["博哥"])
# print(dict1.get("博哥"))
#
# print(dict1.keys())
# print(dict1.values())
# print(dict1.items())
#
# score = dict1.pop("徐立国")
# print(score)
# print(dict1)
#
# del dict1["韩立"]
# print(dict1)
#
# #遍历
# for k in dict1.keys():
#     print(f"{k}:{dict1[k]}")
# print()
# for k,v in dict1.items():
#     print(f"{k}:{v}")
# print()
# for items in dict1.items():
#     print(f"{items[0]}:{items[1]}")


#购物车案例------------------------------
#shopping_car = {"iphone":{"price":18000 , "num":2}
# menu = """
# ########## 购物车系统 ##########
# #        1、添加购物车         #
# #        2、修改购物车         #
# #        3、删除购物车         #
# #        4、查询购物车         #
# #        5、推出购物车         #
# ##############################
# """
# shopping_cart = {}
#
# while True:
#     print(menu)
#     print("请选择要执行的操作：")
#     choice = int(input())
#     match choice:
#         case 1:
#             goods_name = input("请输入商品名称")
#             goods_price = input("请输入商品价格")
#             goods_num = input("请输入商品数量")
#             if goods_name  in shopping_cart:
#                 print("商品存在")
#             else:
#               shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
#             print("商品添加完毕")
#         case 2:
#             goods_name = input("请输入要修改的商品名称")
#             if goods_name not in shopping_cart:
#                 print("商品不存在")
#                 continue
#             goods_price = input("请输入要修改的商品价格")
#             goods_num = input("请输入要修改的商品数量")
#             shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
#             print("商品修改完毕")
#         case 3:
#             goods_name = input("请输入要删除的商品名称")
#             if goods_name not in shopping_cart:
#                 print("我本身就是一个不存在的人啊")
#             else:
#                 del shopping_cart[goods_name]
#         case 4:
#             for goods_name in shopping_cart.keys():
#                 goods_info = shopping_cart[goods_name]#用一个新的字典来接受value
#                 print(f"商品名称{goods_name},商品价格：{goods_info["price"]},商品数量:{goods_info["num"]}")
#         case 5:
#             print("bye")
#             break
#         case _:
#             print("What are u doing?")

#数据容器综合案例

# 采用面向对象的编程思想，完成教务管理系统的开发。教务管理系统可以管理在校学生的成绩信息，通过控制台菜单与用户交互，具体的功能如下：
#     1. 添加学生成绩：根据输入的学生姓名、语文成绩、数学成绩、英语成绩，记录在系统中
#         1.1 输入学生姓名、语文成绩、数学成绩、英语成绩
#         1.2 检查学生姓名是否已存在, 如果学生不存在, 再添加 (存在则, 不添加)
#         1.3 验证成绩范围（0-100分）
#         1.4 创建学生对象并添加到系统
#     2. 修改学生成绩：根据输入的学生姓名，修改对应的学生成绩
#         2.1 输入要修改的学生姓名
#         2.2 根据姓名查找该学生, 显示该生当前成绩信息
#         2.3 输入新的语文、数学、英语成绩
#         2.4 更新学生成绩数据
#     3. 删除学生成绩：根据输入的学生姓名，删除对应的学生成绩
#     4. 查询指定学生成绩：根据输入的学生姓名，查找对应的学生成绩，并输出
#         4.1 输出格式为: "姓名：张三 | 语文：85 | 数学：90 | 英语：88 | 总分：263"
#     5. 展示全部学生成绩：展示出系统中所有学生的成绩

system = """
# # # # # # # # # # # # # # # # # # # # # # # # # # [菜单] # # # # # # # # # # # # # # # # # # # # # # # # # # 
#   1.添加学生信息  2.修改学生信息   3.删除学生信息   4.查询学生信息   5.列出所有学生   6.统计班级信息    7.退出系统    #
# # # # # # # # # # # # # # # # # # # # # # # # # # [菜单] # # # # # # # # # # # # # # # # # # # # # # # # # #
"""

# stu = {"name":{chinese:,math:,english:}}

stu_system = {}
while True:
    print(system)
    choice = int(input("请输入要执行的操作:"))
    match choice:
        case 1:
            stu_name = input("请输入学生姓名")
            if stu_name not in stu_system:
                stu_ch = int(input("请输入语文成绩"))
                stu_mt = int(input("请输入数学成绩"))
                stu_eg = int(input("请输入英语成绩"))
                stu_system[stu_name] = {"Chinese":stu_ch,"Math":stu_mt,"English":stu_eg}
                print("Over,已添加")
            else:
                print(f"{stu_name}已存在，请更换操作")
        case 2:
            stu_name = input("请输入要修改的学生姓名")
            if stu_name not in stu_system:
                print(f"{stu_name}不存在！！")
            else:
                stu_ch = int(input("请输入要修改的语文成绩"))
                stu_mt = int(input("请输入要修改的数学成绩"))
                stu_eg = int(input("请输入要修改的英语成绩"))
                if stu_ch > 0 and stu_mt > 0 and stu_eg > 0 and stu_ch <= 100 and stu_mt <= 100 and stu_eg <= 100:
                    stu_system[stu_name] = {"Chinese":stu_ch,"Math":stu_mt,"English":stu_eg}
                    print("Over,修改完毕")
                else:
                    print("成绩超杠")
                    continue


        case 3:
            stu_name = input("请输入要删除的学生姓名")
            if stu_name not in stu_system:
                print(f"你想删除的学生:{stu_name}不存在！！")
            else:
                del stu_system[stu_name]
                print("Over,删除完毕")
        case 4:
            stu_name = input("请输入要查询的学生姓名")
            if stu_name not in stu_system:
                print(f"你想查询的学生:{stu_name}不存在！！")
            else:

                    stu_info = stu_system[stu_name]
                    print(f"学生:{stu_name} | 语文成绩:{stu_info["Chinese"]} | 数学成绩:{stu_info["Math"]} | 英语成绩:{stu_info["English"]}")
        case 5:
            for stu in stu_system.keys():
                stu_info = stu_system[stu]
                print(
                    f"学生:{stu} | 语文成绩:{stu_info["Chinese"]} | 数学成绩:{stu_info["Math"]} | 英语成绩:{stu_info["English"]}")
        case 6:
            pass
        case 7:
            print("See u again")
            break

