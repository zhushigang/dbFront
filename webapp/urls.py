from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^getChampion/?$', views.getChampion, name='getChampion'),
    url(r'^championList/?$', views.championList, name='championList'),
    url(r'^summoner/?$', views.getSummoner, name='summoner'),
    url(r'^getRecentGames/?$', views.getRecentGames, name='getRecentGames'),
    url(r'^getTeamByMember/?$', views.getTeamByMember, name='getTeamByMember'),
    url(r'^getTeam/?$', views.getTeam, name='getTeam'),
    url(r'^mostPlayed/?$', views.mostPlayed, name='mostPlayed'),
    url(r'^getFriends/?$', views.getFriends, name='getFriends'),
    url(r'^readme/?$', views.readme, name='readme'),
]