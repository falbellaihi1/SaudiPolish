from django.db import models

# Create your models here.

class EmployeesModel(models.Model):
	contract_date = models.DateField(null=True)
	employee_name= models.CharField(default="employee name", max_length=100)
	employee_speciality = models.CharField(default="speciality", max_length=100)
	employee_wage =  models.DecimalField(max_digits=9, decimal_places=2, null = True, default=0.0)
	vacation_balance =  models.IntegerField(null = True, default=0)
	can_take_vacation = models.BooleanField(default=False)
	def __unicode__(self):
		return self.employee_name
	def __str__(self):
		return self.employee_name

#idea here!
# boolean to be set by the user for each employee as to indicate whether employee recieved salary or not
 #will be set using a "PAY button" the pay button will do the following
 # set payroll wage_paid to true, will access employees model finds the specified employee's wage and deduct it from  income model(not sure if this is the best way to implement it but for now this is the idea that might change)
#as for other variables used in payrolls can be added lator, for now emp and bool will be used.
class PayrollModel(models.Model):
	employee=models.OneToOneField(EmployeesModel, on_delete=models.CASCADE, null = True)
	wage_paid = models.BooleanField(default=False)
	def __unicode__(self):
		return self.EmployeesModel.employee_name
	def __str__(self):
		return self.EmployeesModel.employee_name


class IncomeModel(models.Model):
	sales = models.DecimalField(max_digits=9, decimal_places=2, null = True, default=0.0)
	COGS = models.DecimalField(max_digits=9, decimal_places=2, null = True, default=0.0)
	SAE = models.DecimalField(max_digits=9, decimal_places=2, null = True, default=0.0)
	depreciation =models.DecimalField(max_digits=9, decimal_places=2, null = True, default=0.0)
	VAT = models.FloatField(null = True, default=0.0)
	net_income = models.DecimalField(max_digits=9, decimal_places=2, null = True, default=0.0)


"""class IncomeStatementModel(models.Model):
	sales = models.ForeignKey(PurchasesModel,on_delete=models.CASCADE, null = True) # total amount of sales, in the case of this company is -> purchases sold to vehicles
	COGS = models.ForeignKey(AssetsModel,on_delete=models.CASCADE, null = True) # the cost of goods sold to vehicles
	gross_profit=  models.DecimalField(max_digits=9, decimal_places=2, null = True, default=0.0)
	SGA = models.DecimalField(max_digits=9, decimal_places=2, null = True, default=0.0)
	depreciation = models.DecimalField(max_digits=9, decimal_places=2, null = True, default=0.0)
	operating_profit = models.DecimalField(max_digits=9, decimal_places=2, null = True, default=0.0)
	interest =models.DecimalField(max_digits=9, decimal_places=2, null = True, default=0.0)
	EBT=models.DecimalField(max_digits=9, decimal_places=2, null = True, default=0.0) # Earnings Before Taxes (EBT)
	taxes = models.DecimalField(max_digits=9, decimal_places=2, null = True, default=0.0)
	earnings_available = models.DecimalField(max_digits=9, decimal_places=2, null = True, default=0.0)#Earnings available for common stockholders
	dividends = models.DecimalField(max_digits=9, decimal_places=2, null = True, default=0.0)
	net_income =models.DecimalField(max_digits=9, decimal_places=2, null = True, default=0.0)#owner draw
"""
"""class AccountingModel(models.Model):
	income = models.DecimalField(max_digits=9, decimal_places=2, null = True, default=0.0)
	expenses = models.DecimalField(max_digits=9, decimal_places=2, null = True, default=0.0)"""
