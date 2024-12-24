from PIL.ImageOps import scale
from matplotlib import pyplot as plt

from Maths import *

list_x = []
list_y = []

def segment(point1 : tuple[float, float], point2 : tuple[float, float], prime1 : float, prime2 : float):

    for i in range(0, 100):

        x = point1[0] * (1 - i/100) + point2[0] * i/100

        plt.scatter(point1[0], point1[1], color='r', marker='o')
        list_x.append(x)
        list_y.append(hermite(point1, point2, prime1, prime2, x))

#segment composant la forme
segment((1.9, -2), (4, 2), 1, 9)
segment((4, 2), (1, 5), 0.3, 9)
segment((1, 5), (-2, 4), 2.1, -5)
#--------------------------------------------------------


plt.plot(list_x, list_y)
plt.grid(True)
plt.gca().set_aspect("equal")
plt.show()