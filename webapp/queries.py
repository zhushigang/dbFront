from django.db import connection
import json

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