#
# msg = input("请入字符串")
#
# for s in msg:
#     print(f"元素:{s}")
# else:
#     print("悬壶济世")

# total = 0
# for i in range(1,101,2):
#         total += i
#
# print("牛逼666")
# print(total)
# total = 0
# for i in range(100,501):
#     if i % 3 == 0:
#         total += i
#
# print("牛逼666")
# print(f"{total}")

# m = int(input("请输入长度"))
# #录入
# n = int(input("请输入宽度"))
#
# for j in range(n):
#     for i in range(m):
#         print("*", end = " ")
#     print()

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{j}*{i}={j*i}",end="\t")
#     print()
#

# m = int(input("请输入直角边边长"))
#
# for i in range(m):
#     for j in range(i+1):
#         print("*",end = "\t")
#     print()

# for i in range(1,7):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

for i in range(8):
    for k in range(8):
        if (i+k)%2==0:
            print("A",end = "\t")
        else:
            print("B",end = "\t")
    print()
