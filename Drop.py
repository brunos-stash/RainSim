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

    def fall(self, time=1):
        for drop in self.droparray:
            drop[1] = drop[1] + drop[2]*time
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



if __name__ == "__main__":
    from time import sleep
    # time
    updateintervall = 0.1
    time = 5
    speed = 3.888888888888889 # 14 km/h-
    # d = Drop(0,0,3.888888888888889)
    d = DropMaker(100, speed)

    for _ in range(10*time):
        d.fall()
        sleep(updateintervall)
    


    #     d.fall(t)
    #     d.showpos()