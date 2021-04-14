import requests
import re
from bs4 import BeautifulSoup

urls = ['https://www.azmirror.com/author/madeline-ackley/', 'https://www.azmirror.com/author/madeline-ackley/page/2/']

links = []

for url in urls:
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    data = soup.find_all('a')
    for item in data:
        try:
            if 'entry-title' in item.parent['class']:
                links.append(item['href'])
        except:
            print('not a match')

for link in links:
    req = requests.get(link)
    soup = BeautifulSoup(req.text, 'html.parser')

    title = soup.find('title')
    header = soup.find('header')
    texts = soup.find(class_='td-post-content')
    body = str(title) + str(header) + str(texts)

    name = title.text + '.html'
    localpath = '../madeline-ackley/stories/azmirror/' + name
    htmlfile = open(localpath, 'w')

    
    htmlfile.write(body)