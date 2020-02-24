from django.db import models
from model_utils import Choices
# Create your models here.

# Store Module




	#Diagnoses = models.CharField(default="Diagnoses notes", max_length=500)


class Package(models.Model):
	package_name = models.CharField(default ="package", max_length=100)
	package_specification = models.CharField(default ="package", max_length=250)
	package_price = models.DecimalField(default ="0", max_digits=8, decimal_places = 2)


	def __unicode__(self):
		return self.package_name + ": "+self.package_price
	def __str__(self):
		return  self.package_name + ":" +str(self.package_price)



class Customer(models.Model):
	full_name 			= models.CharField(default="Name of Customer", max_length=100)
	phone_number 		= models.CharField(default="Number is not set", max_length=100)
	customer_discount	= models.IntegerField(default=0)
	email 				= models.EmailField(max_length=254)
	#car 				= models.ForeignKey(Vehicles, on_delete=models.CASCADE, null=True)
	#package_purchased 	= models.ForeignKey(Package, on_delete=models.CASCADE, null = True) # from what i know, this is not ness
	def __unicode__(self):
		return self.full_name
	def __str__(self):
		return self.full_name
 	#customer payment history field
	#customer qoutes history field
	#customer inspections  historyfield

class Vehicles(models.Model):
	make = 		models.CharField(default ="make", max_length=100)
	model =		models.CharField(default="model", max_length=100)
	plate_num = models.CharField(default="plate number", max_length=100)
	color = 	models.CharField(default = "color", max_length=100)
	mileage =	models.CharField(default = "mi", max_length=100)
	customer = 	models.ForeignKey(Customer,  on_delete=models.CASCADE, null=True, related_name="customer")
	def __unicode__(self):
		return self.plate_num + " : " + self.make
	def __str__(self):
		return self.plate_num +" : "+ self.make


class PurchasesModel(models.Model):
	vehicle 	= models.ForeignKey(Vehicles,on_delete=models.CASCADE, null = True)
	package 	= models.ForeignKey(Package, on_delete=models.CASCADE, null = True)
	date 		= models.DateField(auto_now=True)
	bookings 	= models.DateField()
	payments	= models.DecimalField(max_digits=6, decimal_places=2, null = True, default=0.0)
	payable		= models.DecimalField(max_digits=6, decimal_places=2, null = True, default=0.0)
	@classmethod
	def booking(self):
		return str(self.date)
	def save(self, *args, **kwargs):
		self.payable = self.package.package_price - self.payments
		super(PurchasesModel, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.vehicle.customer.full_name + ":"  + self.vehicle.plate_num + ":"  + self.package.package_name + ":" + str(self.date)
	def __str__(self):
		return self.vehicle.customer.full_name + ":"  + self.vehicle.plate_num + ":" + self.package.package_name + ":" + str(self.date)







class AssetsModel (models.Model):
	asset_name = models.CharField(default="asset", max_length=100)
	asset_type = models.CharField(default="asset", max_length=100)
	asset_price = models.DecimalField(max_digits=9, decimal_places=2, null = True, default=0.0)
	quantity = models.DecimalField(max_digits=3, decimal_places=1, null = True, default=0)
	total_price = models.DecimalField(max_digits=9, decimal_places=2, null = True, default=0.0)
	def save(self, *args, **kwargs):
		self.total_price = self.asset_price * self.quantity
		super(AssetsModel, self).save(*args, **kwargs)

class StoreExpensesModel(models.Model):
	expenses_choices = Choices(
        ("Food","Food Expenses"),
        ("Needs", "Store Needs"),  
        ("Advanced Payment", "Advanced Payment"),  
        ("Salaries", "Salaries"),
        ("Other", "Other"), 
       
    )
	amount = models.DecimalField(max_digits=9, decimal_places=2, null = True, default=0.0)
	expense_type = models.CharField( 
        max_length = 20, 
        choices = expenses_choices, 
        default = 'Food'
        )
	description = models.TextField(default="", blank=True)




""""
- prodct line
	* products available (packages)
		-desctiptionP

"""


	
#class Orders(models.Model):

	#customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
	#package_purchased = models.OneToOneField(Package, on_delete=models.CASCADE)

	#def __unicode__(self):
	#	return self.id 
	#def __str__(self):
	#	return  self.id



# this will be moved to another module

#	class Purchases(models.Model):
#	purchase_price = models.CharField(default = "0", max_length=25)
#	purchased_item = models.CharField(default="description", max_length=100)
	#TO ADD MORE LATER WHEN DESIGN IS REVISED