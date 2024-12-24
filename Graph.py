import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Graph:
    def __init__(self, plotframe):
        fig, ax = plt.subplots()

        plt.connect('button_press_event', on_click)

        ax.set_title("Curve Generator", fontsize=20, pad=20, color="white")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        fig.patch.set_facecolor("white")
        ax.grid(True)

        ax.scatter(4, 4, color="r")

        canvas = FigureCanvasTkAgg(fig, master=plotframe)
        canvas.get_tk_widget().grid(column=0, row=0, pady=5, padx=5, sticky="nsew")

        canvas.draw()
