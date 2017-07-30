from django.db import models
from django.utils import timezone
from datetime import date

# Create your models here.
class Company(models.Model):
	name = models.CharField(max_length= 50)
	abbr = models.CharField(max_length= 10)
	no_of_transaction=models.IntegerField()
	traded_share=models.FloatField()
	traded_date=models.DateField(default=date.today())
	max_price=models.FloatField()
	min_price=models.FloatField()
	closing_price=models.FloatField()
	
	def __str__(self):
		return self.abbr

class Adbl(models.Model):
	name = models.CharField(max_length= 50)
	abbr = models.CharField(max_length= 10)
	no_of_transaction=models.IntegerField()
	traded_share=models.FloatField()
	traded_date=models.DateField(default=date.today())
	max_price=models.FloatField()
	min_price=models.FloatField()
	closing_price=models.FloatField()
	
	def __str__(self):
		return self.abbr
		
class Adbl_live(models.Model):
	name = models.CharField(max_length= 50)
	abbr = models.CharField(max_length= 10)
	no_of_transaction=models.IntegerField()
	traded_share=models.FloatField()
	traded_date=models.DateField(default=date.today())
	traded_time = models.TimeField(auto_now_add=True, blank=True)
	max_price=models.FloatField()
	min_price=models.FloatField()
	closing_price=models.FloatField()
	
	def __str__(self):
		return self.abbr		

class Chcl(models.Model):
	name = models.CharField(max_length= 50)
	abbr = models.CharField(max_length= 10)
	no_of_transaction=models.IntegerField()
	traded_share=models.FloatField()
	traded_date=models.DateField(default=date.today())
	max_price=models.FloatField()
	min_price=models.FloatField()
	closing_price=models.FloatField()
	
	def __str__(self):
		return self.abbr

class Chcl_live(models.Model):
	name = models.CharField(max_length= 50)
	abbr = models.CharField(max_length= 10)
	no_of_transaction=models.IntegerField()
	traded_share=models.FloatField()
	traded_date=models.DateField(default=date.today())
	traded_time = models.TimeField(auto_now_add=True, blank=True)
	max_price=models.FloatField()
	min_price=models.FloatField()
	closing_price=models.FloatField()
	
	def __str__(self):
		return self.abbr		

class Nabil(models.Model):
	name = models.CharField(max_length= 50)
	abbr = models.CharField(max_length= 10)
	no_of_transaction=models.IntegerField()
	traded_share=models.FloatField()
	traded_date=models.DateField(default=date.today())
	max_price=models.FloatField()
	min_price=models.FloatField()
	closing_price=models.FloatField()
	
	def __str__(self):
		return self.abbr	
class Nabil_live(models.Model):
	name = models.CharField(max_length= 50)
	abbr = models.CharField(max_length= 10)
	no_of_transaction=models.IntegerField()
	traded_share=models.FloatField()
	traded_date=models.DateField(default=date.today())
	traded_time = models.TimeField( auto_now_add=True, blank=True)
	max_price=models.FloatField()
	min_price=models.FloatField()
	closing_price=models.FloatField()
	
	def __str__(self):
		return self.abbr
class Nlic(models.Model):
	name = models.CharField(max_length= 50)
	abbr = models.CharField(max_length= 10)
	no_of_transaction=models.IntegerField()
	traded_share=models.FloatField()
	traded_date=models.DateField(default=date.today())
	max_price=models.FloatField()
	min_price=models.FloatField()
	closing_price=models.FloatField()
	
	def __str__(self):
		return self.abbr
class Nlic_live(models.Model):
	name = models.CharField(max_length= 50)
	abbr = models.CharField(max_length= 10)
	no_of_transaction=models.IntegerField()
	traded_share=models.FloatField()
	traded_date=models.DateField(default=date.today())
	traded_time = models.TimeField( auto_now_add=True, blank=True)
	max_price=models.FloatField()
	min_price=models.FloatField()
	closing_price=models.FloatField()
	
	def __str__(self):
		return self.abbr		


class Ntc(models.Model):
	name = models.CharField(max_length= 50)
	abbr = models.CharField(max_length= 10)
	no_of_transaction=models.IntegerField()
	traded_share=models.FloatField()
	traded_date=models.DateField(default=date.today())
	max_price=models.FloatField()
	min_price=models.FloatField()
	closing_price=models.FloatField()
	
	def __str__(self):
		return self.abbr
class Ntc_live(models.Model):
	name = models.CharField(max_length= 50)
	abbr = models.CharField(max_length= 10)
	no_of_transaction=models.IntegerField()
	traded_share=models.FloatField()
	traded_date=models.DateField(default=date.today())
	traded_time = models.TimeField( auto_now_add=True, blank=True)
	max_price=models.FloatField()
	min_price=models.FloatField()
	closing_price=models.FloatField()
	
	def __str__(self):
		return self.abbr						

class Ohl(models.Model):
	name = models.CharField(max_length= 50)
	abbr = models.CharField(max_length= 10)
	no_of_transaction=models.IntegerField()
	traded_share=models.FloatField()
	traded_date=models.DateField(default=date.today())
	max_price=models.FloatField()
	min_price=models.FloatField()
	closing_price=models.FloatField()
	
	def __str__(self):
		return self.abbr
class Ohl_live(models.Model):
	name = models.CharField(max_length= 50)
	abbr = models.CharField(max_length= 10)
	no_of_transaction=models.IntegerField()
	traded_share=models.FloatField()
	traded_date=models.DateField(default=date.today())
	traded_time = models.TimeField( auto_now_add=True, blank=True)
	max_price=models.FloatField()
	min_price=models.FloatField()
	closing_price=models.FloatField()
	
	def __str__(self):
		return self.abbr		

class Plic(models.Model):
	name = models.CharField(max_length= 50)
	abbr = models.CharField(max_length= 10)
	no_of_transaction=models.IntegerField()
	traded_share=models.FloatField()
	traded_date=models.DateField(default=date.today())
	max_price=models.FloatField()
	min_price=models.FloatField()
	closing_price=models.FloatField()
	
	def __str__(self):
		return self.abbr

class Plic_live(models.Model):
	name = models.CharField(max_length= 50)
	abbr = models.CharField(max_length= 10)
	no_of_transaction=models.IntegerField()
	traded_share=models.FloatField()
	traded_date=models.DateField(default=date.today())
	traded_time = models.TimeField( auto_now_add=True, blank=True)
	max_price=models.FloatField()
	min_price=models.FloatField()
	closing_price=models.FloatField()
	
	def __str__(self):
		return self.abbr		

class Sbi(models.Model):
	name = models.CharField(max_length= 50)
	abbr = models.CharField(max_length= 10)
	no_of_transaction=models.IntegerField()
	traded_share=models.FloatField()
	traded_date=models.DateField(default=date.today())
	max_price=models.FloatField()
	min_price=models.FloatField()
	closing_price=models.FloatField()
	
	def __str__(self):
		return self.abbr

class Sbi_live(models.Model):
	name = models.CharField(max_length= 50)
	abbr = models.CharField(max_length= 10)
	no_of_transaction=models.IntegerField()
	traded_share=models.FloatField()
	traded_date=models.DateField(default=date.today())
	traded_time = models.TimeField( auto_now_add=True, blank=True)
	max_price=models.FloatField()
	min_price=models.FloatField()
	closing_price=models.FloatField()
	
	def __str__(self):
		return self.abbr		

class Scb(models.Model):
	name = models.CharField(max_length= 50)
	abbr = models.CharField(max_length= 10)
	no_of_transaction=models.IntegerField()
	traded_share=models.FloatField()
	traded_date=models.DateField(default=date.today())
	max_price=models.FloatField()
	min_price=models.FloatField()
	closing_price=models.FloatField()
	
	def __str__(self):
		return self.abbr

class Scb_live(models.Model):
	name = models.CharField(max_length= 50)
	abbr = models.CharField(max_length= 10)
	no_of_transaction=models.IntegerField()
	traded_share=models.FloatField()
	traded_date=models.DateField(default=date.today())
	traded_time = models.TimeField( auto_now_add=True, blank=True)
	max_price=models.FloatField()
	min_price=models.FloatField()
	closing_price=models.FloatField()
	
	def __str__(self):
		return self.abbr


class Shl(models.Model):
	name = models.CharField(max_length= 50)
	abbr = models.CharField(max_length= 10)
	no_of_transaction=models.IntegerField()
	traded_share=models.FloatField()
	traded_date=models.DateField(default=date.today())
	max_price=models.FloatField()
	min_price=models.FloatField()
	closing_price=models.FloatField()
	
	def __str__(self):
		return self.abbr

class Shl_live(models.Model):
	name = models.CharField(max_length= 50)
	abbr = models.CharField(max_length= 10)
	no_of_transaction=models.IntegerField()
	traded_share=models.FloatField()
	traded_date=models.DateField(default=date.today())
	traded_time = models.TimeField(auto_now_add=True, blank=True)
	max_price=models.FloatField()
	min_price=models.FloatField()
	closing_price=models.FloatField()
	
	def __str__(self):
		return self.abbr		

class Banking(models.Model):
	traded_date=models.DateField(default=date.today())
	open_price=models.FloatField()
	max_price=models.FloatField()
	min_price=models.FloatField()
	closing_price=models.FloatField()
	volume=models.BigIntegerField(default=0)

	def __str__(self):
		return ("Banking")

class DevBank(models.Model):
	traded_date=models.DateField(default=date.today())
	open_price=models.FloatField()
	max_price=models.FloatField()
	min_price=models.FloatField()
	closing_price=models.FloatField()
	volume=models.BigIntegerField(default=0)

	def __str__(self):
		return ("DevBank")		

class Finance(models.Model):
	traded_date=models.DateField(default=date.today())
	open_price=models.FloatField()
	max_price=models.FloatField()
	min_price=models.FloatField()
	closing_price=models.FloatField()
	volume=models.BigIntegerField(default=0)

	def __str__(self):
		return ("Finance")

class FloatIndex(models.Model):
	traded_date=models.DateField(default=date.today())
	open_price=models.FloatField()
	max_price=models.FloatField()
	min_price=models.FloatField()
	closing_price=models.FloatField()
	volume=models.BigIntegerField(default=0)

	def __str__(self):
		return ("FloatIndex")

class Hydropower(models.Model):
	traded_date=models.DateField(default=date.today())
	open_price=models.FloatField()
	max_price=models.FloatField()
	min_price=models.FloatField()
	closing_price=models.FloatField()
	volume=models.BigIntegerField(default=0)

	def __str__(self):
		return ("Hydropower")	
		
class Insurance(models.Model):
	traded_date=models.DateField(default=date.today())
	open_price=models.FloatField()
	max_price=models.FloatField()
	min_price=models.FloatField()
	closing_price=models.FloatField()
	volume=models.BigIntegerField(default=0)

	def __str__(self):
		return ("Insurance")		

class Hotel(models.Model):
	traded_date=models.DateField(default=date.today())
	open_price=models.FloatField()
	max_price=models.FloatField()
	min_price=models.FloatField()
	closing_price=models.FloatField()
	volume=models.BigIntegerField(default=0)

	def __str__(self):
		return ("Hotel")			

class NEPSE(models.Model):
	traded_date=models.DateField(default=date.today())
	open_price=models.FloatField()
	max_price=models.FloatField()
	min_price=models.FloatField()
	closing_price=models.FloatField()
	volume=models.BigIntegerField(default=0)

	def __str__(self):
		return ("Nepse")	

class Others(models.Model):
	traded_date=models.DateField(default=date.today())
	open_price=models.FloatField()
	max_price=models.FloatField()
	min_price=models.FloatField()
	closing_price=models.FloatField()
	volume=models.BigIntegerField(default=0)

	def __str__(self):
		return ("Others")	

class testingnews(models.Model):
	review = models.TextField()
	date = models.DateField()
						

