from pylab import get_cmap
import pylab as plt
import numpy as np
from urllib.request import urlopen, Request
import threading
FINAL = threading.Lock()
PIXELS = 128 ** 2

""" Gets n random numbers in range [min, max] and returns it as a list"""
def get_rands(n, min, max):
    genericURL = "https://www.random.org/integers/?num={0}&min={1}&max={2}&col={3}&base={4}&format=plain&rnd=new"
    tempURL = genericURL.format(n, min, max, 1, 10)
    requestURL = Request(tempURL)
    requestURL.add_header("Request by", "adikotak@berkeley.edu")

    with FINAL:
        nums = urlopen(requestURL).read()

    return [int(rand) for rand in nums.splitlines()]

""" Creates two numpy arrays and restructures it to be a 2x2 array that
    is used to display the randomly generated RGB bitmap """
def draw():
    halfNums1 = np.array(get_rands(PIXELS/2, 1, 10))
    halfNums2 = np.array(get_rands(PIXELS/2, 1, 10))
    allNums = np.append(halfNums1, halfNums2)
    formattedNums = np.reshape(allNums, (-1, int(PIXELS ** 0.5)))

    plt.imshow(formattedNums, cmap = get_cmap("brg"), interpolation = "nearest")
    plt.show()

draw()
