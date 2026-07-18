import requests
import csv
from lxml import html
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
}



#常量
TMDB_BASE_URL="https://www.themoviedb.org"
TMDB_TOP_URL = "https://www.themoviedb.org/movie/top-rated"


#获取电影详情
def get_movie_info(movie_info_url):
    time.sleep(1)
    #1.发送请求,获取电影详情数据
    movie_response = requests.get(movie_info_url,timeout=60,headers=headers)


    #2.解析数据,获取电影详情
    movie_doc = html.fromstring(movie_response.text)

    #电影名称,年份,时间,耗时,类型,评分,语言,简介等
    movie_names = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/h2/a/text()")
    movie_years = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/h2/span/text()")
    movie_dates = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[2]/text()")
    movie_tags = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[3]/text()")
    movie_runtimes = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[4]/text()")
    movie_scores = movie_doc.xpath("//*[@id='consensus_pill']/div/div[1]/div/div/@data-percent")
    movie_languages = movie_doc.xpath("//*[@id='media_v4']/div/div/div[2]/div/section/div[1]/div/section[1]/p[3]/text()")
    movie_directors = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/ol/li[1]/p[1]/a/text()")
    movie_authors = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/ol/li[4]/p[1]/a/text()")
    movie_descriptions = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/div/p/text()")



    #3.返回电影详情,字典
    movie_info = {
        "电影名":movie_names[0].strip() if movie_names else '',
        "年份":movie_years[0].strip() if movie_years else '',
        "时间":movie_dates[0].strip() if movie_dates else '',
        "耗时":movie_runtimes[0].strip() if movie_runtimes else '',
        "类型":",".join(movie_tags) if movie_tags else '',
        "评分":movie_scores[0].strip() if movie_scores else '',
        "语言":movie_languages[0].strip() if movie_languages else '',
        "导演":movie_directors[0].strip() if movie_directors else '',
        "编剧":movie_authors[0].strip() if movie_authors else '',
        "简介":movie_descriptions[0].strip() if movie_descriptions else '',
    }
    print(movie_info)
    return movie_info




#主函数
def save_all_movies(all_movies):
    pass


def main():
    #1.发送请求,获取高分电影榜单数据
    response = requests.get(TMDB_TOP_URL,timeout=60,headers=headers)

    #2.解析数据,获取电影列表
    document = html.fromstring(response.text)
    # 直接匹配每个电影卡片
    movie_list = document.xpath("//div[@class='media-list-results contents']/div")

    all_movies = []
    for movie in movie_list:  # movie 现在就是每个 comp:poster-card
        movie_info_urls = movie.xpath(".//a/@href")  # 用 .// 在当前卡片里找所有 a 标签
        # 然后过滤出电影链接...
        if movie_info_urls:
            movie_info_url = TMDB_BASE_URL + movie_info_urls[0]
            movie_info =get_movie_info(movie_info_url)
            all_movies.append(movie_info)
    #4.保存数据为csv文件
    save_all_movies(all_movies)
if __name__ == '__main__':
    main()