from tkinter.constants import PROJECTING
from PIL import ImageFont,ImageTk
from PIL import Image
from PIL import ImageDraw
import tkinter.font as tf
from operator import eq
import time
import tkinter as tk
from runtimetext import f1,f2


im1 = None
img = None
im = None
imgpath = None
photo = None
root= tk.Tk()
root.title('控件')
root.geometry('1500x700') # 这里的乘号不是 * ，而是小写英文字母 x
def tlen(text): #文字宽度测量
    lenTxt = len(text) 
    lenTxt_utf8 = len(text.encode('utf-8')) 
    size = int((lenTxt_utf8 - lenTxt)/2 + lenTxt)
    return size
def run1():
#rs
    mmx = 2048
    mmy = 1278
    size = 30
    y = 0
    x = 0
    my = 10
    mx = 10
    color = "#ffffff"
    func = ''
    efunction = False
    functionlist = []
    t = 'awa'
    color = "#ffffff"
    func = ''
    f = ''
    efunction = False
    functionlist = []
#
    input_text = ttext.get('0.0','end')
    img = Image.open('./chace/ak.png')
    for i in input_text:
        print(i,x,y,functionlist,efunction)
        if efunction == False and eq(i,"\\"):
            efunction=True
            functionlist=[] 
            continue
        elif efunction == True:
            if eq(i,"\\"):
                efunction = False
                continue
            functionlist.append(i)
            continue
        else:
            if functionlist != []:
                text = ''.join(functionlist)
                if text.startswith("n"):
                    print('text')
                    if text.replace('n','') != '':x = int(text.replace('n',''))
                    y += size
                    if x > mx : mx = x
                    if y > my: my = y 
                elif text.startswith("b"):size = int(text.replace('b',''))
                elif text.startswith('#'):color = text
                elif text.startswith('y'):y = int(text.replace('y',''))
                functionlist=[] 
        if i >= u'\u4e00' and i <= u'\u9fa5' or i >= u'\u3040' and i <= u'\u31FF':
            fx = size
            f = f1
        else: 
            fx = size / 2 
            f = f2
        x += fx
        if x > mx: mx = x
        if x + size / 2 > mmx :
            y += size
            if y > my: my = y
            x = 0
    if y == 0:my += size 
    my += 10
    mx += 10
    print('mx:' + str(mx) + "|my:" + str(my))
    ly =  (mmy - my) / 2
    im1 = img.crop((0,ly,mx,ly+my))
    mmx = 2048
    mmy = 1278
    size = 30
    y = 0
    x = 0
    my = 10
    mx = 10
    color = "#ffffff"
    func = ''
    efunction = False
    functionlist = []
    t = 'awa'
    color = "#ffffff"
    func = ''
    f = ''
    efunction = False
    functionlist = []
    for i in input_text:
        if efunction == False and eq(i,"\\"):
            efunction=True
            functionlist=[] 
            continue
        elif efunction == True:
            if eq(i,"\\"):
                efunction = False
                continue
            functionlist.append(i)
            continue
        else:
            if functionlist != []:
                text = ''.join(functionlist)
                if text.startswith("n"):
                    if text.replace('n','') != '':x = int(text.replace('n',''))
                    y += size
                    if x > mx : mx = x
                    if y > my: my = y + size
                elif text.startswith("b"):size = int(text.replace('b',''))
                elif text.startswith('#'):color = text
                elif text.startswith('y'):y = int(text.replace('y',''))
                functionlist = []
        if i >= u'\u4e00' and i <= u'\u9fa5' or i >= u'\u3040' and i <= u'\u31FF':
            fx = size
            f = f1
        else: 
            fx = size / 2 
            f = f2
        ImageDraw.Draw(im1).text((x+2, y+2),i,font=ImageFont.truetype(f,size),fill='#000000',direction=None)
        ImageDraw.Draw(im1).text((x, y),i,font=ImageFont.truetype(f,size),fill=color,direction=None)
        x += fx
        if x + size / 2 > mmx :
            x = 0
            y += size
    canvas.delete(tk.ALL)
    im1.save('./chace/1.gif')
    imgpath = './chace/1.gif'
    im1 = Image.open(imgpath)
    photo = ImageTk.PhotoImage(im1)
    canvas.create_image(840+540-200, 350, image=photo)
    canvas.pack()
    canvas.create_window(350, 200, width=700, height=400,window=ttext)
    canvas.create_window(350, 600, width=700, height=40,window=ttext2) 
    root.mainloop()

    
B = tk.Button(root, text ="点我", command = run1)
B.pack()
canvas = tk.Canvas(root, width=1920,height=700,bd=0, highlightthickness=0)
imgpath = './chace/mainbg.gif'
img = Image.open(imgpath)
photo = ImageTk.PhotoImage(img)
canvas.create_image(840+540-200, 350, image=photo)
canvas.pack()
ft = tf.Font(family='微软雅黑',size = 10)
ttext=tk.Text(root,width=920,height=200,insertbackground='blue', highlightthickness =2,exportselection=0,font=ft)
ttext.pack()
ttext2=tk.Text(root,width=920,height=200,insertbackground='blue', highlightthickness =2,exportselection=0,font=ft)
ttext2.pack()
canvas.create_window(350, 200, width=700, height=400,window=ttext)
canvas.create_window(350, 600, width=700, height=40,window=ttext2)

ttext2.insert('1.0','蓝色命令：##99FFFF   绿色变量：##CCFF33  白色默认：##ffffff    换行：\\n  大小：\\b' )

root.mainloop()