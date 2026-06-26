
#元组不可修改,重复有序
# t1 = (80,95,78,50,76,80,85,20)
# print(t1)
# print(t1[0])
# print(t1[-1])
#
# print(t1[0:5])
# print(t1.count(80))
# print(t1.index(80))
#
# #注意,单个元素元组
# t3 = (100,)
# print(t3)
# print(type(t3))

# #解包与组包
# t1 = (5,7,9,10,2,23,12)
# a,b,c,d,e,f,g = t1
# print(a,b,c,d,e,f,g)
#
# first,second,*other,last = t1
# print(first,second)
# print(*other)
#
# print(type(other))


#交换两个变量
# a = 10
# b = 20
# a,b=b,a#组包与解包 t=a,b  a,b = t
# print(a,b)
# #a,b,c赋给c,a,ba=100
# a=100
# b=200
# c=300
# c,a,b=b,a,c
# print(a,b,c)

students = (
    ("S001","王林",85,92,78),
    ("S002","李慕婉",92,88,95),
    ("S003","十三",78,85,82),
    ("S004","曾牛",88,79,91),
    ("S005","周轶",95,95,89),
    ("S006","王卓",76,82,77),
    ("S007","红蝶",89,91,94),
    ("S008","徐立国",75,69,82),
    ("S009","许木",86,89,98),
    ("S010","遁天",66,59,72)
)
#{avg:.1f}一位小数
print("学号\t\t姓名\t\t语文\t\t数学\t\t英语\t\t总分\t\t平均分")
#方式一
# for s in students:
#     total = s[2]+s[3]+s[4]
#     avg = total/3
#     print(f"{s[0]} \t {s[1]} \t {s[2]} \t {s[3]} \t {s[4]} \t {total} \t {avg:.1f}")
print()
#方式2
for id,name,yu,shu,ying in students:
    total = yu+shu+ying
    avg = total/3
    print(f"{id} \t {name} \t {yu} \t {shu} \t {ying} \t {total} \t {avg:.1f}")
print()

#统计各科成绩最低最高平均
chinese_scores = [s[2] for s in students]
math_scores = [s[3] for s in students]
english_scores = [s[4] for s in students]
print(f"语文: 最高分:{max(chinese_scores)},最低分:{min(chinese_scores)},平均分:{sum(chinese_scores)/3:.1f}")
print(f"数学: 最高分:{max(math_scores)},最低分:{min(math_scores)},平均分:{sum(math_scores)/3:.1f}")
print(f"英语: 最高分:{max(english_scores)},最低分:{min(english_scores)},平均分:{sum(english_scores)/3:.1f}")
print()
#统计优秀额学生并输出
print("优秀学生名单如下:")
for id,name,chinese,english,math in students:
    total = chinese+english+math
    avg = total/3
    if avg > 90:
        print(f"{id},{name},{avg:.1f}")
