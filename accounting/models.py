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
	ACCOUNTS_RECEVIABLE ='AR'

	""""					DEBIT	CREDIT		"""
	ACCOUNT_CHOICES =[
	(ASSETS,'Assets'), #	Increase, Decrease
	(LIABILITY,'Libility'),# Decrease, Increase
	(INCOME,'revenue'),#	Decrease, Increase
	(EXPENSE, 'Expense'),# Increase , Decrease
	(CAPITAL, 'Capital'),# Decrease, Increase
	(ACCOUNTS_RECEVIABLE, 'Accounts Receivable')

	]
	name = models.CharField(max_length=64)
	account_type = models.CharField(max_length=3, choices= ACCOUNT_CHOICES, default = ASSETS)
	debit = models.DecimalField(max_digits=12, decimal_places=2, null = True, default=0.0)
	credit = models.DecimalField(max_digits=12, decimal_places=2, null = True, default=0.0)
	balance  = models.DecimalField(max_digits=12, decimal_places=2, null = True, default=0.0)

class JournalModel(models.Model):
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
	name = models.CharField(max_length=64)
	journal_type = models.CharField(max_length=9, choices=JOURNAL_CHOICES, default=SALE)

	defualt_credit_account_id = models.ForeignKey(AccountModel,  on_delete=models.CASCADE, null=True, related_name="credit_account_id")
	defualt_credit_account_id = models.ForeignKey(AccountModel,  on_delete=models.CASCADE, null=True, related_name="debit_account_id")

"""
a customer who owes 500 for car detail is automatically stored in account receivable once vehicle/purchase is created 
a transaction model will hold information about purchases initialized by the user and is automatically created
transaction should atuomatically creats journal and provide journal with the name of whats the transaction and the balance, and what is the type of account that is debited/credited

a journal model  should provide account with the information needed to adjust the balance for every transaction that occured 

"""
class TransactionModel(models.Model):
	#code = models.IntegerField() #auto generated
	name = models.CharField(max_length=64)
	journal_id = models.ForeignKey(JournalModel,  on_delete=models.CASCADE, null=True, related_name="journal_id_transaction") #will choose for example what account to debit from types defined in journal ex: CASH
	balance = models.DecimalField(max_digits=12, decimal_places=2, null = True, default=0.0)

class Invoice(models.Model):
	journal_id = models.ForeignKey(JournalModel,  on_delete=models.CASCADE, null=True, related_name="Journal_id_invoice")
	account_id = models.ForeignKey(AccountModel,  on_delete=models.CASCADE, null=True, related_name="account_id_invoice")
	number = models.CharField(max_length=64)
	amount  = models.DecimalField(max_digits=12, decimal_places=2, null = True, default=0.0)

class FiscalYear(models.Model):
	name = models.CharField(max_length=16, default="fiscal year")
	DateFrom = models.DateField()
	DateTo = models.DateField()

class period(models.Model):
	fiscalyeal_id=models.ForeignKey(FiscalYear,  on_delete=models.CASCADE, null=True, related_name="fiscalyear_id")





class AssetsModel(models.Model):
	ASSET_CHOICES = []
	name = models.CharField(max_length=65, default="asset name")
	asset_type = models.CharField(max_length=3, choices= ASSET_CHOICES, default = "ASSETS")
	amount  = models.DecimalField(max_digits=12, decimal_places=2, null = True, default=0.0)

class LibilitiesMode(models.Model):
	ASSET_CHOICES = []
	name = models.CharField(max_length=65, default="Libility name")
	Libility_type = models.CharField(max_length=3, choices= ASSET_CHOICES, default = "libility")
	amount  = models.DecimalField(max_digits=12, decimal_places=2, null = True, default=0.0)



