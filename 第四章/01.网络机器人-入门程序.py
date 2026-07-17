import requests
from lxml import html

#定义url
target_url="https://www.tiobe.com/tiobe-index/"


#发送请求，获取数据
reponse = requests.get(target_url)


#输出数据到控制台/
document = html.fromstring(reponse.text)

#解析数据
document.xpath("//table/thead/tr/th/text()")
#解析表头
th_list = document.xpath("//table[@id='top20']/thead/tr/th/text()")
# th_list = document.xpath("")  #路径可以在源代码里面直接拷贝xpath路径
print(th_list)

#解析表格数据
tr_list = document.xpath("//table[@id='top20']/tbody/tr")
for tr in tr_list:
    td_list = tr.xpath("./td/text()")
    print(td_list)