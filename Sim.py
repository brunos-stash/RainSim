from Drop import DropMaker, DropMakerNP
from time import sleep
import numpy as np


def simulate(duration=1, dropcount=100, rainspeed=3.888888888888889, update=0.1, dropsize=1):
    '''
    Simulates raindrops falling down

    `duration`:how long letting it rain in seconds

    `dropcount`:how many raindrops to produce

    `rainspeed`:falling speed in m/s

    `update`:time in seconds between updates for all raindrop positions
    '''
    
    def dropvolume(dropcount, dropsize, rainspeed, ybound=10000):
        # volume in millimeter³
        volume = dropsize / 2 * np.pi * 4/3
        fullvolume = volume*dropcount
        liter = fullvolume / 1000000
        # milliliter = fullvolume / 1000
        ybound_m = ybound/1000
        v_per_sec = liter*rainspeed/ybound_m
        v_total = v_per_sec*duration
        return v_total, v_per_sec, liter
    
    def print_estimates():
        vtotal, vsecond, _ = dropvolume(dropcount,dropsize,rainspeed)
        print('Duration: ', duration)
        print('Raindrops: ', dropcount)
        print('Falling Speed: ', rainspeed)
        print(f'(estimate)Total volume in Liter: {vtotal:.10f}')
        print(f'(estimate)Liter per sec: {vsecond:.10f}')

    # update = update
    time_resolution = int(np.ceil(1/update))
    d = DropMakerNP(dropcount, rainspeed)
    print_estimates()
    # 1sec
    for time in range(duration):
        final_time = time
        for _ in range(time_resolution):
            final_time += update
            d.fall(time=update)
            # d.showpos()
            pos = d.getpos()
            dropsfallen = d.dropsonground
            _, _, liter = dropvolume(dropsfallen, dropsize, rainspeed, ybound=d.ybound)
            stat = f'{pos} | Drops hitting ground: {dropsfallen:7d} | Liter: {liter:.10f} | time: {final_time:3.2f}s'
            print(stat)
            # sleep(updateintervall)
    
if __name__ == "__main__":
    # t = 0.1
    # d = Drop(0,0,3.888888888888889)
    # for _ in range(10):
    #     d.fall(t)
    #     d.showpos()
    #     sleep(t)
    # duration = 2
    # dropcount = 100
    # speed = 3.888888888888889
    # timeit.timeit("simulate(duration, dropcount, speed)",setup="from __main__ import simulate",number=1)
    # simulate(dropcount=1000,update=0.1, duration=10, rainspeed=10)
    simulate(dropcount=1000,update=0.1, duration=10)