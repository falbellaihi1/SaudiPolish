from django.contrib import admin

# Register your models here.
from .models import *
# Register your models here.

class EmployeesModelAdmin(admin.ModelAdmin):
	list_display = [ "id","contract_date","employee_name", "employee_speciality", "employee_wage", "vacation_balance", "can_take_vacation"]
	list_display_links = [ "id","employee_name"]
	list_filter = [ "id","contract_date","employee_name", "employee_speciality", "employee_wage", "vacation_balance", "can_take_vacation"]
	search_fields = [ "id","contract_date","employee_name", "employee_speciality", "employee_wage", "vacation_balance", "can_take_vacation"]
	class Meta:
		model = EmployeesModel

admin.site.register(EmployeesModel, EmployeesModelAdmin)



class PayrollModelAdmin(admin.ModelAdmin):
	list_display = [ "id","employee","wage_paid"]
	list_display_links = [ "id","employee","wage_paid"]
	list_filter = [ "id","employee","wage_paid"]
	search_fields = [ "id","employee","wage_paid"]
	class Meta:
		model = PayrollModel

admin.site.register(PayrollModel, PayrollModelAdmin)

class IncomeModelAdmin(admin.ModelAdmin):
	list_display = [ "id","sales","COGS", "SAE", "depreciation", "VAT"]
	list_display_links = [ "id","sales","COGS", "SAE", "depreciation", "VAT"]
	list_filter = [ "id","sales","COGS", "SAE", "depreciation", "VAT"]
	search_fields = [ "id","sales","COGS", "SAE", "depreciation", "VAT"]
	class Meta:
		model = IncomeModel

admin.site.register(IncomeModel, IncomeModelAdmin)