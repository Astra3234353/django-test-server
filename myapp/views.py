from django.shortcuts import render
from django.http import HttpResponse

def hello_world(response):
  return HttpResponse("Hello World")