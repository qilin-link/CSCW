#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import tkinter
from tkinter.messagebox import showinfo

from docx import Document
#from imageio import imread 
import matplotlib.pyplot as plt    
import jieba                       
from wordcloud import WordCloud
#-----------------------------------

class LowWindows(tkinter.Frame):
    
    def __init__(self, master,otherWin):
        frame = tkinter.Frame(master,width=500,height=80)
        frame.grid(row=1, column=0)
        frame.pack()
        self.otherWin = otherWin
        #self.repWin = repWin
        self.buttonCreate = tkinter.Button(frame, text='生成', width=10, height=1, command=self.makeWordsCloud)
        self.buttonCreate.place(x=120, y=15)

        self.buttonQuit = tkinter.Button(frame, text='退出', width=10, height=1, command=frame.quit)
        self.buttonQuit.place(x=300, y=15)

    def makeWordsCloud(self):
        filePath = self.otherWin.fileVar.get()
        picPath = self.otherWin.picVar.get()

        if filePath == '':
            self.replyAddFile()
            #ReplyWindows.replyAddFile()
        elif picPath == '':    
            self.replyAddPic()
            #ReplyWindows.replyAddPic()
        else:
            #stopwords = {}
        
            back_coloring = plt._imread(picPath)
            #back_coloring = imageio.imread(picPath)
            
            wc = WordCloud(font_path = 'C:/Windows/Fonts/simkai.ttf',   
                           background_color= 'white',   
                           max_words = 200,    
                           mask = back_coloring,   
                           max_font_size = 200,  
                           random_state = 42,
                           width=1000, height=860, margin=2,               
                           )

            if filePath.split('.')[1] in ('txt'):
                text = open(filePath).read()
                text = self.jiebaclearText(text)
            elif filePath.split('.')[1] in ('doc','docx'):
                wordDoc = Document(filePath)
                text = ""
                for para in wordDoc.paragraphs:
                    text = text + para.text
                text = self.jiebaclearText(text)

            wc.generate(text)

            plt.imshow(wc,interpolation='bilinear')
            plt.axis('off')   
            plt.show()

    def jiebaclearText(self,text):
        stopwords_path = './stopwords.txt'
        
        jieba.set_dictionary('./dict.txt')
        jieba.initialize()
        
        mywordlist = []
        seg_list = jieba.cut(text, cut_all=False)
        liststr='/ '.join(seg_list)
        f_stop = open(stopwords_path)
        try:
            f_stop_text = f_stop.read()
            f_stop_text = unicode(f_stop_text,'utf8')
        finally:
            f_stop.close()
        f_stop_seg_list = f_stop_text.split('\n')
        for myword in liststr.split('/'):
            if not(myword.strip() in f_stop_seg_list) and len(myword.strip())>1:
                mywordlist.append(myword)
        return ''.join(mywordlist)

    def replyAddFile(self):
        showinfo(title='提示', message='请添加分析文件')

    def replyAddPic(self):
        showinfo(title='提示', message='请添加图片资源')