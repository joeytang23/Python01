#打开文件
# f = open("./resources/test.txt","r",encoding="utf-8") #./当前目录
# #读文件
# content = f.read()
# print(content)
#
# content_list = f.readlines()
# for line in content_list:
#     print(line.strip)
# #关闭文件
# f.close()

# f = open("resources/静夜思.txt","w",encoding="utf-8")
# f.write("静夜思(李白)\n")
# print()
# f.write("床前明月光\n")
# f.write("疑是地上霜\n")
# f.write("举头望明月\n")
# f.write("低头思故乡\n")
# f.close()

#--------------------------------------
# f = open("resources/静夜思.txt","w",encoding="utf-8")
# try:
#     f.write("静夜思(李白)\n\n")
#     f.write("床前明月光\n")
#     f.write("疑是地上霜\n")
#     i = 1 / 0
#     f.write("举头望明月\n")
#     f.write("低头思故乡\n")
# finally:
#     print("关闭文件")
#     f.close()

#资源释放最佳方式
with open("resources/静夜思.txt","w",encoding="utf-8") as f:

    f.write("静夜思(李白)\n\n")
    f.write("床前明月光\n")
    f.write("疑是地上霜\n")

    f.write("举头望明月\n")
    f.write("低头思故乡\n")
    print("关闭文件")
    f.close()



