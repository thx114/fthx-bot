from http.client import METHOD_NOT_ALLOWED
import json
from operator import eq
import re
import shutil
from dateutil import rrule
from datetime import datetime
import time
import urllib
from runtimetext import imgh,admin,op,setu_add_,hsomap,sl,thetypes,resotypes,listtype,istomsg,mainmap,f1,f2,hsolvtext,dlmsg,rb,feback,setu_,bot_qq,authkey,host_,setu_remove_,pixiv_name,pixiv_pw,apikey
from urllib.request import urlretrieve
from PIL import ImageFont,ImageDraw
import cv2
from graia.application import Group,Friend
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
from pixivpy3 import *
import sys

api = AppPixivAPI()
#api.login(pixiv_name, pixiv_pw) #如果不想用 请#此行
print("初始化完成")
#读取配置...
feback_data = feback['data']
jsonfile = open("cfg.json","r")
cfg = json.load(jsonfile)
jsonfile.close()
id_data = cfg['id']
fr_data = cfg['fr']
stlist_data = cfg['stlist']
lstfr_data = cfg['lstfr']
lstgr_data = cfg['lstgr']
qdlist_data = cfg['qdlist']
qd_data = cfg['qd']
hsolvmax_data = cfg['hsolvmax']
hsolvch_data = cfg['hsolvch']
null_data = cfg['null']
rel_data = cfg['relist']
sg_data = cfg['sg']
ban_data = cfg['ban']
setuadd = cfg['setuadd']
t_data = cfg['time']
if t_data.startswith("20") == False:
    print('!')
    cfg['time'] = datetime.now().strftime('%Y-%m-%d 10:10:10')
t_data = cfg['time']
print('读取配置完成')
loop = asyncio.get_event_loop()
bcc = Broadcast(loop=loop)
app = GraiaMiraiApplication(
    broadcast=bcc,
    connect_info=Session(
        host=host_,
        authKey=authkey,
        account=bot_qq,
        websocket=True
    )
)
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
def savecfg():
    jsonfile=open("cfg.json","w")
    json.dump(cfg,jsonfile)
    jsonfile.close()
def setu(group,id,g):
    id = str(id)
    hsolv = id_data[id]
    if group in sg_data: 
        print('in')
        hsolvmax = int(str(hsolvmax_data))
        if hsolv <= hsolvmax or int(id) in admin:
            rootdir = setu_
            file_names = []
            for parent,dirnames, filenames in os.walk(rootdir):
                file_names = filenames
            x = random.randint(0, len(file_names)-1)
            df = rootdir + "/" + file_names[x]
            print("选中色图" + df)
            savename = df.replace(setu_,"").replace('.jpg','')
            lstgr_data[id] = savename
            print('done' + df)
            id_data[id] = id_data[id] + 1
            stlist_data[id] = stlist_data[id] + 1
            return df
    print("2级色图")
    if fr_data[id] >= 1:
        rootdir = setu_
        file_names = []
        for parent,dirnames, filenames in os.walk(rootdir):
            file_names = filenames
        x = random.randint(0, len(file_names)-1)
        df = rootdir + "/" + file_names[x]
        savename = df.replace(setu_,"").replace('.jpg','')
        outmsg = 'https://www.pixivdl.net/artworks' + savename
        if g == 1: lstgr_data[id] = savename
        else:      lstfr_data[id] = savename
        fr_data[id] = fr_data[id] - 1
        outmsg = outmsg + "剩余色图：" + str(fr_data[id])
        print('色图请求完成' + outmsg)
        savecfg()
        return outmsg
    else:
        outmsg = "你没有剩余色图或其他错误"
        print('色图请求完成' + outmsg)
        return outmsg
def toimg(msg,fontl,fonty,ism,imgp,cm):
    string = "~!@#$%^&*()_+-*/<>,.[]\/"
    img = Im.open(imgp)
    mmmx = 700
    mmmx = img.size[0]
    mmmy = img.size[1]
    print('绘图开始')
    for i in istomsg:
        msg = msg.replace(str(i),str(istomsg[i]))
    x = y = my = mx = ghs = qaq = mmx = 0
    fx = fx1 = fx2 = fx0 = 30
    ghslist = [] 
    qaqlist = []
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
    else:
        mx = mmmx
        my = mmmy
        x = mmmx
        y = mmmy
    my = y + fx
    if y == 0:
        mx = x + 3
        my = fx + 3
    mx = round(mx)
    my = round(my) + fx / 2 
    print('mx:' + str(mx) + "|my:" + str(my))
    if ism >= 1:
        img = Im.open(imgp)
        x = mx #707 x 1000
        y = my
        ly = ( 1000 - y ) / 2 
        if cm == 0:
            im1 = img.crop((0, ly, mx, my + ly))
        else: 
            im1 = img
    else:   
        im1 = Im.new("RGB" ,(mx,my),(255,255,255))
    x = y = ghs = qaq = 0
    fx = fx0
    fx2 = fx0
    outghs = []
    outqaq = []
    fillColor = "#ffffff"
    print("for2")
    for j in msg :
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
            elif eq(j,'·'):
                pass
            else:
                ImageDraw.Draw(im1).text((x+2, y+2),j,font=font,fill='#000000',direction=None)
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
def csh(id):
    datas = [id_data,fr_data,stlist_data]
    for i in datas :
        if id not in i:
            i[id] = 0
@bcc.receiver("GroupMessage")
async def group_message_handler(app: GraiaMiraiApplication, message: MessageChain, group: Group, member: Member):
    id = str(member.id)
    if int(id) in ban_data:
        return
    file_count = x = 0
    msg = message.asDisplay()
    txt = str(message)
    out1 = txt[txt.rfind('url='):].replace(", path=None, type=<ImageType.Group: \'Group\'>)]","").replace('url=','').replace('\'','')
#@聊天图片检测
    if out1.startswith('http://gchat.qpic.cn') :
        print(out1)
        name = out1.replace('http://gchat.qpic.cn/gchatpic_new/',"").replace("/","").replace('?term=2','')
        file_path = './chace/' + str(group.id) + ".jpg"
        d = file_path
        urlretrieve(out1, d)
        img1=cv2.imread(file_path)
        hash1= dHash(img1)
        hash2= "1101100001010100100000101100001010000010111001011100000010100000"
        n=cmpHash(hash1,hash2)
        if n == 0 :
            csh(id)
            outmsg="未知错误"
            gr = group.id
            mb = member.id
            g = 1
            outmsg = setu(gr,mb,g)
            st = int(str(hsolvch_data))
            if outmsg.startswith('https:') or outmsg.startswith('你'):
                botmsg = await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
                if st > 0:
                    await asyncio.sleep(60)
                    await app.revokeMessage(botmsg)
            else:
                botmsg = await app.sendGroupMessage(group,MessageChain.create([Image.fromLocalFile(outmsg)]))
                if st > 0:
                    await asyncio.sleep(st)
                    await app.revokeMessage(botmsg)
    if txt.find('target=' + str(bot_qq)) >= 1:
        print('发现@')
#@以图搜图
        if out1.startswith('http://gchat.qpic.cn') :
            print('以图搜图')
            url = "https://saucenao.com/search.php?output_type=2&api_key=$key&testmode=1&dbmask=999&numres=1&url=$url".replace('$url',out1).replace('$key',apikey)
            headers = {}
            text = requests.get(url, headers=headers) 
            data = json.loads(text.text)
            data = data['results']
            data = data[0]
            data = data["data"]
            n = 0
            outmsg = ""
            print('done')
            for i in data:
                outmsg = outmsg + '\n' + str(i) + ":" + str(data[i])
            if outmsg.find('urls:[\'https://www.pixiv') >= 1:
                data = data['pixiv_id']
                cfg['setuadd'] = str(data)
            print(msg)
            if msg.find('setu+') >= 1 and member.id in op:
                print('find')
                text = txt.replace('__root__=','').replace('[','').replace(']','')
                arr = text.split('),')
                print(arr)
                for i in arr:
                    if i.find('lain') >=1:
                        arr1 = i.split(', ')
                        truemsg = arr1[1].replace('text=\'','').replace(')','').replace('\'','')
                        newdata = {}
                        print(truemsg)
                        truemsg = truemsg.replace('setu+','').replace(' ','')
                        pid = cfg['setuadd']
                        srcfile= './chace/' + str(group.id) + ".jpg"
                        dstfile=setu_add_ + pid + "_p0.jpg"
                        shutil.move(srcfile,dstfile)
                        outmsg = 'pid:' + pid + '\n已被从qq下载图片并加入色图库'
            await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
#@机器人
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
                newdata = {}
                n = 0
                for i in feback_data:
                    n = n + 1
                    newdata[str(n)] = i
                csh(id)
                hsolv = stlist_data[id]
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
                if r <= r1:
                    data = newdata['1']
                elif r <= r2:
                    data = newdata['2']
                elif r <= r3:
                    data = newdata['3']
                else:
                    print('几率设置错误')
                    data = newdata['1']
                truemsg = truemsg.replace(' ','')
                for i in data:
                    if truemsg.startswith(i):
                        outmsg = 'truemsg in data'
                        text = data[truemsg]
                        arr = text.split('|')
                        max = len(arr) - 1
                        r = random.randint(0,max)
                        outmsg = str(arr[r])
                        await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
#早
    print(msg)
    if msg.startswith('早') and member.id in admin:
        outmsg = '啊啊啊，主人睡傻了QAQ'
        await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
#setu+
    elif msg.startswith('setu+') and member.id in admin:
        pid = int(cfg['setuadd'])
        if msg.startswith('setu+ '):
            msg = msg.replace('setu+','').replace(' ','')
        print(msg)
        if msg.startswith('sf'):
            print(1)
            msg=msg.replace('sf','')
            pid = int(msg)
            print(1.1)
            pach = './chace/' + str(group.id) + ".jpg"
            srcfile=pach
            dstfile=setu_ + str(pid) + "_p0.jpg"
            print(2)
            shutil.move(srcfile,dstfile)
            print('done')
            await app.sendGroupMessage(group,MessageChain.create([Plain(str(pid) + '已从缓存下载并加入色图库')]))
        else:
            pid = int(msg)
            print(pid)
            url = 'https://api.imjad.cn/pixiv/v2/?type=illust&id=$id'.replace('$id',str(pid))
            headers = {}
            text = requests.get(url, headers=headers)
            print('getdone')
            data = json.loads(text.text)
            data = data['illust']
            data1 = data['meta_pages']
            if data1 == []:
                print('null')
                data1 = data['meta_single_page']
                data = data1['original_image_url']
            else:
                data1 = data['meta_pages']
                data = data1[0]
                data = data["image_urls"]
                data = data["original"]
            print(data)
            print('下载开始')
            api.download(data)
            print('下载完成')
            if data.find('png') >=1:
                srcfile='./' + str(pid) + "_p0.png"
                dstfile=setu_ + str(pid) + "_p0.png"
            else:
                srcfile='./' + str(pid) + "_p0.jpg"
                dstfile=setu_ + str(pid) + "_p0.jpg"
            shutil.move(srcfile,dstfile)
            await app.sendGroupMessage(group,MessageChain.create([Plain(str(pid) + '已加入色图库')]))
#菜单
    elif msg.startswith("/help") or msg.startswith('菜单') or msg.startswith('main'):
        print("main")
        ism = 1
        fontl = f1
        fonty = f2
        img = "./chace/mainbg.png"
        msg = mainmap
        cm = 0
        toimg(msg,fontl,fonty,ism,img,cm)
        await app.sendGroupMessage(group,MessageChain.create([Image.fromLocalFile("./chace/1.png")]))
#帮助
    elif msg.startswith('h ') or msg.startswith('/h'):
        msg = msg.replace('h ','').replace('/','')
        ism = 0
        cm = 0
        print('帮助')
        img = "./chace/mainbg.png"
        ism = 1
        if msg.startswith('hsolv'):
            msg = hsolvtext
            toimg(msg,f1,f2,ism,img,cm)
        elif msg.startswith('扫雷'):
            msg = sl
            toimg(msg,f1,f2,ism,img,cm)
        elif msg.startswith('img'):
            msg = imgh
            toimg(msg,f1,f2,ism,img,cm)
        elif msg.startswith('短链'):
            msg = dlmsg
            toimg(msg,f1,f2,ism,img,cm)
        elif msg.startswith('热榜'):
            msg = rb
            toimg(msg,f1,f2,ism,img,cm)
        if ism == 1:
            await app.sendGroupMessage(group,MessageChain.create([Image.fromLocalFile("./chace/1.png")]))
        else:
            await app.sendGroupMessage(group,MessageChain.create([Plain('帮助文本不存在')]))
#汇报不够色rep
    elif msg.startswith("rep"):
        hsolv = stlist_data[id]
        outmsg = "出现未知问题"
        if msg.startswith('rep '):
            if hsolv >= 80 or member.id in op != 0:
                thetext = msg.replace("rep ","")
                file_names = []
                rootdir = setu_
                for filenames in os.walk(rootdir):
                    file_names = filenames
                print(thetext + ".jpg")
                for item in file_names:
                    if thetext + ".jpg" in item != 0:
                        srcfile=setu_ + thetext + ".jpg"
                        dstfile=setu_remove_ + thetext + ".jpg"
                        fpath,fname=os.path.split(dstfile)    
                        if not os.path.exists(fpath):
                            os.makedirs(fpath)                
                        shutil.move(srcfile,dstfile)          
                        outmsg = thetext + "已汇报且暂时移出色图库"
                    else:outmsg = "文件不存在或出现未知问题"
            else:outmsg = "你没有权限执行此操作"
        else:
            print('未知rep')
            gr = str(group.id)
            if hsolv >= 80 or member.id in op != 0:
                name = str(lstgr_data[gr])
                srcfile=setu_ + name + ".jpg"
                dstfile=setu_remove_ + name + ".jpg"
                shutil.move(srcfile,dstfile)
                outmsg = name + "已汇报且暂时移出色图库"
            else:outmsg = "你没有权限执行此操作"
        await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
#撤回时间
    elif msg.startswith("hsolvch") and member.id in admin != 0:
        thetext = msg.replace("hsolvch ","")
        cfg['hsolvch'] = int(thetext)
        outmsg = "撤回时间已改为" + thetext + "秒"
        await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
#色图群权限
    elif msg.startswith("sg") and member.id in admin != 0:
        setugroup = message.asDisplay().replace('sg','')
        outmsg = "发生未知错误"
        theg = setugroup.replace('-','').replace('+','').replace(' ','')
        if theg.isdigit():
            theg = theg
        else:
            theg = str(group.id)
        if int(theg) in sg_data:
            if setugroup.startswith('-'):
                p = sg_data.index(int(theg))
                del sg_data[p]
                outcfg = ','.join(str(i) for i in sg_data)
                cfg['sg'] = sg_data
                outmsg = "已禁用此群的色图权限"
            else:
                outmsg = "此群已是色图群"
        else:
            if setugroup.startswith('-'):
                outmsg = "此群不存在"
            else:
                new = int(theg)
                sg_data.append(new)
                cfg['sg'] = sg_data
                outmsg = "已将此群变更为色图群"
        await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
#ban
    elif msg.startswith("ban") and member.id in admin != 0 :
        
        msg = msg.replace('ban','').replace(' ','')
        if msg.startswith('-'):
            msg = msg.replace('-','')
            ban_data.remove(int(msg))
            outmsg = msg + "ban-"
            cfg['ban'] = ban_data
        else:
            if int(msg) in ban_data != 0:
                outmsg = "已存在"
            else:
                ban_data.append(int(msg))
                outcfg = ','.join(str(i) for i in ban_data)
                cfg['ban'] = ban_data
                outmsg = msg + "ban+"
        await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
#hsolvmax 色图限制
    elif msg.startswith("hsolvmax") and member.id in admin != 0 :
        thetext = msg.replace("hsolvmax ","")
        cfg['hsolvmax'] = int(thetext)
        outmsg = "色图限制上限已被改为" + thetext
        await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
#hso等级清零
    elif msg.startswith("hsolv") and member.id in admin:
        msg = msg.replace("hsolv",'')
        if msg.startswith('- *'):
            outmsg = "所有当天hso等级被清除"
            for i in id_data:
                id_data[i] = 0
            for i in qdlist_data:
                qd_data[i] = 0
            await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
            savecfg()
            srcfile='./cfg.json'
            name = time.strftime('%Y-%m-%d-%H',time.localtime(time.time()))
            dstfile='./backups/'+ name + '.json'
            shutil.move(srcfile,dstfile)
        elif msg.startswith('-'):
            id = int(msg.replace("-","").replace(' ',''))
            id_data[id] = 0
            outmsg = str(id) + "的hso等级已降到0"
            await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
            savecfg()
#backup
    elif msg.startswith('backup') and member.id in admin:
        savecfg()
        srcfile='./cfg.json'
        name = time.strftime('%Y-%m-%d-%H',time.localtime(time.time()))
        dstfile='./backups/'+ name + '.json'
        shutil.move(srcfile,dstfile)
        outmsg = name + '已备份'
        await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
#lsp排行榜
        if msg.startswith('list'):
            print("list读取")
            groupids = []
            hsolvlist = []
            n = 0
            mlist = await app.memberList(group)
            for i in mlist:
                groupids.append(i.id)
            for item in stlist_data:
                if int(item) in groupids != 0:
                    for i in mlist:
                        if i.id == int(item) != 0:
                            itemid = await app.getMember(group,int(item))
                            inmsg = '|$item:$int'.replace('$item',itemid.name).replace('$int',str(stlist_data[item]))
                            hsolvlist.append(str(inmsg))
            res = sorted(hsolvlist, key=lambda x: (lambda y: (int(y[1]), y[0]))(x.split(':')))
            res.reverse()
            out = ''
            for i in res:
                if n == 0:
                    for i in res[n]:
                        r = random.randint(0,18)
                        out = out + '#' + hsomap[r] + ' ' + ''.join(i)
                    res[n] = '\\b30##FF0000' + out
                if n == 1:
                    res[n] = '\\b25##FF0000' + res[n]
                if n == 3:
                    res[n] = '\\b20##FF3300'+ res[n]
                if n == 6:
                    res[n] = '##FF6600'+ res[n]
                if n == 9:
                    res[n] = '##FF9900'+ res[n]
                if n == 12:
                    res[n] = '##FFCC00'+ res[n]
                if n == 15:
                    res[n] = '##FFFF00'+ res[n]
                if n == 18:
                    res[n] = '##FFFF66'+ res[n]
                if n == 21:
                    res[n] = '##FFFFCC'+ res[n]
                if n == 24:
                    res[n] = '##FFFFFF'+ res[n]
                n = n + 1
            a = '‘'.join(res)
            msg = "-lsp排行榜：‘\\b20" + a + "‘    ‘______________________"
            fontl = f1
            fonty = f2
            ism = 1
            cm = 0
            img = "./chace/mainbg.png"
            toimg(msg,fontl,fonty,ism,img,cm)
            await app.sendGroupMessage(group,MessageChain.create([Image.fromLocalFile("./chace/1.png")]))
        else:
            print("printhsolv")
            id = int(msg.replace("-","").replace(' ',''))
            mid = 0
            mid = int(stlist_data[str(id)])
            outmsg = str(id) + "的hso等级为" + str(mid)
            await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
#签到
    elif msg.startswith('签到'):
        stadd = random.randint(5,20)
        outmsg = "签到成功\n群聊色图限制已重置\n随机获得了色图$张"
        datas = [id_data,fr_data,stlist_data,qdlist_data,qd_data]
        u = 0
        for i in datas :
            if id not in i:
                i[id] = 0
                u = u + 1
        if u >= 1: 
            print(id + ':配置初始化完成')
            stadd = stadd + 10
            outmsg = outmsg + "\n使用来份色图获取色图,群内要色图只会发链接(色图群会优先消耗hsolv*),私聊会发图\n这是你第一次签到"
        if qd_data[id] == 0:
            qd_data[id] = 1
            qdlist_data[id] = qdlist_data[id] + 1
            id_data[id] = 0
            fr_data[id] = fr_data[id] + stadd
            outmsg = outmsg.replace('$',str(stadd))
        else:
            outmsg="你今天已经签到过了"
        await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
#img
    elif msg.startswith("img"):
        cm = 0
        if msg.find('!main') >= 1:
            ism = 1
            img = "./chace/mainbg.png"
            msg = msg.replace('!main','')
        elif msg.find('!cimg') >=1:
            ism = 1
            msg = msg[0:msg.rfind('text=')].replace("/r",'').replace('!cimg','')
            cm = 1
            img = './chace/' + str(group.id) + ".jpg"
        else:
            ism = 0
            img = ""
        fontl = f1
        fonty = f2
        msg = msg.replace('img ','')
        toimg(msg,fontl,fonty,ism,img,cm)
        await app.sendGroupMessage(group,MessageChain.create([Image.fromLocalFile("./chace/1.png")]))
#ping
    elif msg.startswith("ping "):
        ip = message.asDisplay().replace('ping ',"")
        url = "http://weijieyue.cn/api/ping.php?ip=$ip".replace('$ip',ip)
        header = {}
        r = requests.get(url, headers=header)
        await app.sendGroupMessage(group,MessageChain.create([Plain(r.text)]))
#舔狗日记
    elif msg.startswith("舔狗日记"):
        cm = 0
        print('请求舔狗日记...')
        url = "http://www.dashige.xyz/API/tgrj/api.php"
        header = {}
        text = requests.get(url, headers=header) 
        msg ="##FFFFFF- "  + text.text + ""
        getimg()
        l = f1
        y = f2
        ism = 1
        img = "./chace/imgchace.jpg"
        toimg(msg,l,y,ism,img,cm)
        await app.sendGroupMessage(group,MessageChain.create([Image.fromLocalFile("./chace/1.png")]))
#run
    elif msg.startswith('run -getimg') and member.id in admin:
        getimg()
#历史上的今天
    elif msg.startswith('历史'):
        cm = 0
        print('请求历史上的今天...')
        url = "http://kumeng.ihcblog.cn/api/today.php"
        header = {}
        text = requests.get(url, headers=header) 
        text = "历史上的今天：" + text.text.replace('1：','$').replace('2：','$').replace('3：','$').replace('4：','$').replace('5：','$').replace('6：','$').replace('7：','$').replace('8：','$').replace('9：','$').replace('注意：由内容过长，只显示10个列','')
        alist = text.split('$')
        msg = '‘'.join(alist)
        l = f1
        y = f2
        ism = 1
        getimg()
        img = "./chace/imgchace.jpg"
        print('调用def...')
        toimg(msg,l,y,ism,img,cm)
        await app.sendGroupMessage(group,MessageChain.create([Image.fromLocalFile("./chace/1.png")]))
#网抑云
    elif msg.startswith('网抑云'):
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
        await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
#群直链
    elif msg.startswith('群直链'):
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
        await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
#直链
    elif msg.startswith('直链'):
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
                outmsg = 'u$u'.replace('$u',outurl)
        else:
            outmsg = '不支持的直链网站或其他错误'
        await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
#短链 1 xxxxxx
    elif msg.startswith('短链 '):
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
        await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
#热榜
    elif msg.startswith('热榜'):
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
                data = rel_data['data']
                listdata = data['list']
                for i in listdata:
                    n = n + 1
                    if ta == n:
                        outmsg = str(i["link"])
                print(2)
                await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
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
                    imgmsg =  imgmsg + '\\n' + str(n) + "_" + rd + "_"  + title 
                l = f1
                y = f2
                ism = 1
                imgp = "./chace/mainbg.jpg"
                cm = 0
                imgmsg = '\\b20' + imgmsg
                cfg['relist'] = data
                toimg(imgmsg,l,y,ism,imgp,cm)   
            await app.sendGroupMessage(group,MessageChain.create([Image.fromLocalFile("./chace/1.png")]))   
#百科
    elif msg.startswith('百科'):
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
        l = f1
        y = f2
        ism = 1
        cm = 0
        text = '/b20' + text[text.rfind('300±'):].replace('300±','') + '/n_____________________________________________________________________________________'
        toimg(text,l,y,ism,img,cm)
        await app.sendGroupMessage(group,MessageChain.create([Image.fromLocalFile("./chace/1.png")]))
#来份色图
    elif msg.startswith("来份色图") or msg.startswith('色图来'):
        csh(id)
        outmsg="未知错误"
        gr = group.id
        mb = member.id
        g = 1
        outmsg = setu(gr,mb,g)
        st = int(str(hsolvch_data))
        if outmsg.startswith('https:') or outmsg.startswith('你'):
            botmsg = await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
            if int(st) > 0:
                await asyncio.sleep(60)
                await app.revokeMessage(botmsg)
        else:
            botmsg = await app.sendGroupMessage(group,MessageChain.create([Image.fromLocalFile(outmsg)]))
            if int(st) > 0:
                await asyncio.sleep(int(st))
                await app.revokeMessage(botmsg)
#不够色
    elif msg.startswith('不够色'):
        await app.sendGroupMessage(group,MessageChain.create([Plain('那你发')]))
#统计色图-
    elif msg.startswith("统计色图"):
        rootdir = setu_
        for dirpath, dirnames, filenames in os.walk(rootdir):
            for file in filenames:
                file_count = file_count + 1
            print(dirpath,file_count)
        msg = "共有$sl张色图".replace("$sl",str(file_count))
        await app.sendGroupMessage(group,MessageChain.create([Plain(msg)]))
#后执行项目
    savecfg()
    initDate = datetime.strptime(t_data,'%Y-%m-%d %H:%M:%S')
    y1 = initDate.year
    m1 = initDate.month
    d1 = initDate.day
    timedata = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    timedata2 = datetime.strptime(timedata,'%Y-%m-%d %H:%M:%S')
    y2 = timedata2.year
    m2 = timedata2.month
    d2 = timedata2.day
    firstDay = datetime(y1,m1,d1)
    endDay = datetime(y2,m2,d2)
    days = rrule.rrule(freq = rrule.DAILY,dtstart=firstDay,until=endDay)
    if days.count() >= 2:
        if not os.path.exists('./backups'):
            os.makedirs('./backups')
        srcfile='./cfg.json'
        name = time.strftime('%Y-%m-%d-%H',time.localtime(time.time()))
        dstfile='./backups/'+ name + '.json'
        shutil.move(srcfile,dstfile)
        timenow = datetime.now().strftime('%Y-%m-%d 10:10:10')
        cfg['time'] = timenow
        savecfg()
        restart_program()

@bcc.receiver("FriendMessage")
async def friend_message_listener(app: GraiaMiraiApplication, friend: Friend ,message:MessageChain):
#qaq
    frid = str(friend.id)
    ban = ban_data
    if str(friend.id) in ban >=1:
        return
    msg = message.asDisplay()
    print(str(friend.id) + msg)
#rep
    if msg.startswith('rep'):
        if friend.id in op != 0:
            print('未知rep')
            gr = str(friend.id)
            name = str(lstfr_data[gr])
            srcfile=setu_ + name + ".jpg"
            dstfile=setu_remove_ + name + ".jpg"
            shutil.move(srcfile,dstfile)
            outmsg = name + "已汇报且暂时移出色图库"
        else:
            outmsg = "你没有权限这样做"
        await app.sendFriendMessage(friend,MessageChain.create([Plain(outmsg)]))
#色图
    elif msg.startswith('来份色图'):
        csh(frid)
        outmsg="未知错误"
        gr = 'none'
        mb = friend.id
        g = 0
        outmsg = setu(gr,mb,g)
        st = int(str(hsolvch_data))
        if outmsg.startswith('https:'):
            botmsg = await app.sendFriendMessage(friend,MessageChain.create([Plain(outmsg)]))
            if int(st) > 0:
                await asyncio.sleep(60)
                await app.revokeMessage(botmsg)  
            return
        else:
            botmsg = await app.sendFriendMessage(friend,MessageChain.create([Image.fromLocalFile(outmsg)]))
            if int(st) > 0:
                await asyncio.sleep(int(st))
                await app.revokeMessage(botmsg)  
            return
    savecfg()




app.launch_blocking()