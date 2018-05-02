from __future__ import print_function
import sys
from PyQt5 import QtGui
import pyqtgraph as pg
import urllib.request
import requests
import scipy.ndimage as filter
import time
import matplotlib.animation as anim
import matplotlib.patches as patches
from matplotlib.path import Path
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
from matplotlib.path import Path
from matplotlib.patches import PathPatch


# contents = urllib.request.urlopen("https://kaapstone.herokuapp.com/lastdataset").read()

# contents = urllib.request.urlopen("https://kaapstone.herokuapp.com/lastdataset").read()
# print(contents[5])
# print(contents[5])

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    r = requests.get("https://kaapstone.herokuapp.com/lastdataset")
    getFromHeroku = r.text
    print(getFromHeroku)
    sensors = getFromHeroku.split(";")
    currentVoltage = ["","","","","","",""]
    for i in range(0,len(sensors)):
        currentVoltage[i] = ((sensors[i]).split("="))[1]

#pos = np.matrix('3 3.1; -2.5 3; -3.5 7.9; -2.2 -6.4; 2.9 -3; -1.9 -10.5; 0 -11.5')

#pos = np.zeros((7,2))

#pos = np.matrix([[30 31], [25 30], [-35 79], [-22 -64], [29 -30], [-19 -105], [0 -115]])

    pos = np.asarray([[30, 31], [-25, 30], [-35, 79], [-22, -64], [29, -30], [-19, -105], [0, -115]])

# print(pos)
    map = np.zeros((80*4, 240*4))

    for i in range(0,7):
    # print(currentVoltage[i])
    # print((pos[i][0] + 40) * 4)
    # print((pos[i][1] +120)*4)
        map[(pos[i][0] + 40) * 4][(pos[i][1] +120)*4] = currentVoltage[i]

        
   

    leftpad = np.zeros((10*4,240*4))
    rightpad = np.zeros((10*4,240*4))
    uppad = np.zeros((80*4,10*4))
    downpad = np.zeros((100*4,10*4))
   
    map = np.vstack((leftpad, map))
    map = np.vstack((rightpad, map))
    map = np.hstack((downpad, map))
    map = filter.gaussian_filter(map*70,40)
    print(map[100][100])
    ax1.clear()
    ax1.imshow(np.rot90(map,1))
    
    

    # im = plt.imshow(map)
    # fig.canvas.draw()
    # count = count+1
    
ani = anim.FuncAnimation(fig,animate,interval=5000)




plt.show()


# x = [0, 1, 2, 4]
# y = [4, 5, 9, 6]
# pg.plot(x,y,pen=None,symbol='o')
#pg.plot(pos, pen=None, symbol='o')
status = app.exec_()
sys.exit(status)