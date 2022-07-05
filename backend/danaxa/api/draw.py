#in this file i made a function (draw) that gets x[list] and y[list]
# and PATH of raw image and PATH of destenation,
# in destenation image and drawn splines will be saved.


import numpy as np
from scipy.special import binom
import cv2
import numpy as np

def Bernstein(n, k):
    # Bernstein polynomial
    coeff = binom(n, k)

    def _bpoly(x):
        return coeff * x ** k * (1 - x) ** (n - k)

    return _bpoly


def Bezier(points, num=200):
    # Build Bézier curve from points.
    N = len(points)
    t = np.linspace(0, 1, num=num)
    curve = np.zeros((num, 2))
    for ii in range(N):
        curve += np.outer(Bernstein(N - 1, ii)(t), points[ii])
    return curve


def draw(xs, ys, IMG_PATH, RES_PATH):
    x, y = Bezier(list(zip(xs, ys))).T
    img = cv2.imread(IMG_PATH)
    draw_points = (np.asarray([x, y]).T).astype(np.int32)
    image = cv2.polylines(img, [draw_points], False, (0,90,255), thickness=2)
    cv2.imwrite(RES_PATH, image)


