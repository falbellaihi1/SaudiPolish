from django.db import models

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
	email 				= models.CharField(max_length=100)
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

class EmployeesModel(models.Model):
	employee_name= models.CharField(default="employee name", max_length=100)
	employee_speciality = models.CharField(default="speciality", max_length=100)
	employee_wage =  models.DecimalField(max_digits=9, decimal_places=2, null = True, default=0.0)
	def __unicode__(self):
		return self.employee_name
	def __str__(self):
		return self.employee_name

#idea here!
# boolean to be set by the user for each employee as to indicate whether employee recieved salary or not
 #will be set using a "PAY button" the pay button will do the following
 # set payroll wage_paid to true, will access employees model finds the specified employee's wage and deduct it from  income model(not sure if this is the best way to implement it but for now this is the idea that might change)

class PayrollModel(models.Model):
	employee=models.OneToOneField(EmployeesModel, on_delete=models.CASCADE, null = True)
	wage_paid = models.BooleanField(default=False)
	def __unicode__(self):
		return self.EmployeesModel.employee_name
	def __str__(self):
		return self.EmployeesModel.employee_name


class IncomeModel(models.Model):
	sales = models.DecimalField(max_digits=9, decimal_places=2, null = True, default=0.0)
	COGS = models.DecimalField(max_digits=9, decimal_places=2, null = True, default=0.0)
	SAE = models.DecimalField(max_digits=9, decimal_places=2, null = True, default=0.0)
	depreciation =models.DecimalField(max_digits=9, decimal_places=2, null = True, default=0.0)
	VAT = models.FloatField(null = True, default=0.0)
	net_income = models.DecimalField(max_digits=9, decimal_places=2, null = True, default=0.0)


"""class IncomeStatementModel(models.Model):
	sales = models.ForeignKey(PurchasesModel,on_delete=models.CASCADE, null = True) # total amount of sales, in the case of this company is -> purchases sold to vehicles
	COGS = models.ForeignKey(AssetsModel,on_delete=models.CASCADE, null = True) # the cost of goods sold to vehicles
	gross_profit=  models.DecimalField(max_digits=9, decimal_places=2, null = True, default=0.0)
	SGA = models.DecimalField(max_digits=9, decimal_places=2, null = True, default=0.0)
	depreciation = models.DecimalField(max_digits=9, decimal_places=2, null = True, default=0.0)
	operating_profit = models.DecimalField(max_digits=9, decimal_places=2, null = True, default=0.0)
	interest =models.DecimalField(max_digits=9, decimal_places=2, null = True, default=0.0)
	EBT=models.DecimalField(max_digits=9, decimal_places=2, null = True, default=0.0) # Earnings Before Taxes (EBT)
	taxes = models.DecimalField(max_digits=9, decimal_places=2, null = True, default=0.0)
	earnings_available = models.DecimalField(max_digits=9, decimal_places=2, null = True, default=0.0)#Earnings available for common stockholders
	dividends = models.DecimalField(max_digits=9, decimal_places=2, null = True, default=0.0)
	net_income =models.DecimalField(max_digits=9, decimal_places=2, null = True, default=0.0)#owner draw
"""
"""class AccountingModel(models.Model):
	income = models.DecimalField(max_digits=9, decimal_places=2, null = True, default=0.0)
	expenses = models.DecimalField(max_digits=9, decimal_places=2, null = True, default=0.0)"""


	
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