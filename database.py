import sqlite3




def connect():
    subs = sqlite3.connect('subs.db')
    cursor = subs.cursor()
    return cursor

def create(cursor):
    cursor.execute("CREATE TABLE IF NOT EXISTS subs("
                   "name TEXT,"
                   "link TEXT PRIMARY KEY")
    cursor.commit()

def subscribe(name, link):
    subs = sqlite3.connect('subs.db')
    cursor = subs.cursor()
    cursor.execute(f"INSERT INTO subs (name, link) VALUES ('"+name+"', '"+link+"')")
    # cursor.commit()
    subs.commit()
    print("subscribed")

def checkSubs(cursor):
    cursor.execute("SELECT * FROM subs")
    counter = 1
    records = cursor.fetchall()
    return records
    # for row in records:
    #     print(str(counter)+") " +row[1])
    #     counter = counter + 1

