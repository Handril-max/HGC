# py:3
# Handrilsoft
import H_bezier
import H_cpupack as cpk
import H_cartoon as swc
import H_windoweng as swg
from H_windoweng import *
import threading
#cpk.unpathfilewrite("maxmart.psw", "w", " ")

class App(HandrilAppTk):
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
        self.title = title
        self.width, self.height = width, height
        self.overrideredirect(True)
        self.wm_attributes("-alpha", alpha)  # 透明度
        self.wm_attributes("-topmost", topmost)  # 永远处于顶层
        self.bind('<Button-3>', self._startmove, add='+')  # 移动
        self.bind('<B3-Motion>', self._on_move, add='+')
        swc = self.winfo_screenwidth()
        shc = self.winfo_screenheight()
        sw = swc-400
        sh = shc-200
        t_x = (swc-sw)/2
        t_y = ((shc-sh)/2)+27
        swg.HandrilAppTop.to_ship(self, sw, sh, t_x, t_y)
        swg.HandrilAppTop.to_global_close(self)

        def sys_task_oper():  # 进程系统级别标记函数
            with open("all_progress.psw", "r", encoding='utf-8') as f:
                mark = f.read()
            if mark == "1":
                HandrilAppTop.global_close(self)
            elif mark == "0":
                cpk.unpathfilewrite("toptipMessage.message", "w", "")
                cpk.unpathfilewrite("all_progress.psw", "w", "1")
            self.after(100, sys_task_oper)
        #t1 = threading.Thread(target=sys_task_oper,args=())
        #t1.setDaemon(True)
        #t1.start()


    def to_othership(self,rewid, rehig, rex, rey):
        self.rewid, self.rehig, self.rex, self.rey = rewid, rehig, rex, rey
        swg.HandrilAppTop.to_ship(self, self.rewid, self.rehig, self.rex, self.rey)
        
    def icon_mark(the_name):
        cpk.unpathfilewrite("apppath.psw", "w", the_name)

    def to_close(self):
        HandrilAppTop.global_close(self)

    def _startmove(self, event):  # 记录开始移动的坐标
        self.startx = event.x
        self.starty = event.y

    def _on_move(self, event):
        self.geometry("+%s+%s" % (self.winfo_x()+(event.x -
                      self.startx), self.winfo_y()+(event.y-self.starty)))
        self.update_idletasks()

class App_top(HandrilAppTop):
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
        self.title = title
        self.width, self.height = width, height
        self.overrideredirect(True)
        self.wm_attributes("-alpha", alpha)  # 透明度
        self.wm_attributes("-topmost", topmost)  # 永远处于顶层
        self.bind('<Button-3>', self._startmove, add='+')  # 移动
        self.bind('<B3-Motion>', self._on_move, add='+')
        swc = self.winfo_screenwidth()
        shc = self.winfo_screenheight()
        sw = swc-400
        sh = shc-200
        t_x = (swc-sw)/2
        t_y = ((shc-sh)/2)+27
        swg.HandrilAppTop.to_ship(self, sw, sh, t_x, t_y)
        swg.HandrilAppTop.to_global_close(self)

        def sys_task_oper():  # 进程系统级别标记函数
            with open("all_progress.psw", "r", encoding='utf-8') as f:
                mark = f.read()
            if mark == "1":
                HandrilAppTop.global_close(self)
            elif mark == "0":
                cpk.unpathfilewrite("toptipMessage.message", "w", "")
                cpk.unpathfilewrite("all_progress.psw", "w", "1")
            self.after(100, sys_task_oper)
        #t1 = threading.Thread(target=sys_task_oper,args=())
        #t1.setDaemon(True)
        #t1.start()


    def to_othership(self,rewid, rehig, rex, rey):
        self.rewid, self.rehig, self.rex, self.rey = rewid, rehig, rex, rey
        swg.HandrilAppTop.to_ship(self, self.rewid, self.rehig, self.rex, self.rey)
        
    def icon_mark(the_name):
        cpk.unpathfilewrite("apppath.psw", "w", the_name)

    def to_close(self):
        HandrilAppTop.global_close(self)

    def _startmove(self, event):  # 记录开始移动的坐标
        self.startx = event.x
        self.starty = event.y

    def _on_move(self, event):
        self.geometry("+%s+%s" % (self.winfo_x()+(event.x -
                      self.startx), self.winfo_y()+(event.y-self.starty)))
        self.update_idletasks()

