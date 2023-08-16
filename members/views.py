from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def members(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def alifMobi(request):
  template = loader.get_template('alifMobi.html')
  return HttpResponse(template.render())

def visa(request):
  template = loader.get_template('visa.html')
  return HttpResponse(template.render())

def salom(request):
  template = loader.get_template('salom.html')
  return HttpResponse(template.render())

def CarFinancing(request):
  template = loader.get_template('CarFinancing.html')
  return HttpResponse(template.render())

def alifShop(request):
  template = loader.get_template('alifShop.html')
  return HttpResponse(template.render())

def transfers(request):
  template = loader.get_template('transfers.html')
  return HttpResponse(template.render())

def deposits(request):
  template = loader.get_template('deposits.html')
  return HttpResponse(template.render())

def alifOnline(request):
  template = loader.get_template('alifOnline.html')
  return HttpResponse(template.render())