# Copyright Daniel Rastelli 2020
from Vector import Vector

class StringElement:


    def __init__(self, pos, grav, spring_const, dampening=0):
        self.left  = None
        self.right = None
        self.acc   = Vector(0,0)
        self.vel   = Vector(0,0)
        self.pos = pos # Vector representing position.
        self.grav = grav # Vector representing force of gravity.
        self.sc  = spring_const
        self.damp = dampening

    def link(self, left, right):
        self.left = left
        self.right = right

        # Calculated early for dampening, needs to be performed after linking
        self.left_extension = self.left.pos - self.pos
        self.right_extension = self.right.pos - self.pos

    def update_acceleration(self, time_step):
        # Tension to left spring
        new_le        = self.left.pos - self.pos
        f_left        = new_le.scale(self.sc)
        delta_le      = (new_le - self.left_extension).scale(1/time_step)
        f_d_left      = delta_le.scale(self.damp)
        self.left_extension = new_le

        new_re        = self.right.pos - self.pos
        f_right       = new_re.scale(self.sc)
        delta_re      = (new_re - self.right_extension).scale(1/time_step)
        f_d_right     = delta_re.scale(self.damp)
        self.right_extension = new_re

        self.acc      = f_left + f_right + self.grav + f_d_left + f_d_right

    def update_velocity(self, time_step):
        self.vel += self.acc.scale(time_step)
    
    def update_position(self, time_step):
        self.pos += self.vel.scale(time_step)