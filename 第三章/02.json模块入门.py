import json

#写入json数据文件
# user = {
#     "name" : "博崽",
#     "age" : 18,
#    "major" : "Spatial Information and digital technology",
#     "hobby" : ["Python","Gym"]
# }
# with open("resources/user.json","w",encoding = "utf-8")as f:
#     #indent缩进 ensure_ascii=False,非ascii原样输出
#     json.dump(user,f,ensure_ascii=False,indent=2)
#
#读取json
with open("resources/user.json","r",encoding = "utf-8")as f:
    user = json.load(f)
    print(user)
    print(type(user))

