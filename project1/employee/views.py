from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection as con
# Create your views here.
from . import forms

def index(reqeust):
    return HttpResponse("<p>welcome django application employee</p>")

def employeelist(request):
    ob=forms.sample()
    return render(request,"employeelist.html",{'form':ob})
