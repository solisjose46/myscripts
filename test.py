import os
from bs4 import BeautifulSoup

htmlfile = 'downtowndevil_26.html'

with open(htmlfile, encoding='utf8') as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    imgs = soup.find_all('img')

    for img in imgs:
        if '.comwp-' in img['src']:
            #print('old: ' + img['src'])
            newname = '.com/wp-'
            img['src'] = img['src'].replace('.comwp-', newname)
            #print('new: ' + img['src'])

newhtml = soup.prettify("utf-8")
with open(htmlfile, "wb") as f:
    f.write(newhtml)

print('src fixed')