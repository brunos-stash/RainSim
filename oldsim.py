from time import time
from Sim import simulate as simulateNP
from Drop import Drop, DropMaker, DropMakerNP

def simulate(duration, dropcount, rainspeed):
    updateintervall = 0.1
    # droplist = []
    # for _ in range(dropcount):
    #     drop = Drop(0,0,3.888888888888889)
    #     droplist.append(drop)
    # droparray = np.array(droplist)
    
    # for time in range(duration):
    #     print(f'time: {time:2d}')
    #     for _ in range(10):
    #         for drop in droparray:
    #             drop.fall(duration)
    #         droparray[0].showpos()
    #         sleep(updateintervall)
        
    d = DropMaker(dropcount, rainspeed)

    for time in range(duration):
        print(f'time:{time:3d}')
        # 1sec
        for _ in range(int(1/updateintervall)):
            d.fall()
            # sleep(updateintervall)


def oldsimulate(duration, dropcount, rainspeed):
    '''
    Simulate using standard python class and list for comparison with the new `simulate` which uses
    numpy array 
    '''
    updateintervall = 0.1
    droplist = []
    for _ in range(dropcount):
        drop = Drop(0,0,rainspeed)
        droplist.append(drop)
    # droparray = np.array(droplist)
    
    for time in range(duration):
        print(f'time: {time:2d}')
        for _ in range(10):
            for drop in droplist:
                drop.fall(duration)
            droplist[0].showpos()
            # sleep(updateintervall)

if __name__ == "__main__":
    duration = 5
    dropcount = 100000
    speed = 3.888888888888889
    
    start2 = time()
    oldsimulate(duration, dropcount, speed)
    end2 = time()
    
    start = time()
    simulate(duration, dropcount, speed)
    end = time()
    
    start3 = time()
    simulateNP(duration, dropcount, speed)
    end3 = time()
    
    print(f'time taken oldsimulate:{end2-start2}')
    print(f'time taken simulate:{end-start}')
    print(f'time taken simulateNP:{end3-start3}')