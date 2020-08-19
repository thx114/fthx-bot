from operator import eq
import shutil
from runtimetext import imgh,admin,op,sl,thetypes,resotypes,listtype,istomsg,mainmap,f1,f2,hsolvtext,dlmsg,rb,feback
from urllib.request import urlretrieve
from PIL import ImageFont,ImageDraw
import cv2
from graia.application import Group,Friend
from graia.application.entry import NewFriendRequestEvent
from graia.application.event.messages import GroupMessage,FriendMessage
from graia.application.group import Member
from graia.application.message.elements.internal import App, Image, Plain
from graia.broadcast import Broadcast
from graia.application import GraiaMiraiApplication, Session
from graia.application.message.chain import MessageChain
import asyncio
import requests
import random
import os
from PIL import Image as Im
import json
loop = asyncio.get_event_loop()
bcc = Broadcast(loop=loop)
app = GraiaMiraiApplication(
    broadcast=bcc,
    connect_info=Session(
        host="http://127.0.0.1:8080", # 填入 httpapi 服务运行的地址
        authKey="authKey", # 填入 authKey
        account=qq, # 你的机器人的 qq 号
        websocket=True
    )
)
def setu(group,id):
    print('色图请求开始')
    f= open(r'setugroup.txt','r')
    cfgin =f.read()
    arr = cfgin.split(',')
    if str(group) in arr != 0 : 
        theid = id
        jsonfile = open("id.json","r")
        data = json.load(jsonfile)
        jsonfile.close()
        if str(id) not in data:
            print("datanot")
            data[theid] = 1
            jsonfile=open("id.json","w")
            json.dump(data,jsonfile)
            jsonfile.close()
        jsonfile = open("id.json","r")
        data = json.load(jsonfile)
        jsonfile.close()
        jsonfile = open("list.json","r")
        data = json.load(jsonfile)
        jsonfile.close()
        if str(id) not in data:
            print("datanot")
            data[theid] = 1
            jsonfile=open("list.json","w")
            json.dump(data,jsonfile)
            jsonfile.close()
        jsonfile = open("list.json","r")
        data = json.load(jsonfile)
        jsonfile.close()
        hsolv = data[str(id)]
        truehso = int(hsolv)
        truehso = truehso + 1
        data[theid] = truehso
        jsonfile=open("list.json","w")
        json.dump(data,jsonfile)
        jsonfile.close()
        jsonfile = open("id.json","r")
        data = json.load(jsonfile)
        jsonfile.close()
        hsolv = data[str(id)]
        f= open(r'hsolv.txt','r')
        hsolvmax =f.read()
        if hsolv <= int(hsolvmax) or id in admin:
            truehso = int(hsolv)
            truehso = truehso + 1
            data[theid] = truehso
            jsonfile=open("id.json","w")
            json.dump(data,jsonfile)
            jsonfile.close()
            PL = "test"
            rootdir = "C:/MIRAI/bot_irori-master/outsetu"
            file_names = []
            for parent,dirnames, filenames in os.walk(rootdir):
                file_names = filenames
            x = random.randint(0, len(file_names)-1)
            df = rootdir + "/" + file_names[x]
            print("选中色图" + df)
            savename = df.replace("C:/MIRAI/bot_irori-master/outsetu/","").replace('.jpg','')
            f= open(r'cs.txt','r')
            st =f.read()
            jsonfile = open("lastsetu.json","r")
            data = json.load(jsonfile)
            jsonfile.close()
            theid = group
            data[theid] = savename
            jsonfile = open("lastsetu.json","w")
            json.dump(data,jsonfile)
            jsonfile.close()
            print('done' + df)
            return df
    print("2级色图")
    jsonfile = open("fr.json","r")
    data = json.load(jsonfile)
    jsonfile.close()
    id = str(id)
    if id not in data:
        data[id] = 10
        jsonfile=open("fr.json","w")
        json.dump(data,jsonfile)
        jsonfile.close()
    jsonfile = open("fr.json","r")
    data = json.load(jsonfile)
    jsonfile.close()
    print('fr')
    if int(str(data[id])) >= 1:
        theid = id
        jsonfile = open("list.json","r")
        data = json.load(jsonfile)
        jsonfile.close()
        if str(id) not in data:
            print("datanot")
            data[id] = 1
            jsonfile=open("list.json","w")
            json.dump(data,jsonfile)
            jsonfile.close()
        jsonfile = open("list.json","r")
        data = json.load(jsonfile)
        jsonfile.close()
        print('list')
        hsolv = data[str(id)]
        truehso = int(hsolv)
        truehso = truehso + 1
        data[id] = truehso
        jsonfile=open("list.json","w")
        json.dump(data,jsonfile)
        jsonfile.close()
        PL = "test"
        rootdir = "C:/MIRAI/bot_irori-master/outsetu"
        file_names = []
        for parent,dirnames, filenames in os.walk(rootdir):
            file_names = filenames
        x = random.randint(0, len(file_names)-1)
        df = rootdir + "/" + file_names[x]
        savename = df.replace("C:/MIRAI/bot_irori-master/outsetu/","").replace('.jpg','')
        outmsg = 'https://www.pixivdl.net/artworks/' + savename
        jsonfile = open("frsetu.json","r")
        data = json.load(jsonfile)
        jsonfile.close()
        theid = id
        data[theid] = savename
        jsonfile = open("frsetu.json","w")
        json.dump(data,jsonfile)
        jsonfile.close()
        jsonfile = open("fr.json","r")
        data = json.load(jsonfile)
        jsonfile.close()
        data[id] = int(str(data[id])) - 1
        outmsg = outmsg + "剩余色图：" + str(data[id])
        jsonfile = open("fr.json","w")
        json.dump(data,jsonfile)
        jsonfile.close()
        print('色图请求完成' + outmsg)
        return outmsg
    else:
        outmsg = "你没有剩余色图或其他错误"
        print('色图请求完成' + outmsg)
        return outmsg
def toimg(msg,fontl,fonty,ism,imgp,cm):
    img = Im.open(imgp)
    mmmx = 700
    mmmx = img.size[0]
    mmmy = img.size[1]
    print('绘图开始')
    for i in istomsg:
        msg = msg.replace(str(i),str(istomsg[i]))
    msg = msg
    x = y = my = mx = ghs = qaq = mmx = 0
    fx = fx1 = fx2 = fx0 = 30
    ghslist = qaqlist = []
    font = ImageFont.truetype(fontl,fx)
    fillColor = "#ffffff"
    print("for1")
    if cm == 0:
        for u in msg :
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
                if '\u4e00' <= u <= '\u9fff':
                    fx1 = fx
                else:
                    fx1 = fx / 2
                if x >= mmmx:
                    mx = mmmx
                    x = 0
                    y = y + fx
                    x = x + fx1
                elif eq(u,"‘"):
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
    else:
        mx = mmmx
        my = mmmy
        x = mmmx
        y = mmmy
    my = y + fx
    if y == 0:
        mx = x + 3
        my = fx + 3
    mx = round(mx) + fx
    my = round(my) + fx
    print('mx:' + str(mx) + "|my:" + str(my))
    fillColor = "#000000"
    if ism >= 1:
        print(imgp)
        img = Im.open(imgp)
        x = mx #707 x 1000
        y = my
        ly = ( 1000 - y ) / 2 
        if cm == 0:
            im1 = img.crop((0, ly, x, y + ly))
        else: 
            im1 = img
    else:   
        im1 = Im.new("RGB" ,(mx,my),(255,255,255))
    x = y = ghs = qaq =0
    fx = fx0
    fx2 = fx0
    outghs = outqaq = []
    print("for2")
    for j in msg :
        if ghs >= 1:
            ghs = ghs + 1
            ghslist.append(j)
            if ghs >= 8:
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
    mx = mx -2
    fx = fx0
    fx2 = fx0
    outghs = outqaq = []
    fillColor = "#ffffff"
    print("for3")
    for j in msg :
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
    im1.save('chace/1.png')
    print("done")
def dHash(img):
    #缩放8*8
    img=cv2.resize(img,(9,8),interpolation=cv2.INTER_CUBIC)
    #转换灰度图
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    hash_str=''
    #每行前一个像素大于后一个像素为1，相反为0，生成哈希
    for i in range(8):
        for j in range(8):
            if   gray[i,j]>gray[i,j+1]:
                hash_str=hash_str+'1'
            else:
                hash_str=hash_str+'0'
    return hash_str
def cmpHash(hash1,hash2):
    n=0
    if len(hash1)!=len(hash2):
        return -1
    for i in range(len(hash1)):
        if hash1[i]!=hash2[i]:
            n=n+1
    return n
def getimg():
    print('请求图片地址')
    url = "https://v1.alapi.cn/api/acg?Token=DQLznnjagptUuvzN9rsC&format=json"
    headers = {
      'Content-Type': 'application/x-www-form-urlencoded',
      'Content-Type': 'application/x-www-form-urlencoded'
    }
    text = requests.request("POST", url, headers=headers)
    print(text.text)
    data = json.loads(text.text)
    print(data)
    if data["code"] != 200:
        print(200)
        outmsg = "发生错误" + str(data["msg"])
    else :
        datain = data['data']
        outurl = str(datain['url'])
        print('请求图片...')
        header = {}
        r = requests.get(url, headers=header)
        file_path = './chace/imgchace.jpg'
        urlretrieve(outurl, file_path)
        print("getimg done")
@bcc.receiver("GroupMessage")
async def group_message_handler(app: GraiaMiraiApplication, message: MessageChain, group: Group, member: Member):
    f= open(r'ban.txt','r')
    cfgin =f.read()
    ban = cfgin.split(',')
    if str(member.id) in ban >=1:
        return
    file_count = x = 0
    msg = message.asDisplay()
    txt = str(message)
    out1 = txt[txt.rfind('url='):].replace(", path=None, type=<ImageType.Group: \'Group\'>)]","").replace('url=','').replace('\'','')
#@机器人
    if txt.find('target=3311409147') >= 1:
        print('请求聊天api...')
        botid = 3311409147
        text = txt.replace('__root__=','').replace('[','').replace(']','')
        arr = text.split('),')
        for i in arr:
            if i.find('ource') >=1:
                arr1 = i.split(', ')
                sourceid = int(arr1[0].replace('Source(id=',''))
            if i.find('t(') >=1:
                arr1 = i.split(', ')
                atid = int(arr1[1].replace('target=',''))
            if i.find('lain') >=1:
                arr1 = i.split(', ')
                truemsg = arr1[1].replace('text=\'','').replace(')','').replace('\'','')
                print(truemsg)
                data = feback
                data = data['data']
                jsonfile = open("null.json","r")
                newdata = json.load(jsonfile)
                jsonfile.close()
                n = 0
                for i in data:
                    n = n + 1
                    newdata[str(n)] = i
                id = member.id
                jsonfile = open("list.json","r")
                data = json.load(jsonfile)
                jsonfile.close()
                if str(id) not in data:
                    data[id] = 1
                    jsonfile=open("list.json","w")
                    json.dump(data,jsonfile)
                    jsonfile.close()
                jsonfile = open("list.json","r")
                data = json.load(jsonfile)
                jsonfile.close()
                hsolv = data[str(id)]
                if hsolv >= 60:
                    r1 = 20
                    r2 = 100
                    r3 = 101
                elif member.id in admin:
                    r1 = 10
                    r2 = 30
                    r3 = 100
                else:
                    r1 = 100
                    r2 = 101
                    r3 = 102
                r = random.randint(1,100)
                print(type(newdata))
                if r <= r1:
                    data = newdata['1']
                elif r <= r2:
                    data = newdata['2']
                elif r <= r3:
                    data = newdata['3']
                print(data)
                truemsg = truemsg.replace(' ','')
                for i in data:
                    if truemsg.startswith(i):
                        print('truemsg in data')
                        outmsg = 'truemsg in data'
                        print(truemsg)
                        text = data[truemsg]
                        print(text)
                        arr = text.split('|')
                        print(arr)
                        max = len(arr) - 1
                        print(max)
                        r = random.randint(0,max)
                        print(r)
                        outmsg = str(arr[r])
                        print(outmsg)
                        return await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
#聊天图片检测
    if out1.startswith('http://gchat.qpic.cn') :
        name = out1.replace('http://gchat.qpic.cn/gchatpic_new/',"").replace("/","").replace('?term=2','')
        file_path = './chace/formqq.jpg'
        d = file_path
        urlretrieve(out1, d)
        img1=cv2.imread('./chace/formqq.jpg')
        hash1= dHash(img1)
        hash2= "1101100001010100100000101100001010000010111001011100000010100000"
        n=cmpHash(hash1,hash2)
        if n == 0 :
            outmsg="未知错误"
            gr = group.id
            mb = member.id
            outmsg = setu(gr,mb)
            f= open(r'cs.txt','r')
            st =f.read()
            if outmsg.startswith('https:'):
                botmsg = await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
                if int(st) > 0:
                    await asyncio.sleep(60)
                    return await app.revokeMessage(botmsg)  
                return
            else:
                botmsg = await app.sendGroupMessage(group,MessageChain.create([Image.fromLocalFile(outmsg)]))
                if int(st) > 0:
                    await asyncio.sleep(int(st))
                    return await app.revokeMessage(botmsg)  
                return
    print(msg)
    if msg.startswith('早'):
        outmsg = '啊啊啊，主人睡傻了QAQ'
        await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
#菜单
    if msg.startswith("/help") or msg.startswith('菜单') or msg.startswith('main'):
        print("main")
        ism = 1
        fontl = f1
        fonty = f2
        img = "./chace/mainbg.png"
        msg = mainmap
        cm = 0
        toimg(msg,fontl,fonty,ism,img,cm)
        return await app.sendGroupMessage(group,MessageChain.create([Image.fromLocalFile("./chace/1.png")]))
#帮助
    if msg.startswith('h ') or msg.startswith('/h'):
        msg = msg.replace('h ','').replace('/','')
        ism = 0
        cm = 0
        print('帮助')
        if msg.startswith('hsolv'):
            fontl = f1
            fonty = f2
            msg = hsolvtext
            img = "./chace/mainbg.png"
            ism = 1
            toimg(msg,fontl,fonty,ism,img,cm)
        if msg.startswith('扫雷'):
            fontl = f1
            fonty = f2
            msg = sl
            img = "./chace/mainbg.png"
            ism = 1
            toimg(msg,fontl,fonty,ism,img,cm)
        if msg.startswith('img'):
            fontl = f1
            fonty = f2
            msg = imgh
            img = "./chace/mainbg.png"
            ism = 1
            toimg(msg,fontl,fonty,ism,img,cm)
        if msg.startswith('短链'):
            fontl = f1
            fonty = f2
            msg = dlmsg
            img = "./chace/mainbg.png"
            ism = 1
            toimg(msg,fontl,fonty,ism,img,cm)
        if msg.startswith('热榜'):
            fontl = f1
            fonty = f2
            msg = rb
            img = "./chace/mainbg.png"
            ism = 1
            toimg(msg,fontl,fonty,ism,img,cm)
        if ism == 1:
            return await app.sendGroupMessage(group,MessageChain.create([Image.fromLocalFile("./chace/1.png")]))
        else:
            return await app.sendGroupMessage(group,MessageChain.create([Plain('帮助文本不存在')]))
#汇报不够色rep
    if msg.startswith("rep"):
        jsonfile = open("id.json","r")
        data = json.load(jsonfile)
        jsonfile.close()
        hsolv = data[str(member.id)]
        outmsg = "出现未知问题"
        if msg.startswith('rep '):
            if hsolv >= 80 or member.id in op != 0:
                thetext = msg.replace("rep ","")
                file_names = []
                rootdir = "C:/MIRAI/bot_irori-master/outsetu"
                for filenames in os.walk(rootdir):
                    file_names = filenames
                print(thetext + ".jpg")
                for item in file_names:
                    if thetext + ".jpg" in item != 0:
                        srcfile='C:/MIRAI/bot_irori-master/outsetu/' + thetext + ".jpg"
                        dstfile='C:/MIRAI/bot_irori-master/setu/' + thetext + ".jpg"
                        fpath,fname=os.path.split(dstfile)    
                        if not os.path.exists(fpath):
                            os.makedirs(fpath)                
                        shutil.move(srcfile,dstfile)          
                        outmsg = thetext + "已汇报且暂时移出色图库"
                    else:
                        outmsg = "文件不存在或出现未知问题"
            else:
                outmsg = "你没有权限执行此操作"
        else:
            print('未知rep')
            jsonfile = open("lastsetu.json","r")
            data = json.load(jsonfile)
            jsonfile.close()
            gr = str(group.id)
            if hsolv >= 80 or member.id in op != 0:
                name = str(data[gr])
                srcfile='C:/MIRAI/bot_irori-master/outsetu/' + name + ".jpg"
                dstfile='C:/MIRAI/bot_irori-master/setu/' + name + ".jpg"
                shutil.move(srcfile,dstfile)
                outmsg = name + "已汇报且暂时移出色图库"
            else:
                outmsg = "你没有权限执行此操作"
        return await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
#撤回时间
    if msg.startswith("hsolvch") and member.id in admin != 0:
        thetext = msg.replace("hsolvch ","")
        print(thetext)
        with open("cs.txt","w") as f:
            f.write(thetext)
        outmsg = "撤回时间已改为" + thetext + "秒"
        return await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
#色图群权限
    if msg.startswith("sg") and member.id in admin != 0:
        setugroup = message.asDisplay().replace('sg','')
        print
        f= open(r'setugroup.txt','r')
        cfgin =f.read()
        arr = cfgin.split(',')
        print(arr)
        outmsg = "发生未知错误"
        theg = setugroup.replace('-','').replace('+','').replace(' ','')
        print(theg)
        if theg in arr != 0:
            print("is in")
            if setugroup.startswith('-'):
                p = arr.index(theg)
                del arr[p]
                outcfg = ','.join(str(i) for i in arr)
                print(outcfg)
                with open("setugroup.txt","w") as f:
                    f.write(outcfg)
                outmsg = "已禁用此群的色图权限"
            else:
                outmsg = "此群已是色图群"
        else:
            print("notin")
            if setugroup.startswith('-'):
                outmsg = "此群不存在"
            else:
                print("no -")
                new = int(setugroup.replace('-','').replace('+','').replace(' ',''))
                print(1)
                arr.append(new)
                print(arr)
                outcfg = ','.join(str(i) for i in arr)
                print(outcfg)
                with open("setugroup.txt","w") as f:
                    f.write(outcfg)
                outmsg = "已将此群变更为色图群"
        return await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
#ban
    if msg.startswith("ban") and member.id in admin != 0 :
        f= open(r'ban.txt','r')
        cfgin =f.read()
        ban = cfgin.split(',')
        msg = msg.replace('ban','').replace(' ','')
        if msg.startswith('-'):
            msg = msg.replace('-','')
            ban.remove(msg)
            outmsg = msg + "ban-"
            outcfg = ','.join(str(i) for i in ban)
            with open("ban.txt","w") as f:
                f.write(outcfg)
            print(outmsg)
        else:
            print(1)
            if msg in ban != 0:
                outmsg = "已存在"
                print(outmsg)
            else:
                print(2)
                ban.append(msg)
                print(3)
                outcfg = ','.join(str(i) for i in ban)
                with open("ban.txt","w") as f:
                    f.write(outcfg)
                outmsg = msg + "ban+"
                print(outmsg)
        return await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
#hsolvmax 色图限制
    if msg.startswith("hsolvmax") and member.id in admin != 0 :
        thetext = msg.replace("hsolvmax ","")
        print(thetext)
        with open("hsolv.txt","w") as f:
            f.write(thetext)
        outmsg = "色图限制上限已被改为" + thetext
        return await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
#hso等级清零
    if msg.startswith("hsolv") and member.id in admin != 0 :
        msg = msg.replace("hsolv",'')
        if msg.startswith('- *'):
            outmsg = "所有当天hso等级被清除"
            jsonfile = open("id.json","r")
            data = json.load(jsonfile)
            jsonfile.close()
            for i in data:
                data[i] = 0
            jsonfile=open("id.json","w")
            json.dump(data,jsonfile)
            jsonfile.close()
            jsonfile = open("qdli.json","r")
            data = json.load(jsonfile)
            jsonfile.close()
            for i in data:
                data[i] = 0
            jsonfile=open("qdli.json","w")
            json.dump(data,jsonfile)
            jsonfile.close()
            return await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
        elif msg.startswith('-'):
            id = int(msg.replace("-","").replace(' ',''))
            print(id)
            jsonfile = open("id.json","r")
            data = json.load(jsonfile)
            jsonfile.close()
            data[id] = 0
            jsonfile=open("id.json","w")
            json.dump(data,jsonfile)
            jsonfile.close()
            print("admin:" + str(id) +str(data[id]))
            outmsg = str(id) + "的hso等级已降到0"
            return await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
#lsp排行榜
        if msg.startswith('list'):
            print("list读取")
            jsonfile = open("list.json","r")
            data = json.load(jsonfile)
            jsonfile.close()
            groupids = []
            hsolvlist = []
            mlist = await app.memberList(group)
            for i in mlist:
                groupids.append(i.id)
            for item in data:
                if int(item) in groupids != 0:
                    for i in mlist:
                        if i.id == int(item) != 0:
                            itemid = await app.getMember(group,int(item))
                            inmsg = '|$item:$int'.replace('$item',itemid.name).replace('$int',str(data[item]))
                            hsolvlist.append(str(inmsg))
            res = sorted(hsolvlist, key=lambda x: (lambda y: (int(y[1]), y[0]))(x.split(':')))
            res.reverse()
            a = '‘'.join(res)
            msg = "-lsp排行榜：‘/b20" + a + "‘    ‘______________________"
            fontl = "C:/WINDOWS/Fonts/ResourceHanRoundedCN-Heavy.ttf"
            fonty = "C:/WINDOWS/Fonts/GenShinGothic-Monospace-Heavy.ttf"
            ism = 1
            cm = 0
            img = "./chace/mainbg.png"
            toimg(msg,fontl,fonty,ism,img,cm)
            return await app.sendGroupMessage(group,MessageChain.create([Image.fromLocalFile("./chace/1.png")]))
        else:
            print("printhsolv")
            id = int(msg.replace("-","").replace(' ',''))
            jsonfile = open("list.json","r")
            data = json.load(jsonfile)
            jsonfile.close()
            mid = 0
            mid = int(data[str(id)])
            outmsg = str(id) + "的hso等级为" + str(mid)
            return await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
#签到
    if msg.startswith('签到'):
        id = str(member.id)
        stadd = random.randint(5,20)
        outmsg = "签到成功\n群聊色图限制已重置\n随机获得了色图$张"
        jsonfile = open("qdli.json","r")
        data = json.load(jsonfile)
        jsonfile.close()
        if str(member.id) not in data:
            data[id] = 0
            jsonfile=open("qdli.json","w")
            json.dump(data,jsonfile)
            jsonfile.close()
        jsonfile = open("qdli.json","r")
        data = json.load(jsonfile)
        jsonfile.close()
        if int(str(data[id])) == 0:
            data[id] = int(str(data[id])) + 1
            jsonfile=open("qdli.json","w")
            json.dump(data,jsonfile)
            jsonfile.close()
            jsonfile = open("qd.json","r")
            data = json.load(jsonfile)
            jsonfile.close()
            print(8)
            if str(member.id) not in data:
                print("datanot")
                data[id] = 0
                jsonfile=open("qd.json","w")
                json.dump(data,jsonfile)
                jsonfile.close()
            jsonfile = open("qd.json","r")
            data = json.load(jsonfile)
            jsonfile.close()
            data[id] = int(str(data[id])) + 1
            jsonfile=open("qd.json","w")
            json.dump(data,jsonfile)
            jsonfile.close()
            jsonfile = open("id.json","r")
            data = json.load(jsonfile)
            jsonfile.close()
            print(1)
            if str(member.id) not in data:
                print("datanot")
                data[id] = 0
                jsonfile=open("id.json","w")
                json.dump(data,jsonfile)
                jsonfile.close()
                outmsg = outmsg + "\n使用来份色图获取色图,群内要色图只会发链接(色图群会优先消耗hsolv*),私聊会发图"
            data[id] = 0
            jsonfile=open("id.json","w")
            json.dump(data,jsonfile)
            jsonfile.close()
            jsonfile = open("fr.json","r")
            data = json.load(jsonfile)
            jsonfile.close()
            if str(member.id) not in data:
                data[id] = 10
                jsonfile=open("fr.json","w")
                json.dump(data,jsonfile)
                jsonfile.close()
                stadd = stadd + 10
                outmsg = outmsg + "\n(这是你第一次签到获取色图)"
            jsonfile = open("fr.json","r")
            data = json.load(jsonfile)
            jsonfile.close()
            dataid = int(str(data[id]))
            dataid = dataid + stadd
            data[id] = dataid
            jsonfile=open("fr.json","w")
            json.dump(data,jsonfile)
            jsonfile.close()
            outmsg = outmsg.replace('$',str(stadd))
        else:
            print('all签到')
            outmsg="你今天已经签到过了"
        
        return await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
#img
    if msg.startswith("img"):
        print('img')
        cm = 0
        if msg.find('!main') >= 1:
            print(1)
            ism = 1
            img = "./chace/mainbg.png"
            msg = msg.replace('!main','')
        elif msg.find('!cimg') >=1:
            print("cimg")
            ism = 1
            msg = msg[0:msg.rfind('text=')].replace("/r",'').replace('!cimg','')
            print(msg)
            cm = 1
            img = "./chace/formqq.jpg"
        else:
            ism = 0
            img = ""
        fontl = "C:/WINDOWS/Fonts/ResourceHanRoundedCN-Heavy.ttf"
        fonty = "C:/WINDOWS/Fonts/GenShinGothic-Monospace-Heavy.ttf"
        msg = msg.replace('img ','')
        toimg(msg,fontl,fonty,ism,img,cm)
        return await app.sendGroupMessage(group,MessageChain.create([Image.fromLocalFile("./chace/1.png")]))
#ping
    if msg.startswith("ping "):
        ip = message.asDisplay().replace('ping ',"")
        url = "http://weijieyue.cn/api/ping.php?ip=$ip".replace('$ip',ip)
        header = {}
        r = requests.get(url, headers=header)
        return await app.sendGroupMessage(group,MessageChain.create([Plain(r.text)]))
#舔狗日记
    if msg.startswith("舔狗日记"):
        cm = 0
        print('请求舔狗日记...')
        url = "http://www.dashige.xyz/API/tgrj/api.php"
        header = {}
        text = requests.get(url, headers=header) 
        msg ="##FFFFFF- "  + text.text + ""
        getimg()
        l = "C:/WINDOWS/Fonts/ResourceHanRoundedCN-Heavy.ttf"
        y = "C:/WINDOWS/Fonts/GenShinGothic-Monospace-Heavy.ttf"
        ism = 1
        img = "./chace/imgchace.jpg"
        print('调用def...')
        toimg(msg,l,y,ism,img,cm)
        return await app.sendGroupMessage(group,MessageChain.create([Image.fromLocalFile("./chace/1.png")]))
#run
    if msg.startswith('run -getimg') and member.id in admin:
        getimg()
#历史上的今天
    if msg.startswith('历史'):
        cm = 0
        print('请求历史上的今天...')
        url = "http://kumeng.ihcblog.cn/api/today.php"
        header = {}
        text = requests.get(url, headers=header) 
        text = "历史上的今天：" + text.text.replace('1：','$').replace('2：','$').replace('3：','$').replace('4：','$').replace('5：','$').replace('6：','$').replace('7：','$').replace('8：','$').replace('9：','$').replace('注意：由内容过长，只显示10个列','')
        alist = text.split('$')
        msg = '‘'.join(alist)
        l = "C:/WINDOWS/Fonts/ResourceHanRoundedCN-Heavy.ttf"
        y = "C:/WINDOWS/Fonts/GenShinGothic-Monospace-Heavy.ttf"
        ism = 1
        getimg()
        img = "./chace/imgchace.jpg"
        print('调用def...')
        toimg(msg,l,y,ism,img,cm)
        return await app.sendGroupMessage(group,MessageChain.create([Image.fromLocalFile("./chace/1.png")]))
#网抑云
    if msg.startswith('网抑云'):
        cm = 0
        print('请求网抑云api...')
        url =  'https://nd.2890.ltd/api/'
        headers = {}
        text = requests.get(url, headers=headers)
        print(1)
        if text.text.find('520: 源站返回未知错误') >=1:
            outmsg='错误：520'
        else:
            print(text.text)
            data = json.loads(text.text)
            data = data['data']
            data = data['content']
            outmsg = str(data['content'])
        return await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
#群直链
    if msg.startswith('群直链'):
        msg = msg.replace('群直链','')
        if msg.startswith(' '):
            msg = msg.replace(' ','')
            qun = msg
        else:
            qun = str(group.id)
        url =  'https://v1.alapi.cn/api/qun?Token=DQLznnjagptUuvzN9rsC&format=json&guin=$id'.replace('$id',qun)
        headers = {'Content-Type': "application/x-www-form-urlencoded"}
        text = requests.request("POST", url, data=url, headers=headers)
        data = json.loads(text.text)
        if data["code"] != 200:
            outmsg = "发生错误" + str(data["msg"])
        else :
            datain = data['data']
            qunid = str(datain['guin'])
            outurl = str(datain['url'])
            outmsg = '群号:$i\n链接:$u'.replace('$i',qunid).replace('$u',outurl)
        return await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
#直链
    if msg.startswith('直链'):
        msg = msg.replace('直链 ','')
        if msg.startswith('www'):
           msg = msg.replace('www','https://www')
        if msg.find('lanzous') >= 1:
            print('蓝奏云解析')
            if msg.find('密码') >= 1:
                mm = msg[msg.rfind('密码'):].replace('密码')
                msg = msg[0:msg.rfind('密码')] 
                url = "https://v1.alapi.cn/api/lanzou?Token=DQLznnjagptUuvzN9rsC&url=$h&format=&$f&$m".replace('$h',msg).replace('$f','json').replace('$m',"pwd=" + mm)
            else:
                url = "https://v1.alapi.cn/api/lanzou?Token=DQLznnjagptUuvzN9rsC&url=$h&format=$f".replace('$h',msg).replace('$f','json')
            headers = {'Content-Type': "application/x-www-form-urlencoded"}
            text = requests.request("POST", url, data=url, headers=headers)
            data = json.loads(text.text)
            if data["code"] != 200:
                outmsg = "发生错误" + str(data["msg"])
            else :
                datain = data['data']
                outurl = str(datain['url'])
                #dataa = data['author']
                #outname = str(dataa['name'])
                outmsg = 'u$u'.replace('$u',outurl)
        else:
            outmsg = '不支持的直链网站或其他错误'
        return await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
#短链 1 xxxxxx
    if msg.startswith('短链 '):
        tt = 1
        uf = ' '
        print('短链' + msg)
        msg = msg.replace('短链 ','')
        for i in thetypes:
            uf = str(i) + " "
            if msg.startswith(uf):
                msg = msg.replace(uf,'')
                tt = uf.replace(' ','')
        msg = msg.replace(uf,'').replace(' ','')
        print('type=',str(tt))
        url = "https://v1.alapi.cn/api/url?url=$u&Token=DQLznnjagptUuvzN9rsC&type=$tt".replace('$tt',str(tt)).replace('$u',msg)
        print(url)
        headers = {'Content-Type': "application/x-www-form-urlencoded"}
        response = requests.request("POST", url, headers=headers)
        print('请求完成')
        outmsg = "发生未知错误"
        data = json.loads(response.text)
        if data["code"] != 200:
            outmsg = "发生错误" + str(data["msg"])
        else :
            datain = data['data']
            outurl = str(datain['short_url'])
            outmsg = str(outurl)
        return await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
#热榜
    if msg.startswith('热榜'):
        qaq = False
        t = "bilibili"
        outmsg = "发生未知错误"
        msg = msg.replace('热榜','').replace(' ','')
        for i in resotypes:
            if msg.startswith(i):
                t = i
                msg = msg.replace(i,'')
        print(t)
        print(msg)
        for i in listtype:
            if msg.startswith(i):
                qaq = True
                ta = int(msg)
                n = 0
                jsonfile = open("relist.json","r")
                data = json.load(jsonfile)
                jsonfile.close()
                data1 = data['data']
                listdata = data1['list']
                for i in listdata:
                    n = n + 1
                    if ta == n:
                        outmsg = str(i["link"])
                print(2)
                return await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
        if qaq == False:
            print('type=',t)
            url = "https://v1.alapi.cn/api/tophub/get?type=$t".replace('$t',t)
            print(url)
            headers = {'Content-Type': "application/x-www-form-urlencoded"}
            response = requests.request("POST", url, headers=headers)
            print('请求完成')
            data = json.loads(response.text)
            if data["code"] != 200:
                outmsg = "发生错误" + str(data["msg"])
            else :
                data1 = data['data']
                listname = str(data1['name'])
                lastupdate = str(data1['last_update'])
                listdata = data1['list']
                imgmsg = listname + '     最后更新时间：' + lastupdate 
                n = 0
                for i in listdata:
                    n = n + 1
                    if n >= 21:
                        break
                    title = str(i['title'])
                    rd = str(i["other"])
                    imgmsg =  imgmsg +'   热度:' + rd + '/n' + str(n) + "_" + title 
                l = "C:/WINDOWS/Fonts/ResourceHanRoundedCN-Heavy.ttf"
                y = "C:/WINDOWS/Fonts/GenShinGothic-Monospace-Heavy.ttf"
                ism = 1
                #getimg()
                imgp = "./chace/mainbg.jpg"
                cm = 0
                imgmsg = '/b20' + imgmsg
                jsonfile=open("relist.json","w")
                json.dump(data,jsonfile)
                jsonfile.close()
                toimg(imgmsg,l,y,ism,imgp,cm)   
            return await app.sendGroupMessage(group,MessageChain.create([Image.fromLocalFile("./chace/1.png")]))   
#百科
    if msg.startswith('百科'):
        msg = msg.replace('百科','')
        print('请求百科...')
        url = "http://beimoapi.xyz/baike/api.php/?msg=$msg".replace('$msg',msg)
        header = {}
        text = requests.get(url, headers=header) 
        text = text.text.replace('/n','/n|').replace('（','(').replace('）',')').replace('《','<').replace('》','>')
        print('下载百科图片...')
        url = text[0:text.rfind('300±')] + "300"
        url = url.replace('±img=','')
        print(url)
        file_path = './chace/baikechace.jpg'
        urlretrieve(url, file_path)
        img = cv2.imread("./chace/baikechace.jpg", -1) 
        fx = fy = 3.6
        print("缩放")
        img = cv2.resize(img, (0, 0), fx=fx, fy=fy, interpolation=cv2.INTER_CUBIC)  
        print("高斯模糊")
        img = cv2.GaussianBlur(img,(13,13),0)
        print("保存文件")
        cv2.imwrite("./chace/baikechace.jpg", img)
        cv2.waitKey(0)  
        img="./chace/baikechace.jpg"
        print('调用def...')
        l = "C:/WINDOWS/Fonts/ResourceHanRoundedCN-Heavy.ttf"
        y = "C:/WINDOWS/Fonts/GenShinGothic-Monospace-Heavy.ttf"
        ism = 1
        cm = 0
        text = '/b20' + text[text.rfind('300±'):].replace('300±','') + '/n___________________________________________________________________________________________________________'
        toimg(text,l,y,ism,img,cm)
        return await app.sendGroupMessage(group,MessageChain.create([Image.fromLocalFile("./chace/1.png")]))
#来份色图
    if msg.startswith("来份色图"):
        outmsg="未知错误"
        gr = group.id
        mb = member.id
        outmsg = setu(gr,mb)
        f= open(r'cs.txt','r')
        st =f.read()
        if outmsg.startswith('https:'):
            botmsg = await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
            if int(st) > 0:
                await asyncio.sleep(60)
                return await app.revokeMessage(botmsg)  
            return
        else:
            botmsg = await app.sendGroupMessage(group,MessageChain.create([Image.fromLocalFile(outmsg)]))
            if int(st) > 0:
                await asyncio.sleep(int(st))
                return await app.revokeMessage(botmsg)  
            return
#统计色图
    if msg.startswith("统计色图"):
        rootdir = "C:/MIRAI/bot_irori-master/outsetu"
        for dirpath, dirnames, filenames in os.walk(rootdir):
            for file in filenames:
                file_count = file_count + 1
            print(dirpath,file_count)
        msg = "共有$sl张色图".replace("$sl",str(file_count))
        return await app.sendGroupMessage(group,MessageChain.create([Plain(msg)]))
#更新色图
    if msg.startswith("更新色图") and member.id in admin:
        al = dl = 0
        from urllib import request
        import xml.dom.minidom
        print("获取列表中..")
        await app.sendGroupMessage(group,MessageChain.create([Plain("获取色图列表中...")]))
        province_info = request.urlopen('https://yande.re/post.xml?tags=pantsu&limit=50')
        DOMTree = xml.dom.minidom.parse(province_info)
        province_data = DOMTree.documentElement
        print(province_data)
        provinces = province_data.getElementsByTagName("post")
        await app.sendGroupMessage(group,MessageChain.create([Plain("下载中")]))
        for province in provinces:
            iurl = province.getAttribute("jpeg_url")
            iid = province.getAttribute("id")
            directoy = 'C:/MIRAI/bot_irori-master/outsetu/'
            target = iid + ".jpg"
            for (root,dirs,files) in os.walk(directoy):
                if target in files:
                    al = al + 1
                else:
                    print(iid + "下载中..")
                    dpath = 'C:/MIRAI/bot_irori-master/setu/$iname.jpg'.replace('$iname',iid)
                    urlretrieve(iurl, dpath)
                    dl = dl + 1
                    print(str(iid) + "下载完成" + str(dl))
        msg = "色图更新完毕！\n[$al个已存在]\n[$dl个色图已下载]".replace('$al',str(al)).replace("$dl",str(dl))
        print(msg)
        return await app.sendGroupMessage(group,MessageChain.create([Plain(msg)]))
#none
@bcc.receiver("FriendMessage")
async def friend_message_listener(app: GraiaMiraiApplication, friend: Friend ,message:MessageChain):
#qaq
    f= open(r'ban.txt','r')
    cfgin =f.read()
    ban = cfgin.split(',')
    if str(friend.id) in ban >=1:
        return
    msg = message.asDisplay()
    print(str(friend.id) + msg)
#rep
    if msg.startswith('rep'):
        if friend.id in op != 0:
            print('未知rep')
            jsonfile = open("frsetu.json","r")
            data = json.load(jsonfile)
            jsonfile.close()
            gr = str(friend.id)
            name = str(data[gr])
            srcfile='C:/MIRAI/bot_irori-master/outsetu/' + name + ".jpg"
            dstfile='C:/MIRAI/bot_irori-master/setu/' + name + ".jpg"
            shutil.move(srcfile,dstfile)
            outmsg = name + "已汇报且暂时移出色图库"
        else:
            outmsg = "你没有权限这样做"
        return await app.sendFriendMessage(friend,MessageChain.create([Plain(outmsg)]))
#色图
    if msg.startswith('来份色图'):
        outmsg="未知错误"
        gr = 'none'
        mb = friend.id
        outmsg = setu(gr,mb)
        f= open(r'cs.txt','r')
        st =f.read()
        if outmsg.startswith('https:'):
            botmsg = await app.sendFriendMessage(friend,MessageChain.create([Plain(outmsg)]))
            if int(st) > 0:
                await asyncio.sleep(60)
                return await app.revokeMessage(botmsg)  
            return
        else:
            botmsg = await app.sendFriendMessage(friend,MessageChain.create([Image.fromLocalFile(outmsg)]))
            if int(st) > 0:
                await asyncio.sleep(int(st))
                return await app.revokeMessage(botmsg)  
            return


@bcc.receiver('NewFriendRequestEvent')
async def NewFriend(app: GraiaMiraiApplication,event:NewFriendRequestEvent):
    print('new')
    event.accept()

    

app.launch_blocking()