from django.urls import path
from accounts.views import *
urlpatterns = [


#CUSTOMERS
path('login/',CustomLoginView.as_view(),name="user_login"),
#path('profile/',Profile.as_view(),name="profile"),

]