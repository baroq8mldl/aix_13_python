from urllib import request
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

def get_dust(city="서울"):
    city = quote_plus(city)
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80+"+city
    target = request.urlopen(url)#접속정보 등록
    soup = BeautifulSoup(target, "html.parser")

    tag = "div.detail_info.lv3 > dl"#미세먼지 오전
#포함한 모든 글자 추출
    temp = soup.select_one(tag).get_text()
    temp = ' '.join(temp.split())
    temp = temp.split()
    result = {temp[0] : temp[1]}#{'오전':'나쁨'}

    tag = "div.detail_info.lv2 > dl"#미세먼지 오후
#포함한 모든 글자 추출
    temp = soup.select_one(tag).get_text()
    temp = ' '.join(temp.split())
    temp = temp.split()
    result[temp[0]] = temp[1] #{'오후':'보통'}
    # print('result:', result)
    return result

get_dust()
# temp = soup.select("dd.lvl")#여러개
# print(list(temp))