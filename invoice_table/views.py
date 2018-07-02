from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    '''return HttpResponse("sadfsfsdfsdfsdfsdf")'''
    return render(request, 'invoice_table/index.html', {})