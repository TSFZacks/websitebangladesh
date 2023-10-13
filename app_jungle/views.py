from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Costumer_Data, CreditCardInfo

def new_jungleing(request):
    return render(request,'jungleings/new_jungleing.html')

def jungleings(request):

    data = {
        'costumerdata':Costumer_Data.objects.all(),
        'card_info': CreditCardInfo.objects.all()
    }

    return render(request,'jungleings/jungleings.html',context=data)

