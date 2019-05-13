import numpy as np

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
