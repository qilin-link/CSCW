#!/usr/bin/env python
#_*_ coding:utf-8 _*_
from tkinter.messagebox import showinfo

class ReplyWindows(object):
    def __init__(self, master):
        pass
        
    
    #弹出“请添加分析文件”提示窗口
    def replyAddFile(self):
        showinfo(title='提示', message='请添加分析文件')
    
    #弹出“请添加图片资源”提示窗口
    def replyAddPic(self):
        showinfo(title='提示', message='请添加图片资源')
    
    #弹出“添加成功”提示窗口方法
    def replyOkWin(self):
        showinfo(title='提示', message='添加成功！')
        
    #弹出“重复添加”提示窗口方法
    def replyDupWin(self,dupWords):
        showinfo(title='提示', message='以下词语：' + dupWords + ' 已经收录，无需再次添加。')