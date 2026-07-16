import requests

#定义url
target_url="https://www.tiobe.com/tiobe-index/"


#发送请求，获取数据
reponse = requests.get(target_url)


#输出
print(reponse.text)