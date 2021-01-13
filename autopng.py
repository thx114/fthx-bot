import json
import math
from tkinter.constants import PROJECTING
from PIL import ImageFont,ImageTk
from PIL import Image
from PIL import ImageDraw
import tkinter.font as tf
from operator import eq
import time
import tkinter as tk
from runtimetext import fl1,fl2,maximgpass


im1 = None
img = None
im = None
imgpath = None
photo = None
root= tk.Tk()
root.title('控件')
root.geometry('1500x700') # 这里的乘号不是 * ，而是小写英文字母 x
f1 = fl1
f2 = fl2
def tlen(text): #文字宽度测量
    lenTxt = len(text) 
    lenTxt_utf8 = len(text.encode('utf-8')) 
    size = int((lenTxt_utf8 - lenTxt)/2 + lenTxt)
    return size
def run1():
#rs
    global x
    global y
    global mx
    global my
    global mmx
    global mmy
    global size
    global color
    global pz
    pz = True
    lispuimg = []
    xin = -200
    xout = -100
    yin = -200
    yout = -100
    mmx = 2048
    mmy = 1278
    size = 30
    y = 0 
    x = 0
    my = 10
    mx = 10
    color = "#ffffff"
    efunction = False
    functionlist = []
    f = ''
    '''变量:
    x : 坐标x
    y : 坐标y
    mx :裁剪后图片宽度 (如果要设定必须在末尾)
    my :裁剪后图片长度 (如果要设定必须在末尾)
    mmx :原图大小(如果要设定必须在开头)
    mmy :原图大小(如果要设定必须在开头)
    # "y": y + size 是可行的
    size:目前文字大小
    color:颜色
    '''
    input_text = ttext.get('0.0','end').replace('\n','').replace('\r','')
    img = Image.open('./chace/ak.png')
    for i in input_text: # 遍历所有文字,探测\指令,输出所有文字占图片最大宽 高
        print(i,x,y)
        if efunction == False and eq(i,"\\"): #探测到 \ 则进入功能模式
            efunction=True
            functionlist=[] 
            continue
        elif efunction == True: #功能模式
            if eq(i,"\\"): #在功能模式下再次探测到 \ 则退出功能模式
                efunction = False
                text = ''.join(functionlist)
                if text.startswith("n"): #n:换行
                    if x + size > mx: mx = x + size
                    if y + size > my: my = y + size
                    text = text[1:]
                    if text.isdigit():x = int(text) #n<int> 换行并使x = int
                    if text.startswith('s'):x = x  #ns 换行并保持x
                    else: x = 0
                    y += size
                    if x + size > mx: mx = x + size 
                    if y + size > my: my = y + size
                elif text.startswith("b"):size = int(text[1:]) #b<int>:文字大小
                elif text.startswith('#'):color = text ##<16进制颜色>:文字颜色
                elif text.startswith('y'):y = int(text[1:]) #y<int>:立即切换到y坐标
                elif text.startswith('x'): 
                    """
                    xx<int>: x += int
                    xx-<int>: x -= int

                    xy<int>: y += int
                    xy-<int>: y -= int
                    """
                    text = text[1:]
                    if text.startswith('x'):
                        text = text[1:]
                        if text.startswith('-'):x -= int(text[1:])
                        else: x += int(text)
                    elif text.startswith('y'):
                        text = text[1:]
                        if text.startswith('-'):y -= int(text[1:])
                        else: x += int(text)
                    if x + size > mx: mx = x + size 
                    if y + size > my: my = y + size
                elif text.startswith('p'): #p<图片路径>: 添加图片
                    putpath = text[1:]
                    print(putpath)
                    putimg =  Image.open(putpath)
                    putmx = putimg.size[0]
                    putmy = putimg.size[1]
                    xin = x
                    xout = x + putmx
                    yin = y
                    yout = y + putmy
                    if yout > my: my = yout + size
                    if xout > mx: mx = xout + size
                    print(mx,my)
                    x = x + putmx + 1
                    putdata = {"xin":xin,"xout":xout,"yin":yin,"yout":yout} #因为该图片而产生的文字禁区:(xin,yin),(xout,yout)
                    lispuimg.append(putdata) #所有图片的文字禁区
                elif text.startswith('d'): #p<字典>: 变量修改(可用该功能一次性修改 x y color size 等等)
                    if x + size > mx: mx = x + size
                    if y + size > my: my = y + size
                    testx = 0
                    text = text[1:]
                    print(text)
                    dict_ing = json.loads(text)
                    print('修改:',dict_ing)
                    globals().update(dict_ing)
                    print(testx)
                functionlist=[] 
                continue
            functionlist.append(i) #退出后保存功能模式下所探测的文字到 functionlist
            continue
        if i >= u'\u4e00' and i <= u'\u9fa5' or i >= u'\u3040' and i <= u'\u31FF':#中文
            fx = size
            f = f1
        else:   #如果是英文，使用英文字体，并每次x跃进时只会跃进半个文字大小
            fx = size / 2 
            f = f2
        x += fx
        for r in range(maximgpass): #在 单个文字能跨过(图片中的)图片的最多次数 内循环
            code = False
            if pz == True:
                for i in lispuimg: #文字撞到(图片中的)图片则跃进图片宽度
                    if i['xin'] <= x < i['xout'] and i['yin'] <= y < i['yout']:
                        print('撞到图片啦:',x,y,i['xin'],i['xout'])
                        x = i['xout'] + size
                        code = True
                        break
                    if i['xin'] <= x + size < i['xout'] and i['yin'] <= y < i['yout']:
                        print('撞到图片啦:',x,y,i['xin'],i['xout'])
                        x = i['xout'] + size
                        code = True
                        break
                    if i['xin'] <= x < i['xout'] and i['yin'] <= y + size < i['yout']:
                        print('撞到图片啦:',x,y,i['xin'],i['xout'])
                        x = i['xout'] + size
                        code = True
                        break
                    if i['xin'] <= x + size < i['xout'] and i['yin'] <= y + size < i['yout']:
                        print('撞到图片啦:',x,y,i['xin'],i['xout'])
                        x = i['xout'] + size
                        code = True
                        break
            if x + size / 2 > mmx : #文字撞到边缘则换行
                print(x,y,mmx,mmy)
                if x + size > mx: mx = x + size
                if y + size > my: my = y + size
                x = 0
                y += size
                code = True
            if code == False : break #跳出循环
    if x > mx: mx = x + size
    if y > my: my = y + size
    if my == 0:mx = x + size
    if my == 0:my += size 
    print('mx:' + str(mx) + "|my:" + str(my))
    ly =  (mmy - my) / 2
    im1 = img.crop((0,ly,mx,ly+my))
    mmx = mx
    mmy = my
    size = 30
    y = 0
    x = 0
    color = "#ffffff"
    efunction = False
    functionlist = []
    lispuimg = []
    f = ''
    for i in input_text: # 遍历文字,探测\指令, 在图片内写入 文字/图片
        if efunction == False and eq(i,"\\"): #探测到 \ 则进入功能模式
            efunction=True
            functionlist=[] 
            continue
        elif efunction == True: #功能模式
            if eq(i,"\\"): #在功能模式下再次探测到 \ 则退出功能模式
                efunction = False
                text = ''.join(functionlist)
                if text.startswith("n"): #n:换行
                    text = text[1:]
                    if text.isdigit():x = int(text) #n<int> 换行并使x = int
                    if text.startswith('s'):x = x  #ns 换行并保持x
                    else: x = 0
                    y += size
                elif text.startswith("b"):size = int(text[1:]) #b<int>:文字大小
                elif text.startswith('#'):color = text ##<16进制颜色>:文字颜色
                elif text.startswith('y'):y = int(text[1:]) #y<int>:立即切换到y坐标
                elif text.startswith('x'): 
                    """
                    xx<int>: x += int
                    xx-<int>: x -= int

                    xy<int>: y += int
                    xy-<int>: y -= int
                    """
                    text = text[1:]
                    if text.startswith('x'):
                        text = text[1:]
                        if text.startswith('-'):x -= int(text[1:])
                        else: x += int(text)
                    elif text.startswith('y'):
                        text = text[1:]
                        if text.startswith('-'):y -= int(text[1:])
                        else: x += int(text)
                elif text.startswith('p'): #p<图片路径>: 添加图片
                    print(x,y)
                    putpath = text[1:]
                    putimg =  Image.open(putpath).convert('RGBA')
                    putmx = putimg.size[0]
                    putmy = putimg.size[1]
                    layer = Image.new('RGBA', im1.size, (0,0,0,0))
                    layer.paste(putimg,(math.floor(x),math.floor(y)))
                    im1 = Image.composite(layer, im1, layer)
                    xin = x
                    xout = x + putmx
                    yin = y
                    yout = y + putmy
                    x = x + putmx + 1
                    putdata = {"xin":xin,"xout":xout,"yin":yin,"yout":yout} #因为该图片而产生的文字禁区:(xin,yin),(xout,yout)
                    print(putdata,x,y)
                    lispuimg.append(putdata) #所有图片的文字禁区
                elif text.startswith('d'): #p<字典>: 变量修改(可用该功能一次性修改 x y color size 等等)
                    testx = 0
                    text = text[1:]
                    print(text)
                    dict_ing = json.loads(text)
                    print('修改:',dict_ing)
                    globals().update(dict_ing)
                    print(testx)
                functionlist=[] 
                continue
            functionlist.append(i) #退出后保存功能模式下所探测的文字到 functionlist
            continue
        if i >= u'\u4e00' and i <= u'\u9fa5' or i >= u'\u3040' and i <= u'\u31FF': #中文
            fx = size
            f = f1
        else:  #如果是英文，使用英文字体，并每次x跃进时只会跃进半个文字大小
            fx = size / 2 
            f = f2
        ImageDraw.Draw(im1).text((x+2, y-6),i,font=ImageFont.truetype(f,size),fill='#000000',direction=None) #文字阴影
        ImageDraw.Draw(im1).text((x, y-8),i,font=ImageFont.truetype(f,size),fill=color,direction=None) #文字
        x += fx
        for r in range(maximgpass): #在 单个文字能跨过(图片中的)图片的最多次数 内循环
            code = False
            if pz == True:
                for i in lispuimg: #文字撞到(图片中的)图片则跃进图片宽度
                    if i['xin'] <= x < i['xout'] and i['yin'] <= y < i['yout']:
                        print('撞到图片啦:',x,y,i['xin'],i['xout'])
                        x = i['xout'] + size
                        code = True
                        break
                    if i['xin'] <= x + size < i['xout'] and i['yin'] <= y < i['yout']:
                        print('撞到图片啦:',x,y,i['xin'],i['xout'])
                        x = i['xout'] + size
                        code = True
                        break
                    if i['xin'] <= x < i['xout'] and i['yin'] <= y + size < i['yout']:
                        print('撞到图片啦:',x,y,i['xin'],i['xout'])
                        x = i['xout'] + size
                        code = True
                        break
                    if i['xin'] <= x + size < i['xout'] and i['yin'] <= y + size < i['yout']:
                        print('撞到图片啦:',x,y,i['xin'],i['xout'])
                        x = i['xout'] + size
                        code = True
                        break
            if x + size / 2 > mmx : #文字撞到边缘则换行
                print('撞到墙啦:',x,y)
                x = 0
                y += size
                code = True
            if code == False : break #跳出循环
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