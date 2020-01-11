from django import template
from ..models import Customer, Vehicles, PurchasesModel, AssetsModel


register = template.Library()

@register.simple_tag()
def get_customer_count():
    return Customer.objects.count()

@register.simple_tag()
def get_assets_count():
    return AssetsModel.objects.count()

