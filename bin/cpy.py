import array
import matplotlib.pyplot as plt   
from scipy.fftpack import fft, ifft


def show():
    plt.axis('equal')
    plt.show()

def subplot(i):
    plt.subplot(i)

def plot(x, y, op):
    plt.plot(x, y, op)

def tplot(x, op):
    plt.plot(x, op)

def grid():
    plt.grid()

def figure(id, figsize):
    plt.figure(id, figsize)



