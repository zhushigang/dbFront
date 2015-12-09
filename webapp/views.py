from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from django import forms
import hashlib
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
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

def signup(req):
  if (req.method == "POST" and
      all(x in req.POST and req.POST[x] != "" for x in
      ("email", "password", "password2", "last", "first"))):
    email = req.POST['email']
    password1 = req.POST['password']
    password2 = req.POST['password2']
    if forms.EmailField().clean(email) and password1==password2:
      new_user = User.objects.create_user(email, email, password1)
      new_user.first_name = req.POST['first']
      new_user.last_name = req.POST['last']
      new_user.save()
      return redirect('main')
    last = req.POST['last']
  return render(req, 'webapp/signup.html', {})

def login(req):
  if req.method == "POST":
    if "username" in req.POST and "password" in req.POST:
      uname = req.POST['username']
      password = req.POST['password']
      user = auth.authenticate(username=uname, password=password)
      if user is not None and user.is_active:
        auth.login(req, user)
        return redirect(req.GET['next'] if 'next' in req.GET else 'main')
    messages.warning(req, 'Username and password did not match.')
  return render(req, 'webapp/login.html', {})

@login_required
def main(req):
    return render(req, 'webapp/main.html', {})

@login_required
def addSummoner(req):
    if req.method == "POST":
        if "summoner" in req.POST:
            sName = req.POST['summoner']
            level = req.POST['level']
            id = int(hashlib.sha1(sName).hexdigest(), 16) % 10**8
            queries.addSummoner(sName, level, id, 0)
    return redirect("main")

@login_required
def deleteSummoner(req):
    if req.method == "POST":
        if "summoner" in req.POST:
            sName = req.POST['summoner']
            queries.deleteSummoner(sName)
    return redirect("main")

@login_required
def addChampion(req):
    if req.method =="POST":
        if "champion" in req.POST:
            cName = req.POST['champion']
            title = req.POST['title']
            id = int(hashlib.sha1(cName).hexdigest(), 16) % 10**3
            queries.addChampion(cName, title, id)
    return redirect("main")

@login_required
def deleteChampion(req):
    if req.method =="POST":
        if "champion" in req.POST:
            cName = req.POST['champion']
            queries.deleteChampion(cName)
    return redirect("main")

@login_required
def addItem(req):
    if req.method =="POST":
        if "item" in req.POST:
            iName = req.POST['item']
            description = req.POST['description']
            itemGroup = req.POST['group']
            id = int(hashlib.sha1(iName).hexdigest(), 16) % 10**4
            queries.addItem(iName, description, itemGroup, id)
    return redirect("main")

@login_required
def deleteItem(req):
    if req.method == "POST":
        if "item" in req.POST:
            iName = req.POST['item']
            queries.deleteItem(iName)
    return redirect("main")

@login_required
def logout_view(request):
    logout(request)
    return redirect('index')