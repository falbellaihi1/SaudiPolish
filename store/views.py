from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.template.loader import get_template
import requests
from django import forms
from django.conf import settings
import datetime
from datetime import time
from django.views.generic import TemplateView, CreateView
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
	PackageModelForm,
	ExpenseModelForm)
from .models import (
	AssetsModel,
	Package,
	Customer,
	Vehicles,
	StoreExpensesModel)

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
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
@method_decorator(login_required, name='dispatch')
class CustomerList(generic.ListView):
    model = Customer
    context_object_name = 'customers'
    template_name = 'customers/list_customers.html'
@method_decorator(login_required, name='dispatch')
class PackageList(generic.ListView):
    model = Package
    context_object_name = 'packages'
    template_name = 'packages/package_list.html'
@method_decorator(login_required, name='dispatch')
class VehicleList(generic.ListView):
    model = Vehicles
    context_object_name = 'vehicles'
    template_name = 'vehicles/vehicle_list.html'
@method_decorator(login_required, name='dispatch')
class AssetsList(generic.ListView):
    model = AssetsModel
    context_object_name = 'assets'
    template_name = 'asset_list.html'
@method_decorator(login_required, name='dispatch')
class PurchasesList(generic.ListView):
    model = PurchasesModel
    context_object_name = 'purchases'
    template_name = 'purchases/purchase_list.html'

@method_decorator(login_required, name='dispatch')
class ExpenseList(generic.ListView):
    model = StoreExpensesModel
    context_object_name = 'expenses'
    template_name = 'expenses/expense_list.html'

@method_decorator(login_required, name='dispatch')
class CustomerProfileReadView(generic.DetailView):
	model = PurchasesModel
	template_name = 'customers/customer_profile.html'
	def get_context_data(self, **kwargs):
		
		contexts = super().get_context_data(**kwargs)
		vehicle_id = self.object.vehicle.id
		contexts['vehicles'] = PurchasesModel.objects.filter(vehicle=vehicle_id).values(
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
@method_decorator(login_required, name='dispatch')
class StoreFinancialPosition(generic.ListView):
    model = PurchasesModel
    context_object_name = 'purchases'
    template_name = 'financial.html'
    


    def get_context_data(self, **kwargs):
    	context = super(StoreFinancialPosition, self).get_context_data(**kwargs)
    	context['assets'] =AssetsModel.objects.all()
    	context['expenses'] =StoreExpensesModel.objects.all()
    	pos =self.Financial()
    	context['t'] = pos
    	print(pos)
    	
    	#print(context)
    	return context
    def Financial(self):
    	assets_objects = AssetsModel.objects.all()
    	expenses_objects =StoreExpensesModel.objects.all()
    	purchase_objects = PurchasesModel.objects.all()
    	assets_total_costs = 0 # total cost of asset *quantity purchased
    	expense_total = 0
    	purchase_total = 0
    	purchase_recieveable = 0
    	for asset in assets_objects:
    		print(asset.asset_name,'-->',asset.total_price)
    		assets_total_costs = assets_total_costs + asset.total_price
    	for expense in expenses_objects:
    		expense_total = expense_total + expense.amount

    	for purchase in purchase_objects:
    		purchase_total = purchase_total + purchase.payments
    		purchase_recieveable = purchase_recieveable + abs(purchase.payable)
    
    	financial_summary = {'recivable':purchase_recieveable, 'paid':purchase_total,'expenses':expense_total,'assets':assets_total_costs}

    	return financial_summary

#########################CUSTOMER ########################

#C- CREATE
@method_decorator(login_required, name='dispatch')
class CustomerCreateView(BSModalCreateView):
    template_name = 'create_object.html'
    form_class = CustomerModelForm
    success_message = 'Success: Customer was created.'
    success_url = reverse_lazy('customer_list')
@method_decorator(login_required, name='dispatch')
class PackageCreateView(BSModalCreateView):
    template_name = 'create_object.html'
    form_class = PackageModelForm
    success_message = 'Success: Package was created.'
    success_url = reverse_lazy('package_list')
@method_decorator(login_required, name='dispatch')
class PurchaseCreateView(BSModalCreateView):
    template_name = 'create_object.html'
    form_class = PurchasesModelForm
    success_message = 'Success: asset was created.'
    success_url = reverse_lazy('customer_list')
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
        	package = form.cleaned_data['package']
        	payments = orm.cleaned_data['payments']
        	package_price = package.package_price
        	if(payments > package_price):
        		print("why??????????")
        		return
        	return HttpResponseRedirect('/success/')

@method_decorator(login_required, name='dispatch')
class VehicleCreateView(BSModalCreateView):
    template_name = 'create_object.html'
    form_class = VehiclesModelForm
    success_message = 'Success: asset was created.'
    success_url = reverse_lazy('customer_list')

class ExpenseCreateView(BSModalCreateView):
    template_name = 'create_object.html'
    form_class = ExpenseModelForm
    success_message = 'Success: asset was created.'
    success_url = reverse_lazy('expense_list')




@method_decorator(login_required, name='dispatch')
class AssetCreateView(BSModalCreateView):
	#to create assets purchased for the store 
	# this increases assets and decreases cash/bank accounts as the store owner will be paying for the assets
    template_name = 'create_object.html'
    form_class = AssetsModelForm
    success_message = 'Success: asset was created.'
    success_url = reverse_lazy('assets_list')

############################################


#U update
@method_decorator(login_required, name='dispatch')
class CustomerUpdateView(BSModalUpdateView):
    model = Customer
    template_name = 'update/update_object.html'
    form_class = CustomerModelForm
    success_message = 'Success: Customer was updated.'
    success_url = reverse_lazy('customer_list')
@method_decorator(login_required, name='dispatch')
class PackageUpdateView(BSModalUpdateView):
    model = Package
    template_name = 'update/update_object.html'
    form_class = PackageModelForm
    success_message = 'Success: Customer was updated.'
    success_url = reverse_lazy('package_list')
@method_decorator(login_required, name='dispatch')
class VehicleUpdateView(BSModalUpdateView):
    model = Vehicles
    template_name = 'update/update_object.html'
    form_class = VehiclesModelForm
    success_message = 'Success: Vehicle was updated.'
    success_url = reverse_lazy('vehicle_list')
@method_decorator(login_required, name='dispatch')
class AssetUpdateView(BSModalUpdateView):
    model = AssetsModel
    template_name = 'update/update_object.html'
    form_class = AssetsModelForm
    success_message = 'Success: Asset was updated.'
    success_url = reverse_lazy('assets_list')
@method_decorator(login_required, name='dispatch')
class PurchaseUpdateView(BSModalUpdateView):
    model = PurchasesModel
    template_name = 'update/update_object.html'
    form_class = PurchasesModelForm
    success_message = 'Success: Purchase was updated.'
    success_url = reverse_lazy('purchases_list')

class ExpenseUpdateView(BSModalUpdateView):
    model = StoreExpensesModel
    template_name = 'update/update_object.html'
    form_class = ExpenseModelForm
    success_message = 'Success: Expense was updated.'
    success_url = reverse_lazy('expense_list')
############################################

#d delete
@method_decorator(login_required, name='dispatch')
class CustomerDeleteView(BSModalDeleteView):
    model = Customer
    template_name = 'customers/delete_customer.html'
    success_message = 'Success: Customer was deleted.'
    success_url = reverse_lazy('customer_list')
@method_decorator(login_required, name='dispatch')
class PackageDeleteView(BSModalDeleteView):
    model = Package
    template_name = 'packages/delete_package.html'
    success_message = 'Success: Customer was deleted.'
    success_url = reverse_lazy('customer_list')

@method_decorator(login_required, name='dispatch')
class VehiclesDeleteView(BSModalDeleteView):
    model = Vehicles
    template_name = 'vehicles/delete_vehicle.html'
    success_message = 'Success: Vehicle was deleted.'
    success_url = reverse_lazy('vehicle_list')
@method_decorator(login_required, name='dispatch')
class AssetDeleteView(BSModalDeleteView):
    model = AssetsModel
    template_name = 'assets/delete_asset.html'
    success_message = 'Success: Asset was deleted.'
    success_url = reverse_lazy('assets_list')
@method_decorator(login_required, name='dispatch')
class PurchaseDeleteView(BSModalDeleteView):
    model = PurchasesModel
    template_name = 'purchases/delete_purchase.html'
    success_message = 'Success: Purchase was deleted.'
    success_url = reverse_lazy('purchases_list')

class ExpenseDeleteView(BSModalDeleteView):
    model = ExpenseModelForm
    template_name = 'expenses/delete_expenses.html'
    success_message = 'Success: Expense was deleted.'
    success_url = reverse_lazy('expense_list')

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