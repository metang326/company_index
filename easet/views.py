from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django import forms
from . import models
from .models import product

def index(request):
	myProducts=models.product.objects.all()	
	return render(request,'easet/index.html',{'myProducts':myProducts})

	

def home(request):
    return render(request,'easet/home.html')

def aboutUS(request):
    return render(request,'easet/aboutUS.html')

def business(request):
    return render(request,'easet/business.html')

def products(request):
	myProducts=models.product.objects.all()	
	return render(request,'easet/products.html',{'myProducts':myProducts})

def job(request):
    return render(request,'easet/job.html')
    
def contactUS(request):
    return render(request,'easet/contactUS.html')