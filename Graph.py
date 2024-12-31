import matplotlib.pyplot as plt
from matplotlib.backend_bases import MouseButton
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from Point import Point
from Maths import *

class Graph:

    def __init__(self, plotframe, point_pos_text, derivative_input):

        #poits de controle (point rouge)
        self.points = []
        self.point_map = {}
        #tous les points qui composent la courbe (utile pour les difference finies)
        self.total_points = []

        self.point_pos_text = point_pos_text
        self.derivative_input = derivative_input
        self.selected = None

        self.fig, self.ax = plt.subplots()

        plt.connect('button_press_event', self.on_click)
        plt.connect('pick_event', self.on_point_click)
        derivative_input.bind('<Return>', self.on_derivative_input_changed)

        self.ax.set_title("Curve Generator", fontsize=20, pad=20, color="white")
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("y")
        self.ax.xaxis.label.set_color("white")
        self.ax.yaxis.label.set_color("white")
        self.ax.tick_params(axis='x', colors='white')
        self.ax.tick_params(axis='y', colors='white')
        self.ax.set(xlim=(0, 100), ylim=(-10, 10))
        self.ax.locator_params(axis='x', nbins=20)
        self.ax.locator_params(axis='y', nbins=20)
        self.fig.patch.set_facecolor("#222f3e")
        self.ax.grid(True)
        self.canvas = FigureCanvasTkAgg(self.fig, master=plotframe)
        self.canvas.get_tk_widget().grid(column=0, row=1, pady=10, padx=10, sticky="nsew")

        self.canvas.draw()

    def update(self):
        self.canvas.draw()

    def segment(self, point1: Point, point2: Point, prime1: float, prime2: float):
        list_x = []
        list_y = []
        for i in range(0, 100):
            x = point1.x * (1 - i / 100) + point2.x * i / 100
            y = hermite((point1.x, point1.y), (point2.x, point2.y), prime1, prime2, x)

            list_x.append(x)
            list_y.append(y)
            self.total_points.append((x, y))
        self.ax.plot(list_x, list_y, color="blue")

    def draw_curve(self):
        #supprimer touts les segments existants
        for plot in self.ax.lines:
            plot.remove()

        #dessiner les tangentes
        for point in self.points:
            self.draw_tan(point, point.derivative)

        for point in range(len(self.points)-1):
            self.segment(self.points[point], self.points[point+1], self.points[point].derivative, self.points[point+1].derivative)
        self.update()

    def draw_tan(self, point : Point, prime : float):
            l = 10
            if prime == 0:
                dx = l / 2
            else:
                dx = (l / 2) / (2 * (sqrt(1 + prime * prime))) #vecteur normalise de la tangente sqrt(1 + prime * prime) = norme
            dy = prime * dx

            x = [point.x - dx, point.x + dx]
            y = [point.y - dy, point.y + dy]
            self.ax.plot(x, y, color="green")

    #creation d'un point
    def on_click(self, event):
        if event.inaxes:
            if event.button == MouseButton.RIGHT:

                artist = self.ax.scatter(event.xdata, event.ydata, color="r", s=10, picker=True, pickradius = 5, zorder=3)
                #ajouter les points dans une liste
                point = Point(event.xdata, event.ydata, artist)
                self.points.append(point)
                self.point_map[event.xdata] = point
                self.points.sort()

                self.update()
                print(f'data coords {event.xdata} {event.ydata},',
                      f'pixel coords {event.x} {event.y}')
                if len(self.points) >= 2:
                    self.draw_curve()

    #selection d'un point
    def on_point_click(self, event):
        if self.selected is not None:
            self.selected.set_color("red")
            #self.selected.set(facecolor = "red")

        data = event.artist.get_offsets().data.tolist()
        x = str(data[0][0])[:4]
        y = str(data[0][1])[:4]

        #event.artist.set(facecolor = "yellow")
        self.selected = self.point_map[data[0][0]]
        self.selected.set_color("yellow")

        self.point_pos_text.configure(text=f"({x}, {y})")

        self.derivative_input.delete(0)
        self.derivative_input.insert(0, self.selected.derivative)

        self.update()
        print(x, y)

    def on_derivative_input_changed(self, event):
        self.selected.derivative = float(self.derivative_input.get())
        print(self.selected.derivative)
        self.draw_curve()
        self.update()