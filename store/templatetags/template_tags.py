from django import template
from ..models import Customer, Vehicles, PurchasesModel, AssetsModel
from django.template import Context
import datetime

register = template.Library()

@register.simple_tag()
def get_customer_count():
    return Customer.objects.count()

@register.simple_tag()
def get_assets_count():
    return AssetsModel.objects.count()


@register.simple_tag()
def get_assets_count():
    return AssetsModel.objects.count()
@register.simple_tag()
def get_paid_count():
	paid = PurchasesModel.objects.filter(payable=0.0).count()
	return paid
@register.simple_tag()
def get_bookings_count():
	today = datetime.date.today()
	#KSA WEEKDAYS
	start_week = today - datetime.timedelta(today.weekday() + 1)
	end_week = start_week + datetime.timedelta(6)
	purchases = PurchasesModel.objects.filter(bookings__range=[start_week, end_week]).count()
	print(purchases)
	return purchases

