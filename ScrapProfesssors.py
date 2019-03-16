
import urllib.request

from bs4 import BeautifulSoup

import csv

def scrapProfessors():

    urlpage =  'https://nastava.foi.hr/'

    page = urllib.request.urlopen(urlpage)

    soup = BeautifulSoup(page, 'html.parser')

    nastavnici = soup.findAll('div', {'class': 'media-body'})

    professors = {}
    
    for div in nastavnici:
        h = div.find('h4', {'class': 'media-heading'})
        a = h.find('a')
        b = a.get_text().split(',')[0].strip()
        arr = b.split(' ')
        name = []
        for elem in arr:
            if not elem.endswith('.'):
                name.append([elem])
        professors[' '.join(word[0] for word in name)] = a['href'].split('=')[1]

    return(professors)
