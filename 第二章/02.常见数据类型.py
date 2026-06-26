#常见数据类型 type()获取字面量和变量的类型

# print(type("Hello"))
# print(type(10))
# print(type(None))
# print(type(3.14))
# print(type(True))
# num = -100;
# print(type(num))
# # ----------------
# #isinstance(数据，类型)-bool
# print(isinstance(num,int))
# print(isinstance(num,float))
# print(isinstance(num,bool))

#定义字符串三种方式
# s1 = "Hello"#单双引号不能换行
# s2 = 'Python'
# s3 = """
# Hello:
#     欢迎大家学习Python
#     666~~~
# """ #三引号，可以换行
# print(s1)
# print(s2)
# print(s3)
#
# print(type(s1))
# print(isinstance(s2,str))
#
# #msg = 'It's very good'' 英文缩写引号和单引号的冲突
# msg ='It\'s very simultaneously'
# print(msg)
# msg1="It's very simultaneously"
# print(msg1)
# msg3="Hello means \"你好"
# msg31='Hello means "你好"'
# #转义字符 \'  \" \n \t
# print("\t欢迎\t大家学习python\n\t天天开心!")

#字符串拼接
# s1 = "人生苦短" "我用python" ",,fine" #+号可以省略
# print(s1)
#
# msg1="人生苦短"
# msg2="我用python"
# print("龟叔说："+msg1+","+msg2)
#
# #案例：str(int 数字)转为str
# name = "博崽"
# age = 18
# major = "Spatial Information and digital technology"
# hobby = "Python,Gym"
# print("大家好，我是： "+name+","+"今年"+ str(age) +"岁,""学习的专业是:"+major+","+"爱好是:"+hobby)

#字符串格式化 %s/  f"{}“
# name = "博崽"
# age = 18
# major = "Spatial Information and digital technology"
# hobby = "Python,Gym"
# print("大家好，我是：%s,今年%s岁,专业%s爱好%s" %(name,age,major,hobby))name = "博崽" age = 18
major = "Spatial Information and digital technology"
hobby = "Python,Gym"
age,name = 18,"bozai"
print(f"大家好，我是：{name}今年{age}岁,专业{major}爱好{hobby}" )