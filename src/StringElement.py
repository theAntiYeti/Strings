# Copyright Daniel Rastelli 2020
from Vector import Vector

class StringElement:


    def __init__(self, pos, grav, spring_const):
        self.left  = None
        self.right = None
        self.acc   = Vector(0,0)
        self.vel   = Vector(0,0)
        self.pos = pos # Vector representing position.
        self.grav = grav # Vector representing force of gravity.
        self.sc  = spring_const

    def link(self, left, right):
        self.left = left
        self.right = right

    def update_acceleration(self):
        # Tension to left spring
        dist_to_left  = self.left.pos - self.pos
        f_left        = dist_to_left.scale(self.sc)
        
        dist_to_right = self.right.pos - self.pos
        f_right       = dist_to_right.scale(self.sc)

        self.acc      = f_left + f_right + self.grav

    def update_velocity(self, time_step):
        self.vel += self.acc.scale(time_step)
    
    def update_position(self, time_step):
        self.pos += self.vel.scale(time_step)