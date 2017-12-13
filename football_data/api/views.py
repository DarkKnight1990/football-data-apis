import time

from django.core.cache import cache
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .service import FootballService


def _competitions():
    cache_key = 'competition'
    cache_time = 24 * 60 * 60
    data = cache.get(cache_key)

    if not data:
        data = FootballService.get_competition()
        cache.set(cache_key, data, cache_time)
    return data


def _competition_id(league):
    comp_id = ''
    competitions = _competitions()
    for competition in competitions:
        if competition['league'] == league:
            comp_id = competition['id']
            comp_id = str(comp_id)
            break
    return comp_id


@api_view(['GET'])
def get_teams(request, league):
    t1 = time.time()
    league = str(league)
    cache_key = league + '_teams'
    cache_time = 24 * 60 * 60

    comp_id = _competition_id(league)
    league_teams = cache.get(cache_key)

    if not league_teams:
        if comp_id:
            league_teams = FootballService.get_teams(comp_id)
            cache.set(cache_key, league_teams, cache_time)

    t2 = time.time()
    print(t2-t1)
    return Response(league_teams, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_league_table(request, league):
    t1 = time.time()
    league = str(league)
    cache_key = league + '_table'
    cache_time = 24 * 60 * 60

    comp_id = _competition_id(league)
    league_table = cache.get(cache_key)

    if not league_table:
        if comp_id:
            league_table = FootballService.get_league_table(comp_id)
            cache.set(cache_key, league_table, cache_time)
    t2 = time.time()
    print(t2-t1)
    return Response(league_table, status=status.HTTP_200_OK)
