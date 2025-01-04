from PIL.ImageOps import scale
from matplotlib import pyplot as plt

from Maths import *

list_x = []
list_y = []

def segment(point1 : tuple[float, float], point2 : tuple[float, float], prime1 : float, prime2 : float):
    for i in range(0, 100):

        x = point1[0] * (1 - i/100) + point2[0] * i/100

        plt.scatter(point1[0], point1[1], color='r', marker='o', zorder=10, s=10)
        list_x.append(x)
        list_y.append(hermite(point1, point2, prime1, prime2, x))

def segment_lagrange(points : list[tuple[float, float]]):
    for i in range(0, 100):

        x = points[0][0] * (1 - i/100) + points[-1][0] * i/100

        plt.scatter(points[0][0], points[0][1], color='r', marker='o', zorder=10, s=10)
        list_x.append(x)
        list_y.append(lagrange(points, x))


#segment composant la forme
def Trace():
    segment_lagrange([(1.9, -2), (3, -1), (4, 2)])
    segment((4, 2), (1, 5), -0.1, -3)
    segment((1, 5), (-2, 4), -0.5, 2.5)
    segment((-2, 4), (-5,2), 2, 0)
    segment((-5, 2), (-6.15, 1.5), -1, 3.5)
    segment_lagrange([(-6.15, 1.5), (-6, 1), (-5.5, 0.75), (-5.2, 0.85), (-5, 1)])
    segment_lagrange([(-5, 1), (-2, 3)])
    segment_lagrange([(-2, 3), (-1.3, 3.3), (-1.1, 3.3), (-0.9, 3.25)])
    segment((-0.9, 3.25), (-2, 2), 3, 0.2)
    segment_lagrange([(-2, 2), (-3, 1.4), (-3.4, 1), (-4, 0), (-4.5,-1.6)])
    segment((-4.5,-1.6), (-4, -3), -7, -1.3)
    segment((-4, -3), (0, -1), 1.35, -0.7)
    segment((0, -1), (1.9, -2), 0.5, -2.8)
#--------------------------------------------------------

Trace()

plt.plot(list_x, list_y)
plt.arrow(-7, 0, 15,0 , width=0.07, zorder=20, length_includes_head=True, color='black')
plt.arrow(0, -4, 0, 10, width=0.07, zorder=20, length_includes_head=True, color='black')

plt.grid(True)
plt.xlim(-6.5, 8)
plt.ylim(-3.5, 6)
plt.locator_params(axis='x', nbins=20)
plt.locator_params(axis='y', nbins=10)
plt.gca().set_aspect("equal")
plt.show()