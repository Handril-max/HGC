# py:3
# HandrilOS Handrilsoft2021
# HFS_tkinter_GUImode_of_Hanchen_Architecture
# app window engine
# Handril PC screen
# -*- coding:utf-8 -*-
class FileOperate():
    def unpathfilewrite(filename,statue,result):
        with open(filename,statue,encoding='utf-8') as f:
            f.write(str(result))
    def pathfilewrite(path,statue):
        filejob = open(path,statue)
        filejob.close()

def unpathfilewrite(filename, statue, result):
    FileOperate.unpathfilewrite(filename, statue, result)
