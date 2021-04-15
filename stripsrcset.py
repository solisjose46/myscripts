import os
from bs4 import BeautifulSoup

paths = ['../local-journalist-archive/stories/azmirror/', '../local-journalist-archive/stories/downtowndevil/']

for count, path in enumerate(paths):
    for filename in os.listdir(path):
        with open(path + filename, encoding='utf8') as fp:
            soup = BeautifulSoup(fp, 'html.parser')
        
        imgs = soup.find_all('img')

        for i, img in enumerate(imgs):
            img['srcset'] = ''
        
        #update html file via new soup
        newhtml = soup.prettify("utf-8")
        with open(path + filename, "wb") as f:
            f.write(newhtml)
            
print('img srcset removed')    
