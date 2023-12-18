from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Seller, Buyer, Product, Receipt
# Create your views here.

def sellers(request):
  mysellers = Seller.objects.all().values()
  template = loader.get_template('all_sellers.html')
  context = {
    'mysellers': mysellers,
  }
  return HttpResponse(template.render(context, request))

def buyers(request):
  mybuyers = Buyer.objects.all().values()
  template = loader.get_template('all_buyers.html')
  context = {
    'mybuyers': mybuyers,
  }
  return HttpResponse(template.render(context, request))

def products(request):
  myproducts = Product.objects.all().values()
  template = loader.get_template('all_products.html')
  context = {
    'myproducts': myproducts,
  }
  return HttpResponse(template.render(context, request))

def receipts(request):
  myreceipts = Product.objects.all().values()
  template = loader.get_template('all_receipts.html')
  context = {
    'myreceipts': myreceipts,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())


def seller_details(request, id):
  mysellers = Seller.objects.get(id=id)
  template = loader.get_template('seller_details.html')
  context = {
    'mysellers': mysellers,
  }
  return HttpResponse(template.render(context, request))

def buyer_details(request, id):
  mybuyers = Buyer.objects.get(id=id)
  template = loader.get_template('buyer_details.html')
  context = {
    'mybuyers': mybuyers,
  }
  return HttpResponse(template.render(context, request))

def product_details(request, id):
  myproducts = Product.objects.get(id=id)
  template = loader.get_template('product_details.html')
  context = {
    'myproducts': myproducts,
  }
  return HttpResponse(template.render(context, request))

def receipt_details(request, id):
  myreceipts = Receipt.objects.get(id=id)
  total_expense = myreceipts.product.price*myreceipts.quantity

  template = loader.get_template('receipt_details.html')
  context = {
    'myreceipts': myreceipts,
    'total_expense': total_expense,
  }
  return HttpResponse(template.render(context, request))

# def patients(request):
#   mypatients = Patient.objects.all().values()
#   template = loader.get_template('all_patients.html')
#   context = {
#     'mypatients': mypatients,
#   }
#   return HttpResponse(template.render(context, request))

# def patients_details(request, id):
#   mypatients = Patient.objects.get(id=id)
#   template = loader.get_template('patients_details.html')
#   context = {
#     'mypatients': mypatients,
#   }
#   return HttpResponse(template.render(context, request))


# def medical(request):
#   template = loader.get_template('medical.html')
#   return HttpResponse(template.render())
