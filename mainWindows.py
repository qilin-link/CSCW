#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import tkinter
from ScrolledText import ScrolledText
import os
import re
from tkFileDialog import askopenfilename
from tkinter.messagebox import showinfo

class MainWindows(tkinter.Frame):
    def __init__(self, master):
        frame = tkinter.Frame(master,width=500,height=220)
        frame.grid(row=0, column=0)
        frame.pack()
        #self.repWin = repWin

        self.labelFile = tkinter.Label(frame,
                                       text='文件',
                                       font=('黑体'),
                                       justify='left',
                                       )
        self.labelFile.place(x=35, y=30)

        self.fileVar = tkinter.Variable()
        self.fileEntry = tkinter.Entry(frame,textvariable=self.fileVar, width=45)
        #self.fileEntry.delete(0, 'end')
        self.fileEntry.place(x=90,y=30)
        
        self.buttonOpenFile = tkinter.Button(frame, text='打开', width=5, height=1, command=self.openFile)
        self.buttonOpenFile.place(x=430, y=30) 
        
        self.labelPic = tkinter.Label(frame,
                                       text='图片',
                                       font=('黑体'),
                                       justify='left',
                                       )
        self.labelPic.place(x=35, y=90)
        
        self.picVar = tkinter.Variable()
        self.picEntry = tkinter.Entry(frame,textvariable=self.picVar, width=45)
        self.picEntry.place(x=90,y=90)
        
        self.buttonOpenPic = tkinter.Button(frame, text='打开', width=5, height=1, command=self.openPic)
        self.buttonOpenPic.place(x=430, y=90)
        
        self.labelPic = tkinter.Label(frame,
                                       text='过滤词',
                                       font=('黑体'),
                                       justify='left',
                                       )
        self.labelPic.place(x=20, y=150)
        
        self.st = ScrolledText(frame, width=43, height=3)
        self.st.place(x=90,y=150)
        
        self.buttonAddWords = tkinter.Button(frame, text='添加', width=5, height=1, command=self.addWords)
        self.buttonAddWords.place(x=430, y=150)        

      
    def openFile(self):

        path = os.path.split(os.path.realpath(__file__))[0]
        fileName = askopenfilename(initialdir = path,filetypes=[('Word文档', '*.doc;*.docx'), ('文本文件', '*.txt')])
        self.fileVar.set(fileName)
        return fileName
        
    def openPic(self):
        path = os.path.split(os.path.realpath(__file__))[0]
        picName = askopenfilename(initialdir = path,filetypes=[('JPEG', '*.jpg;*.jpeg;*.jpe;*.jfif'), ('PNG', '*.png')])
        self.picVar.set(picName)
        return picName
    
    def addWords(self):
        
        f = open('./stopwords.txt','a+')
        text = f.read()
        dupWords = list()

        tempStrings = self.st.get('1.0', 'end-1c')

        tempStrings = tempStrings.encode('UTF-8')
        if tempStrings == '':
            self.replyNoneWin()
        else:
            wordList = re.split(',|，',tempStrings) 
            for i in range(len(wordList)):
                if wordList[i].strip() not in text:
                    f.seek(0,2)
                    f.write(wordList[i].strip()+'\n')
                else:
                    dupWords.append(wordList[i].strip())
                    
            self.replyOkWin()
            
            if dupWords != '':
                self.replyDupWin(dupWords)
        f.close()
        
    def replyOkWin(self):
        showinfo(title='提示', message='添加成功！')

    def replyDupWin(self,dupWords):
        showinfo(title='提示', message='以下词语："' + ','.join(dupWords) + '" 已经收录，无需再次添加。')

    def replyNoneWin(self):
        showinfo(title='提示', message='没有添加内容')
    