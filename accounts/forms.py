
from django import forms

from .models import *

from datetime import date
from django.forms import widgets, SelectDateWidget
from bootstrap_modal_forms.forms import BSModalForm

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
class UserLoginForm(BSModalForm):
	class Meta:
		model = MyUser
		fields = ['username', 'password']
		exclude =[]