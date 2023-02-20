from django.db import models

class Income(models.Model):
  incomeName = models.CharField(max_length=200, null=False)
  incomeDescription = models.CharField(max_length=500, default=None, null=True)
  incomeAmount = models.PositiveIntegerField("amouont", null=False)
  incomeDate = models.DateField()
  
  def __str__(self):
    return self.item_name + self.amount