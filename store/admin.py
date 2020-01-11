from django.contrib import admin
from .models import Customer, Vehicles, Package, PurchasesModel, AssetsModel
# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
	list_display = [ "id","full_name","phone_number"]
	list_display_links = ["full_name", "phone_number"]
	list_filter = ["phone_number", "full_name"]
	search_fields = ["phone_number","full_name"]
	class Meta:
		model = Customer

admin.site.register(Customer, CustomerAdmin)


class VehiclesAdmin(admin.ModelAdmin):
	list_display = [ "id","plate_num","make", "customer"]
	list_display_links = ["plate_num", "make","customer"]
	list_filter = ["plate_num", "make", "customer"]
	search_fields = ["plate_num","make", "customer"]
	class Meta:
		model = Vehicles

admin.site.register(Vehicles, VehiclesAdmin)

class PackageAdmin(admin.ModelAdmin):
	list_display = [ "package_name","package_price","package_specification"]
	list_display_links = [ "package_name","package_price","package_specification"]
	list_filter = [ "package_name","package_price"]
	search_fields = [ "package_name","package_price"]
	class Meta:
		model = Package

admin.site.register(Package, PackageAdmin)

class PurchasesAdmin(admin.ModelAdmin):
	list_display = [ "package", "vehicle", "date", "bookings"]
	list_display_links = [ "package", "vehicle", "date", "bookings"]
	list_filter = [ "package", "vehicle", "date", "bookings"]
	search_fields = [ "package", "vehicle", "date", "bookings"]
	class Meta:
		model = PurchasesModel

admin.site.register(PurchasesModel, PurchasesAdmin)


class AseetsAdmin(admin.ModelAdmin):
	list_display = [ "asset_name", "asset_type", "asset_price", "quantity", "total_price"]
	list_display_links = [ "asset_name", "asset_type", "asset_price", "quantity", "total_price"]
	list_filter = [ "asset_name", "asset_type", "asset_price", "quantity", "total_price"]
	search_fields = [ "asset_name", "asset_type", "asset_price", "quantity", "total_price"]
	readonly_fields = ["total_price"]
	class Meta:
		model = AssetsModel

admin.site.register(AssetsModel, AseetsAdmin)





