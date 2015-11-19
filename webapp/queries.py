from django.db import connection

def getAllChamps():
    query ='''
        SELECT * FROM Champion
        '''
    cursor = connection.cursor()
    cursor.execute(query)
    return cursor.fetchall()