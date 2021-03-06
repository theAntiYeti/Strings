from Vector import Vector

class StringEnd:
    def __init__(self, pos, dynamics=None):
        self.pos = pos
        self.acc = Vector(0,0)
        self.vel = Vector(0,0)
        self.dynamics = dynamics
        self.t = 0

    def link(self, next_el):
        self.next_el = next_el

    def update_acceleration(self, k):
        pass
    
    def update_velocity(self, k):
        pass

    def update_position(self, k):
        self.t += k
        if self.dynamics:
            self.pos = self.dynamics(self.t)

    def kinetic_energy(self):
        return 0

    def stress(self):
        return 2*((self.next_el.pos - self.pos).norm_sq())**(1/2)