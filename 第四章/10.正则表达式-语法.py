import re

s1 = "18809090000是我的手机号,188开头的,以00结尾的:我的另一个手机号是15500008888,两个QQ号是1259989092和13809091293821,邮箱是python666@163.com"

#正则表达式
# print(re.findall(r"188.*",s1))# *匹配任意个
# print(re.findall(r"188.?",s1))# ?匹配0/1个
# print(re.findall(r"188.+",s1))# +匹配1或多个

# print(re.findall(r"188\d{8}",s1))   # \d{8}匹配8个数字
# print(re.findall(r"155\d{6,10}",s1)) # \d{4}匹配6到10个数字
# print(re.findall(r"155\d{6,}",s1))

# print(re.findall(r"1[38]\d{8}",s1)) #[38]匹配3/8
# print(re.findall(r"1[^38]\d{8}",s1))# [^38]匹配不是3/8
# print(re.findall(r"1[3-9]\d{8}",s1))# [3-9]匹配3/4/5/6/7/8/9
# print(re.findall(r"^1[3-9]\d{9}",s1))# [3-9]匹配3/4/5/6/7/8/9
# print(re.findall(r"^1[3-9]\d{9}$",s1))#^匹配字符串的开头,$匹配字符串的结尾

# print(re.findall(r"\w+@\w+\.\w+",s1))#\w匹配任意数字/字母/下划线
# print(re.findall(r"\w+@\w+\.\w+",s1,re.ASCII))#\w匹配英文,不匹配中日韩等
# print(re.findall(r"\w+@\w+\.\w+",s1,re.UNICODE))#\w匹配中文,日文,韩文
#


s2 = "现在的时间是2026-07-18 10:10:10,今天的天气还可以,气温38度"
print(re.findall(r"\d{4}-\d{2}-\d{2}",s2))
print(re.findall(r"(\d{4})-(\d{2})-(\d{2})",s2))


