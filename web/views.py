from django.shortcuts import render
from django.http import JsonResponse
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt
from web.models import User, Expense, Income, Token
from datetime import datetime
# Create your views here.

@csrf_exempt
def submit_expense(request):
    #TODO;valitaion fake amout , validation fake user and valitaion fake ...

    this_token = request.POST['token']
    this_user = User.objects.filter(token__token = this_token).get()
    if 'date' not in request.POST:
        now =  datetime.now()

    Expense.objects.create(user = this_user,date = now, amount =request.POST['amount'], text = request.POST['text'])
    return JsonResponse({
        "status" : "O.K",
     },encoder=JSONEncoder)

def submit_income(request):
    #TODO;valitaion fake amout , validation fake user and valitaion fake ...
    
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token = this_token).get()
    if 'date' not in request.POST:
        now =  datetime.now()

    Income.objects.create(user = this_user,date = now, amount =request.POST['amount'], text = request.POST['text'])
    return JsonResponse({
        "status" : "O.K",
     },encoder=JSONEncoder)