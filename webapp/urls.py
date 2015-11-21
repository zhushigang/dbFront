from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^getChampion/?$', views.getChampion, name='getChampion'),
    url(r'^championList/?$', views.championList, name='championList'),
    url(r'^summoner/?$', views.getSummoner, name='summoner')
]