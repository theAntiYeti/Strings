from PIL import Image, ImageDraw

def two_chx(col):
    cnvs = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    return cnvs[col // 16] + cnvs[col % 16]



class Render:
    def __init__(self, width, width_padding, height, do_blur=False, color_high='#FF0055', color_low='#00FF00'):
        self.width = width
        self.height = height
        self.wp = width_padding
        self.mid_y = height // 2
        self.blur = do_blur
        self.color = color_high
        
        # Colours for above
        self.Rl = int(color_low[1:3],16)
        self.Gl = int(color_low[3:5],16)
        self.Bl = int(color_low[5:7],16)

        self.Rh = int(color_high[1:3],16)
        self.Gh = int(color_high[3:5],16)
        self.Bh = int(color_high[5:7],16)

    def plot_points(self, points, dark_q=1, previous=None):
        if self.blur and previous:
            canvas = previous.point(lambda x: x*0.75)
        else:
            canvas = Image.new("RGB", (2*self.wp + self.width, self.height), "#000000")
        n = len(points)
        draw = ImageDraw.Draw(canvas)

        # Calculate darkened colour
        color = self.scale_color(dark_q)
        for i in range(n-1):
            a = points[i]
            b = points[i+1]
            draw.line((a[0] + self.wp, self.mid_y - a[1], b[0] + self.wp, self.mid_y - b[1]), fill=color)
        return canvas

    def scale_color(self, dark_q):
        return ('#' + two_chx(int((self.Rh * dark_q) + ((1-dark_q) * self.Rl))) + 
                    two_chx(int((self.Gh * dark_q) + ((1-dark_q) * self.Gl)))  + 
                    two_chx(int((self.Bh * dark_q) + ((1-dark_q) * self.Bl)))) 


if __name__ == "__main__":
    rend = Render(100, 50,100)
    rend.plot_points([(5,10), (45,43)])
    rend.canvas.show()
