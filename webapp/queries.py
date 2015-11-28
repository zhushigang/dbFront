from django.db import connection
import json
import datetime

def getAllChamps():
    query ='''
        SELECT * FROM Champion
        '''
    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    results = list()
    for (id, name, title) in data:
        results.append([id,name])
    return results

def getChamp(name):
    query = '''
        SELECT title FROM Champion
        WHERE id = %d
        ''' % int(name)

    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    results = list()
    for (name,) in data:
        results.append(name)
    return results

def getSummoner(name):
    query = '''
        SELECT * FROM Summoner
        WHERE sName = '%s'
        ''' %name

    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    if len(data) == 0: return None
    (id, sName, level, icon) = data[0]
    summoner = {"id":id, "sName":sName, "level":level}
    return summoner

def getRecentGames(sid):
    query = '''
        SELECT Game.mapId, Game.creation, Game.duration, Game.version
        FROM Game
        JOIN RecentMatch
        ON MatchId = id
        WHERE RecentMatch.summonerId = %d
        ''' %int(sid)

    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    if len(data) == 0: return None
    results = list()
    for (mapId, creation, duration, version) in data:
        results.append({"mapId":mapId,\
                        "creation": datetime.datetime.fromtimestamp(int(creation) / 1e3).strftime("%Y-%m-%d %H:%M:%S"),\
                        "duration": int(duration)/60, "version": version})
    return results

def getTeamByMember(sid):
    query = '''
        SELECT Team.id, Team.tName, Team.createDate, Team.lastGameDate
        FROM Team
        JOIN TeamHas
        ON TeamId = id
        WHERE TeamHas.summonerId = %d
        ''' %int(sid)

    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    if len(data) == 0: return None
    results = list()
    for (id, tName, createDate, lastGame) in data:
        results.append({"id":id, "name": tName, \
                        "createDate": datetime.datetime.fromtimestamp(int(createDate) / 1e3).strftime("%Y-%m-%d %H:%M:%S"),\
                        "lastGame": datetime.datetime.fromtimestamp(int(lastGame) / 1e3).strftime("%Y-%m-%d %H:%M:%S"),\
                        })
    return results

def getTeam(id):
    query = '''
        SELECT Summoner.id, Summoner.sName
        FROM Summoner
        JOIN
        TeamHas
        ON
        Summoner.id = SummonerId
        WHERE TeamHas.TeamId = "%s"
        '''%id

    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    if len(data) == 0: return None
    results = list()
    for (id, name) in data:
        results.append({"id":id, "name":name})
    return results

def mostPlayed():
    query = '''
        SELECT Champion.id, cName, title FROM Champion
        JOIN (SELECT ChampionId FROM RecentChamp
        GROUP BY ChampionId
        HAVING COUNT(ChampionId) = (SELECT MAX(c)
        FROM
        (SELECT COUNT(ChampionId) as c FROM RecentChamp
        GROUP BY ChampionId)t1))t2 ON id=ChampionId
        '''

    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    if len(data) == 0: return None
    results = list()
    for (id, name, title) in results:
        results.append({"id":id, "name":name, "title":title})
    return data

def getFriends(sid):
    query = '''
        SELECT sName
        FROM Summoner
        JOIN FriendWith
        ON
        summonerId2 = Summoner.id
        WHERE
        summonerId1 = %d
        '''%int(sid)

    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    if len(data) == 0: return None
    results = list()
    for (sName,) in data:
        results.append({"name":sName})
    return results