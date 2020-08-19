from PIL import ImageFont,ImageTk
from PIL import Image
from PIL import ImageDraw
import tkinter.font as tf
from operator import eq
import time
import tkinter as tk
root= tk.Tk()
root.title('控件')
root.geometry('1500x700') # 这里的乘号不是 * ，而是小写英文字母 x

im1 = None
img = None
im = None
imgpath = None
photo = None
def run1():
    thetext = ttext.get('0.0','end')
    print(thetext)
    thetext = thetext.replace("\\n","‘").replace("##","’#").replace("\\b","；")
    time.sleep(3)
    from runtimetext import mainmap
    x = y = my = mx = ghs = qaq = mmx = main = xq = 0
    fx = fx1 = fx2 = fx0 = 30
    ghslist = qaqlist = []
    msg = ""
    print(msg)
    main = 1
    print("输入文字：" + thetext)
    fontl = "C:\\WINDOWS\\Fonts\\ResourceHanRoundedCN-Heavy.ttf"
    fonty = "C:\\WINDOWS\\Fonts\\GenShinGothic-Monospace-Heavy.ttf"
    font = ImageFont.truetype(fontl,fx)
    fillColor = "#ffffff"
    for u in thetext :
        if ghs >= 1:
            ghs = ghs + 1
            if ghs >= 8:
                ghs = 0
        elif qaq >= 1:
            qaq = qaq +1
            qaqlist.append(u)
            if qaq >= 3:
                outqaq = ''.join(qaqlist)
                qaq = 0
                print(outqaq)
                fx1 = int(outqaq)
                fx = int(outqaq)
                outqaq = ""
                qaqlist = []
        else:
            if '\u4e00' <= u <= '\u9fff':
                fx1 = fx
            else:
                fx1 = fx / 2
            if x >= 1080:
                mx = x + fx1
                x = 0
                y = y + fx
                x = x + fx1
            elif eq(u,"‘"):
                mx = x + fx1
                x = 0
                y = y + fx
            elif eq(u,"’"):
                ghs = 1
            elif eq(u,"；"):
                qaq = 1
            elif eq(u,'·'):
                pass
            else:
                x = x + fx1
                mmx = x
                if mmx > mx:
                    mx = mmx
    my = y + fx
    if y == 0:
        mx = x + 1
        my = fx + 1
    mx = round(mx) + 2
    my = round(my) + 2
    print(mx)
    print(my)
    fillColor = "#000000"
    if main >= 1:
        img = Image.open("C:\\MIRAI\\fthxbot\\chace\\mainbg.jpg")
        x = mx #707 x 1000
        y = my
        ly = ( 1000 - y ) / 2 
        im1 = img.crop((0, ly, x, y + ly))
    else:
        im1 = Image.new("RGB" ,(mx,my),(255,255,255))
    x = y = ghs = qaq =0
    fx = fx0
    fx2 = fx0
    outghs = outqaq = []
    for j in thetext :
        if ghs >= 1:
            ghs = ghs + 1
            ghslist.append(j)
            if ghs >= 8:
                outghs = ''.join(ghslist)
                outghs = outghs[::-1]
                fillColor = "#000000"
                ghs = 0
                outghs = ""
                ghslist = []
        elif qaq >= 1:
            qaq = qaq + 1
            qaqlist.append(j)
            if qaq >= 3:
                outqaq = ''.join(qaqlist)
                qaq = 0
                fx2 = int(outqaq)
                fx = int(outqaq)
                font = ImageFont.truetype(fontl,fx)
                outqaq = ""
                qaqlist = []
        else:
            if '\u4e00' <= j <= '\u9fff':
                fx2 = fx
            else:
                fx2 = fx / 2
                font = ImageFont.truetype(fonty,fx)
            if x >= mx - fx2:
                x = 0
                y = y + fx
                ImageDraw.Draw(im1).text((x, y),j,font=font,fill=fillColor,direction=None)
                font = ImageFont.truetype(fontl,fx)
                x = x + fx2
            elif eq(j,"‘"):
                x = 0
                y = y + fx
            elif eq(j,"’"):
                ghs = 1
            elif eq(j,"；"):
                qaq = 1
            elif eq(j,'·'):
                pass
            else:
                ImageDraw.Draw(im1).text((x, y),j,font=font,fill=fillColor,direction=None)
                font = ImageFont.truetype(fontl,fx)
                x = x + fx2
    x = y = ghs = qaq =0
    x= -2
    y = -2
    fx = fx0
    fx2 = fx0
    outghs = outqaq = []
    fillColor = "#ffffff"
    for j in thetext :
        if ghs >= 1:
            ghs = ghs + 1
            ghslist.append(j)
            if ghs >= 8:
                outghs = ''.join(ghslist)
                ghs = 0
                fillColor = outghs
                outghs = ""
                ghslist = []
        elif qaq >= 1:
            qaq = qaq + 1
            qaqlist.append(j)
            if qaq >= 3:
                outqaq = ''.join(qaqlist)
                qaq = 0
                fx2 = int(outqaq)
                fx = int(outqaq)
                font = ImageFont.truetype(fontl,fx)
                outqaq = ""
                qaqlist = []
        else:
            if '\u4e00' <= j <= '\u9fff':
                fx2 = fx
            else:
                fx2 = fx / 2
                font = ImageFont.truetype(fonty,fx)
            if x >= mx - fx2:
                x = -2
                y = y + fx
                ImageDraw.Draw(im1).text((x, y),j,font=font,fill=fillColor,direction=None)
                font = ImageFont.truetype(fontl,fx)
                x = x + fx2
            elif eq(j,"‘"):
                x = -2
                y = y + fx
            elif eq(j,"’"):
                ghs = 1
            elif eq(j,"；"):
                qaq = 1
            elif eq(j,'·'):
                pass
            else:
                ImageDraw.Draw(im1).text((x, y),j,font=font,fill=fillColor,direction=None)
                font = ImageFont.truetype(fontl,fx)
                x = x + fx2

    canvas.delete(tk.ALL)
    print(qaq)
    im1.save('./chace/1.gif')
    imgpath = './chace/1.gif'
    img = Image.open(imgpath)
    photo = ImageTk.PhotoImage(img)
    canvas.create_image(840+540-200, 350, image=photo)
    canvas.pack()
    
    canvas.create_window(350, 200, width=700, height=400,
                                       window=ttext)
    canvas.create_window(350, 600, width=700, height=40,
                                       window=ttext2)
                
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
canvas.create_window(350, 200, width=700, height=400,
                                       window=ttext)
canvas.create_window(350, 600, width=700, height=40,
                                       window=ttext2)


ttext2.insert('1.0','蓝色命令：##99FFFF   绿色变量：##CCFF33  白色默认：##ffffff    换行：\\n  大小：\\b' )

root.mainloop()