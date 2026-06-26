
# s = [56,78,"A",True,666,888,751]
# print(type(s))
#
# print(s[0])
# print(s[-4])
#
# s[0]=88
# # print(s)
# #
# # # del s[0]
# # # print(s)
# # # del s[0]
# # # print(s)
# # for item in s:
# #     print(item,end="\t")
# #
# #
# # s = ["a","b","c","d","e","f","g","h","i","j"]
# # print(s[:5])
# # print(type(s[0:5:1]))
# # print(s[0:5:2])
# # print(s[0:-1])
#
# s = [56,90,88,65,90,100,209,72,145]
# print(s)
#
# s.append(188)
# print(s)
#
# s.insert(2,80)
# print(s)
#
# s.remove(90)
# print(s)
# 
# e=s.pop(1)
# print(e)
# print(s)
# s.pop()
# print(s)
#
# s.sort()
# print(s)
#
# s.reverse()
#
# print(s)
# num_list = []
# for i in range(10):
#     num = int(input("输入数字"))
#     num_list.append(num)
# print(num_list)
# num_list.sort()
# print(f"排序后：{num_list}")
# print(f"最小值：{num_list[0]}")
# print(f"最大值：{num_list[-1]}")
# print("平均值：",sum(num_list)/
#
#
# 合并两个列表并去重
#
# num_list1 = [1,2,3,4,5,81,6,7,99,210,32]
# num_list2 = [4,5,6,7,8,7,81,66,99,222,333]
#
# # num_list = []
# # for num in num_list1:
# #     if num not in num_list:
# #         num_list.append(num)
# # print(num_list)
#
# # num_list = num_list1 + num_list2
# num_list = [*num_list1,*num_list2]
# print(num_list)
#
# 生成1-20平方列表1
# num_list = []
# for i in range(1,21):
#     num_list.append(i**2)
#
# print(num_list)
#
# 方式2列表推导式
# num_list2 = [i**2 for i in range(1,21)]
# print(num_list2)
#
# 从一个数字列表提取偶数并算平方
# num_list = [12,32,65,85,95,45,6,32,1,5,2,6,8]
# new_list = [i**2 for i in num_list if i % 2 == 0]
# print(new_list)
#
# list1 = ['M','A','C','E','F','G','H','L','N','I','J','K','O']
# list2 = ['X','Z','T','Y','D','E','F','G']
# list3 = ['W','A','S','D']
#
# newlist = list1 + list2
# targetlist = []
# for item in newlist:
#     if item not in targetlist:
#         targetlist.append(item)
# print(targetlist)
#
# list1 = [i for i in range(1,31)]
# newlist = [i**2 for i in list1 if i%3==0 or i%5==0]
# print(newlist)


list1 = [11,2,31,4,-5,15,17,28,49,10,-11,16,54,-14,36,-16,87,-39]
newlist = [i for i in list1 if i > 0]
print(newlist)
