import os
from bs4 import BeautifulSoup
import requests

paths = ['../local-journalist-archive/stories/azmirror/', '../local-journalist-archive/stories/downtowndevil/']
newpath = ['../images/azmirror/', '../images/downtowndevil/']
des = ['../local-journalist-archive/images/azmirror/', '../local-journalist-archive/images/downtowndevil/']
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

for count, path in enumerate(paths):
    for filename in os.listdir(path):
        with open(path + filename, encoding='utf8') as fp:
            soup = BeautifulSoup(fp, 'html.parser')
        
        imgs = soup.find_all('img')

        for i, img in enumerate(imgs):
            link = img['src']
            name = filename.replace('.html', '') + str(i) + '.jpg'
            newsrc = newpath[count] + name
            img['src'] = newsrc
            newlocation = des[count] + name
            req = requests.get(link, headers=headers)
            with open(newlocation, 'wb') as f:
                f.write(req.content)
        
        #update html file via new soup
        newhtml = soup.prettify("utf-8")
        with open(path + filename, "wb") as f:
            f.write(newhtml)
            
print('images saved')    
