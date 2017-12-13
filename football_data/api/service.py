import memcache
import requests
import time

BASE_URL = 'http://api.football-data.org/v1/'
TIME = 24 * 60 * 60

HEADERS = dict()
HEADERS['Content-Type'] = 'application/json'
# HEADERS['X-Response-Control'] = 'minified'


class FootballService():

    @staticmethod
    def get_competition():
        url = BASE_URL + 'competitions/'
        headers = HEADERS
        r = requests.get(url, headers=headers)
        competitions = r.json()
        return competitions

    @staticmethod
    def get_teams(comp_id):
        url = BASE_URL + 'competitions/' + comp_id + '/teams'
        headers = HEADERS
        r = requests.get(url, headers=headers)
        teams = r.json()
        return teams

    @staticmethod
    def get_league_table(comp_id):
        url = BASE_URL + 'competitions/' + comp_id + '/leagueTable'
        headers = HEADERS
        r = requests.get(url, headers=headers)
        table = r.json()
        return table



# memc = memcache.Client(['127.0.0.1:11211'])
#
#
# def _set_memc(cache_key, value):
#     memc.set(cache_key, value, time=TIME)
#
#
# def get_competitions():
#     cache_key = "competitions"
#     if not memc.get("competitions"):
#         url = BASE_URL + 'competitions/'
#         headers = HEADERS
#         r = requests.get(url, headers=headers)
#         competitions = r.json()
#         _set_memc(cache_key, competitions)
#     return memc.get(cache_key)
#
#
# def get_season_competition(season):
#     cache_key = "competition_" + str(season)
#     if not memc.get(cache_key):
#         url = BASE_URL + 'competitions/?season=' + str(season)
#         headers = HEADERS
#         r = requests.get(url, headers=headers)
#         competitions = r.json()
#         _set_memc(cache_key, competitions)
#     return memc.get(cache_key)
#
#
# if __name__ == "__main__":
#     t1 = time.time()
#     comps = get_season_competition(2013)
#     t2 = time.time()

