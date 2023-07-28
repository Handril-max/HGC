# py:3
# HandrilOS Handrilsoft2021
# HFS_tkinter_GUImode_of_Hanchen_Architecture
# app window engine
# Handril PC screen
# -*- coding:utf-8 -*-
from distutils.command.build import build
import os
import sys
import time
from turtle import title
import random
import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.messagebox
from PIL import ImageTk, Image, ImageFilter
from tkinter import filedialog
from shutil import *
import numpy as np
import H_bezier
import H_cpupack as cpk
import H_cartoon as swc
import H_threadpool as thdpol
import platform

winnum = 0
w_box = 30
h_box = w_box

def system_dpi():
    host_os = platform.system()
    if host_os == 'Windows':
        #import ctypes
        #ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)
        ScaleFactor = 100
        return ScaleFactor
    if host_os == 'Linux':
        ScaleFactor = 200
        return ScaleFactor
    if host_os == 'Darwin':
        ScaleFactor = 200
        return ScaleFactor
    if host_os == 'Haniux':
        ScaleFactor = 200
        return ScaleFactor

def to_dpi():
    for_dpi = int((int(system_dpi()))/100)
    return for_dpi

def basize_line(start_num,end_num,speed):
    points = np.array([[0, start_num],[400, end_num],[400, end_num]])
    x, y = points[:, 0], points[:, 1]
    by = H_bezier.evaluate_bezier(points, speed)
    return list(by)

class cpk():
    def unpathfilewrite(filename,statue,result):
        with open(filename,statue,encoding='utf-8') as f:
            f.write(str(result))
    def pathfilewrite(path,statue):
        filejob = open(path,statue)
        filejob.close()

class HandrilAppTk(tk.Tk):
    global winnum
    if winnum == 0:
        None
    else:
        None
    winnum += 1
    root_x, root_y, abs_x, abs_y = 0, 0, 0, 0
    width, height = None, None
    
    def __init__(self,title=None, en_title=None, topmost=True, alpha=1, bg=None, width=None, height=None):
        super().__init__()
        self["bg"] = bg
        self.bg = bg
        self.en_title = en_title
        if title == None:
            self.title = 'Loading'
        else:
            self.title = title

        self.for_dpi = to_dpi()
        self.width, self.height = width, height
        self.overrideredirect(True)
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        self.wm_attributes("-alpha", alpha)  # 透明度
        self.wm_attributes("-topmost", topmost)  # 永远处于顶层
        win_side_wid = 3
        win_side_col = '#272727'
        win_max_side_col = 'white'
        self.config(cursor='circle')
        canvas = tk.Canvas(self, height=win_side_wid,
                           width=sw, bd=0, bg=win_side_col)
        canvas.config(highlightthickness=0)
        canvas.pack(side='top')

        def to_up(_):
            swc.to_max(self, 1, 100, sw, sh)
            #canvas.config(bg='white')
            def back(_):
                swc = self.winfo_screenwidth()
                shc = self.winfo_screenheight()
                sw = swc-200
                sh = shc-200
                t_x = (swc-sw)/2
                t_y = shc/15
                from . import sys_win_cartoon as swc
                swc.to_ship(self, sw, sh, t_x, t_y)
                
        self.bind('<Control-KeyPress-Up>', to_up)

        swc.display_show(self)

        right_bind = tk.Canvas(
            self, height=sh, width=win_side_wid, bd=0, bg=win_side_col)
        right_bind.config(highlightthickness=0)
        right_bind.pack(side='right')

        def right_to_mouse(_):
            right_bind.config(cursor='fleur')
        right_bind.bind('<Enter>', right_to_mouse)

        left_bind = tk.Canvas(
            self, height=sh, width=win_side_wid, bd=0, bg=win_side_col)
        left_bind.config(highlightthickness=0)
        left_bind.pack(side='left')
        
        buttom_bind = tk.Canvas(self, height=win_side_wid,
                                width=sw, bd=0, bg=win_side_col)
        buttom_bind.config(highlightthickness=0)
        buttom_bind.pack(side='bottom')

        #cpk.unpathfilewrite("all_progress.psw", "w", "app_taask_forget")

        def win_close(_):
            self.destroy()
            #cpk.unpathfilewrite("apppath.psw", "w", "标签")
            #cpk.unpathfilewrite("toptip.message", "w", 'None')
        self.bind('<Alt-F4>', win_close)
        #self.bind('<Double-Button-1>', win_close)

        def to_normal_type(_):
            right_bind.config(bg=win_side_col)
            left_bind.config(bg=win_side_col)
            swc.to_normal(self, 1, 100, sw, sh)
        self.bind('<Alt-Shift-M>', to_normal_type)
        self.bind('<Alt-Shift-m>', to_normal_type)

        def to_max_type(_):
            swc.to_max(self, 1, 100, sw, sh)
            right_bind.config(bg=win_max_side_col)
            left_bind.config(bg=win_max_side_col)
        self.bind('<Alt-M>', to_max_type)
        self.bind('<Alt-m>', to_max_type)
        
        def to_task_back(_):
            swc.to_max(self, 1, 100, sw, sh)
            self.bind('<Control-Tab>',to_task_go)
        def to_task_go(_):
            swc.to_ship(self,sw-200*self.for_dpi,sh-200*self.for_dpi,(sw-(sw-200*self.for_dpi))/2,(sh-(sh-200*self.for_dpi))/2)
            self.bind('<Control-Tab>',to_task_back)
            from .. import desktopGrid
            desktopGrid.main()
            
        self.bind('<Control-Tab>',to_task_go)
        #self.bind('<KeyRelease-A>',to_task_back)
        

    def to_global_close(self):
        None

    def global_close(self):
        self.destroy()
        #cpk.unpathfilewrite("apppath.psw", "w", "标签")
        #cpk.unpathfilewrite("toptip.message", "w", 'None')
        
    def mousedown(self, event):
        widget = event.widget
        widget.startx = event.x  # 开始拖动时, 记录控件位置
        widget.starty = event.y

    def drag(self, event):
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        widget = event.widget
        dx = event.x-widget.startx
        dy = event.y-widget.starty
        # 底部操作
        if widget.starty <= sh-20:
            if dy < 0:
                if abs(dx) <= 20:
                    HandrilAppTop.destroyof(self)
            if dy > 0:
                if abs(dx) <= 20:
                    thdpol.dissetp.thd2(swc.to_ship(self, sw, sh/2, 0, sh/2))
            if dx < 0:
                if abs(dy) <= 20:
                    thdpol.dissetp.thd2(swc.to_ship(self, sw/2, sh-20, 0, 27))
            if dx > 0:
                if abs(dy) <= 20:
                    thdpol.dissetp.thd2(swc.to_ship(
                        self, sw/2, sh-20, sw/2, 27))

    def to_ship(self, rewid, rehig, rex, rey):
        self.rewid, self.rehig, self.rex, self.rey = rewid, rehig, rex, rey
        thdpol.dissetp.thd2(swc.to_ship(
            self, self.rewid, self.rehig, self.rex, self.rey))

        #bottomtype3.config(width=(self.winfo_width())/2)

    def to_random_ship(self, rewid, rehig, rex, rey):
        self.rewid, self.rehig, self.rex, self.rey = rewid, rehig, rex, rey
        thdpol.dissetp.thd2(swc.to_ship(
            self, self.rewid, self.rehig, self.rex, self.rey))
        

    def destroyof(self):
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        thdpol.dissetp.thd2(swc.to_hide(self, 1, 8000, sw,
                            sh, self.winfo_width(), self.winfo_height()))
        self.destroy()
        
class HandrilAppTop(tk.Toplevel):
    global winnum
    if winnum == 0:
        None
    else:
        None
    winnum += 1
    root_x, root_y, abs_x, abs_y = 0, 0, 0, 0
    width, height = None, None
    
    def __init__(self,title=None, en_title=None, topmost=True, alpha=1, bg=None, width=None, height=None):
        super().__init__()
        self["bg"] = bg
        self.bg = bg
        self.en_title = en_title
        if title == None:
            self.title = 'Loading'
        else:
            self.title = title

        self.for_dpi = to_dpi()
        self.width, self.height = width, height
        self.overrideredirect(True)
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        self.wm_attributes("-alpha", alpha)  # 透明度
        self.wm_attributes("-topmost", topmost)  # 永远处于顶层
        win_side_wid = 3
        win_side_col = '#272727'
        win_max_side_col = 'white'
        self.config(cursor='circle')
        canvas = tk.Canvas(self, height=win_side_wid,
                           width=sw, bd=0, bg=win_side_col)
        canvas.config(highlightthickness=0)
        canvas.pack(side='top')

        def to_up(_):
            swc.to_max(self, 1, 100, sw, sh)
            #canvas.config(bg='white')
            def back(_):
                swc = self.winfo_screenwidth()
                shc = self.winfo_screenheight()
                sw = swc-200
                sh = shc-200
                t_x = (swc-sw)/2
                t_y = shc/15
                from . import sys_win_cartoon as swc
                swc.to_ship(self, sw, sh, t_x, t_y)
                
        self.bind('<Control-KeyPress-Up>', to_up)

        swc.display_show(self)

        right_bind = tk.Canvas(
            self, height=sh, width=win_side_wid, bd=0, bg=win_side_col)
        right_bind.config(highlightthickness=0)
        right_bind.pack(side='right')

        def right_to_mouse(_):
            right_bind.config(cursor='fleur')
        right_bind.bind('<Enter>', right_to_mouse)

        left_bind = tk.Canvas(
            self, height=sh, width=win_side_wid, bd=0, bg=win_side_col)
        left_bind.config(highlightthickness=0)
        left_bind.pack(side='left')
        
        buttom_bind = tk.Canvas(self, height=win_side_wid,
                                width=sw, bd=0, bg=win_side_col)
        buttom_bind.config(highlightthickness=0)
        buttom_bind.pack(side='bottom')

        #cpk.unpathfilewrite("all_progress.psw", "w", "app_taask_forget")

        def win_close(_):
            self.destroy()
            #cpk.unpathfilewrite("apppath.psw", "w", "标签")
            #cpk.unpathfilewrite("toptip.message", "w", 'None')
        self.bind('<Alt-F4>', win_close)
        #self.bind('<Double-Button-1>', win_close)

        def to_normal_type(_):
            right_bind.config(bg=win_side_col)
            left_bind.config(bg=win_side_col)
            swc.to_normal(self, 1, 100, sw, sh)
        self.bind('<Alt-Shift-M>', to_normal_type)
        self.bind('<Alt-Shift-m>', to_normal_type)

        def to_max_type(_):
            swc.to_max(self, 1, 100, sw, sh)
            right_bind.config(bg=win_max_side_col)
            left_bind.config(bg=win_max_side_col)
        self.bind('<Alt-M>', to_max_type)
        self.bind('<Alt-m>', to_max_type)
        
        def to_task_back(_):
            swc.to_max(self, 1, 100, sw, sh)
            self.bind('<Control-Tab>',to_task_go)
        def to_task_go(_):
            swc.to_ship(self,sw-200*self.for_dpi,sh-200*self.for_dpi,(sw-(sw-200*self.for_dpi))/2,(sh-(sh-200*self.for_dpi))/2)
            self.bind('<Control-Tab>',to_task_back)
            from .. import desktopGrid
            desktopGrid.main()
            
        self.bind('<Control-Tab>',to_task_go)
        #self.bind('<KeyRelease-A>',to_task_back)
        

    def to_global_close(self):
        None

    def global_close(self):
        self.destroy()
        #cpk.unpathfilewrite("apppath.psw", "w", "标签")
        #cpk.unpathfilewrite("toptip.message", "w", 'None')
        
    def mousedown(self, event):
        widget = event.widget
        widget.startx = event.x  # 开始拖动时, 记录控件位置
        widget.starty = event.y

    def drag(self, event):
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        widget = event.widget
        dx = event.x-widget.startx
        dy = event.y-widget.starty
        # 底部操作
        if widget.starty <= sh-20:
            if dy < 0:
                if abs(dx) <= 20:
                    HandrilAppTop.destroyof(self)
            if dy > 0:
                if abs(dx) <= 20:
                    thdpol.dissetp.thd2(swc.to_ship(self, sw, sh/2, 0, sh/2))
            if dx < 0:
                if abs(dy) <= 20:
                    thdpol.dissetp.thd2(swc.to_ship(self, sw/2, sh-20, 0, 27))
            if dx > 0:
                if abs(dy) <= 20:
                    thdpol.dissetp.thd2(swc.to_ship(
                        self, sw/2, sh-20, sw/2, 27))

    def to_ship(self, rewid, rehig, rex, rey):
        self.rewid, self.rehig, self.rex, self.rey = rewid, rehig, rex, rey
        thdpol.dissetp.thd2(swc.to_ship(
            self, self.rewid, self.rehig, self.rex, self.rey))

        #bottomtype3.config(width=(self.winfo_width())/2)

    def to_random_ship(self, rewid, rehig, rex, rey):
        self.rewid, self.rehig, self.rex, self.rey = rewid, rehig, rex, rey
        thdpol.dissetp.thd2(swc.to_ship(
            self, self.rewid, self.rehig, self.rex, self.rey))
        

    def destroyof(self):
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        thdpol.dissetp.thd2(swc.to_hide(self, 1, 8000, sw,
                            sh, self.winfo_width(), self.winfo_height()))
        self.destroy()
        
