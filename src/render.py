from PIL import Image, ImageDraw

class Render:
    def __init__(self, width, width_padding, height):
        self.width = width
        self.height = height
        self.wp = width_padding
        self.mid_y = height // 2

    def plot_points(self, points):
        canvas = Image.new("RGB", (2*self.wp + self.width, self.height), "#FFFFFF")
        n = len(points)
        draw = ImageDraw.Draw(canvas)

        for i in range(n-1):
            a = points[i]
            b = points[i+1]
            draw.line((a[0] + self.wp, self.mid_y - a[1], b[0] + self.wp, self.mid_y - b[1]), fill=128)
        return canvas

if __name__ == "__main__":
    rend = Render(100, 50,100)
    rend.plot_points([(5,10), (45,43)])
    rend.canvas.show()
