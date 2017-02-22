#proj2.py
import urllib.request, urllib.parse, urllib.error
import re
from bs4 import BeautifulSoup
import requests

#### Problem 1 ####
print('\n*********** PROBLEM 1 ***********')
print('New York Times -- First 10 Story Headings\n')

### Your Problem 1 solution goes here
nyt = 'https://www.nytimes.com/'

nythtml = urllib.request.urlopen(nyt)
nytsoup = BeautifulSoup(nythtml, 'html.parser')

headings = nytsoup.find_all('h2', class_='story-heading')
for h in headings[:10]:
    print (h.get_text().strip())

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


#### Problem 3 ####
print('\n*********** PROBLEM 3 ***********')
print("Mark's page -- Alt tags\n")

### Your Problem 3 solution goes here
cat = 'http://newmantaylor.com/gallery.html'

cathtml = urllib.request.urlopen(cat)
catsoup = BeautifulSoup(cathtml, 'html.parser')

gallery = catsoup.find_all('img')
for img in gallery:
    alt = img.get('alt', '')
    if alt != '':
        print (alt)
    else:
        print ("No altenative text provided!")

#### Problem 4 ####
print('\n*********** PROBLEM 4 ***********')
print("UMSI faculty directory emails\n")

### Your Problem 4 solution goes here
counter = 1
for page in range(6): #change range
    directory = 'https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4&page='
    url = directory+str(page)
    #urlhtml = urllib.request.Request(url, None,{'User-Agent': 'SI_CLASS'})
    urlhtml = requests.get(url, headers={'User-Agent': 'SI_CLASS'})
    urlsoup = BeautifulSoup(urlhtml.text, 'html.parser')
    contact_list = urlsoup.find_all('div', class_='field field-name-contact-details field-type-ds field-label-hidden')
    for contact in contact_list:
        indurl = 'https://www.si.umich.edu'+re.findall(r'\/.+\d', str(contact))[0]
        #indhtml = urllib.request.Request(indurl, None,{'User-Agent': 'SI_CLASS'})
        indhtml = requests.get(indurl, headers={'User-Agent': 'SI_CLASS'})
        indsoup = BeautifulSoup(indhtml.text, 'html.parser')
        for link in indsoup.find_all(href=re.compile("@")):
            print (str(counter) + " " +link.get_text())
            counter +=1
