from django.db import models

"""
	ACCOUNT_PAYABLE = "AP"
	ACCOUNT_RECEIVABLE = "AR"
	CASH ="CASH"
	COST_OF_GOODS_SOLD = "COGS"

"""

class AccountModel(models.Model):

	ASSETS = 'A'
	LIABILITY= 'L'
	INCOME = 'Rev'
	EXPENSE ='EXP'
	CAPITAL = 'CAP'

	""""					DEBIT	CREDIT		"""
	ACCOUNT_CHOICES =[
	(ASSETS,'Assets'), #	Increase, Decrease
	(LIABILITY,'Libility'),# Decrease, Increase
	(INCOME,'revenue'),#	Decrease, Increase
	(EXPENSE, 'Expense'),# Increase , Decrease
	(CAPITAL, 'Capital'),# Decrease, Increase

	]
	code = models.IntegerField()
	name = models.CharField(max_lenght=64)
	account_type = models.CharField(max_length=3, choices= ACCOUNT_CHOICES, default = ASSETS)
	debit = models.DecimalField(max_digits=12, decimal_places=2, null = True, default=0.0)
	credit = models.DecimalField(max_digits=12, decimal_places=2, null = True, default=0.0)
	balance  = models.DecimalField(max_digits=12, decimal_places=2, null = True, default=0.0)

class Journal(models.Model):
	SALE = 'Sale.'
	PURCHASE= 'Purchase.'
	BANK = 'Bank.'
	CASH = 'Cash.'
	GENERAL = 'General.'
	JOURNAL_CHOICES =[
	(SALE,'SALE'),
	(PURCHASE,'PURCHASE'),
	(BANK,'BANK'),
	(CASH,'CASH'),
	(GENERAL,'GENERAL')

	]
	name = models.CharField(max_lenght=64)
	journal_type = models.CharField(max_length=9, choices=JOURNAL_CHOICES, default=SALE)
	defualt_credit_account_id = models.ForeignKey(Account,  on_delete=models.CASCADE, null=True, related_name="credit_account_id")
	defualt_credit_account_id = models.ForeignKey(Account,  on_delete=models.CASCADE, null=True, related_name="debit_account_id")

class Invoice(models.Model):
	journal_id = models.ForeignKey(Journal,  on_delete=models.CASCADE, null=True, related_name="Journal_ID")
	account_id = models.ForeignKey(Account,  on_delete=models.CASCADE, null=True, related_name="Account_ID")
	number = models.CharField(max_lenght=64)
	amount  = models.DecimalField(max_digits=12, decimal_places=2, null = True, default=0.0)

class FiscalYear(models.Model):
	name = models.CharField(max_length=16, default="fiscal year")
	DateFrom = models.DateField()
	DateTo = models.DateField()

class period(models.Model):
	fiscalyeal_id=models.ForeignKey(fiscalyear,  on_delete=models.CASCADE, null=True, related_name="fiscalyear_id")

class InvoiceLine(models.Model):
	Invoice_id = models.ForeignKey(Invoice,  on_delete=models.CASCADE, null=True, related_name="Journal_ID")
	product_id = models.ForeignKey(Account,  on_delete=models.CASCADE, null=True, related_name="Account_ID")
	account_id = models.ForeignKey(Account,  on_delete=models.CASCADE, null=True, related_name="account_id")
	period_id =models.ForeignKey(Account,  on_delete=models.CASCADE, null=True, related_name="account_id")
	amount  = models.DecimalField(max_digits=12, decimal_places=2, null = True, default=0.0)


class AssetsModel(model.Models):
	ASSET_CHOICES = []
	name = models.CharField(max_length=65, default="asset name")
	asset_type = models.CharField(max_length=3, choices= ASSET_CHOICES, default = "ASSETS")
	amount  = models.DecimalField(max_digits=12, decimal_places=2, null = True, default=0.0)

class LibilitiesMode(model.Models):
	ASSET_CHOICES = []
	name = models.CharField(max_length=65, default="Libility name")
	Libility_type = models.CharField(max_length=3, choices= ASSET_CHOICES, default = "libility")
	amount  = models.DecimalField(max_digits=12, decimal_places=2, null = True, default=0.0)



