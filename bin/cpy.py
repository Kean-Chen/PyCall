'''
Author: ChenGen chengen1993@126.com
Date: 2022-07-28 17:04:15
LastEditors: ChenGen chengen1993@126.com
LastEditTime: 2022-07-29 17:11:51
FilePath: /pln_new/build/cpy.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import matplotlib.pyplot as plt   



def show():
    plt.axis('equal')
    plt.show()

def subplot(i):
    plt.subplot(i)

def plot(x, y, op):
    plt.plot(x, y, op)
    plt.pause(0.001)

def tplot(x, op):
    plt.plot(x, op)

def grid():
    plt.grid()

def figure(id, figsize):
    plt.figure(id, figsize)

def close():
    plt.close()

def ion():
    plt.ion()

def ioff():
    plt.ioff()

def clf():
    plt.clf()
    # plt.autoscale(False)

def xlim(lim_min, lim_max):
    plt.xlim(lim_min, lim_max)

def ylim(lim_min, lim_max):
    plt.ylim(lim_min, lim_max)
