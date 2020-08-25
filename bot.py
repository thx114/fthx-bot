from http.client import METHOD_NOT_ALLOWED
import json
from operator import eq
from random import randint
import shutil
from tkinter.constants import OUTSIDE
from dateutil import rrule
from datetime import datetime
from runtimetext import stag,hash2,imgh,admin,op,setu_add_,hsomap,sl, stag2,thetypes,resotypes,listtype,istomsg,mainmap,f1,f2,hsolvtext,dlmsg,rb,feback,setu_,bot_qq,authkey,host_,setu_remove_,pixiv_name,pixiv_pw,apikey
from urllib.request import urlretrieve
from PIL import ImageFont,ImageDraw
import cv2
from graia.application import Group,Friend
from graia.application.event.messages import GroupMessage,FriendMessage
from graia.application.group import Member
from graia.application.message.elements.internal import App, At, Image, Plain, Source
from graia.broadcast import Broadcast
from graia.application import GraiaMiraiApplication, Session
from graia.application.message.chain import MessageChain
import asyncio
import requests
import random
from pathlib import Path
import os
from PIL import Image as Im
from pixivpy3 import *
import sys
import time
api = AppPixivAPI()
dirs = './chace/s'
if not os.path.exists(dirs):
    os.makedirs(dirs)
try:
    print('登录pixiv中....')
    #api.login(pixiv_name, pixiv_pw) #如果不想用 请#此行
except Exception:
    print('PixivAPI:登录失败\n会导致:无法使用setu+ [pid]下载色图')
    pass
try:
    fx = 1
    fontl = f1
    fonty = f2
    font = ImageFont.truetype(fontl,fx)
    font = ImageFont.truetype(fonty,fx)
except IOError:
    print('没有找到配置中字体的路径 或 你安装了字体后没有重启\n会导致:任何需要文字到图片的指令将引起崩溃')
    pass

print("初始化完成")
#读取配置...
try:
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
   null_data = cfg['null']
   rel_data = cfg['relist']
   sl_data = cfg['slist']
   if cfg['time'].startswith("20") == False:
        print('!')
        cfg['time'] = datetime.now().strftime('%Y-%m-%d 10:10:10')
except Exception:
    print('严重问题:cfg载入失败,请尝试重置cfg')
try:
    folders = os.listdir(setu_)
    allfolderspach = []
    filepachs = []
    for i in folders:
        folderspach=setu_ +'/' + i  
        for dirpath, dirnames, filenames in os.walk(folderspach):
            for file in filenames:
                filepachs.append(folderspach + '/' + file)
    setulen = len(filepachs)
    if filepachs == []:print('没有找到色图')
    else:print('色图载入成功')
except Exception:
    print('色图载入错误')
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
def sdir(tdir):
    if not os.path.exists(tdir):
        print('新建目录:',tdir)
        os.makedirs(tdir)
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
def savecfg():
    try:
        jsonfile=open("cfg.json","w")
        json.dump(cfg,jsonfile,indent=4)
        jsonfile.close()
    except Exception:
        print('save cfg 出现错误')
def setu(group,id):
    print('开始请求色图')
    id = str(id)
    gr = str(group)
    hsolv = id_data[id]
    outmsg = [(Plain("你没有剩余色图或其他错误"))]
    if group in cfg['sg'] or fr_data[id] >= 1:
        x = randint(0,setulen)
        filepach = str(filepachs[x])
        filename = filepach.replace(setu_ + '/','')
        print("选中色图" + filepach)
        hsolvmax = cfg['hsolvmax']
        if group in cfg['sg'] and hsolv <= hsolvmax: 
            lstgr_data[id] = filename
            id_data[id] = id_data[id] + 1
            stlist_data[id] = stlist_data[id] + 1
            outmsg = [Image.fromLocalFile(filepach)]
        elif fr_data[id] >= 1:
            df = 'https://pixiv.lxns.org/i/' + filename
            if group == 0: lstfr_data[id] = filename
            else:          
                lstgr_data[gr] = filename
                print(lstgr_data[gr])
            fr_data[id] = fr_data[id] - 1
            stlist_data[id] = stlist_data[id] + 1
            savecfg()
            outmsg = [(Plain(df + "剩余色图：" + str(fr_data[id])))]
    return outmsg
    
def toimg(msg,fontl,fonty,ism,imgp,cm):
    img = Im.open(imgp)
    mmmx = 700
    mmmx = img.size[0]
    mmmy = img.size[1]
    mmmmmx = img.size[0]
    mmmmmy = img.size[1]
    print('绘图开始')
    for i in istomsg:
        msg = msg.replace(str(i),str(istomsg[i]))
    print(msg)
    x = y = my = mx = ghs = qaq = mmx = zx = zx_x = 0
    fx = fx1 = fx2 = fx0 = 30
    ghslist = [] 
    qaqlist = []
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
                elif eq(u,'：'):
                    y = mmmmmy - 1.5 * fx 
                    print(y)
                elif eq(u,'·'):
                    pass
                else:
                    x = x + fx1
        my = y + fx
        if y == 0:
            mx = x + 3
            my = fx + 3
        mx = round(mx)
        my = round(my) + fx / 2 
    else:
        mx = mmmx
        my = mmmy
        x = mmmx
        y = mmmy
        mx = round(mx)
        my = round(my)
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
    x = y = ghs = qaq = zx_x = zx = 0
    fx = fx0
    fx2 = fx0
    outghs = []
    outqaq = []
    zxlist = []
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
            elif eq(j,'·'):
                pass
            elif eq(j,'：'):
                print(fx)
                y = my - 1.5 * fx 
                print('跳转:',y)
            elif eq(j,'【'):
                x = 0
                zx = 1
            else:
                ImageDraw.Draw(im1).text((x+2, y+2),j,font=font,fill='#000000',direction=None)
                ImageDraw.Draw(im1).text((x, y),j,font=font,fill=fillColor,direction=None)
                font = ImageFont.truetype(fontl,fx)
                x = x + fx2
    im1.save('chace/1.png')
    print("done")
def dHash(img):
    img=cv2.resize(img,(9,8),interpolation=cv2.INTER_CUBIC)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    hash_str=''
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
def papi(url):
    headers = {}
    text = requests.get(url, headers=headers)
    data = json.loads(text.text)
    data = data['illusts']
    outmsg = ''
    n = 0
    msglist = []
    for i in data:
        if n <= 6:
            r18 = 0
            surl = i['image_urls']['medium']
            tags = i['tags']
            pid = i['id']
            title = i['title']
            print(type(title),title,':',tags)
            for i in tags:
                if i['name'].find('18') >=1:
                    r18 = 1
            if r18 == 0:
                srcfile= './' + str(pid) + "_p0_master1200.jpg"
                dstfile='./chace/s/' + str(pid) + "_p0_master1200.jpg"
                my_file = Path(dstfile)
                print(n,pid,'下载中')
                try:
                   if my_file.is_file() == False:
                       print(1)
                       api.download(surl)
                       print('下载完成')
                       shutil.move(srcfile,dstfile)
                   else:
                       print('略过')
                except Exception:
                    print('none')
                    pass
                outmsg ='\n-' + str(n) + ':' + title 
                msglist.append(Plain(outmsg))
                msglist.append(Image.fromLocalFile(dstfile))
                print('appdone')
            else:
                print(n,pid,'r18被屏蔽')
                outmsg ='\n-' + str(n) + ':' + title + '-r18图不显示预览'
                msglist.append(Plain(outmsg))
            n = n + 1
        else:
            break
    
    msglist.append(Plain('\n通过tp[id]来查看详细信息'))
    cfg['slist'] = data
    if cfg['slist'] == []:
        msglist = [(Plain('没有搜索结果'))]
        
    return msglist

@bcc.receiver("GroupMessage")
async def group_message_handler(app: GraiaMiraiApplication, message: MessageChain, group: Group, member: Member):
    tmsg = ""
    timg = ""
    tat = 0
    id = str(member.id)
    if int(id) in cfg['ban']:
        return
    if message.has((Plain)):tmsg = str(message.get((Plain))[0].text)
    tsource = int(str(message.get((Source))[0].id))
    file_count = x = 0
    msg = message.asDisplay()
#@聊天图片检测
    if message.has((Image)):
        timg = str(message.get(Image)[0].url)
        print(timg)
        file_path = './chace/' + str(group.id) + ".jpg"
        d = file_path
        urlretrieve(timg, d)
        img1=cv2.imread(file_path)
        hash1= dHash(img1)
        n=cmpHash(hash1,hash2)
        if n == 0 :
            csh(id)
            outmsg="未知错误"
            gr = group.id
            mb = member.id
            outmsg = setu(gr,mb)
            st = cfg['hsolvch']
            botmsg = await app.sendGroupMessage(group,MessageChain.create(outmsg))
            await asyncio.sleep(int(st))
            await app.revokeMessage(botmsg)
        if message.has((At)):
            tat = int(str(message.get((At))[0].target))
            if tat == bot_qq:
#@以图搜图
                print('以图搜图')
                url = "https://saucenao.com/search.php?output_type=2&api_key=$key&testmode=1&dbmask=999&numres=1&url=$url".replace('$url',timg).replace('$key',apikey)
                headers = {}
                text = requests.get(url, headers=headers) 
                data = json.loads(text.text)
                datadata = data['results'][0]["data"]
                n = 0
                outmsg = ""
                print('done')
                uid = "justsetu"
                for i in datadata:
                    outmsg = outmsg + '\n' + str(i) + ":" + str(datadata[i])
                if outmsg.find('urls:[\'https://www.pixiv') >= 1:
                    pid = str(datadata['pixiv_id'])
                    uid = str(data['results'][0]['data']['member_id'])
                    cfg['setuadd'] = pid
                    dstfile=setu_ + uid + '/' +  pid + "_p0.jpg"
                    sdir(setu_+ '/' + uid)
                tmsg = tmsg.replace(' ','')
                print(tmsg)
                if msg.find('setu+') >=1 and member.id in op:
                    print('setu+')
                    tmsg = tmsg.replace('setu+','')
                    pid = cfg['setuadd']
                    print(1)
                    srcfile= './chace/' + str(group.id) + ".jpg"
                    dstfile=setu_ + '/' + uid + '/' +  pid + "_p0.jpg"
                    print(dstfile)
                    shutil.move(srcfile,dstfile)
                    print(2)
                    outmsg = 'pid:' + pid + 'by' + uid + '\n已被从qq下载图片并加入色图库'
                await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
#@机器人
    elif message.has((At)):
        tat = int(str(message.get((At))[0].target))
        if tat == bot_qq:
            newdata = {}
            n = 0
            for i in feback_data:
                n = n + 1
                newdata[str(n)] = i
            csh(id)
            hsolv = stlist_data[id]
            if hsolv >= 60:
                r1 = 20
                r2 = 96
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
            tmsg = tmsg.replace(' ','')
            print(tmsg)
            for i in data:
                if tmsg.startswith(i):
                    outmsg = 'truemsg in data'
                    text = data[tmsg]
                    arr = text.split('|')
                    max = len(arr) - 1
                    r = random.randint(0,max)
                    outmsg = str(arr[r])
                    await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
#早
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
            msg=msg.replace('sf','')
            pid = int(msg)
            pach = './chace/' + str(group.id) + ".jpg"
            srcfile=pach
            dstfile=setu_ + 'justsetu' + '/' +  str(pid) + "_p0.jpg"
            shutil.move(srcfile,dstfile)
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
            userid = str(data['user']['id'])
            data1 = data['meta_pages']
            if data1 == []:
                print('null')
                data1 = data['meta_single_page']
                data = data1['original_image_url']
            else:
                data1 = data['meta_pages']
                data = data1[0]["image_urls"]["original"]
            print(data)
            if data.find('png') >=1:
                srcfile='./' + str(pid) + "_p0.png"
                dstfile=setu_ + "/"  + userid + '/' + str(pid) + "_p0.png"
            else:
                srcfile='./' + str(pid) + "_p0.jpg"
                dstfile=setu_ + "/" + userid + '/' +  str(pid) + "_p0.jpg"
            print(srcfile,dstfile)
            my_file = Path(dstfile)
            print(pid,'下载中')
            if my_file.is_file() == False:
                sdir(setu_ + '/' + userid)
                print(1)
                api.download(data)
                print('下载完成'.en)
                shutil.move(srcfile,dstfile)
                await app.sendGroupMessage(group,MessageChain.create([Plain(str(pid) + '已加入色图库')]))
            else:
                print('略过')
                await app.sendGroupMessage(group,MessageChain.create([Plain(dstfile + '已存在')]))
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
#汇报不够色 - rep
    elif msg.startswith("rep"):
        gr = str(group.id)
        msg = msg.replace('rep','')
        hsolv = stlist_data[id]
        if msg.startswith('- ') and member.id in op:
            msg = msg.replace('- ','')
            dstfile=setu_ +'/' + msg.replace('-','/')
            srcfile=setu_remove_ +'/' + msg
            print(srcfile,'to',dstfile,':',gr + '-' + str(member.id))
            shutil.move(srcfile,dstfile)
            outmsg = msg.replace('-','/') + "已恢复"
        elif hsolv >= 80 or member.id in op:
            name = str(lstgr_data[gr])
            srcfile=setu_ +'/' + name
            dstfile=setu_remove_ +'/' + name.replace('/','-')
            print(srcfile,'to',dstfile,':',gr + '-' + str(member.id))
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
        if int(theg) in cfg['sg']:
            if setugroup.startswith('-'):
                p = cfg['sg'].index(int(theg))
                del cfg['sg'][p]
                outmsg = "已禁用此群的色图权限"
            else:
                outmsg = "此群已是色图群"
        else:
            if setugroup.startswith('-'):
                outmsg = "此群不存在"
            else:
                new = int(theg)
                cfg['sg'].append(new)
                outmsg = "已将此群变更为色图群"
        await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
#ban
    elif msg.startswith("ban") and member.id in admin != 0 :
        
        msg = msg.replace('ban','').replace(' ','')
        if msg.startswith('-'):
            msg = msg.replace('-','')
            cfg['ban'].remove(int(msg))
            outmsg = msg + "ban-"
        else:
            if int(msg) in cfg['ban'] != 0:
                outmsg = "已存在"
            else:
                cfg['ban'].append(int(msg))
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
#lsp排行榜
        elif msg.startswith('list'):
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
                        out = out + '#' + hsomap[r] + ''.join(i)
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
            msg = "-lsp排行榜:‘\\b20" + a + "‘    ‘______________________"
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
    elif msg.startswith('backup') and member.id in admin:
        savecfg()
        srcfile='./cfg.json'
        name = time.strftime('%Y-%m-%d-%H',time.localtime(time.time()))
        dstfile='./backups/'+ name + '.json'
        shutil.move(srcfile,dstfile)
        outmsg = name + '已备份'
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
            msg = msg.replace('!cimg','').replace('[图片','')
            msg = msg[0:msg.rfind('text=')].replace("/r",'')
            cm = 1
            img = './chace/' + str(group.id) + ".jpg"
        elif msg.find('!xm') >=1:
            ism = 1
            msg = msg.replace('!xm','')
            msg = msg[0:msg.rfind('text=')].replace("/r",'')
            cm = 1
            img = './chace/xm.jpg'
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
        if msg.startswith('p'):
            csh(id)
            if fr_data[id] >= 3:
                await app.sendGroupMessage(group,MessageChain.create([Plain('你消耗了3个色图进行搜索....')]))
                url = 'https://api.imjad.cn/pixiv/v2/?type=rank'
                msglist = papi(url)
                st = cfg['hsolvch']
                botmsg = await app.sendGroupMessage(group,MessageChain.create(msglist))
                fr_data[id] = fr_data[id] - 3
                savecfg()
                if int(st) > 0:
                    st = int(st)
                    st = st * 8
                    await asyncio.sleep(st)
                    await app.revokeMessage(botmsg)
            else:await app.sendGroupMessage(group,MessageChain.create([Plain('你的剩余色图不足3')]))
        else:
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
        outmsg = setu(gr,mb)
        st = cfg['hsolvch']
        botmsg = await app.sendGroupMessage(group,MessageChain.create(outmsg))
        await asyncio.sleep(int(st))
        await app.revokeMessage(botmsg)
#搜
    elif msg.startswith('搜'):
        csh(id)
        n = 0
        if fr_data[id] >= 3:
            if msg.find('入り')>=1:
                url = 'https://api.imjad.cn/pixiv/v2/?type=search&word=' + msg.replace('搜索','').replace('搜','')
                msglist = papi(url)
                await app.sendGroupMessage(group,MessageChain.create([Plain('你消耗了3个色图进行[指定收藏数]搜索....')]))
            else:
                msglist = [(Plain('没有搜索结果'))]
                for i in stag:
                    imsg = await app.sendGroupMessage(group,MessageChain.create([Plain(stag2[n])]))
                    url = 'https://api.imjad.cn/pixiv/v2/?type=search&word=' + msg.replace('搜索','').replace('搜','') +' ' + stag[n]
                    msglist = papi(url)
                    n = n + 1
                    if msglist != [(Plain('没有搜索结果'))]:
                        print(len(msglist))
                        await app.revokeMessage(imsg)
                        break
                    else:await app.revokeMessage(imsg)
            st = cfg['hsolvch']
            botmsg = await app.sendGroupMessage(group,MessageChain.create(msglist))
            fr_data[id] = fr_data[id] - 3
            if msglist == [(Plain('没有搜索结果'))]:
                fr_data[id] = fr_data[id] + 3
                print('backfr')
            savecfg()
            if int(st) > 0:
                st = int(st)
                st = st * 8
                await asyncio.sleep(st)
                await app.revokeMessage(botmsg)
        else:await app.sendGroupMessage(group,MessageChain.create([Plain('你的剩余色图不足3')]))
#搜 - tp
    if msg.startswith('tp'):
        msg = msg.replace('tp','').replace(' ','')
        setid = int(msg)
        print('选择tp',setid)
        data = cfg['slist'][setid]
        pid = data['id']
        title = data['title']
        user = data['user']['name']
        tags = data['tags']
        tag = ''
        print(1)
        for i in tags:
            tag = tag + '|' + i['name']
        print(tag)
        ptime = data['create_date']
        try:
            imgurl = data['meta_single_page']['original_image_url']
        except Exception:
            imgurl = data['meta_pages'][0]['image_urls']['original']
        await app.sendGroupMessage(group,MessageChain.create([Plain('原图下载中..')]))
        api.download(imgurl)
        print('下载完成')
        if imgurl.find('png') >=1:
            srcfile='./' + str(pid) + "_p0.png"
            dstfile='./chace/s/tp.png'
        else:
            srcfile='./' + str(pid) + "_p0.jpg"
            dstfile='./chace/s/tp.jpg'
        shutil.move(srcfile,dstfile)
        outmsg1 = "id:" + str(pid) + '|标题:' + title + '|by - ' + user
        outmsg2 = 'tags:' + tag + '\n创建时间:' + ptime
        if tag.find('18') >=1:
            print(tag)
            await app.sendGroupMessage(group,MessageChain.create([Plain('r18图不支持tp')]))
        else:
            st = cfg['hsolvch']
            botmsg = await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg1),Image.fromLocalFile(dstfile),Plain(outmsg2)]))
            if int(st) > 0:
                st = int(st) * 3
                await asyncio.sleep(st)
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
    print(msg)
    savecfg()
    initDate = datetime.strptime(cfg['time'],'%Y-%m-%d %H:%M:%S')
    timedata = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    timedata2 = datetime.strptime(timedata,'%Y-%m-%d %H:%M:%S')
    firstDay = datetime(initDate.year,initDate.month,initDate.day)
    endDay = datetime(timedata2.year,timedata2.month,timedata2.day)
    days = rrule.rrule(freq = rrule.DAILY,dtstart=firstDay,until=endDay)
    if days.count() >= 2:
        await app.sendGroupMessage(group,MessageChain.create([Plain('执行自动重启项目----')]))
        if not os.path.exists('./backups'):
            os.makedirs('./backups')
        srcfile='./cfg.json'
        name = time.strftime('%Y-%m-%d-%H',time.localtime(time.time()))
        dstfile='./backups/'+ name + '.json'
        shutil.move(srcfile,dstfile)
        timenow = datetime.now().strftime('%Y-%m-%d 10:10:10')
        cfg['time'] = timenow
        for i in id_data:
            id_data[i] = 0
        for i in qdlist_data:
            qd_data[i] = 0
        savecfg()
        restart_program()

@bcc.receiver("FriendMessage")
async def friend_message_listener(app: GraiaMiraiApplication, friend: Friend ,message:MessageChain):
#qaq
    frid = str(friend.id)
    ban = cfg['ban']
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
        gr = 0
        mb = friend.id
        outmsg = setu(gr,mb)
        st = cfg['hsolvch']
        botmsg = await app.sendFriendMessage(friend,MessageChain.create(outmsg))
        await asyncio.sleep(int(st))
        await app.revokeMessage(botmsg)
    savecfg()


app.launch_blocking()