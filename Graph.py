import matplotlib.pyplot as plt
from matplotlib.backend_bases import MouseButton
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from Point import Point
from Maths import *

class Graph:

    def __init__(self, plotframe, point_pos_text, derivative_input, derivative_second_input,
                 limx_min, limx_max, limy_min, limy_max):

        #points de controle (point rouge)
        self.points = []
        self.point_map = {}
        #tous les points qui composent la courbe (utile pour les difference finies)
        self.total_points = []

        self.point_pos_text = point_pos_text
        self.derivative_input = derivative_input
        self.derivative_second_input = derivative_second_input

        self.limx_min = limx_min
        self.limx_max = limx_max
        self.limy_min = limy_min
        self.limy_max = limy_max

        self.selected = None
        self.mirror = False

        self.fig, self.ax = plt.subplots()

        plt.connect('button_press_event', self.on_click)
        plt.connect('pick_event', self.on_point_click)
        derivative_input.bind('<Return>', self.on_derivative_input_changed)
        derivative_second_input.bind('<Return>', self.on_derivative_input_second_changed)
        limx_max.bind('<Return>', self.on_axes_input_change)
        limy_min.bind('<Return>', self.on_axes_input_change)
        limy_max.bind('<Return>', self.on_axes_input_change)
        limx_min.bind('<Return>', self.on_axes_input_change)

        self.ax.set_title("Curve Generator", fontsize=20, pad=20, color="white")
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("y")
        self.ax.xaxis.label.set_color("white")
        self.ax.yaxis.label.set_color("white")
        self.ax.tick_params(axis='x', colors='white')
        self.ax.tick_params(axis='y', colors='white')
        self.ax.set(xlim=(-10, 10), ylim=(-10, 10))
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
        step = 200
        for i in range(0, step+1):
            x = point1.x * (1 - i / step) + point2.x * i / step
            y = hermite((point1.x, point1.y), (point2.x, point2.y), prime1, prime2, x)

            list_x.append(x)
            list_y.append(y)
            self.total_points.append((x, y))
        self.ax.plot(list_x, list_y, color="blue")

    def draw_curve(self):
        #supprimer touts les segments existants
        for plot in self.ax.lines:
            plot.remove()

        self.total_points.clear()

        #dessiner les tangentes
        for point in self.points:
            self.draw_tan(point, point.derivative)

        for point in range(len(self.points)-1):
            self.segment(self.points[point], self.points[point+1], self.points[point].derivative, self.points[point+1].derivative)

        self.update()

    def draw_tan(self, point : Point, prime : float):
            l = 2

            magnitude = sqrt(1 + prime * prime)
            # vecteur normalise de la tangente sqrt(1 + prime * prime) = norme
            dx = l / magnitude
            dy = prime * l / magnitude

            x = [point.x - dx, point.x + dx]
            y = [point.y - dy, point.y + dy]
            self.ax.plot(x, y, color="green")

    #creation d'un point
    def on_click(self, event):
        if event.inaxes:
            if event.button == MouseButton.RIGHT:

                self.place_point(event.xdata, event.ydata)

                if self.mirror:
                    center = (float(self.limx_min.get()) + float(self.limx_max.get())) / 2
                    self.place_point(center - (event.xdata-center), event.ydata)

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

        self.derivative_input.delete(0, 100)
        self.derivative_input.insert(0, self.selected.derivative)

        self.derivative_second_input.delete(0, 100)
        self.derivative_second_input.insert(0, self.selected.derivative2)

        self.update()

    def on_derivative_input_changed(self, event):
        self.selected.derivative = float(self.derivative_input.get())
        self.draw_curve()
        self.update()

    def on_derivative_input_second_changed(self, event):

        current = (self.selected.x, self.selected.y)
        index = self.total_points.index(current)

        prime = 0
        h = 0

        if index == 0:
            current_p1 = self.total_points[index+1]
            current_p2 = self.total_points[index+2]

            h = current_p2[0] - current_p1[0]
            prime = d_forward(current_p1, current_p2)
        elif index == len(self.total_points)-1:
            current_m1 = self.total_points[index-1]
            current_m2 = self.total_points[index-2]

            h = current_m1[0] - current_m2[0]
            prime = d_backward(current_m1, current_m2)
        else:
            current_m1 = self.total_points[index-1]
            current_p1 = self.total_points[index+1]
            h = (current[0] - current_m1[0]) * 2
            prime = d_center(current_m1, current_p1)

        d = derivative(float(self.derivative_second_input.get()), h, prime)

        self.selected.derivative = d
        self.derivative_input.delete(0, 100)
        self.derivative_input.insert(0, d)
        self.draw_curve()
        self.update()

    def on_mirror_click(self):
        self.mirror = not self.mirror

    def on_axes_input_change(self, event):
        xlim = float(self.limx_min.get()), float(self.limx_max.get())
        ylim = float(self.limy_min.get()), float(self.limy_max.get())
        self.ax.set(xlim=xlim, ylim=ylim)
        self.draw_curve()

    def place_point(self, x : float, y : float):
        artist = self.ax.scatter(x, y, color="r", s=10, picker=True, pickradius=5, zorder=3)
        # ajouter les points dans une liste
        point = Point(x, y, artist)
        self.points.append(point)
        self.point_map[x] = point