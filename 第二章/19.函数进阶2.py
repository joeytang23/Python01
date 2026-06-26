##函数作为参数

# def add(x,y):
#     return x+y
# def sub(x,y):
#     return x-y
# def mul(x,y):
#     return x*y
# def div(x,y):
#     return x/y
#
# def cal(x,y,oper):
#     return oper(x,y)
#
# print(cal(2,3,mul))

# #匿名函数
# out_line = lambda : print("-----------------------")
# out_line()
#
# add = lambda x, y :x+y
# print(add(10,20))
#
# #按字符个数排序
# data_list = ["C++","C","Python","Jack","PHP","Java","Go","JavaScript","Rust"]
# print(data_list)
# data_list.sort(key=lambda item:len(item),reverse=True)#匿名函数典型应用
# print(data_list)

#----------------------------------------------------------#
#计算阶乘
#递归：在函数里面自己调用自己,一点要用终结点
# def jc(n):
#     if n==1:
#         return 1
#     else:
#         return n*jc(n-1)
#
# result = jc(10)
# print(result)

# def calc(*args,coupon=0,score=0,express=0.0):
#     """
#
#     :param args: 商品名称价格数量
#     :param coupon: 优惠券
#     :param score: 积分≥5000抵扣，只能100/1
#     :param express: 邮费
#     :return: 总额
#     """
#     total_price = [goods[1]*goods[2]for goods in args]
#     total_cost = sum(total_price)
#     if total_cost >=5000 & coupon <=total_cost:
#         total_cost -= coupon
#     if total_cost >= 5000 & score//100<=total_cost:
#         total_cost -= score//100
#     total_cost += express
#     return total_cost
#
# result = calc(("鼠标",399,2),("键盘",666,3),("笔记本电脑",6999,1),coupon=10,score=40000,express=100)
# print(result)


def calc(*args:tuple[str,float,int],coupon=0,score=0,express=0.0)->float:

    total_price = [goods[1]*goods[2]for goods in args]
    total_cost = sum(total_price)
    if total_cost >=5000 & coupon <=total_cost:
        total_cost -= coupon
    if total_cost >= 5000 & score//100<=total_cost:
        total_cost -= score//100
    total_cost += express
    return total_cost

result = calc(("鼠标",399,2),("键盘",666,3),("笔记本电脑",6999,1),coupon=10,score=40000,express=100)
print(result)
