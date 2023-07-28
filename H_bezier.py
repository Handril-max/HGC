# py:3
# HandrilOS Handrilsoft2021
# HFS_tkinter_GUImode_of_Hanchen_Architecture
# HandrilFunctionServices
# Handril screen top status
# -*- coding:utf-8 -*-

import numpy as np
#import matplotlib.pyplot as plt
from math import factorial
import tkinter as tk

########################################################################################
#任意阶贝塞尔曲线
def comb(n, k):
    return factorial(n) // (factorial(k) * factorial(n-k))

def get_bezier_curve(points):
    n = len(points) - 1
    return lambda t: sum(comb(n, i)*t**i * (1-t)**(n-i)*points[i] for i in range(n+1))

def evaluate_bezier(points, total):
    bezier = get_bezier_curve(points)
    new_points = np.array([bezier(t) for t in np.linspace(0, 1, total)])
    return new_points[:, 1]
########################################################################################

#测试线
def text_line():
    points = np.array([[0, 0], [4, 3], [6, 0], [7, 2.5]])
    x, y = points[:, 0], points[:, 1]
    bx, by = evaluate_bezier(points, 50)
    #plt.plot(bx, by, 'b-')
    #plt.plot(x, y, 'r.')
    #plt.show()
#用线
def to_use_line(num):
    points = np.array([[0, 0], [400, 300], [600, 300], [700, 250],[300,890]])
    x, y = points[:, 0], points[:, 1]
    by = evaluate_bezier(points, 5000)
    return list(by)
#测试窗口
def to_window():
    root = tk.Tk()
    root.overrideredirect(True)
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    for i in to_use_line(sw/4)[::1]:
        root.geometry("%dx%d+%d+%d" % (i,sh, sw-i, i))
        root.update()
    root.mainloop()
