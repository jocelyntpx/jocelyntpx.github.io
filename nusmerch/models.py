from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _
from datetime import date
from django.shortcuts import reverse
from django.dispatch import receiver
from django.conf import settings

# Create your models here.
class userInfo(models.Model):
	faculty_types = [
	('FASS','Arts and Social Sciences'),
	('BIZ','Business'),
	('COM','Computing'),
	('DEN','Dentistry'),
	('SDE','Design and Environment'),
	('ENG','Engineering'),
	('LAW','Law'),
	('MED','Medicine'),
	('SCI','Science'),
	]

	Campus_Residential = [
    ('TH', 'Temasek Hall'),
    ('EH', 'Eusoff Hall'),
   	('SH', 'Sheares Hall'),
   	('RH', 'Raffles Hall'),
   	('KR', 'Kent Ridge Hall'),
   	('TEM', 'Tembusu'),    	
   	('RVRC', 'Ridge View Residences'),
	('CAPT', 'College of Alice and Peter Tan'),
    ('USP', 'University Scholars Programme'),
    ('RC4', 'Residential College 4'),
    ('NIL', 'Do Not Stay On Campus'),
    ]
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField('Full Name',max_length=200)
	number = models.IntegerField('Phone Number', unique=True)
	matric = models.CharField('Matric Number',max_length=10,help_text='AXXXXXXXB', unique=True)
	email = models.EmailField('NUS Email', max_length=200, blank=False, unique=True)
	faculty = models.CharField(max_length=50,choices=faculty_types,default='FASS')
	campus_residential_type = models.CharField('Campus Residential Type',
    max_length=100, choices=Campus_Residential,
    default='NIL')
	password = models.CharField(max_length=50)
	image = models.ImageField(upload_to='media', blank=True)

	def __str__(self):
		return self.email


class Product(models.Model):
	cat = [
    ('Shirt', 'Shirt'),
    ('Outerwear', 'Outerwear'),
   	('Bottom', 'Bottom'),
   	('Laptop Accessories', 'Laptop Accessories'),
   	('Others', 'Others'),
   	]
	name = models.CharField(max_length=200,null=True)
	price = models.DecimalField(decimal_places=2,max_digits=5)
	organisation = models.CharField(max_length=200,null=True)
	category = models.CharField(max_length=200,null=True,choices=cat)
	form = models.URLField(max_length=200)
	image = models.ImageField(null=True, blank=True)

	def __str__(self):
		return self.name


class Order(models.Model):
	customer = models.ForeignKey(userInfo,on_delete=models.SET_NULL,blank=True,null=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False,null=True,blank=False)
	transaction_id = models.CharField(max_length=200,null=True)

	def __str__(self):
		return str(self.transaction_id)

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total
	

class OrderItem(models.Model):
	product = models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True)
	order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
	quantity = models.IntegerField(default=0,null=True,blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.order)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total
	
