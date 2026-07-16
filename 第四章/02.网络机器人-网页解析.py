from lxml import html

#读取html文件
with open("resources/豆包包.html","r",encoding="utf-8") as f:
    html_text = f.read()
    # print(html_text)

    document = html.fromstring(html_text)

    tx_list = document.xpath("//text()")
    print(tx_list)
