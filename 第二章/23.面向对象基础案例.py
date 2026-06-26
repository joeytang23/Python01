"""
采用面向对象的编程思想，完成教务管理系统的开发。教务管理系统可以管理在校学生的成绩信息，通过控制台菜单与用户交互，具体的功能如下：
    1. 添加学生成绩：根据输入的学生姓名、语文成绩、数学成绩、英语成绩，记录在系统中
        1.1 输入学生姓名、语文成绩、数学成绩、英语成绩
        1.2 检查学生姓名是否已存在, 如果学生不存在, 再添加 (存在则, 不添加)
        1.3 验证成绩范围（0-100分）
        1.4 创建学生对象并添加到系统
    2. 修改学生成绩：根据输入的学生姓名，修改对应的学生成绩
        2.1 输入要修改的学生姓名
        2.2 根据姓名查找该学生, 显示该生当前成绩信息
        2.3 输入新的语文、数学、英语成绩
        2.4 更新学生成绩数据
    3. 删除学生成绩：根据输入的学生姓名，删除对应的学生成绩
    4. 查询指定学生成绩：根据输入的学生姓名，查找对应的学生成绩，并输出
        4.1 输出格式为: "姓名：张三 | 语文：85 | 数学：90 | 英语：88 | 总分：263"
    5. 展示全部学生成绩：展示出系统中所有学生的成绩
"""
class Student:
    def __init__(self, name,chinese,math,english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english
    def __str__(self):
        return f"姓名:{self.name} | 语文:{self.chinese} | 数学:{self.math} | 英语:{self.english} | 总分:{self.chinese+self.math+self.english}"
    def update_score(self,chinese=None,math=None,english=None):
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english
        print("修改完毕")


class EduSystem:
    system_version = "1.0"
    system_name = "学生信息教务管理系统"
    def __init__(self):
        self.stu_list = []

    def add_stu(self):
        name = input("请输入学生姓名")
        for s in self.stu_list:
            if s.name == name:
                print(f"{name}学生已存在")
                return
        chinese = int(input("请输入学生语文成绩"))
        math = int(input("请输入学生数学成绩"))
        english = int(input("请输入学生英语成绩"))
        if 0<=chinese<=100 and 0<=math<=100 and 0<=english<=100:
            s1 = Student(name,chinese,math,english)
            self.stu_list.append(s1)
            print("学生信息表添加成功")

    def update_stu(self):
        name = input("请输入要修改的学生姓名")
        for s in self.stu_list:
            if s.name == name:
               print(f"当前学生{s}")
               chinese = int(input("请输入要修改的学生语文成绩"))
               math = int(input("请输入要修改的学生数学成绩"))
               english = int(input("请输入要修改的学生英语成绩"))
               if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                   s.update_score(chinese,math,english)
                   return
               else:
                   print("各科成绩不在正确范围内")
                   return

        print("不存在未找到")

    def delete_stu(self):
        name = input("请输入要删除的学生姓名")
        for s in self.stu_list:
            if s.name == name:
                self.stu_list.remove(s)
                print("成功删除")
                return

        print("未找到学生删除失败")
    def query_stu(self):
        name = input("请输入要查询的学生姓名")
        for s in self.stu_list:
                if s.name == name:

                    print("展示")
                    print(f"学生信息表{s}")
                    return
        print("未找到学生查询你雷霆")

    def show_stu(self):
        for s in self.stu_list:
            print(s)

    def run(self):
        print(f"欢迎使用教务管理系统 V{EduSystem.system_version}")

        while True:
            print()
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            print("# 1.统计显示  2.修改学生  3.删除学生  4.查询指定学生  5.展示全班学生  6.退出系统#")
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            print()
            choice = int(input("请输入操作(1-6):"))
            print()
            try:
                match choice:
                    case 1:
                        self.add_stu()
                    case 2:
                        self.update_stu()
                    case 3:
                        self.delete_stu()
                    case 4:
                        self.query_stu()
                    case 5:
                        self.show_stu()
                    case 6:
                        print("See u")
                        break
                    case _:
                        print("好好输入可以吗")
                        break
            except ValueError as e:
                print("error",e)
if __name__ == "__main__":
    edu_management = EduSystem()
    edu_management.run()


"""
   采用面向对象的编程思想，开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用自定义对象存储商品数据，通过控制台菜单与用户交互。具体功能如下：
1.添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
2.修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
3.删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
4.查询购物车：将购物车中的商品信息展示出来，格式为："商品名称：xxx，商品价格：xxx，商品数量：xxx"。
5.退出购物车
"""
# class goods:
#     def __init__(self,name,price,number):
#         self.name = name
#         self.price = price
#         self.number = number
#     def __str__(self):
#         return (f"商品名称:{self.name},商品价格:{self.price},商品数量:{self.number}")
#     def update_goods(self,name=None,price=None,number=None):
#         if name is not None:
#             self.name = name
#         if price is not None:
#             self.price = price
#         if number is not None:
#             self.number = number
#         print("修改完毕")
#
# class shopping_cart:
#     version = "1.0"
#     name = "购物车管理系统"
#     def __init__(self):
#         self.cart_list = []
#     def add_cart(self):
#         name = input("请输入要添加的商品名称:")
#         for c in self.cart_list:
#             if c.name == name:
#                 print("商品已存在")
#                 return
#         price = int(input("请输入要添加的商品的价格"))
#         number = int(input("请输入要添加的商品的数量"))
#         if price > 0 and number > 0:
#             good1 = goods(name, price, number)
#             self.cart_list.append(goods(name,price,number))
#             self.cart_list.append(good1)
#             print("添加完毕")
#         else:
#             print("价格和数量不能小于0")
#     def update_shopping_cart(self):
#         name = input("请输入要修改的商品名称:")
#         for c in self.cart_list:
#             if c.name == name:
#                 print(f"{c}")
#                 price = int(input("请输入要修改的商品的价格"))
#                 number = int(input("请输入要修改的商品的数量"))
#                 c.update_goods(name,price,number)
#                 return
#         print("商品不存在，修改个毛")
#         return
#     def delete_shopping_cart(self):
#         name = input("请输入要修改的商品名称:")
#         for c in self.cart_list:
#             if c.name == name:
#                 self.cart_list.remove(c)
#                 print("删除完毕")
#                 return
#         print("商品不存在，无法删除")
#
#     def query_shopping_cart(self):
#         name = input("请输入要查询的商品名称:")
#         for c in self.cart_list:
#             if c.name == name:
#                 print(f"{c}")
#                 return
#         print("商品不存在，无法查询")
#
#
#
#     def run(self):
#         print("Welcome!")
#         while True:
#             print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
#             print("#  1.添加购物车  2.修改购物车  3.删除购物车  4.查询购物车  5.退出购物车  #")
#             print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
#             print()
#             choice = int(input("请输入操作(1-5):"))
#             match choice:
#                 case 1:
#                     self.add_cart()
#                 case 2:
#                     self.update_shopping_cart()
#                 case 3:
#                     self.delete_shopping_cart()
#                 case 4:
#                     self.query_shopping_cart()
#                 case 5:
#                     print("See u")
#                     break
#                 case _:
#                     print("请输入合法选项")
#                     break
#
# if __name__ == "__main__":
#     cart = shopping_cart()
#     cart.run()