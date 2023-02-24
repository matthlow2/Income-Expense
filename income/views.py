from django.shortcuts import render
from .models import IncomeSource, Income
import json
from django.http import JsonResponse

def income_list(request):
  if request.method == 'POST':
    search_str = json.loads(request.body).get('searchText')
    income = Income.objects.filter(
      
    )

# Create your views here.
