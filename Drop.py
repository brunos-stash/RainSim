from dataclasses import dataclass
import numpy as np
import random

@dataclass
class Drop:
    x:  float
    y: float
    speed: float

    def fall(self, time=1):
        # # self.x = self.x + self.speed*time
        self.y = self.y + self.speed*time

    def pos(self):
        return (self.x, self.y)

    def showpos(self):
        # f'{value:{width}.{precision}}'
        # value is any expression that evaluates to a number
        # width specifies the number of characters used in total to display, but if value needs more space than the width specifies then the additional space is used.
        # precision indicates the number of characters used after the decimal point
        print ( f'x:{self.x:7.2f} | y:{self.y:7.2f}' )
class DropMaker:
    '''
    Contains array of drops with x, y position and speed value

    `dropcounter`:
        how man drops
    `speed`:
        y speed in meter/sec
    `xbound=100`:
        boundary 0-xbound X axis,
    `ybound=100`:
        boundary 0-ybound Y axis,
    '''
    def __init__(self, dropcounter, speed, xbound=100, ybound=100):
        # self.droparray = np.array(dtype=float)
        droplist = []
        speed = speed
        for _ in range(dropcounter):
            rx = random.randint(0, xbound*100) / 100 
            ry = random.randint(0, ybound*100) / 100 
            drop = [rx, ry, speed]
            droplist.append(drop)
        
        self.droparray = np.array(droplist, dtype=float)

    def fall(self, duration=1):
        for drop in self.droparray:
            drop[1] = drop[1] + drop[2]*duration
        # prints the first drop position of the array 
        print ( f'x:{self.droparray[0][0]:7.2f} | y:{self.droparray[0][1]:7.2f}' )


    # def pos(self):
    #     return (self.x, self.y)

    # def showpos(self):
    #     # f'{value:{width}.{precision}}'
    #     # value is any expression that evaluates to a number
    #     # width specifies the number of characters used in total to display, but if value needs more space than the width specifies then the additional space is used.
    #     # precision indicates the number of characters used after the decimal point
    #     print ( f'x:{self.x:7.2f} | y:{self.y:7.2f}' )
    
    # def get_array(self):
    #     arr = np.array([self.x, self.x, self.speed])

@dataclass
class DropNP:
    def __init__(self, x, y, speed):
        # 1000mm = 1m
        self.array = np.array([x,y,speed])
        self.x = self.array[0]
        self.y = self.array[1]
        self.speed = self.array[2]

        # array: np.array([x,y,speed], dtype=int)

    def fall(self, time=1):
        # # self.x = self.x + self.speed*time
        # self.array[1] = self.array[1] + self.array[2]*time
        self.y -= self.speed*time
        # print(self.y)
        # print(self.speed)
        # print(self.array[1])

    def getpos(self):
        return (self.x, self.y)

    def getspeed(self):
        return self.speed

    def showpos(self):
        # f'{value:{width}.{precision}}'
        # value is any expression that evaluates to a number
        # width specifies the number of characters used in total to display, but if value needs more space than the width specifies then the additional space is used.
        # precision indicates the number of characters used after the decimal point
        print ( f'x:{self.x:7.2f} | y:{self.y:7.2f}' )

class DropMakerNP:
    '''
    Contains array of drops with x, y position and speed value

    `dropcounter`:
        how man drops
    `speed`:
        y speed in meter/sec
    `xbound=10000`:
        boundary 0-xbound X axis,
        1 unit = 1 mm
        default is 10meter
    `ybound=10000`:
        boundary 0-ybound Y axis,
        1 unit = 1 mm
        default is 10meter
    '''

    def __init__(self, dropcounter, speed, xbound=10000, ybound=10000, dropsize=1):
        self.xbound = xbound
        self.ybound = ybound
        self.dropsize = dropsize
        self.droplist = np.empty(dropcounter, dtype=DropNP)
        # speed * 1000 because smallest drop will be 1 mm
        speed = speed * 1000 
        for _ in range(dropcounter):
            rx = random.randint(0, xbound) 
            ry = random.randint(0, ybound)
            # 3,8 m/s =>3800 mm/s 
            drop = DropNP(rx,ry,speed)
            self.droplist[_] = drop
        # print(self.droplist)
        
    def fall(self, time=1):
        for drop in self.droplist:
            drop.fall(time=time)
            if drop.y <= 0:
                drop.y = self.ybound
            
    def showpos(self, dropid=0):
        '''
        Prints position of the drop in `self.droplist`
        '''
        print ( f'x:{self.droplist[dropid].x/1000:7.2f}m | y:{self.droplist[dropid].y/1000:7.2f}m | speed:{self.droplist[dropid].speed/1000:5.2f}m/s' )

    def getpos(self, dropid=0):
        '''
        returns position of the drop in `self.droplist` as string
        '''
        return f'x:{self.droplist[dropid].x/1000:7.2f}m | y:{self.droplist[dropid].y/1000:7.2f}m | speed:{self.droplist[dropid].speed/1000:5.2f}m/s'

    

if __name__ == "__main__":
    from time import sleep

    updateintervall = 0.1
    duration = 1
    speed = 1 # 14 km/h
    # speed = 3.888888888888889 # 14 km/h
    dropcounter = 3
    
    print()

    d = DropMakerNP(dropcounter, speed, xbound=1, ybound=1)
    for time in range(duration):
        print(f'time:{time:3d}')
        # 1sec
        for _ in range(int(1/updateintervall)):
            d.fall()
            d.showpos()
            sleep(updateintervall)