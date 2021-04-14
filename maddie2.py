import requests
import re
from bs4 import BeautifulSoup

urls = ['https://downtowndevil.com/author/madeline-ackley/', 'https://downtowndevil.com/author/madeline-ackley/page/2/', 'https://downtowndevil.com/author/madeline-ackley/page/3/']
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
# list of headers to use: http://www.useragentstring.com/pages/useragentstring.php?name=Chrome
links = []

for url in urls:
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.text, 'html.parser')
    data = soup.find_all('a')
    for item in data:
        try:
            if 'entry-title' in item.parent['class']:
                links.append(item['href'])
        except:
            print('not a match')

for link in links:
    req = requests.get(link, headers=headers)
    soup = BeautifulSoup(req.text, 'html.parser')

    title = soup.find('title')
    header = soup.find('header')
    texts = soup.find(class_='td-post-content')
    body = str(title) + str(header) + str(texts)

    name = title.text + '.html'
    localpath = '../madeline-ackley/stories/downtowndevil/' + name
    htmlfile = open(localpath, 'w')
    
    htmlfile.write(body)




# url = 'https://downtowndevil.com/author/madeline-ackley/page/3/'
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

# req = requests.get(url, headers=headers)

# #sprint(req.status_code)

# soup = BeautifulSoup(req.text, 'html.parser')
# data = soup.find_all('a')

# for item in data:
#     #print(item.parent['class'])
#     try:
#         if 'entry-title' in item.parent['class']:
#             print(item['href'])
#             #links.append(item['href'])
#     except:
#         print('not a match')