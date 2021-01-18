import requests
from bs4 import BeautifulSoup

response = requests.get('https://askdjango.github.io/lv1/')

# 응답 html코드를 text로 변환
html = response.text
# 응답받은 html 코드를 Beautifulsoup에 사용하기 위해서 인스턴스 지정
soup = BeautifulSoup(html, 'html.parser')

# 원하는 태그 지정해서 출력
for tag in soup.select('li[class=course]'):
    print(tag.text)
