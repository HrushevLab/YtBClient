import os

def startVideo(url):
    file = open('play.cmd', 'w')
    cmdStr = "cd mpv/ \nmpv --profile=V30 "+url
    file.write(cmdStr)
    file.close()
    ask = os.system("play.cmd")
    print(ask)

# startVideo('https://www.youtube.com/watch?v=B5werjS45Nc')