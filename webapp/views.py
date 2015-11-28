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
    sName = request.POST['sName']
    summoner = queries.getSummoner(sName)
    context = {'summoner': summoner}
    #return HttpResponse(results)
    return render(request, 'webapp/summoner.html', context)

def getRecentGames(request):
    sid = request.GET['id']
    games = queries.getRecentGames(sid)
    context = {'games': games}
    return render(request, 'webapp/getRecentGames.html', context)

def getTeamByMember(request):
    sid = request.GET['id']
    teams = queries.getTeamByMember(sid)
    context = {'teams': teams}
    return render(request, 'webapp/getTeamByMember.html', context)

def getTeam(request):
    id = request.GET['id']
    team = queries.getTeam(id)
    context = {'team': team}
    return render(request, 'webapp/getTeam.html', context)

def mostPlayed(request):
    results = queries.mostPlayed()
    context = {"results": results}
    return render(request, 'webapp/championList.html', context)

def getFriends(request):
    sid = request.GET['id']
    friends = queries.getFriends(sid)
    context = {"friends": friends}
    return render(request, 'webapp/getFriends.html', context)

def readme(request):
    return render(request, 'webapp/README.txt')