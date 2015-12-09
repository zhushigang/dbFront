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
    url(r'^signup/?$', views.signup, name='signup'),
    url(r'^login/?$', views.login, name='login'),
    url(r'^main/?$', views.main, name='main'),
    url(r'^logout/?$', views.logout_view, name='logout_view'),
    url(r'^addSummoner/?$', views.addSummoner, name='addSummoner'),
    url(r'^deleteSummoner/?$', views.deleteSummoner, name='deleteSummoner'),
    url(r'^addChampion/?$', views.addChampion, name='addChampion'),\
    url(r'^deleteChampion/?$', views.deleteChampion, name='deleteChampion'),
    url(r'^addItem/?$', views.addItem, name='addItem'),
    url(r'^deleteItem/?$', views.deleteItem, name='deleteItem'),
]