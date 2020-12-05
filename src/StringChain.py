from StringElement import StringElement
from Vector import Vector
from StringEnd import StringEnd

class StringChain:
    def __init__(self, pos_array, grav, spring_const, left_dyna=None, right_dyna=None):
        self.points = [StringElement(pos, grav, spring_const) for pos in pos_array]
        self.points[0] = StringEnd(pos_array[0], left_dyna)
        self.points[-1] = StringEnd(pos_array[-1], right_dyna)

        # Link up points.
        for i in range(1,len(self.points) - 1):
            self.points[i].link(self.points[i-1], self.points[i+1])

        self.points[0].link(self.points[1])
        self.points[-1].link(self.points[-2])

    def step(self, time_step):
        for point in self.points:
            point.update_acceleration()
        for point in self.points:
            point.update_velocity(time_step)
            point.update_position(time_step)


    def positions(self):
        return [point.pos.to_tuple(round=True) for point in self.points]

from render import Render

if __name__ == "__main__":
    pos = [Vector(i*10, 0) for i in range(50+1)]
    chain = StringChain(pos, Vector(0, -10), 10)

    rend = Render(100, 10, 100)

    for _ in range(5):
        chain.step(0.1)
        print(chain.positions())
        #rend.plot_points(chain.positions())
  
