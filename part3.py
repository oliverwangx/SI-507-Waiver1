# these should be the only imports you need

import requests
from bs4 import BeautifulSoup




# write your code here
# usage should be python3 part3.py

html = requests.get("https://www.michigandaily.com/").text

soup = BeautifulSoup(html, 'html.parser')
#print(soup)


items = (soup.find('div', attrs = {'class': 'view view-most-read view-id-most_read view-display-id-panel_pane_1 view-dom-id-996'
'58157999dd0ac5aa62c2b284dd266'}))
list_items = items.find_all('li')

#
web=[]
print("Michigan Daily -- MOST READ ")
for li in list_items:
    print(li.text)
    web=li.a.get('href')
    web="https://www.michigandaily.com/"+web
    html = requests.get(web).text
    soup = BeautifulSoup(html, 'html.parser')
    items = (soup.find('div', attrs={
        'class': 'link'}))
    print("  by "+items.text)




