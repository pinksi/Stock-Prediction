from django.shortcuts import render
from .models import *
from .live_crawler import get_data
from .scrapy import crawler
from .BagOfWords import news_prediction
import datetime
from datetime import date,timedelta
from datetime import datetime
# from your_app_name.models import Dodavatel
# p = Dodavatel(nazov='Petr', dostupnost=1)
# p.save()
# company_list=['ADBL','CHCL','NABIL','NLIC','NTC','OHLC','PLIC','SBI','SCB','SHL']
# assuming obj is a model instance
# def update_news(request):
# 	news_data = crawler()


def check_result(): 		#function to check the result
	result = news_prediction()
	count1 = 0
	count0 = 0
	count = 0
    
	for i in range(len(result)):#count the number of 1,0,-1
		if result[i] == 1:
			count1 = count1 + 1
		elif result[i] == 0:
			count0 = count0 + 1
		else:
			count = count + 1
	return {"positive" : count1, "neutral" : count0, "negative" : count}
	# if (count1 > count0) and (count1 > count):
	# 	#count1 = 1
	# 	#print("The Nepse index will increase")
	# 	return {"1" : count1}

	# elif (count0 > count1) and (count0 > count):
	# 	#print("The Nepse index remain same")
	# 	#count0 = 0
	# 	return {"0" : count0}
	# else:
	# 	#print("The Nepse index will decrease")
	# 	#count = -1
	# 	return {"-1" : count}

def prediction(request):
	result = check_result()
	sorted_result = sorted(result.items(), key=lambda x: x[1] )
	#sorted_result = sorted(result.values(), key=None, reverse=True)
	c = sorted_result[2][0]
	# context = {"result" : result,
	# 		"highest" : c
	# 	}
	if  c == 'positive':
		context = {"result" : result,
			"prediction" : "increase"}
	elif a == 'neutral' :
		context = {"result" : result,
			"prediction" : "neutral"}
	else :
		context = {"result" : result,
			"prediction" : "decrease"}
	return render(request,"prediction.html",context)


def change_to_int(strin):
    sep=strin.split(',')
    if(len(sep)==2):
        return sep[0]+sep[1]
    else:
        return strin

def check_inc_decrease(company_object,Company):
		number=1
		count=1
		while(number):
			dates=company_object.traded_date-timedelta(days=count)
			company_object_previous_list=Company.objects.filter(traded_date=dates)
			length=len(company_object_previous_list)
			company_object_previous=company_object_previous_list[0]
			if(length==0):
				number=1
			else:
				number=0
			count=count+1	
		if(company_object.closing_price>company_object_previous.closing_price):
			company_change=1
		else:
			company_change=0
		return company_change	        
def home(request):
	
	adbl_object=Adbl.objects.latest('traded_date')
	adbl_change=check_inc_decrease(adbl_object,Adbl)	
	
	chcl_object=Chcl.objects.latest('traded_date')
	chcl_change=check_inc_decrease(chcl_object,Chcl)

	nabil_object=Nabil.objects.latest('traded_date')
	nabil_change=check_inc_decrease(nabil_object,Nabil)

	nlic_object=Nlic.objects.latest('traded_date')
	nlic_change=check_inc_decrease(nlic_object,Nlic)

	ntc_object=Ntc.objects.latest('traded_date')
	ntc_change=check_inc_decrease(ntc_object,Ntc)

	ohl_object=Ohl.objects.latest('traded_date')
	ohl_change=check_inc_decrease(ohl_object,Ohl)

	plic_object=Plic.objects.latest('traded_date')
	plic_change=check_inc_decrease(plic_object,Plic)

	sbi_object=Sbi.objects.latest('traded_date')
	sbi_change=check_inc_decrease(sbi_object,Sbi)

	scb_object=Scb.objects.latest('traded_date')
	scb_change=check_inc_decrease(scb_object,Scb)

	shl_object=Shl.objects.latest('traded_date')
	shl_change=check_inc_decrease(shl_object,Shl)

	date=adbl_object.traded_date
	
	context = {'Adbl':{'N_O_T':adbl_object.no_of_transaction,'T_S':adbl_object.traded_share,'Max_P':adbl_object.max_price,
					'Min_P':adbl_object.min_price,'Clo_P':adbl_object.closing_price,'price_change':adbl_change},
				'Chcl':{'N_O_T':chcl_object.no_of_transaction,'T_S':chcl_object.traded_share,'Max_P':chcl_object.max_price,
					'Min_P':chcl_object.min_price,'Clo_P':chcl_object.closing_price,'price_change':chcl_change},
				'Nabil':{'N_O_T':nabil_object.no_of_transaction,'T_S':nabil_object.traded_share,'Max_P':nabil_object.max_price,
					'Min_P':nabil_object.min_price,'Clo_P':nabil_object.closing_price,'price_change':nabil_change},
				'Nlic':{'N_O_T':nlic_object.no_of_transaction,'T_S':nlic_object.traded_share,'Max_P':nlic_object.max_price,
					'Min_P':nlic_object.min_price,'Clo_P':nlic_object.closing_price,'price_change':nlic_change},	
				'Ntc':{'N_O_T':ntc_object.no_of_transaction,'T_S':ntc_object.traded_share,'Max_P':ntc_object.max_price,
					'Min_P':ntc_object.min_price,'Clo_P':ntc_object.closing_price,'price_change':ntc_change},
				'Ohl':{'N_O_T':ohl_object.no_of_transaction,'T_S':ohl_object.traded_share,'Max_P':ohl_object.max_price,
					'Min_P':ohl_object.min_price,'Clo_P':ohl_object.closing_price,'price_change':ohl_change},
				'Plic':{'N_O_T':plic_object.no_of_transaction,'T_S':plic_object.traded_share,'Max_P':plic_object.max_price,
					'Min_P':plic_object.min_price,'Clo_P':plic_object.closing_price,'price_change':plic_change},
				'Sbi':{'N_O_T':sbi_object.no_of_transaction,'T_S':sbi_object.traded_share,'Max_P':sbi_object.max_price,
					'Min_P':sbi_object.min_price,'Clo_P':sbi_object.closing_price,'price_change':sbi_change},
				'Scb':{'N_O_T':scb_object.no_of_transaction,'T_S':scb_object.traded_share,'Max_P':scb_object.max_price,
					'Min_P':scb_object.min_price,'Clo_P':scb_object.closing_price,'price_change':scb_change},
				'Shl':{'N_O_T':shl_object.no_of_transaction,'T_S':shl_object.traded_share,'Max_P':shl_object.max_price,
					'Min_P':shl_object.min_price,'Clo_P':shl_object.closing_price,'price_change':shl_change},
				'date':date	
				}

	return render(request,"index2.html",context)

def data(request):
	
	# last_ten = Adbl.objects.all().order_by('-id')
	# last_ten=last_ten.reverse()
	# # for i in last_ten:
	# # 	print(i.closing_price)
	list_data=Adbl.objects.filter(closing_price=1)
	#print("asdasddassadssadadsads",list_data)
	# # list_data=Adbl.objects.filter(closing_price__gt=400).order_by('-id')

	# list_data=Adbl.objects.latest('traded_date')
	# dates=list_data.traded_date-timedelta(days=1)

	context={'list':list_data}
	return render(request,"data.html",context)

def update_data(request):

	company_dictionary=get_data()
	#print("this is companuy data",company_dictionary)
	adbl_object=[company_dictionary['ADBL'][1],company_dictionary['ADBL'][2],int(int(change_to_int(company_dictionary['ADBL'][7]))/98),int(change_to_int(company_dictionary['ADBL'][7])),str(datetime.date.today()),int(company_dictionary['ADBL'][4]),int(company_dictionary['ADBL'][5]),int(company_dictionary['ADBL'][6])]
	chcl_object=[company_dictionary['CHCL'][1],company_dictionary['CHCL'][2],int(int(change_to_int(company_dictionary['CHCL'][7]))/98),int(change_to_int(company_dictionary['CHCL'][7])),str(datetime.date.today()),int(company_dictionary['CHCL'][4]),int(company_dictionary['CHCL'][5]),int(company_dictionary['CHCL'][6])]
	nabil_object=[company_dictionary['NABIL'][1],company_dictionary['NABIL'][2],int(int(change_to_int(company_dictionary['NABIL'][7]))/98),int(change_to_int(company_dictionary['NABIL'][7])),str(datetime.date.today()),int(company_dictionary['NABIL'][4]),int(company_dictionary['NABIL'][5]),int(company_dictionary['NABIL'][6])]
	nlic_data=[company_dictionary['NLIC'][1],company_dictionary['NLIC'][2],int(int(change_to_int(company_dictionary['NLIC'][7]))/98),int(change_to_int(company_dictionary['NLIC'][7])),str(datetime.date.today()),int(company_dictionary['NLIC'][4]),int(company_dictionary['NLIC'][5]),int(company_dictionary['NLIC'][6])]
	ntc_object=[company_dictionary['NTC'][1],company_dictionary['NTC'][2],int(int(change_to_int(company_dictionary['NTC'][7]))/98),int(change_to_int(company_dictionary['NTC'][7])),str(datetime.date.today()),int(company_dictionary['NTC'][4]),int(company_dictionary['NTC'][5]),int(company_dictionary['NTC'][6])]
	ohl_object=[company_dictionary['OHL'][1],company_dictionary['OHL'][2],int(int(change_to_int(company_dictionary['OHL'][7]))/98),int(change_to_int(company_dictionary['OHL'][7])),str(datetime.date.today()),int(company_dictionary['OHL'][4]),int(company_dictionary['OHL'][5]),int(company_dictionary['OHL'][6])]
	plic_object=[company_dictionary['PLIC'][1],company_dictionary['PLIC'][2],int(int(change_to_int(company_dictionary['PLIC'][7]))/98),int(change_to_int(company_dictionary['PLIC'][7])),str(datetime.date.today()),int(company_dictionary['PLIC'][4]),int(company_dictionary['PLIC'][5]),int(company_dictionary['PLIC'][6])]
	sbi_object=[company_dictionary['SBI'][1],company_dictionary['SBI'][2],int(int(change_to_int(company_dictionary['SBI'][7]))/98),int(change_to_int(company_dictionary['SBI'][7])),str(datetime.date.today()),int(company_dictionary['SBI'][4]),int(company_dictionary['SBI'][5]),int(company_dictionary['SBI'][6])]
	scb_object=[company_dictionary['SCB'][1],company_dictionary['SCB'][2],int(int(change_to_int(company_dictionary['SCB'][7]))/98),int(change_to_int(company_dictionary['SCB'][7])),str(datetime.date.today()),int(company_dictionary['SCB'][4]),int(company_dictionary['SCB'][5]),int(company_dictionary['SCB'][6])]
	shl_object=[company_dictionary['SHL'][1],company_dictionary['SHL'][2],int(int(change_to_int(company_dictionary['SHL'][7]))/98),int(change_to_int(company_dictionary['SHL'][7])),str(datetime.date.today()),int(company_dictionary['SHL'][4]),int(company_dictionary['SHL'][5]),int(company_dictionary['SHL'][6])]
	
	p = Adbl_live(name=adbl_object[0],abbr=adbl_object[1],no_of_transaction=adbl_object[2],traded_share=adbl_object[3],traded_date=adbl_object[4],max_price=adbl_object[5],min_price=adbl_object[6],closing_price=adbl_object[7])
	p.save()
	p = Chcl_live(name=chcl_object[0],abbr=chcl_object[1],no_of_transaction=chcl_object[2],traded_share=chcl_object[3],traded_date=chcl_object[4],max_price=chcl_object[5],min_price=chcl_object[6],closing_price=chcl_object[7])
	p.save()
	p =Nabil_live(name=nabil_object[0],abbr=nabil_object[1],no_of_transaction=nabil_object[2],traded_share=nabil_object[3],traded_date=nabil_object[4],max_price=nabil_object[5],min_price=nabil_object[6],closing_price=nabil_object[7])
	p.save()
	p =Nlic_live(name=nlic_data[0],abbr=nlic_data[1],no_of_transaction=nlic_data[2],traded_share=nlic_data[3],traded_date=nlic_data[4],max_price=nlic_data[5],min_price=nlic_data[6],closing_price=nlic_data[7])
	p.save()
	p =Ntc_live(name=ntc_object[0],abbr=ntc_object[1],no_of_transaction=ntc_object[2],traded_share=ntc_object[3],traded_date=ntc_object[4],max_price=ntc_object[5],min_price=ntc_object[6],closing_price=ntc_object[7])
	p.save()
	p=Ohl_live(name=ohl_object[0],abbr=ohl_object[1],no_of_transaction=ohl_object[2],traded_share=ohl_object[3],traded_date=ohl_object[4],max_price=ohl_object[5],min_price=ohl_object[6],closing_price=ohl_object[7])
	p.save()
	p =Plic_live(name=plic_object[0],abbr=plic_object[1],no_of_transaction=plic_object[2],traded_share=plic_object[3],traded_date=plic_object[4],max_price=plic_object[5],min_price=plic_object[6],closing_price=plic_object[7])
	p.save()
	p =Sbi_live(name=sbi_object[0],abbr=sbi_object[1],no_of_transaction=sbi_object[2],traded_share=sbi_object[3],traded_date=sbi_object[4],max_price=sbi_object[5],min_price=sbi_object[6],closing_price=sbi_object[7])
	p.save()
	p =Scb_live(name=scb_object[0],abbr=scb_object[1],no_of_transaction=scb_object[2],traded_share=scb_object[3],traded_date=scb_object[4],max_price=scb_object[5],min_price=scb_object[6],closing_price=scb_object[7])
	p.save()
	p =Shl_live(name=shl_object[0],abbr=shl_object[1],no_of_transaction=shl_object[2],traded_share=shl_object[3],traded_date=shl_object[4],max_price=shl_object[5],min_price=shl_object[6],closing_price=shl_object[7])
	p.save()
	return render(request,"index.html",{})

def update_data_daily(request):

	company_dictionary=get_data()
	adbl_object=[company_dictionary['ADBL'][1],company_dictionary['ADBL'][2],int(int(change_to_int(company_dictionary['ADBL'][7]))/98),int(change_to_int(company_dictionary['ADBL'][7])),str(datetime.date.today()),int(company_dictionary['ADBL'][4]),int(company_dictionary['ADBL'][5]),int(company_dictionary['ADBL'][6])]
	chcl_object=[company_dictionary['CHCL'][1],company_dictionary['CHCL'][2],int(int(change_to_int(company_dictionary['CHCL'][7]))/98),int(change_to_int(company_dictionary['CHCL'][7])),str(datetime.date.today()),int(company_dictionary['CHCL'][4]),int(company_dictionary['CHCL'][5]),int(company_dictionary['CHCL'][6])]
	nabil_object=[company_dictionary['NABIL'][1],company_dictionary['NABIL'][2],int(int(change_to_int(company_dictionary['NABIL'][7]))/98),int(change_to_int(company_dictionary['NABIL'][7])),str(datetime.date.today()),int(company_dictionary['NABIL'][4]),int(company_dictionary['NABIL'][5]),int(company_dictionary['NABIL'][6])]
	nlic_data=[company_dictionary['NLIC'][1],company_dictionary['NLIC'][2],int(int(change_to_int(company_dictionary['NLIC'][7]))/98),int(change_to_int(company_dictionary['NLIC'][7])),str(datetime.date.today()),int(company_dictionary['NLIC'][4]),int(company_dictionary['NLIC'][5]),int(company_dictionary['NLIC'][6])]
	ntc_object=[company_dictionary['NTC'][1],company_dictionary['NTC'][2],int(int(change_to_int(company_dictionary['NTC'][7]))/98),int(change_to_int(company_dictionary['NTC'][7])),str(datetime.date.today()),int(company_dictionary['NTC'][4]),int(company_dictionary['NTC'][5]),int(company_dictionary['NTC'][6])]
	ohl_object=[company_dictionary['OHL'][1],company_dictionary['OHL'][2],int(int(change_to_int(company_dictionary['OHL'][7]))/98),int(change_to_int(company_dictionary['OHL'][7])),str(datetime.date.today()),int(company_dictionary['OHL'][4]),int(company_dictionary['OHL'][5]),int(company_dictionary['OHL'][6])]
	plic_object=[company_dictionary['PLIC'][1],company_dictionary['PLIC'][2],int(int(change_to_int(company_dictionary['PLIC'][7]))/98),int(change_to_int(company_dictionary['PLIC'][7])),str(datetime.date.today()),int(company_dictionary['PLIC'][4]),int(company_dictionary['PLIC'][5]),int(company_dictionary['PLIC'][6])]
	sbi_object=[company_dictionary['SBI'][1],company_dictionary['SBI'][2],int(int(change_to_int(company_dictionary['SBI'][7]))/98),int(change_to_int(company_dictionary['SBI'][7])),str(datetime.date.today()),int(company_dictionary['SBI'][4]),int(company_dictionary['SBI'][5]),int(company_dictionary['SBI'][6])]
	scb_object=[company_dictionary['SCB'][1],company_dictionary['SCB'][2],int(int(change_to_int(company_dictionary['SCB'][7]))/98),int(change_to_int(company_dictionary['SCB'][7])),str(datetime.date.today()),int(company_dictionary['SCB'][4]),int(company_dictionary['SCB'][5]),int(company_dictionary['SCB'][6])]
	shl_object=[company_dictionary['SHL'][1],company_dictionary['SHL'][2],int(int(change_to_int(company_dictionary['SHL'][7]))/98),int(change_to_int(company_dictionary['SHL'][7])),str(datetime.date.today()),int(company_dictionary['SHL'][4]),int(company_dictionary['SHL'][5]),int(company_dictionary['SHL'][6])]
		
	# list_data=Adbl.objects.filter(traded_date=date.today())
	data_object=Adbl.objects.latest('traded_date')
	if(data_object.traded_date==date.today() or (data_object.closing_price==adbl_object[7] and data_object.traded_share==adbl_object[3])):
		print("data already added")
	else:	
	# 	if(list_data[0].traded_share==adbl_object[3] and list_data[0].closing_price==adbl_object[7])
		p = Adbl(name=adbl_object[0],abbr=adbl_object[1],no_of_transaction=adbl_object[2],traded_share=adbl_object[3],traded_date=adbl_object[4],max_price=adbl_object[5],min_price=adbl_object[6],closing_price=adbl_object[7])
		p.save()
		p = Chcl(name=chcl_object[0],abbr=chcl_object[1],no_of_transaction=chcl_object[2],traded_share=chcl_object[3],traded_date=chcl_object[4],max_price=chcl_object[5],min_price=chcl_object[6],closing_price=chcl_object[7])
		p.save()
		p =Nabil(name=nabil_object[0],abbr=nabil_object[1],no_of_transaction=nabil_object[2],traded_share=nabil_object[3],traded_date=nabil_object[4],max_price=nabil_object[5],min_price=nabil_object[6],closing_price=nabil_object[7])
		p.save()
		p =Nlic(name=nlic_data[0],abbr=nlic_data[1],no_of_transaction=nlic_data[2],traded_share=nlic_data[3],traded_date=nlic_data[4],max_price=nlic_data[5],min_price=nlic_data[6],closing_price=nlic_data[7])
		p.save()
		p =Ntc(name=ntc_object[0],abbr=ntc_object[1],no_of_transaction=ntc_object[2],traded_share=ntc_object[3],traded_date=ntc_object[4],max_price=ntc_object[5],min_price=ntc_object[6],closing_price=ntc_object[7])
		p.save()
		p=Ohl(name=ohl_object[0],abbr=ohl_object[1],no_of_transaction=ohl_object[2],traded_share=ohl_object[3],traded_date=ohl_object[4],max_price=ohl_object[5],min_price=ohl_object[6],closing_price=ohl_object[7])
		p.save()
		p =Plic(name=plic_object[0],abbr=plic_object[1],no_of_transaction=plic_object[2],traded_share=plic_object[3],traded_date=plic_object[4],max_price=plic_object[5],min_price=plic_object[6],closing_price=plic_object[7])
		p.save()
		p =Sbi(name=sbi_object[0],abbr=sbi_object[1],no_of_transaction=sbi_object[2],traded_share=sbi_object[3],traded_date=sbi_object[4],max_price=sbi_object[5],min_price=sbi_object[6],closing_price=sbi_object[7])
		p.save()
		p =Scb(name=scb_object[0],abbr=scb_object[1],no_of_transaction=scb_object[2],traded_share=scb_object[3],traded_date=scb_object[4],max_price=scb_object[5],min_price=scb_object[6],closing_price=scb_object[7])
		p.save()
		p =Shl(name=shl_object[0],abbr=shl_object[1],no_of_transaction=shl_object[2],traded_share=shl_object[3],traded_date=shl_object[4],max_price=shl_object[5],min_price=shl_object[6],closing_price=shl_object[7])
		p.save()
	return render(request,"index2.html",{})

def analysis(request):
	context = {
		"analysis" : "analysis"
	}
	return render(request, 'analysis.html', context) 

def about(request):
	context = {
		"about" : "This is about us"
			}
	return render(request, 'about.html', context) 


