import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
# BeautifulSoup Document
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#limit


encText = urllib.parse.quote("오늘 반여동 날씨")
url = "https://search.naver.com/search.naver?where=nexearch&query="+encText
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
rescode = response.getcode()

if (rescode == 200):
    response_body = response.read()
    # print(response_body.decode('utf-8'))
    soup = BeautifulSoup(response_body.decode('utf-8'), 'lxml')
    inner_data = soup.find('span', class_='todaytemp').text.strip()
    print('\n날씨 {}\n'.format(inner_data))

    inner_data = soup.find('p', class_='cast_txt').text.strip()
    inner_data = inner_data.replace('˚', '도', 1)
    print('{}\n'.format(inner_data))

    inner_data = soup.find_all('span', class_='num',  limit=7)
    inner_data = [temp.text.strip() for temp in inner_data]
    # print(inner_data)
    print('최저온도 {} '.format(inner_data[0]))
    print('최고온도 {} '.format(inner_data[1]))
    print('체감온도 {} '.format(inner_data[2]))
    print('미세먼지 {} '.format(inner_data[4].split('㎍/㎥')[0]))
    print('초미세먼지 {} '.format(inner_data[5].split('㎍/㎥')[0]))
    print('오존지수 {} '.format(inner_data[6].split('ppm')[0]))


else:
    print("Error Code:" + rescode)