#proj2.py
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

#### Problem 1 ####
print('\n*********** PROBLEM 1 ***********')
print('New York Times -- First 10 Story Headings\n')

### Your Problem 1 solution goes here
nyt = 'https://www.nytimes.com/'

nythtml = urllib.request.urlopen(nyt)
nytsoup = BeautifulSoup(nythtml, 'html.parser')

headings = nytsoup.find_all('h2', class_='story-heading')
for h in headings[:10]:
    print (h.get_text().lstrip().rstrip())

#### Problem 2 ####
print('\n*********** PROBLEM 2 ***********')
print('Michigan Daily -- MOST READ\n')

### Your Problem 2 solution goes here
mdl = 'https://www.michigandaily.com/'

mdlhtml = urllib.request.urlopen(mdl)
mdlsoup = BeautifulSoup(mdlhtml, 'html.parser')

most_reads = mdlsoup.find_all('div', class_='view view-most-read view-id-most_read view-display-id-panel_pane_1 view-dom-id-99658157999dd0ac5aa62c2b284dd266')
for h in most_reads:
    print (h.get_text().rstrip().lstrip())

'''
#### Problem 3 ####
print('\n*********** PROBLEM 3 ***********')
print("Mark's page -- Alt tags\n")

### Your Problem 3 solution goes here


#### Problem 4 ####
print('\n*********** PROBLEM 4 ***********')
print("UMSI faculty directory emails\n")

### Your Problem 4 solution goes here
'''
