from lxml import html

with open("resources/仙逆人物志.html","r",encoding="utf-8") as f:
    html_text = f.read()

    #解析html文本,将其转换为一个html文档对象
    document = html.fromstring(html_text)

    #解析表头 xpath语法
    #/从根目录开始查找，需要一级一级往下写
    # th_list = document.xpath("/html/body/div/div/table/thead/tr/th/text()")
    # print(th_list)
    #//直接查找,从任意位置开始匹配
    th_list = document.xpath("//thead/tr/th/text()")
    print(th_list)


    #tr[2]匹配第二个tr标签
    # tr[last()]最后一行
    #tr[last()-1]倒数第二哥
    td_list = document.xpath("//tbody/tr[2]/td/text()")
    print(td_list)

    td_list = document.xpath("//tbody/tr[last()]/td/text()")
    print(td_list)

    td_list = document.xpath("//tbody/tr[last()-1]/td/text()")
    print(td_list)

    #p[@class]:匹配class属性为p的标签
    p_list = document.xpath("//p[@class = 'xn']/text()")
    print(p_list)

    #匹配class属性为xn的p标签
    p_list = document.xpath("//p[@class ]/text()")
    print(p_list)

    #@src匹配src属性
    #@*匹配任意属性
    a_list = document.xpath("//td/img/@*")
    print(a_list)
