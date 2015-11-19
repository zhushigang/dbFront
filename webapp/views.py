from django.shortcuts import render
from django.http import HttpResponse
from . import queries
# Create your views here.

def index(request):
    results = queries.getAllChamps()
    return HttpResponse(results)