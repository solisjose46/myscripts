import requests
import re

url = 'https://img1.wsimg.com/blobby/go/4af964a4-a988-45b3-b838-1a43b5725bf3/gpub/a508463ec4ac95f6/script.js'

req = requests.get(url)
data = req.text

matches = re.findall(r'img1(.*?)(JPG|jpg)', data)

i = 0
for par in matches:
    image = 'https://img1' + par[0] + par[1]
    name = 'image' + str(i) + '.jpg'
    i+=1
    pic = requests.get(image)
    if pic.status_code == 200:
            with open(name, 'wb') as f:
                        f.write(pic.content)
    else:
        print('error') 
