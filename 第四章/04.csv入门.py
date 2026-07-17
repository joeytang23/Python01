#csv操作 -方式-:文件操作原始方式

# with open("csv_data/01.csv","w",encoding="utf-8") as f:
#     f.write("姓名,年龄,性别,爱好\n")#表头
#     f.write("小王,18,男,'football,GYM'\n")
#     f.write("小李,18,女,python\n")
#     f.write("小张,18,男,C++\n")
#     f.write("小王,20,男,GO\n")

#读
# with open("csv_data/01.csv","r",encoding="utf-8") as f:
#     for line in f:
#         print(line.strip())

#方式2- csv标准库

import csv

with open("csv_data/02.csv",'w',encoding="utf-8",newline="") as f:
    writer = csv.DictWriter(f,fieldnames=["姓名","年龄","性别","爱好"])
    writer.writeheader()#写入表头
    writer.writerow({"姓名":"小王","年龄":"18","性别":"男","爱好":"football,GYM"})
    writer.writerow({"姓名":"小李","年龄":"18","性别":"女","爱好":"python"})
    writer.writerow({"姓名":"小张","年龄":"18","性别":"男","爱好":"C++"})
    writer.writerow({"姓名":"小王","年龄":"20","性别":"男","爱好":"GO,Java "})
#读取
with open("csv_data/02.csv",'r',encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
