from requests_html import HTMLSession
import pyppdf.patch_pyppeteer
#issues with ssl cert and pyppeteer, apply above patch
from bs4 import BeautifulSoup
import requests

session = HTMLSession()

req = session.get('https://abitofsunshine.net/gallery')
req.html.render(sleep=1, keep_page=True, scrolldown=1)
req.html.render()

soup = BeautifulSoup(req.html.raw_html, 'html.parser')
images = soup.find_all('img')

i = 0
for image in images:
    name = image['alt']
    link = image['src']
    name = name + str(i) + '.jpg'
    i +=1
    link = link.replace('//', 'https://')
    pic = requests.get(link)
    if pic.status_code == 200:
            with open(name, 'wb') as f:
                        f.write(pic.content)