from django.contrib import admin
from .models import *
# Register your models here.


class AccountModelAdmin(admin.ModelAdmin):
	list_display = [ "id","name","account_type", "debit","credit", "balance"]
	list_display_links = [ "id","name","account_type", "debit","credit", "balance"]
	list_filter = [ "id","name","account_type", "debit","credit", "balance"]
	search_fields = [ "id","name","account_type", "debit","credit", "balance"]
	class Meta:
		model = AccountModel

admin.site.register(AccountModel, AccountModelAdmin)

	

class JournalModelAdmin(admin.ModelAdmin):
	list_display = [ "id","name","journal_type", "defualt_credit_account_id","defualt_credit_account_id"]
	list_display_links = [ "id","name","journal_type", "defualt_credit_account_id","defualt_credit_account_id"]
	list_filter = [ "id","name","journal_type", "defualt_credit_account_id","defualt_credit_account_id"]
	search_fields = [ "id","name","journal_type", "defualt_credit_account_id","defualt_credit_account_id"]
	class Meta:
		model = JournalModel

admin.site.register(JournalModel, JournalModelAdmin)

class TransactionModelAdmin(admin.ModelAdmin):
	list_display = [ "id","name","journal_id", "balance"]
	list_display_links =  [ "id","name","journal_id", "balance"]
	list_filter =  [ "id","name","journal_id", "balance"]
	search_fields =  [ "id","name","journal_id", "balance"]
	class Meta:
		model = TransactionModel

admin.site.register(TransactionModel, TransactionModelAdmin)