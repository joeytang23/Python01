#案例1 定义一个函数计算三角形面积
def cal_triangle(d,h):
    area = 0.5*d*h
    return area
print(cal_triangle(3,4))
#案例2 定义一个函数统计元音字母个数
def count_aeiou(s):
    num = 0
    for item in s:
        if item in 'aeiouAEIOU':
            num += 1
    return num
str = "Hello World"
print(count_aeiou(str))


#案例3统计最高分最低分平均分
def show_scores(score_list):
    ma_s= max(score_list)
    mi_s=min(score_list)
    avg = round(sum(score_list)/len(score_list),1)
    return ma_s,mi_s,avg

list = [600,750,890]
print(show_scores(list))