import matplotlib.pyplot as plt
from matplotlib.backend_bases import MouseButton
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Graph:
    def __init__(self, plotframe, pointPos):

        self.point_pos = pointPos
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
        self.ax.set(xlim=(-1, 1), ylim=(-1, 1))
        self.fig.patch.set_facecolor("#222f3e")
        self.ax.grid(True)
        self.canvas = FigureCanvasTkAgg(self.fig, master=plotframe)
        self.canvas.get_tk_widget().grid(column=0, row=1, pady=10, padx=10, sticky="nsew")

        self.canvas.draw()

    def update(self):
        self.canvas.draw()

    def on_click(self, event):
        if event.inaxes:
            if event.button == MouseButton.RIGHT:
                self.ax.scatter(event.xdata, event.ydata, color="r", picker=True, pickradius = 5)
                self.update()
                print(f'data coords {event.xdata} {event.ydata},',
                      f'pixel coords {event.x} {event.y}')

    def on_point_click(self, event):
        if self.selected is not None:
            self.selected.set(facecolor = "red")

        data = event.artist.get_offsets().data.tolist()
        x = str(data[0][0])[:4]
        y = str(data[0][1])[:4]

        event.artist.set(facecolor = "yellow")
        self.selected = event.artist
        self.point_pos.configure(text=f"({x}, {y})")

        self.update()
        print(x, y)
