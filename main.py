from menus import *
import threading

e1 = threading.Event()
e2 = threading.Event()

t1 = threading.Thread(target=mainMenu, args=())
t2 = threading.Thread(target=mainMenu, args=())