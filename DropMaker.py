from Drop import DropNP, np
import Intersection
import random

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

    def __init__(self, dropcounter, rainspeed, xbound=10000, ybound=10000, dropsize=1):
        self.xbound = xbound
        self.ybound = ybound
        self.dropsize = dropsize
        self.droplist = np.empty(dropcounter, dtype=DropNP)
        self.dropsonground = 0
        # speed * 1000 because smallest drop will be 1 mm
        self.rainspeed = rainspeed * 1000
        
        # defining a line segment for drop colliding
        # 1m wide and 1m tall
        # start point
        self.collider_a = (4000, 4000)
        # endpoint
        self.collider_b = (5000, 4000)
        self.collider_hits = 0

        for _ in range(dropcounter):
            rx = random.randint(0, xbound) 
            ry = random.randint(0, ybound)
            # 3,8 m/s =>3800 mm/s 
            drop = DropNP(rx,ry,self.rainspeed)
            self.droplist[_] = drop
        # print(self.droplist)
        
    def fall(self, time=1):
        for drop in self.droplist:
            start_point = drop.getpos()
            drop.fall(time=time)
            end_point = drop.getpos()
            self.collision_test(start_point, end_point)
            if drop.y <= 0:
                drop.y = self.ybound + drop.y
                self.countdrops()
            
    def showpos(self, dropid=0):
        '''
        Prints position of the drop in `self.droplist`
        '''
        print ( f'x:{self.droplist[dropid].x/1000:7.2f}m | y:{self.droplist[dropid].y/1000:7.2f}m | speed:{self.droplist[dropid].speed/1000:5.2f}m/s' )

    def getpos(self, dropid=0):
        '''
        returns position of the drop with the given id in `self.droplist` as string

        `"x:   6.30m | y:   2.22m | speed: 3.89m/s"`
        '''
        return f'x:{self.droplist[dropid].x/1000:7.2f}m | y:{self.droplist[dropid].y/1000:7.2f}m | speed:{self.droplist[dropid].speed/1000:5.2f}m/s'

    def countdrops(self):
        self.dropsonground += 1
    
    def collision_test(self, start_point, end_point):
        '''
        returns if path of drop collided with `self.collider_a` and `self.collider_b`

        c and d should be `tuple` or `list`:
            (x,y) or [x,y]
        '''
        start_x = int(start_point[0])
        start_y = int(start_point[1])
        end_x = int(end_point[0])
        end_y = int(end_point[1])

        start_point = (start_x,start_y)
        end_point = (end_x,end_y)
        # in case a drop gets reset from ground to top so doesnt count as a hit
        if start_point[1] < end_point[1]:
            return False

        if Intersection.closed_segment_intersect(self.collider_a, self.collider_b, start_point, end_point):
            self.collider_hits += 1 


    

if __name__ == "__main__":
    from time import sleep

    updateintervall = 0.1
    duration = 1
    speed = 1 # 14 km/h
    # speed = 3.888888888888889 # 14 km/h
    dropcounter = 3
    
    print()

    dropmaker = DropMakerNP(dropcounter, speed, xbound=1, ybound=1)
    c = (4000,5000)
    d = (4000,5000)
    Intersection.closed_segment_intersect(dropmaker.collider_a, dropmaker.collider_b, c,d)
    for time in range(duration):
        print(f'time:{time:3d}')
        # 1sec
        for _ in range(int(1/updateintervall)):
            dropmaker.fall()
            dropmaker.showpos()
            sleep(updateintervall)