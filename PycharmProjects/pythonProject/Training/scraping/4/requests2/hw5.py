import requests
import re
import json
import sqlite3



def get_content():
    url = 'https://www.lejobadequat.com/emplois'
    response = requests.get(url)
    html = response.text

    pattern = r'<a href="(?P<link>https://www\.lejobadequat\.com/emplois/[^"]+)"[^>]*>\s*<header[^>]*>.*?</header>\s*<h3[^>]*>(?P<title>.*?)</h3>'
    matches = re.findall(pattern, html, re.DOTALL)

    conn = sqlite3.connect("results.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS vacancies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        url TEXT NOT NULL
    )
    """)

    for link, title in matches:
        cursor.execute("INSERT INTO vacancies (title, url) VALUES (?, ?)", (title.strip(), link))

    conn.commit()
    conn.close()

    print("Данные успешно сохранены в базе данных results.db'")


if __name__ == '__main__':
    get_content()