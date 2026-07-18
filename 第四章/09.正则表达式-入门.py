import re

s1 = "18809090000是我的手机号,你记住了吗?我的另一个手机号是18800008888,两个QQ号是155998992和18809091293821你记住了吗"
s2 = "我的手机号是18809090000,你记住了吗?我的另一个手机号是18800008888,两个QQ号是155998992和18809091293821你记住了吗"

#match-从字符串的开头开始匹配
result = re.match(r"1[3-9]\d{9}",s1)
print(result.group())
print(result.span())
print(result.start())


#search-从任意位置开始,搜索第一个匹配项
result = re.search(r"1[3-9]\d{9}",s2)
print(result.group())
print(result.span())
print(result.start())

#findall从任意位置开始搜索所有匹配项,返回对象是list列表
result = re.findall(r"1[3-9]\d{9}",s2)
print(result)
