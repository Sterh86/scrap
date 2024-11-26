import requests
from bs4 import BeautifulSoup
import json


def parse_html():
    url = 'https://www.bbc.com/sport'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'

    #response = requests.get(url, headers={'user-agent': user_agent})

    #with open('bbc.html', 'w', encoding='utf-8') as f:
        #f.write(response.text)
    with open('bbc.html', 'r', encoding='utf-8') as f:
        text = f.read()
        soup = BeautifulSoup(text, features='lxml')

        data = []
        cards = soup.find_all('div', class_ ='ssrcss-1f3bvyz-Stack e1y4nx260')

    for card in cards:
        url = card.find('a').get('href')
        url = 'https://www.bbc.com/' + url
        print(url)
        title = card.find('span', class_ = 'ssrcss-1if1g9v-MetadataText e4wm5bw1')
        print(title)

        data.append({
            'url': url,
            'title': title
        })
    with open('results.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

if __name__ == '__main__':

    parse_html()
