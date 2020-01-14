from django import forms

from .models import *

from datetime import date
from django.forms import widgets, SelectDateWidget
from bootstrap_modal_forms.forms import BSModalForm


class EmployeesModelForm(BSModalForm):

	class Meta:
		model = EmployeesModel
		fields = ["contract_date","employee_name","employee_speciality", "employee_wage", "vacation_balance" ]
		exclude =[]
		widgets = {
        'contract_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),}

