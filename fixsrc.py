import os
from bs4 import BeautifulSoup

path = '../journalist-archive/stories/downtowndevil/'


for filename in os.listdir(path):
    with open(path + filename, encoding='utf8') as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    
    imgs = soup.find_all('img')
    updatefile = False
    for img in imgs:
        if '.comwp-' in img['src']:
            updatefile = True
            newname = '.com/wp-'
            img['src'] = img['src'].replace('.comwp-', newname)
    
    if updatefile:
        print('fixing: ' + path + filename)
        updatefile = False
        newhtml = soup.prettify("utf-8")
        with open(path + filename, "wb") as f:
            f.write(newhtml)
        

print('src fixed')