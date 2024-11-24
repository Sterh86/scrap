import requests
import re
import json


def get_content():
    url = 'https://www.lejobadequat.com/emplois'
    response = requests.get(url)
    html = response.text

    pattern = r'<a href="(?P<link>https://www\.lejobadequat\.com/emplois/[^"]+)"[^>]*>\s*<header[^>]*>.*?</header>\s*<h3[^>]*>(?P<title>.*?)</h3>'
    matches = re.findall(pattern, html, re.DOTALL)

    results = [{"title": title.strip(), "url": link} for link, title in matches]

    with open("results.txt", "w", encoding="utf-8") as file:
        json.dump(results, file, ensure_ascii=False, indent=2)

    print("результыты сохранены в results.txt")


if __name__ == '__main__':
    get_content()