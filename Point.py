class Point:
    def __init__(self, x, y, artist):
        self.x = x
        self.y = y
        self.derivative = 1
        self.artist = artist

    def set_color(self, color):
        self.artist.set(facecolor = color)

    def __le__(self, obj):
        return self.x <= obj.x

    def __lt__(self, obj):
        return self.x < obj.x