import urllib.parse
import urllib.request
from bs4 import BeautifulSoup
import urllib.request as p
import csv
import pandas as pd
import io
from io import StringIO

def crawler():
	page = 1
	max_pages = 2
	newdict = {'date': None, 'review': None}
	fop = open('testdata.csv', 'w')
	w = csv.DictWriter(fop, newdict.keys(),dialect='excel' ,delimiter="\t", quoting=csv.QUOTE_NONE)
	w.writeheader()
	while page <= max_pages:
		url = 'http://www.sharesansar.com/type/news/page/' + str(page)
		#url = 'http://www.sharesansar.com/category/nepse-news/page/' + str(page)
		req = urllib.request.Request(url)
		with urllib.request.urlopen(req) as response:
		   the_page = response.read()

		soup=BeautifulSoup(the_page,"lxml")
		#print(soup)
		divs = soup.find('div', attrs={'class':'col-lg-12 col-md-9 col-sm-12 col-xs-12 rem-p'})
		div = divs.find_all('div', attrs={'class':'media component-elements-divider'})
		
		emptylist = []
		for i in div:
			d = i.find('span', attrs={'class':'red'})
			d = d.text
			h = i.find('h4', attrs={'class':'media-heading'})
			headlines = h.text
			#p = i.find('p')
			#print(p)
			#newlist = d.append
			newdict = {'date' : d, 'review':headlines}
			#print(newdict)
			emptylist.append(newdict)
		#print(emptylist)
		for items in emptylist:
			#print(items['date'])
			#if items['date']=='2017-06-30':
			#	print(items['news'])
			w.writerow(items)
				
		page = page + 1

	fop.close()	
#crawler()
