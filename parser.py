import requests
from bs4 import BeautifulSoup

URL = 'https://www.severelectro.kg/content/article/69-planovye-otklyucheniya'
HOST = 'https://www.severelectro.kg'


def get_html(url):
    r = requests.get(url)
    return r.text

def get_posts(html):
    soup = BeautifulSoup(html, 'lxml')
    posts = soup.find_all('div', class_='post-item')
    links = []
    for post in posts:
        link = post.find('div', class_='post-title').find('a').text
        links.append(link)
    return links

def parse():
    HTML = get_html(URL)
    POSTS = get_posts(HTML)
    return POSTS

if __name__ == '__main__':
    print(len(parse()))