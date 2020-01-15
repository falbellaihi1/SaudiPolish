from django.shortcuts import render


from django.urls import reverse_lazy
from django.views import generic

from bootstrap_modal_forms.generic import (BSModalLoginView,
                                           BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)

from .forms import UserLoginForm

# Create your views here.


class CustomLoginView(BSModalLoginView):
    authentication_form = UserLoginForm
    template_name = 'login.html'
    success_message = 'Success: You were successfully logged in.'
    success_url = reverse_lazy('index')