import requests
import csv
from lxml import html


#常量
TMDB_BASE_URL="https://www.themoviedb.org"
TMDB_TOP_URL = "https://www.themoviedb.org/movie/top-rated"


#获取电影详情
def get_movie_info(movie_info_url):
    pass

#主函数
def save_all_movies(all_movies):
    pass


def main():
    #1.发送请求,获取高分电影榜单数据
    response = requests.get(TMDB_TOP_URL,timeout=60)

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