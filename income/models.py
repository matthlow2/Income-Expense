from django.db import models
from django.utils.timezone import now
class IncomeSource(models.Model):
  sourceName = models.CharField(max_length=200, null=False)
  
class Income(models.Model):
  incomeName = models.CharField(max_length=200, null=False)
  incomeDescription = models.TextField(max_length=500, default=None, null=True)
  incomeSource = models.ForeignKey(IncomeSource, on_delete=models.CASCADE, related_name='income', null=True)
  incomeAmount = models.FloatField("incomeamouont", null=False)
  incomeDate = models.DateField(default=now)
  
  def __str__(self):
    return self.incomeName + self.incomeAmount