from django import forms

from .models import Customer, Vehicles, PurchasesModel, AssetsModel, Package

from datetime import date
from django.forms import widgets, SelectDateWidget
from bootstrap_modal_forms.forms import BSModalForm
from .RelatedFieldWidgetCanAdd import RelatedFieldWidgetCanAdd

"""



class Vehicles(models.Model):
	make = 		models.CharField(default ="make", max_length=100)
	model =		models.CharField(default="model", max_length=100)
	plate_num = models.CharField(default="plate number", max_length=100)
	color = 	models.CharField(default = "color", max_length=100)
	mileage =	models.CharField(default = "mi", max_length=100)
	def __unicode__(self):
		return self.plate_num + " : " + self.make
	def __str__(self):

"""



class CustomerModelForm(BSModalForm):

	class Meta:
		model = Customer
		fields = ["full_name","phone_number", "customer_discount", "email" ]
		exclude =[]
	

class VehiclesModelForm(BSModalForm):


	class Meta:
		model = Vehicles
		fields = ["make","model", "plate_num", "color", "mileage", "customer"]
		exclude =[]



class PurchasesModelForm(BSModalForm):

	class Meta:
		model = PurchasesModel
		fields = ["vehicle","package", "bookings","payments"]
		exclude =[]
		widgets = {
        'bookings': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
    }


class EditVehiclesModelForm(forms.ModelForm):
	print("editing")

	class Meta:
		model = Vehicles
		fields = ["make","model", "plate_num", "color", "mileage"]
		exclude =[]

class AssetsModelForm(BSModalForm):


	class Meta:
		model = AssetsModel
		fields = ["asset_name","asset_type", "asset_price", "quantity"]
		exclude =[]

class PackageModelForm(BSModalForm):


	class Meta:
		model = Package
		fields = ["package_name","package_specification", "package_price"]
		exclude =[]