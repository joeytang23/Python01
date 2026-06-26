#set无序不可重复，可以修改
# s1 = {5,3,2,0,9,12,43,64,22,5,0}
# print(s1)
#
# s2 = ()
# print(s2)
# #s2 = {}!!!字典，不是空集合定义
#
# s1 = {100,200,300,400,500,600,700,800}
# print(s1)
#
# s1.add(1200)
# print(s1)
#
# s1.remove(200)
# print(s1)
#
# e= s1.pop()
# print(e)
# print(s1)
#
# s1.clear()
# print(s1)
#
# s2 = {"A","B","C","D","E","X","Y"}
# s3 = {"C","E","Y","Z"}
#
# print(s2.difference(s3))#存在于s2不在s3
# print(s3.difference(s2))
#
# print(s2.union(s3))
# print(s2.intersection(s3))


# 选修足球学生名单
football_set = {"王林", "曾牛", "徐立国", "遁天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}
# 选修篮球学生名单
basketball_set = {"张铁", "墨居仁","王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}
# 选修法语学生名单
french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子",  "红蝶", "厉飞雨", "韩立", "曾牛"}
# 选修艺术学生名单
art_set = { "遁天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}

#1同时学法语和艺术
# 方式一
fa_set = french_set.intersection(art_set)
print(fa_set)
#方式二&
fa1_set = french_set & art_set
print(fa1_set)



#2同学学了四门的
all_set = football_set | basketball_set | french_set | art_set
print(all_set)

#3学了足球没学篮球
part_set = football_set - basketball_set
print(part_set)
#法2
part1_set = football_set.difference(basketball_set)
print(part1_set)
#法3集合推导式   { for s in set 1 if}
part2_set = {s for s in football_set if s not in basketball_set}
print(part2_set)

#每位学生选课数量 并集（|）
all_set = football_set | basketball_set | french_set| art_set
#获取学生名单
stu_list =[*football_set,*basketball_set,*french_set,*art_set]
#解包
for s in all_set:
    print(f"{s}选了{stu_list.count(s)}门")

