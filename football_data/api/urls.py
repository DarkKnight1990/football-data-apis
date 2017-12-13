from django.conf.urls import url

from .views import get_teams, get_league_table

urlpatterns = [
    url(r'^(?P<league>[\w\d]{2,4})/teams/$', get_teams),
    url(r'^(?P<league>[\w\d]{2,4})/table/$', get_league_table)
]