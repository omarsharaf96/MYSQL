import mysql.connector
import os

def Getfiles():
    files = open("Update.txt", "r").read().split('\n')
    for f in files:
        MainSQL = open(f, "r").read()
        RunSQL(MainSQL)

def RunSQL(SQL):
    conn = mysql.connector.connect(user=os.environ['MySQL_User'], password=os.environ['MySQL_Passwords'], host='127.0.0.1')
    cursor = conn.cursor()
    try:
        cursor.execute(SQL.replace('${ENV}',os.environ['MYSQL_ENV']))
        conn.commit()
    except:
        conn.rollback()
    conn.close()

Getfiles()