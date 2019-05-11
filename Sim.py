from Drop import Drop
from time import sleep
import numpy as np

def simulate(time, dropcount):
    updateintervall = 0.1
    t = time
    droplist = []
    for _ in range(dropcount):
        drop = Drop(0,0,3.888888888888889)
        droplist.append(drop)
    droparray = np.array(droplist)
    

    for time in range(t):
        print(f'time: {time:2d}')
        for _ in range(10):
            for drop in droparray:
                drop.fall(t)
            droparray[0].showpos()
            sleep(updateintervall)
        

if __name__ == "__main__":
    # t = 0.1
    # d = Drop(0,0,3.888888888888889)
    # for _ in range(10):
    #     d.fall(t)
    #     d.showpos()
    #     sleep(t)
    simulate(5,1000000)