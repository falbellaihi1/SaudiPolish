from django.shortcuts import render
from django.template.loader import get_template
import requests
from django import forms
from django.conf import settings
import datetime
from datetime import time
from django.views.generic import TemplateView
from django.views import generic
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalDeleteView, BSModalReadView
from .forms import (
	CustomerModelForm,
	VehiclesModelForm,
	EditVehiclesModelForm,
	PurchasesModel,
	PurchasesModelForm,
	AssetsModelForm,
	PackageModelForm)
from .models import (
	AssetsModel,
	Package,
	Customer,
	Vehicles)
# Create your views here.

def home(request):
	template_name = "index.html"
	customers_count = Customer.objects.all().count()
	context = {"count": customers_count}
	return render (request, template_name , context)
def data(request):
	template_name = "base.html"
	context = {'customer':Customer.objects.all().count()}
	print(context)
	return render(request, template_name,context)

######################################
#R
class CustomerList(generic.ListView):
    model = Customer
    context_object_name = 'customers'
    template_name = 'customers/list_customers.html'

class PackageList(generic.ListView):
    model = Package
    context_object_name = 'packages'
    template_name = 'packages/package_list.html'

class VehicleList(generic.ListView):
    model = Vehicles
    context_object_name = 'vehicles'
    template_name = 'vehicles/vehicle_list.html'

class AssetsList(generic.ListView):
    model = AssetsModel
    context_object_name = 'assets'
    template_name = 'asset_list.html'

class PurchasesList(generic.ListView):
    model = PurchasesModel
    context_object_name = 'purchases'
    template_name = 'purchases/purchase_list.html'

class CustomerProfileReadView(generic.DetailView):
	model = PurchasesModel
	template_name = 'customers/customer_profile.html'
	def get_context_data(self, **kwargs):
		
		contexts = super().get_context_data(**kwargs)
		a = self.object.vehicle.id
		contexts['vehicles'] = PurchasesModel.objects.filter(vehicle=a).values(
		'package__package_name', 
		'package__package_specification',
		'date', 
		'bookings',
		'payments',
		'payable',
		'vehicle__plate_num',
		'vehicle__model',
		'vehicle__make',
		'vehicle__color',
		'vehicle__mileage',
		)
		
		return contexts


#########################CUSTOMER ########################

#C- CREATE

class CustomerCreateView(BSModalCreateView):
    template_name = 'create_object.html'
    form_class = CustomerModelForm
    success_message = 'Success: Customer was created.'
    success_url = reverse_lazy('customer_list')

class PackageCreateView(BSModalCreateView):
    template_name = 'create_object.html'
    form_class = PackageModelForm
    success_message = 'Success: Package was created.'
    success_url = reverse_lazy('package_list')

class PurchaseCreateView(BSModalCreateView):
    template_name = 'create_object.html'
    form_class = PurchasesModelForm
    success_message = 'Success: asset was created.'
    success_url = reverse_lazy('customer_list')


class VehicleCreateView(BSModalCreateView):
    template_name = 'create_object.html'
    form_class = VehiclesModelForm
    success_message = 'Success: asset was created.'
    success_url = reverse_lazy('customer_list')

class AssetCreateView(BSModalCreateView):
    template_name = 'create_object.html'
    form_class = AssetsModelForm
    success_message = 'Success: asset was created.'
    success_url = reverse_lazy('assets_list')

############################################


#U update
class CustomerUpdateView(BSModalUpdateView):
    model = Customer
    template_name = 'update/update_object.html'
    form_class = CustomerModelForm
    success_message = 'Success: Customer was updated.'
    success_url = reverse_lazy('customer_list')

class PackageUpdateView(BSModalUpdateView):
    model = Package
    template_name = 'update/update_object.html'
    form_class = PackageModelForm
    success_message = 'Success: Customer was updated.'
    success_url = reverse_lazy('package_list')

class VehicleUpdateView(BSModalUpdateView):
    model = Vehicles
    template_name = 'update/update_object.html'
    form_class = VehiclesModelForm
    success_message = 'Success: Vehicle was updated.'
    success_url = reverse_lazy('vehicle_list')

class AssetUpdateView(BSModalUpdateView):
    model = AssetsModel
    template_name = 'update/update_object.html'
    form_class = AssetsModelForm
    success_message = 'Success: Asset was updated.'
    success_url = reverse_lazy('assets_list')

class PurchaseUpdateView(BSModalUpdateView):
    model = PurchasesModel
    template_name = 'update/update_object.html'
    form_class = PurchasesModelForm
    success_message = 'Success: Purchase was updated.'
    success_url = reverse_lazy('purchases_list')
############################################

#d delete

class CustomerDeleteView(BSModalDeleteView):
    model = Customer
    template_name = 'customers/delete_customer.html'
    success_message = 'Success: Customer was deleted.'
    success_url = reverse_lazy('customer_list')

class PackageDeleteView(BSModalDeleteView):
    model = Package
    template_name = 'packages/delete_package.html'
    success_message = 'Success: Customer was deleted.'
    success_url = reverse_lazy('customer_list')


class VehiclesDeleteView(BSModalDeleteView):
    model = Vehicles
    template_name = 'vehicles/delete_vehicle.html'
    success_message = 'Success: Vehicle was deleted.'
    success_url = reverse_lazy('vehicle_list')

class AssetDeleteView(BSModalDeleteView):
    model = AssetsModel
    template_name = 'assets/delete_asset.html'
    success_message = 'Success: Asset was deleted.'
    success_url = reverse_lazy('assets_list')

class PurchaseDeleteView(BSModalDeleteView):
    model = PurchasesModel
    template_name = 'purchases/delete_purchase.html'
    success_message = 'Success: Purchase was deleted.'
    success_url = reverse_lazy('purchases_list')

##############################
"""

def edit_customers(request, id = None):
	customer_object = get_object_or_404(Customer, id=id)
	form =CustomerModelForm(request.POST or None, instance=customer_object)
	context = {"form":form , "customer" :customer_object}
	if form.is_valid():
		customer_object = form.save(commit=False)
		print(customer_object)
		customer_object.save()
		#provide sucess message
		#redirect
	template_name = "editCustomer.html"
	return render(request, template_name, context)



def list_purchases(request):
	template_name = "purchases_list.html"
	#customer_object = Customer.objects.all()
	vehicle_object = Vehicles.objects.all()
	context = {"vehicles":vehicle_object}
	print(vehicle_object)
	return render(request, template_name, context)



def customers_purchases(request):
	template_name = "customers_purchases.html"
	purchases_object_all = PurchasesModel.objects.all()
	context = {"purchases" :purchases_object_all}
	return render(request, template_name, context)


def customer_profile(request, id=None):
	template_name = "customer_profile.html"

	purchase_object = get_object_or_404(Vehicles, id=id)
	print(purchase_object)
	#customer_object = get_object_or_404(Customer, id = purchase_object.vehicle.customer.id)
	orders = PurchasesModel.objects.filter(vehicle=purchase_object).values(
		'package__package_name', 
		'package__package_specification',
		'date', 
		'bookings',
		'payments',
		'payable',
		'vehicle__plate_num',
		'vehicle__model',
		'vehicle__make',
		'vehicle__color',
		'vehicle__mileage',
		)
	print(orders)

	context = {"vehicle":purchase_object, "purchases":orders}
	for i in context:
		print (i[0])
	return render(request, template_name, context)

#######################################################



def full_form(request):
	form_purchase = PurchasesModelForm(request.POST or None)
	if form_purchase.is_valid():
		form_purchase.save()
	form_customer = CustomerModelForm(request.POST or None)
	if form_customer.is_valid():
		form_customer.save()
	vehicle_form =VehiclesModelForm(request.POST or None)
	if vehicle_form.is_valid():
		vehicle_form = vehicle_form.save()
	context = {"customer_form" : form_customer, "vehicle_form":vehicle_form,"form_purchase":form_purchase }
	return render(request, "full_form.html", context )

############### vehicles ################################



def list_vehicles(request):
	template_name = "vehicles.html"
	Vehicle_object = Vehicles.objects.all()
	context = {"customer" :customer_object}
	return render(request, template_name, context)
#############################################################################
def editVehiclePopUp(request):
	instance =get_object_or_404(Vehicles)
	form =EditVehiclesModelForm(request.POST or None, instance=instance)
	return render(request, "editvehicles.html", {"form" : form})
############################################################################

def list_assets(request):
	template_name = "asset_list.html"
	asset_object = AssetsModel.objects.all()
	context ={"assets":asset_object}
	return render(request, template_name, context)



#######################TESTINGS ###############################
#wrong implementation i will get back later


def baseTemplate(request):
	template_name = "base.html"
	customer_object = Customers.objects.all()
	context = {"customer":customer_object}
	return render(request,template_name, context)"""