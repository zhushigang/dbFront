from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from . import queries
# Create your views here.

def index(request):
    results = queries.getAllChamps()
    context = {'results': results}
    return render(request, 'webapp/index.html', context)


def championList(request):
    results = queries.getAllChamps()
    context = {'results': results}
    return render(request, 'webapp/championList.html', context)

def getChampion(request):
    name = request.GET['id']
    results = queries.getChamp(name)
    context = {'results': results}
    return render(request, 'webapp/getChamp.html', context)

def getSummoner(request):
    cName = request.POST['sName']
    summoner = queries.getSummoner(cName)
    context = {'summoner': summoner}
    #return HttpResponse(results)
    return render(request, 'webapp/summoner.html', context)