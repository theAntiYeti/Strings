from PIL import Image, ImageDraw

class Render:
    def __init__(self, width, width_padding, height, do_blur=False, color='#FF7700'):
        self.width = width
        self.height = height
        self.wp = width_padding
        self.mid_y = height // 2
        self.blur = do_blur
        self.color = color

    def plot_points(self, points, previous=None):
        if self.blur and previous:
            canvas = previous.point(lambda x: x*0.75)
        else:
            canvas = Image.new("RGB", (2*self.wp + self.width, self.height), "#000000")
        n = len(points)
        draw = ImageDraw.Draw(canvas)

        for i in range(n-1):
            a = points[i]
            b = points[i+1]
            draw.line((a[0] + self.wp, self.mid_y - a[1], b[0] + self.wp, self.mid_y - b[1]), fill=self.color)
        return canvas

if __name__ == "__main__":
    rend = Render(100, 50,100)
    rend.plot_points([(5,10), (45,43)])
    rend.canvas.show()
