import os
import nltk
from nltk import FreqDist
from nltk.text import Text
import pymorphy2
import re
from pathlib import Path
import textstat
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.tokenize import RegexpTokenizer
import tkinter
import tkinter as tk
from tkinter import*
from tkinter.ttk import *
from tkinter import scrolledtext
morph = pymorphy2.MorphAnalyzer()

#Creating a window
window = Tk()
window.title("Simple Preprocessor")
window.geometry('1098x698')
window.configure(bg='#dbfcfe')
window.resizable(0,0)

tk.Label(window, text="Preprocessor", bg='#dbfcfe', font=("Arial Bold", 20)).place(relx=0.43, rely=0.001)
#insert your text here
tk.Label(window, text= "Your text ", bg='#dbfcfe', font=("Arial Bold", 16)).place(x=110, y=55)
textArea = scrolledtext.ScrolledText(window, height=32, width=50)
textArea.place(x=110, y=95)

tk.Label(window, text="Results ", bg='#dbfcfe', font=("Arial Bold", 16)).place(x=577, y=55)
#freq of 5 most common vocab
tk.Label(window, text="Frequency of 5 most used words:", bg='#dbfcfe').place(x=577, y=95)
sv1 = StringVar()
r1 = tkinter.Entry(window, width=63, textvariable=sv1)
r1.place(x=577, y=115)

#length of the text
tk.Label(window, text="Length of the text:", bg='#dbfcfe').place(x=577, y=150)
sv2 = StringVar()
r2 = tkinter.Entry(window, width=28, textvariable=sv2)
r2.place(x=577, y=170)

#length of the text, no duplicates
tk.Label(window, text="Length of the text, no duplicates:", bg='#dbfcfe').place(x=783.5, y=150)
sv3 = StringVar()
r3 = tkinter.Entry(window, width=28, textvariable=sv3)
r3.place(x=783.5, y=170)

#length of the text, no articles
tk.Label(window, text="Length of the text, no articles:", bg='#dbfcfe').place(x=577, y=200)
sv4 = StringVar()
r4 = tkinter.Entry(window, width=28, textvariable=sv4)
r4.place(x=577, y=220)

#lexical richness
tk.Label(window, text="Lexical richness:", bg='#dbfcfe').place(x=577, y=250)
sv5 = StringVar()
r5 = tkinter.Entry(window, width=28, textvariable=sv5)
r5.place(x=577, y=270)

#syntactical complexity
tk.Label(window, text="Syntactical complexity:", bg='#dbfcfe').place(x=783.5, y=250)
sv6 = StringVar()
r6 = tkinter.Entry(window, width=28, textvariable=sv6)
r6.place(x=783.5, y=270)

#average word length
tk.Label(window, text="Average word length:", bg='#dbfcfe').place(x=783.5, y=200)
sv7 = StringVar()
r7 = tkinter.Entry(window, width=28, textvariable=sv7)
r7.place(x=783.5, y=220)

#fog-index
tk.Label(window, text="Fog Index:", bg='#dbfcfe').place(x=577, y=300)
sv9 = StringVar()
r9 = tkinter.Entry(window, width=28, textvariable=sv9)
r9.place(x=577, y=320)

#flesch R E
tk.Label(window, text="Flesch Reading Ease:", bg='#dbfcfe').place(x=783.5, y=300)
sv10 = StringVar()
r10 = tkinter.Entry(window, width=28, textvariable=sv10)
r10.place(x=783.5, y=320)

#collocations
tk.Label(window, text="Collocations:", bg='#dbfcfe').place(x=577, y=350)
ta11 = Text(window, height=12, width=47)
ta11.place(x=577, y=370)

def Launch():
    #СИНТАКСИЧЕСКОЕ РАЗНООБРАЗИЕ СЧИТАЕМ УНИКАЛЬНЫЕ СЛОВА ИЛИ ВООБЩЕ ВСЕ?#
    text1=textArea.get('1.0', END)
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text1)
    text2=[]
    for word in tokens:
        p = morph.parse(word)[0]
        wordx=p.normal_form
        text2.append(wordx)
    fdist = FreqDist(text2)
    FDist= fdist.most_common(5)
    sv1.set(FDist)
    leng=len(tokens)
    sv2.set(leng)
    lennodup=len(set(word.lower() for word in text2))
    sv3.set(lennodup)
    textnoart = text2.count("a") + text2.count("an") + text2.count("the") + text2.count( "A") + text2.count("An") + text2.count("The")
    textlennoart= len(text2)- textnoart
    sv4.set(textlennoart)
    lexrich=((len(set(tokens)))/(len(tokens)))*100
    sv5.set(lexrich)
    sentok = sent_tokenize(text1)
    lensentok=len(sentok)
    lenwrds=len(set(tokens))
    syntcomp= 1-(lensentok/lenwrds)
    sv6.set(syntcomp)
    sredsum = sum(len(w) for w in text2)
    avwl=sredsum/len(text2)
    sv7.set(avwl)
    fog= (textstat.gunning_fog(text1))
    sv9.set(fog)
    flesch= (textstat.flesch_reading_ease(text1))
    sv10.set(flesch)
    text4=nltk.Text(text2)
    colloc=text4.collocation_list()
    ta11.insert('1.0', colloc)

def freqdistfn():
    text1=textArea.get('1.0', END)
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text1)
    text2=[]
    for word in tokens:
        p = morph.parse(word)[0]
        wordx=p.normal_form
        text2.append(wordx)
    fdist = FreqDist(text2)
    print(fdist.plot(50))

#Launch the function button       
btn = tk.Button (window, text= "Launch", bg="#8EC760", width=13, command=Launch)
btn.place (x=615, y=589)

#fdist (maybe a separate button for this)
btn2 = tk.Button (window, text= "Build FDist graph", bg="#5ab0ed", width=13, command = freqdistfn)
btn2.place (x=820, y=589)

window.mainloop()
