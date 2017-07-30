import urllib.request
from bs4 import BeautifulSoup

def get_data():

	url = "http://sharesansar.com/c/today-share-price.html"
	company_list=['ADBL','CHCL','NABIL','NLIC','NTC','OHL','PLIC','SBI','SCB','SHL']
	company_dictionary={}
	request = urllib.request.Request(url)
	response = urllib.request.urlopen(request)
	html = response.read()
	soup=BeautifulSoup(html,"lxml")
	d=soup.find_all('td')
	list2=[]
	for i in d:
		a=i.text
		list2.append(a)
	count=0
	double_list=[]
	for i in range(int(len(list2)/19)):
		b=list2[i*19:(i+1)*19]
		double_list.append(b)
	print(double_list)	
	for company in double_list:
		if company[2] in company_list:
			company_dictionary[company[2]] = company
	return company_dictionary
			
		
	
	
