from DropMaker import DropMakerNP, np
from time import sleep


class Simulation:
    '''
    Simulates raindrops falling down

    `duration`:how long letting it rain in seconds

    `dropcount`:how many raindrops to produce
        use this for a fixed dropcount and variable volume 

    `rainspeed`:falling speed in m/s

    `update`:time in seconds between updates for all raindrop positions

    `volumegoal`: volume for 1 liter/m² in 1 hour
        use this for a variable dropcount and fixed volume

    '''

    def __init__(self, duration=1, dropcount=100, rainspeed=3.888888888888889, update=0.1, dropsize=1, volumegoal=None, ybound=10000, xbound=10000):
        self.duration=duration
        self.dropcount=dropcount
        self.rainspeed=rainspeed
        self.update=update
        self.dropsize=dropsize
        self.xbound=xbound
        self.ybound=ybound
        if volumegoal:
            self._set_dropcount(volumegoal,dropsize,rainspeed,xbound=xbound,ybound=ybound)

    def dropvolume(self, dropcount, dropsize, rainspeed, ybound=10000, xbound=10000, volumegoal=None):
        '''
        Returns 3 variables:

        `volume_over_full_duration`,`volume_per_second`, `volume_for_dropcount`

        All are in Liter
        '''
        #-------------------------------------------------------
        xbound_m = xbound/1000
        ybound_m = ybound/1000
        # volume in millimeter³
        dropvolume_mm3 = dropsize**3 / 2 * np.pi * 4/3
        fullvolume_mm3 = dropvolume_mm3*dropcount
        # 1000000mm³ = 1l = 1000cm³ = 1dm³ = 0.001m³
        liter = fullvolume_mm3 / 1000000
        # 1mm² = 0.01cm² = 0.000001m²
        # liter/m² in a second
        l_m2_per_sec = (liter / xbound_m) * (ybound_m/rainspeed)
        v_total = l_m2_per_sec*self.duration
        #-------------------------------------------------------
        vp = dropsize**3/2*np.pi*4/3
        # vg = vp*dropcount
        self.dcestimate = self.duration*dropcount/(ybound_m/rainspeed)
        self.vg = vp * self.dcestimate
        self.vm = self.vg/xbound



        return v_total, l_m2_per_sec, liter
    
    def _set_dropcount(self, volumegoal, dropsize, rainspeed, ybound=10000,xbound=10000):
        '''
        Sets dropcount if given a f0856
        volume in liter/m² per hour0856
        '''
        #-------------------------------------------------------
        # xbound_m = xbound/1000
        # ybound_m = ybound/1000
        # volume_per_s = volumegoal/3600
        # liter = volume_per_s * xbound_m / (ybound_m/rainspeed)
        # fullvolume_mm3 = liter*1000000
        # dropvolume_mm3 = dropsize**3 / 2 * np.pi * 4/3
        # self.dropcount = int(fullvolume_mm3/dropvolume_mm3)
        # print('')
        #-----------------------------------------------------------
        # fixed volume
        # volume in liter, meter³
        # volume_mm3 = volume*1000000
        # rainspeed_mm_per_s = rainspeed*1000
        # m = xbound/1000
        # self.dropcount = int(squaremeter*6*(volume_mm3*ybound)/(4*(dropsize**3)*np.pi*(rainspeed_mm*3600)))
        #------------------------------------------------------------------
        # rainspeed_mm = rainspeed*1000
        # dropcount = (3*volumegoal*1000000*(ybound/rainspeed_mm))/(2*dropsize**3*np.pi)
        # dropcount_per_s = dropcount/3600
        # self.dropcount = int(dropcount_per_s)
        #------------------------------------------------------------------
        vm = volumegoal*10**6
        vp = dropsize**3/2*np.pi*4/3
        t = ybound/(rainspeed*1000)
        self.dropcount = int((vm * xbound * t ) / (vp * self.duration))
        pass

    def print_estimates(self):
        '''
        Prints estimates for stats
        '''
        xbound = self.xbound
        ybound = self.ybound
        vtotal, vsecond, _ = self.dropvolume(self.dropcount,self.dropsize, self.rainspeed, xbound=xbound, ybound=ybound)
        print('Duration: ', self.duration)
        print('Raindrops: ', self.dropcount)
        print('Falling Speed: ', self.rainspeed)
        # print(f'(estimate)Total volume in Liter: {vtotal:.10f}')
        # print(f'(estimate)Liter per sec: {vsecond:.10f}')
        # # print(f'(estimate)Liter per hour: {vsecond*3600:.10f}')
        # # print(f'(estimate)Liter per hour per m² : {vsecond*3600/(xbound/1000):.10f}')
        # print(f'(estimate)Liter per hour per m² : {vsecond*3600:.10f}')
        print('new estimates')
        print(f'(estimate)Total Raindrops : {self.dcestimate:.10f}')
        print(f'(estimate)Total volume in Liter: {self.vg/10**6:.10f}')
        print(f'(estimate)Liter per m² : {self.vm/10**6:.10f}')

        print('')


    def simulate(self):
        time_resolution = int(np.ceil(1/self.update))
        xbound = self.xbound
        ybound = self.ybound

        d = DropMakerNP(self.dropcount, self.rainspeed, xbound=xbound,ybound=ybound)
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
                _, _, liter = self.dropvolume(dropsfallen, d.dropsize, self.rainspeed, xbound=d.xbound, ybound=d.ybound)
                hits = d.collider_hits
                stat = f'{pos} | Drops hitting ground: {dropsfallen:7d} | Liter: {liter:.10f} | Hits: {hits:4d} | time: {final_time:3.2f}s'
                print(stat)
                # sleep(updateintervall)
    
if __name__ == "__main__":

    #---------------------------------------------
    # to do
    # + estimate in liter for only a square meter not full bound area
    #
    #---------------------------------------------
    # sim = Simulation(dropcount=5000,update=1, duration=5, volumegoal=0.000010471975511965976)
    sim = Simulation(dropcount=5000,update=1, duration=5, xbound=1000,ybound=10000)
    sim.simulate()
