import os
from bs4 import BeautifulSoup

paths = ['../madeline-ackley/stories/azmirror/', '/madeline-ackley/stories/downtowndevil/']

indexpage = '../madeline-ackley/index.html'

with open(indexpage, encoding='utf8') as fp:
    soup = BeautifulSoup(fp, "html.parser")

ins = soup.find('insert-here') 
temp = '<div></div>'
temp = BeautifulSoup(temp, features='html.parser')
temp.div
print(temp)

# for path in paths:
#     card-body = '<div class="card"><div class="card-header"></div><ul class="list-group list-group-flush"></ul></div>'
#     temp = BeautifulSoup(card-body)
#     to_insert = temp.find(class_='list-group')
#     for count, filename in enumerate(os.listdir(path)):
        
