import os
import re
import requests
import urllib.request as ur
from bs4 import BeautifulSoup as bs
from collections import Counter

url = "https://quotes.toscrape.com/tag/life/"
html = ur.urlopen(url)
soup = bs(html.read(), 'html.parser')
quotes = soup.find_all('div', {"class": "quote"})

# 모든 단어를 담을 리스트
all_words = []

for quote in quotes:
    quote = quote.find_all('span', {"class": "text"})
    for i in quote:
        # 정규표현식을 사용하여 단어 추출
        words = re.findall(r'\b\w+\b', i.text.lower())
        all_words.extend(words)

# 단어들의 빈도수 계산
word_counts = Counter(all_words)

# 상위 5개 단어 출력
top_words = word_counts.most_common(5)
for word, count in top_words:
    print(f"{word}: {count}번")