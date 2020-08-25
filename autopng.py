from PIL import ImageFont,ImageTk
from PIL import Image
from PIL import ImageDraw
import tkinter.font as tf
from operator import eq
import time
import tkinter as tk
from runtimetext import f1,f2
root= tk.Tk()
root.title('控件')
root.geometry('1500x700') # 这里的乘号不是 * ，而是小写英文字母 x

im1 = None
img = None
im = None
imgpath = None
photo = None
def run1():
    mmmx = 707
    mmmy = 1000
    thetext = ttext.get('0.0','end')
    print(thetext)
    thetext = thetext.replace("\\n","‘").replace("##","’#").replace("\\b","；").replace("\n","").replace("\\[","【").replace("\\]","】").replace('\\d','：').replace('：',':')
    time.sleep(3)
    from runtimetext import mainmap
    x = y = my = mx = ghs = qaq = mmx = main = xq = 0
    fx = fx1 = fx2 = fx0 = 30
    ghslist = []
    qaqlist = []
    main = 1
    print("输入文字：" + thetext)
    fontl = f1
    fonty = f2
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
                fx1 = int(outqaq)
                fx = int(outqaq)
                outqaq = ""
                qaqlist = []
        else:
            if u >= u'\u4e00' and u <= u'\u9fa5' or u >= u'\u3040' and u <= u'\u31FF':
                fx1 = fx 
            else:
                fx1 = fx / 2
            if x >= mmmx:
                mx = mmmx
                x = 0
                y = y + fx
                x = x + fx1
            elif eq(u,"‘"):
                mmx = x + fx
                if mmx > mmmx: mmx = mmmx
                if mmx > mx:   mx = mmx
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
                if mmx > mx and mx < mmmx - fx1:
                    mx = mmx
        my = y + fx
        if y == 0:
            mx = x + 3
            my = fx + 3
        mx = round(mx)
        my = round(my) + fx / 2 
    print(y)
    mx = round(mx)
    my = round(my)
    print('mx:' + str(mx) + "|my:" + str(my))
    img = Image.open('./chace/mainbg.png')
    ly =  (mmmy - my) / 2
    print(y)
    im1 = img.crop((0,ly,mx,ly+my))
    x = y = ghs = qaq = zx_x = zx = 0
    fx = fx0
    fx2 = fx0
    outghs = []
    outqaq = []
    zxlist = []
    fillColor = "#ffffff"
    print("for3")
    for j in thetext :
        if ghs >= 1:
            ghs = ghs + 1
            ghslist.append(j)
            if ghs >= 8:
                outghs = ''.join(ghslist)
                ghs = 0
                fillColor = outghs
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
        elif zx >=1:
            zx = zx + 1
            zxlist.append(j)
            if j == u'\u3011':
                zx = 0
                x = (mx - zx_x) / 2
                zxlist.remove(j)
                for i in zxlist:
                    if i >= u'\u4e00' and i <= u'\u9fa5' or i >= u'\u3040' and i <= u'\u31FF':
                        font = ImageFont.truetype(fontl,fx)
                        fx2 = fx
                    else:
                        fx2 = fx / 2
                        font = ImageFont.truetype(fonty,fx)
                    print(x,y)
                    ImageDraw.Draw(im1).text((x+2, y+2),i,font=font,fill='#000000',direction=None)
                    ImageDraw.Draw(im1).text((x, y),i,font=font,fill=fillColor,direction=None)
                    x = x + fx2
                x = zx = zx_x = 0
                y = y + fx
                zxlist = []
            else:
                if j >= u'\u4e00' and j <= u'\u9fa5' or j >= u'\u3040' and j <= u'\u31FF':
                    zx_x = zx_x + fx
                else:
                    zx_x = zx_x + fx / 2
        else:
            if j >= u'\u4e00' and j <= u'\u9fa5' or j >= u'\u3040' and j <= u'\u31FF':
                font = ImageFont.truetype(fontl,fx)
                fx2 = fx 
            else:
                fx2 = fx / 2
                font = ImageFont.truetype(fonty,fx)
            if x >= mx - fx2:
                x = 0
                y = y + fx
                ImageDraw.Draw(im1).text((x+2, y+2),j,font=font,fill='#000000',direction=None)
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
            elif eq(j,'：'):
                print(fx)
                y = my - 1.5 * fx 
                print('跳转:',y)
            elif eq(j,'【'):
                x = 0
                zx = 1
            elif eq(j,'·'):
                pass
            else:
                ImageDraw.Draw(im1).text((x+2, y+2),j,font=font,fill='#000000',direction=None)
                ImageDraw.Draw(im1).text((x, y),j,font=font,fill=fillColor,direction=None)
                font = ImageFont.truetype(fontl,fx)
                x = x + fx2
    canvas.delete(tk.ALL)
    im1.save('./chace/1.gif')
    imgpath = './chace/1.gif'
    img = Image.open(imgpath)
    photo = ImageTk.PhotoImage(img)
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