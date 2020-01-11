"""bstworkshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from store.views import *

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', home),
    path('index/', home),
    #CUSTOMERS
    path('customer/list',CustomerList.as_view(),name="customer_list"),
    path('customer/create', CustomerCreateView.as_view(), name='customer_create'),
    path('customer/update/<int:pk>', CustomerUpdateView.as_view(), name='update_customer'),
    path('customer/delete/<int:pk>', CustomerDeleteView.as_view(), name='delete_customer'),
    #VEHICLES
    path('vehicle/list',VehicleList.as_view(),name="vehicle_list"),
    path('vehicle/create', VehicleCreateView.as_view(), name = "vehicle_create"),
    path('vehicle/update/<int:pk>', VehicleUpdateView.as_view(), name='update_vehicle'),
    path('vehicle/delete/<int:pk>', VehiclesDeleteView.as_view(), name='delete_vehicle'),
      #Packages
    path('package/list',PackageList.as_view(),name="package_list"),
    path('package/create', PackageCreateView.as_view(), name = "package_create"),
    path('package/update/<int:pk>', PackageUpdateView.as_view(), name='update_package'),
    path('package/delete/<int:pk>', PackageDeleteView.as_view(), name='delete_package'),
    #ASSETS
    path('assets/list', AssetsList.as_view(), name='assets_list'),
    path('assets/create', AssetCreateView.as_view(), name='asset_create'),
    path('asset/update/<int:pk>', AssetUpdateView.as_view(), name='update_asset'),
    path('asset/delete/<int:pk>', AssetDeleteView.as_view(), name='delete_asset'),
    #PURCHASES
    path('purchase/list',PurchasesList.as_view(),name='purchases_list'),
    path('purchase/create', PurchaseCreateView.as_view(), name = "purchase_create"),
    path('purchase/update/<int:pk>', PurchaseUpdateView.as_view(), name='update_purchase'),
    path('purchase/delete/<int:pk>', PurchaseDeleteView.as_view(), name='delete_purchase'),
    #PRIFLE LINK
    path('profile/<int:pk>', CustomerProfileReadView.as_view(), name='customer_profile'),

]
# ( 
#     # home,
#     # CustomerList,
#     # customers_purchases,
#     # customer_profile,
#     # AssetCreateView,
#     # CustomerCreateView,
#     # PurchaseCreateView,
#     # VehicleCreateView,
#     # CustomerDeleteView,
#     # CustomerUpdateView,
#     # VehicleList,
#     # VehiclesDeleteView,
#     # VehicleUpdateView,
#     # AssetsList,
#     # AssetUpdateView,
#     # AssetDeleteView,
#     # PurchaseUpdateView,
#     # PurchaseDeleteView,
#     # PurchasesList,
#     # CustomerProfileReadView)