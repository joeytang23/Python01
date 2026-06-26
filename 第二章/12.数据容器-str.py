# s = "Hello Python"
# print(s[-7])
#
# #s[4]= "x" str不能进行修改操作
#
# for item in s:
#     print(item,end = "")

#切片 step > 0 前到后 step < 0 后到前
# print(s[0:5:1])
# print(s[6::])
# print(s[::-1])

# s = "  Hello-Python-Hello-World   "
# index = s.find("-")
# print(index)
#
# c = s.count("o")
# print(c)
#
# su = s.upper()
# print(su)
#
# sl = s.lower()
# print(sl)
#
# slist = s.split("-")
# print(slist)
#
# ss = s.strip()  #去除两端空格
# print(ss)
#
# sr = s.replace("-","_")
# print(sr)
#
# print(s.startswith("Hello"))
# print(s.endswith("Python"))
#
# print("---------------------")
# print(s)

#邮箱格式验证
# mail = input("请输入邮箱")
#
# if mail.count("@") == 1 and "."in mail:
#     print(f"{mail}合法")
# else:
#     print(f"{mail}不合法s


           #判断回文
# str = input("请输入要判断的字符串")
# left = 0
# right = len(str)-1
# while str[left]==str[right]:
#     left += 1
#     right -= 1
#     if left == right:
#         print(f"{str}是回文")
#         break

# s = input()
# if s == s[::-1]:
#     print(f"'{s}' 是回文")
# else:
#     print(f"'{s}' 不是回文")
s_list = []
for i in range(2):
    s = input("请输入字符串:")
    s_list.append(s[::-1].upper())

for i in s_list:
    print(i)