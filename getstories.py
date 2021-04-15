import requests
from bs4 import BeautifulSoup

urls = ['https://www.azmirror.com/author/madeline-ackley/', 'https://www.azmirror.com/author/madeline-ackley/page/2/','https://downtowndevil.com/author/madeline-ackley/', 'https://downtowndevil.com/author/madeline-ackley/page/2/', 'https://downtowndevil.com/author/madeline-ackley/page/3/']
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
# list of headers to use: http://www.useragentstring.com/pages/useragentstring.php?name=Chrome
links = []

#get list of urls to scrape from profile pages
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

#extract from urls collected above
count = 0
for link in links:
    req = requests.get(link, headers=headers)
    soup = BeautifulSoup(req.text, 'html.parser')

    title = soup.find('title')
    header = soup.find('header')
    texts = soup.find(class_='td-post-content')
    body = str(title) + str(header) + str(texts)

    if 'azmirror' in link:
        name = 'azmirror_'
        localpath = '../journalist-archive/stories/azmirror/'
    else:
        name = 'downtowndevil_'
        localpath = '../journalist-archive/stories/downtowndevil/'

    name = name + str(count) + '.html'
    count = count + 1
    localpath = localpath + name
    htmlfile = open(localpath, 'w')
    
    htmlfile.write(body)

print('scrape complete')