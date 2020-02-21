from django.urls import path
from store.views import *

urlpatterns = [

path('', home, name="home"),
path('index/', home, name="index"),
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

#EXPENSES LINKES
path('expense/list', ExpenseList.as_view(), name='expense_list'),
path('expense/create', ExpenseCreateView.as_view(), name='expense_create'),
path('expense/update/<int:pk>', ExpenseUpdateView.as_view(), name='update_expense'),
path('expense/delete/<int:pk>', ExpenseDeleteView.as_view(), name='delete_expense'),

path('financial/list', StoreFinancialPosition.as_view(), name='financial'),
#path('transaction/create', TransactionCreation.as_view(), name='transaction_create'),
#path("transactions/create/purchase/<int:purchase_pk>/",TransactionCreateViewPass.as_view(),name="transactions_create_purchase"),
#path("transactions/create/assets/<int:asset_pk>/",TransactionCreateViewPass.as_view(),name="transactions_create_asset")
 
]