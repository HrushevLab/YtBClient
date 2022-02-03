from bs4 import BeautifulSoup
import requests
from database import checkSubs, connect

# import menus
from player import startVideo


def exists(var):
    var_exists = var in locals() or var in globals()
    return var_exists

def channel_Parse(url,pageNum):
    # url = "https://vid.wxzm.sx/channel/UC7f5bVxWsm3jlZIPDzOMcAg"
    page = requests.get(url+"?page="+str(pageNum))
    page.encoding = 'utf-8'
    if page.status_code != 200:
        print(str(page.status_code) + 'ERROR')
    else:
        all_video = []
        soup = BeautifulSoup(page.text, "html.parser")
        all_video = soup.findAll('div', class_='pure-u-1 pure-u-md-1-4')
        count = 1
        for item in all_video:
            name = item.findAll('p')
            link = item.findAll('a')
            # print(link[2].get('href'))
            print(str(count)+") "+name[1].text + " | " + link[2].get('href'))
            count = count+1
        print(str(count) + ") Main menu")
        command = input()
        if command == "+":
            return 'next'

        if command != str(count):
            item = all_video[int(command) - 1]
            link = item.findAll('a')
            linkStr = link[2].get('href')
            try:
                startVideo(linkStr)
            except:
                # menus.mainMenu()
                print('123')

def find_channel(name):
    queryName = name.replace(' ','+')
    url = 'https://vid.wxzm.sx/search?q='+queryName+'+content_type%3Achannel&page=1'
    page = requests.get(url)
    page.encoding = 'utf-8'
    if page.status_code != 200:
        print(str(page.status_code) + 'ERROR')
        return ('error')
    else:
        info = []
        soup = BeautifulSoup(page.text, "html.parser")
        channelCard = soup.find('div', class_ = 'pure-u-1 pure-u-md-1-4')
        channelLink = channelCard.find('a')
        name = channelCard.findAll('p')
        info.append(name[0].text)
        link = channelLink.get('href')
        link = link[9:len(link)]
        print(link)
        info.append(link)
        print(info[0])
        print('1) Subscribe')
        print('2) Back')
        return(info)

def findVideo(name):
    queryName = name.replace(' ', '+')
    url = 'https://vid.wxzm.sx/search?q=' + queryName+"+content_type%3Avideo&page=1"
    page = requests.get(url)
    page.encoding = 'utf-8'
    if page.status_code != 200:
        print(str(page.status_code) + 'ERROR')
        return ('error')
    else:
        soup = BeautifulSoup(page.text, "html.parser")
        all_video = soup.findAll('div', class_='pure-u-1 pure-u-md-1-4')
        count = 1
        for item in all_video:
            try:
                name = item.findAll('p')
                link = item.findAll('a')
                print(str(count) + ") " + name[1].text + " | " + link[2].get('href'))
                count = count + 1
            except:
                print('123')
        print(str(count)+") Main menu")
        command = input()
        if command != str(count):
            item = all_video[int(command) - 1]
            link = item.findAll('a')
            linkStr = link[2].get('href')
            try:
                startVideo(linkStr)
            except:
                # menus.mainMenu()
                print('123')

def myFeed():
    subs = checkSubs(connect())
    for sub in subs:
        print("======================="+sub[1]+"===============================")
        url = "https://vid.wxzm.sx/channel/"+sub[0]
        channel_Parse(url,1)