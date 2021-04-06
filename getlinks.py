import requests
import re
#make get request to retrieve js file and scrape any images (url)

url = 'https://img1.wsimg.com/blobby/go/4af964a4-a988-45b3-b838-1a43b5725bf3/gpub/a508463ec4ac95f6/script.js'

req = requests.get(url)
data = req.text

matches = re.findall(r'img1(.*?)(JPG|jpg)', data)


list_of_urls = open('links.txt', 'w')
for par in matches:
    image = 'https://img1' + par[0] + par[1]
    list_of_urls.write(image + '\n')
