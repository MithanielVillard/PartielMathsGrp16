import matplotlib.pyplot as plt
from matplotlib.backend_bases import MouseButton
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Maths import *

class Graph:

    def __init__(self, plotframe, point_pos_text, derivative_input):

        self.points = []
        self.derivative = []
        self.point_pos_text = point_pos_text
        self.derivative_input = derivative_input
        self.selected = None

        self.fig, self.ax = plt.subplots()

        plt.connect('button_press_event', self.on_click)
        plt.connect('pick_event', self.on_point_click)

        self.ax.set_title("Curve Generator", fontsize=20, pad=20, color="white")
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("y")
        self.ax.xaxis.label.set_color("white")
        self.ax.yaxis.label.set_color("white")
        self.ax.tick_params(axis='x', colors='white')
        self.ax.tick_params(axis='y', colors='white')
        self.ax.set(xlim=(0, 10), ylim=(-10, 10))
        self.ax.locator_params(axis='x', nbins=20)
        self.ax.locator_params(axis='y', nbins=20)
        self.fig.patch.set_facecolor("#222f3e")
        self.ax.grid(True)
        self.canvas = FigureCanvasTkAgg(self.fig, master=plotframe)
        self.canvas.get_tk_widget().grid(column=0, row=1, pady=10, padx=10, sticky="nsew")

        self.canvas.draw()

    def update(self):
        self.canvas.draw()

    def segment(self, point1: tuple[float, float], point2: tuple[float, float], prime1: float, prime2: float):
        list_x = []
        list_y = []
        for i in range(0, 100):
            x = point1[0] * (1 - i / 100) + point2[0] * i / 100

            list_x.append(x)
            list_y.append(hermite(point1, point2, prime1, prime2, x))
        self.ax.plot(list_x, list_y, color="blue")

    def draw_curve(self):
        #supprimer touts les segments existants
        for plot in self.ax.lines:
            plot.remove()

        for point in range(len(self.points)-1):
            self.segment(self.points[point], self.points[point+1], 1, 1)
        self.update()

    def draw_tan(self, point : tuple[float, float], prime : float):
        x = []
        #x.append(prime * )
        self.ax.plot()

    def on_click(self, event):
        if event.inaxes:
            if event.button == MouseButton.RIGHT:
                self.ax.scatter(event.xdata, event.ydata, color="r", picker=True, pickradius = 5, zorder=3)
                #ajouter les points dans une liste
                self.points.append((event.xdata, event.ydata))
                self.points.sort()
                self.update()
                print(f'data coords {event.xdata} {event.ydata},',
                      f'pixel coords {event.x} {event.y}')

                if len(self.points) >= 2:
                    self.draw_curve()

    def on_point_click(self, event):
        if self.selected is not None:
            self.selected.set(facecolor = "red")

        data = event.artist.get_offsets().data.tolist()
        x = str(data[0][0])[:4]
        y = str(data[0][1])[:4]

        event.artist.set(facecolor = "yellow")
        self.selected = event.artist
        self.point_pos_text.configure(text=f"({x}, {y})")

        self.update()
        print(x, y)