import os
from bs4 import BeautifulSoup

paths = ['../journalist-archive/stories/azmirror/', '../journalist-archive/stories/downtowndevil/']

indexpage = '../journalist-archive/index.html'

with open(indexpage, encoding='utf8') as fp:
    soup = BeautifulSoup(fp, 'html.parser')

insert_here = soup.find(class_='insert-here')

for count, path in enumerate(paths):
    #create wrapper for each publication
    card_body = '<div class="card"><div class="card-header"></div><ul class="list-group list-group-flush"></ul></div>'
    card_body = BeautifulSoup(card_body, 'html.parser')

    #Insert title of publication in card header
    if 'azmirror' in path:
        title = 'AZ Mirror'
    else:
        title = 'Downtown Devil'

    card_body.find(class_='card-header').insert(0, title)

    #create a new list element for each article
    for i, filename in enumerate(os.listdir(path)):
        #create list element for each article
        list_element = '<li class="list-group-item"><a href="" target="_blank" rel="noreferrer noopener"></a></li>'
        list_element = BeautifulSoup(list_element, 'html.parser')
        
        #config path relative to index.html for link
        if count == 0 and i == 0:
            localpath = './stories/azmirror/'
        elif i == 0:
            localpath = './stories/downtowndevil/'
        
        #get title from each article for <a>
        with open(path + filename, encoding='utf8') as gp:
             filehtml = BeautifulSoup(gp, 'html.parser')
        
        #putting <li> together
        link = localpath + filename
        content = filehtml.title.string
        list_element.a.insert(0, content)
        list_element.a['href'] = link

        #insert in card body
        card_body.find(class_='list-group').insert(i, list_element)
    
    #insert card body in index.html
    insert_here.insert(count, card_body)

#overwrite old html, could overwite with open but print is ok too..
print(soup.prettify())
