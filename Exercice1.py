#module fait maison (fichier Maths.py)
from Maths import *
import matplotlib.pyplot as plt

def ellipse(xC : float, yC : float, a : float, b : float, step : int = 500):
    if a <= 0 or b <= 0:
        raise ValueError('a, b must be positive')

    angle_step = 360.0/step * PI/180
    x = []
    y = []
    for i in range(step):
        x.append(cos(i*angle_step) * a + xC)
        y.append(sin(i*angle_step) * b + yC)

    plt.plot(x, y)
    plt.scatter(xC, yC, color='red')
    plt.axis('scaled')
    plt.show()

ellipse(8, 5, 5, 3)