from django.db import models
from django.utils.timezone import now

class ExpenseSource(models.Model):
  expenseName = models.CharField(max_length=200, null=False)

class Expense(models.Model):
  expenseName = models.CharField(max_length=200, null=False)
  expenseDescription = models.TextField(max_length=500, default=None, null=True)
  expenseSource = models.ForeignKey(ExpenseSource, on_delete=models.CASCADE, related_name='expense', null=True)
  expenseAmount = models.FloatField('expenseamount', null=False)
  expenseDate = models.DateField(default=now)
  
  def __str__(self):
    return self.expenseName + self.expenseAmount