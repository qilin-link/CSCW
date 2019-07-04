#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Application Name: 词云生成器
Version: V1.0
Author: qi lin
Date: 2019-6-27
'''
import tkinter
from mainWindows import MainWindows
from lowWindows import LowWindows

def main():

    win = tkinter.Tk()
    win.title('词云生成器V1.0')
    win.geometry('500x290+400+200')
    win.resizable(0, 0)
    win.iconbitmap('./icon.ico')
    
    mainWin = MainWindows(win)
    #repWin = ReplyWindows(win)
    lowWin = LowWindows(win,mainWin)
        
    win.mainloop()
    
if __name__ == '__main__':
    main()