import os
from bs4 import BeautifulSoup
import requests

paths = ['../local-journalist-archive/stories/azmirror/', '../local-journalist-archive/stories/downtowndevil/']
dest = ['./images/azmirror/', './images/downtowndevil/']
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

for count, path in enumerate(paths):
    #print(count, path)
    for filename in os.listdir(path):
        #print(count, filename)
        with open(path + filename, encoding='utf8') as fp:
            soup = BeautifulSoup(fp, 'html.parser')
        
        imgs = soup.find_all('img')

        for i, img in enumerate(imgs):
            link = img['src']
            name = filename.replace('.html', '') + str(i) + '.jpg'
            newsrc = dest[count] + name
            img['src'] = newsrc
            #print('get: ' + link)
            #print('save as: ' + name)
            #print('update src: ' + img['src'])
            req = requests.get(link, headers=headers)
            with open(newsrc, 'wb') as f:
                f.write(req.content)
        
        #update html file via new soup
        newhtml = soup.prettify("utf-8")
        with open(path + filename, "wb") as f:
            f.write(newhtml)



# for count, path in enumerate(paths):
#     for filename in os.listdir(path):
#         #print(path + filename)
#         with open(path + filename, encoding='utf8') as fp:
#             soup = BeautifulSoup(fp, 'html.parser')
        
#         imgs = soup.find_all('img')

#         for i, img in enumerate(imgs):
#             link = img['src']
#             print(link)
        
        # for i, img in enumerate(imgs):
        #     link = img['src']
        #     namefile = filename.replace('.html', str(i))
        #     print(namefile)

        # for i, link in enumerate(imgs):
        #     newname = name + '_' + str(i)
        #     print(newname)
        #     req = requests.get(link, headers=headers)
        #     imagename = dest[count] + str(newname) + '.jpg'
        #     print('saving: ' + imagename)
        #     with open(imagename, 'wb') as f:
        #         f.write(req.content)





# for count, path in enumerate(paths):
#     for filename in os.listdir(path):
#         #print(path + filename)
#         with open(path + filename, encoding='utf8') as fp:
#             soup = BeautifulSoup(fp, 'html.parser')
        
#         imgs = soup.find_all('img')
#         name = filename.replace('.html', '')
#         for i, link in enumerate(imgs):
#             newname = name + '_' + str(i)
#             print(newname)
#             req = requests.get(link, headers=headers)
#             # imagename = dest[count] + str(newname) + '.jpg'
#             # print('saving: ' + imagename)
#             # with open(imagename, 'wb') as f:
#             #     f.write(req.content)

print('images saved')    
