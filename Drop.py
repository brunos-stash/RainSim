from dataclasses import dataclass
import numpy as np

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
    def __init__(self, dropcounter, speed):
        # self.droparray = np.array(dtype=float)
        droplist = []
        x = 0
        y = 0
        speed = speed
        for _ in range(dropcounter):
            drop = [x, y, speed]
            droplist.append(drop)
        
        self.droparray = np.array(droplist, dtype=float)

    def fall(self, time=1):
        for drop in self.droparray:
        # # self.x = self.x + self.speed*time
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
    speed = 3.888888888888889 # 14 km/h
    # d = Drop(0,0,3.888888888888889)
    d = DropMaker(100000, speed)

    for _ in range(10*time):
        d.fall()
        sleep(updateintervall)
    

    #     d.fall(t)
    #     d.showpos()