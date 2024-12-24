import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.patches import FancyBboxPatch

class Graph:
    def __init__(self, plotframe):
        self.fig, self.ax = plt.subplots()

        plt.connect('button_press_event', self.on_click)

        self.ax.set_title("Curve Generator", fontsize=20, pad=20, color="white")
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("y")
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
            self.ax.scatter(event.xdata, event.ydata, color="r")
            self.update()
            print(f'data coords {event.xdata} {event.ydata},',
                  f'pixel coords {event.x} {event.y}')