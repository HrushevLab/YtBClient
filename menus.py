from parsePage import find_channel, findVideo

import database

def findChannel():
    name = input()
    info =find_channel(name=name)
    command = input()
    if command == "1":
        database.subscribe(info[0],info[1])
        mainMenu()
    else:
        mainMenu()

def checkSubs():
    database.checkSubs(database.connect())

def mainMenu():
    print('1) My feeds')
    print('2) Subscriber')
    print('3) Search video')
    print('4) Search channel')

    command = input()
    if command == "2":
        checkSubs()

    if command == "3":
        name = input()
        findVideo(name)

    if command == "4":
        findChannel()

# findChannel()
# checkSubs()
mainMenu()