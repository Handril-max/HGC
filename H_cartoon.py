# py:3
# Handrilsoft
# Abot system windows cartoon
import time

import numpy as np
from H_bezier import *
import H_dpi

for_dpi = H_dpi.to_dpi()
stt_num = 1000
speedment = 50
def basize_line(start_num, end_num, speed):
    points = np.array([[0, start_num], [stt_num, end_num], [stt_num, end_num], [stt_num, end_num], [stt_num, end_num]
    , [stt_num, end_num], [stt_num, end_num], [stt_num, end_num], [stt_num, end_num], [stt_num, end_num]])
    x, y = points[:, 0], points[:, 1]
    by = evaluate_bezier(points, speed)
    return list(by)


def display_show(root):  # in
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    root.geometry('%dx%d+%d+%d' % (sw, sh, 0, round(sh*(27/sh))*for_dpi))
    for h in range(0, 100, 10):
        root.wm_attributes("-alpha", h/50)  # 透明度
        root.update()
        time.sleep(0.023)

def display_show_random(root, startint, endint, sw, sh, wid, win_hig, xn):  # in
    sh = root.winfo_screenheight()
    end_x = root.winfo_x()
    end_y = root.winfo_y()
    for h in basize_line(startint, endint, speedment):
        i = h*(100/endint)
        #wc_wid = (wid/100)*i
        wc_wid = (wid/100)*i
        wc_hig = (win_hig/100)*i
        x = ((xn*i)/100)
        y = (sh-wc_hig)/(i/50)+(round(sh*(27/sh)))/2
        root.geometry('%dx%d+%d+%d' % (wc_wid, wc_hig, x, y))
        root.update()


def to_hide(root, startint, endint, sw, sh, wid, win_hig):  # hide
    sh = root.winfo_screenheight()
    for h in basize_line(startint, endint, speedment)[::-1]:
        i = h*(100/endint)
        wc_wid = (wid/i)*i
        wc_hig = (win_hig/i)*i
        now_x = (root.winfo_x()*i)/i
        now_y = (root.winfo_y()*i)/i
        x = now_x
        y = (now_y*i)/i-(round(sh*(27/sh)))
        root.geometry('%dx%d+%d+%d' % (wc_wid, wc_hig, x, y))
        root.update()


def to_show_tool(root):  # tool_win_sow
    for h in range(0, 100, 10):
        root.wm_attributes("-alpha", h/100)  # 透明度
        root.update()
        time.sleep(0.013)


def to_hide_tool(root):  # tool_win_hode
    for h in range(0, 100, 10)[::-1]:
        root.wm_attributes("-alpha", h/100)  # 透明度
        root.update()
        time.sleep(0.013)


def intend_display(root):  # hide
    for h in range(0, 100, 10)[::-1]:
        root.wm_attributes("-alpha", h/100)  # 透明度
        root.update()
        time.sleep(0.013)


def to_max(root, startint, endint, sw, sh):  # hide
    start_wid = root.winfo_width()
    start_hig = root.winfo_height()
    start_x = root.winfo_x()
    start_y = root.winfo_y()
    for i in basize_line(0, 100, speedment):
        with open("maxmart.psw", "r", encoding='utf-8') as f:
            data1 = f.read()
        if data1 == 'left':
            end_wid = start_wid+(((sw*i)/100)-(start_wid*i)/100)-round(sw*(40/sw))*for_dpi
            end_hig = start_hig+(((sh*i)/100)-(start_hig*i)/100)-round(sh*(27/sh))*for_dpi
            x = 0-((start_x*i)/100)+start_x+40*for_dpi
            y = (27*for_dpi-((start_y*i)/100)+start_y)+0
        if data1 == 'down':
            end_wid = start_wid+(((sw*i)/100)-(start_wid*i)/100)
            end_hig = start_hig+(((sh*i)/100)-(start_hig*i)/100)-round(sh*(84/sh))*for_dpi
            x = 0-((start_x*i)/100)+start_x
            y = (27*for_dpi-((start_y*i)/100)+start_y)+0
        if data1 == 'up':
            end_wid = start_wid+(((sw*i)/100)-(start_wid*i)/100)
            end_hig = start_hig+(((sh*i)/100)-(start_hig*i)/100)-round(sh*(67/sh))*for_dpi
            x = 0-((start_x*i)/100)+start_x
            y = (27*for_dpi-((start_y*i)/100)+start_y)+0
        root.geometry('%dx%d+%d+%d' % (end_wid, end_hig, x, y))
        root.update()

def to_normal(root, startint, endint, sw, sh):  # hide
    start_wid = root.winfo_width()
    start_x = root.winfo_x()
    for i in basize_line(start_wid, sw/2+200, speedment):
        end_hig = (sh*i)/(sw/2+200)/2+200
        x = (((sw/i)*i)-i)/2
        y = (((sh/i)*i)-end_hig)/2-10
        root.geometry('%dx%d+%d+%d' % (i, end_hig, x, y))
        root.update()


def to_ship(root, widn, hign, xn, yn):  # hide
    start_wid = root.winfo_width()
    start_hig = root.winfo_height()
    start_x = root.winfo_x()
    start_y = root.winfo_y()
    for i in basize_line(0, 100, speedment):
        end_wid = start_wid+(((widn*i)/100)-(start_wid*i)/100)
        end_hig = start_hig+(((hign*i)/100)-(start_hig*i)/100)-round(hign*(57/hign))*for_dpi
        x = ((xn*i)/100)-((start_x*i)/100)+start_x
        y = ((yn*i)/100)-((start_y*i)/100)+start_y
        root.geometry('%dx%d+%d+%d' % (end_wid, end_hig, x, y))
        root.update()

def to_top_ship(root, widn, hign, xn, yn):  # hide
    start_wid = root.winfo_width()
    start_hig = root.winfo_height()
    start_x = root.winfo_x()
    start_y = root.winfo_y()
    for i in basize_line(0, 100, speedment):
        end_wid = start_wid+(((widn*i)/100)-(start_wid*i)/100)
        end_hig = start_hig+(((hign*i)/100)-(start_hig*i)/100)-round(hign*(57/hign))*for_dpi
        x = ((xn*i)/100)-((start_x*i)/100)+start_x
        y = (27*for_dpi-((start_y*i)/100)+start_y)+0
        root.geometry('%dx%d+%d+%d' % (end_wid, end_hig, x, y))
        root.update()


def to_ship_sys_ui(root, widn, hign, xn, yn):  # hide
    start_wid = root.winfo_width()
    start_hig = root.winfo_height()
    start_x = root.winfo_x()
    start_y = root.winfo_y()
    for i in basize_line(0, 100, speedment):
        end_wid = start_wid+(((widn*i)/100)-(start_wid*i)/100)
        end_hig = start_hig+(((hign*i)/100)-(start_hig*i)/100)-((27*for_dpi*i)/100)
        x = ((xn*i)/100)-((start_x*i)/100)+start_x
        y = (((yn*i)/100)-((start_y*i)/100)+start_y)+0
        root.geometry('%dx%d+%d+%d' % (end_wid, end_hig, x, y))
        root.update()
