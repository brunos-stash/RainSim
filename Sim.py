from DropMaker import DropMakerNP, np
from time import sleep


class Simulation:
    '''
    Simulates raindrops falling down

    `duration`:how long letting it rain in seconds

    `dropcount`:how many raindrops to produce

    `rainspeed`:falling speed in m/s

    `update`:time in seconds between updates for all raindrop positions
    '''

    def __init__(self, duration=1, dropcount=100, rainspeed=3.888888888888889, update=0.1, dropsize=1):
        self.duration=duration
        self.dropcount=dropcount
        self.rainspeed=rainspeed
        self.update=update
        self.dropsize=dropsize

    def dropvolume(self, dropcount, dropsize, rainspeed, ybound=10000):
        '''
        Returns 3 variables:

        `volume_over_full_duration`,`volume_per_second`, `volume_for_dropcount`

        All are in Liter
        '''
        # volume in millimeter³
        volume = dropsize / 2 * np.pi * 4/3
        fullvolume = volume*dropcount
        liter = fullvolume / 1000000
        # milliliter = fullvolume / 1000
        ybound_m = ybound/1000
        v_per_sec = liter*rainspeed/ybound_m
        v_total = v_per_sec*self.duration
        return v_total, v_per_sec, liter
    
    def print_estimates(self):
        '''
        Prints estimates for stats
        '''
        vtotal, vsecond, _ = self.dropvolume(self.dropcount,self.dropsize, self.rainspeed)
        print('Duration: ', self.duration)
        print('Raindrops: ', self.dropcount)
        print('Falling Speed: ', self.rainspeed)
        print(f'(estimate)Total volume in Liter: {vtotal:.10f}')
        print(f'(estimate)Liter per sec: {vsecond:.10f}')
        print(f'(estimate)Liter per hour: {vsecond*3600:.10f}')

    def simulate(self):
        time_resolution = int(np.ceil(1/self.update))
        d = DropMakerNP(self.dropcount, self.rainspeed)
        self.print_estimates()
        # 1sec
        for time in range(self.duration):
            final_time = time
            # depends on update time, lower updatetime => more repetition
            for _ in range(time_resolution):
                final_time += self.update
                d.fall(time=self.update)
                pos = d.getpos()
                dropsfallen = d.dropsonground
                _, _, liter = self.dropvolume(dropsfallen, d.dropsize, d.rainspeed, ybound=d.ybound)
                hits = d.collider_hits
                stat = f'{pos} | Drops hitting ground: {dropsfallen:7d} | Liter: {liter:.10f} | Hits: {hits:4d} | time: {final_time:3.2f}s'
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
    sim = Simulation(dropcount=1000,update=1, duration=10)
    sim.simulate()
