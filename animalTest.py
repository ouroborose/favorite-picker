# -*- coding: utf-8 -*-

# import libraries
import urllib2
from bs4 import BeautifulSoup
import csv
import json
from collections import OrderedDict
import re

# specify the url
quote_page = 'https://www.ign.com/wikis/animal-crossing-new-horizons/Villagers_and_Other_Characters'

# query the website and return the html to the variable ‘page’
page = urllib2.urlopen(quote_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

# get the individual data point
sections = soup.find_all('section', attrs={'class':'jsx-4115608983 wiki-image images-1'})

animalArr=[]

for animal in sections:
	image = animal.find("img")
	imgText = image.attrs.get("src")
	imgAlt = image.attrs.get("alt")
	#print(imgText.split('?')[0])
	animalObject = OrderedDict()
	animalObject['id'] = imgAlt.split('.')[0]
	animalObject['name'] = imgAlt.split('.')[0]
	animalObject['image'] = imgText.split('?')[0]

	animalArr.append(animalObject)

	
with open('animalData.json', 'w') as outfile:
	json.dump(animalArr, outfile)
	
with open('animalData2.json', 'w') as f:
	json_data = open('animalData.json').read()
	f.write(re.sub(r'"(id|name|image)"(?=: )',r'\1', json_data))
	