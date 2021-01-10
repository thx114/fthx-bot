import random
import aiohttp
import math
from PIL import ImageFile
from typing_extensions import runtime
ImageFile.LOAD_TRUNCATED_IMAGES = True
from random import randint
import requests
import hashlib
import json
import shutil
from PIL import ImageFont,ImageDraw
from graia.broadcast import Broadcast
from graia.application import GraiaMiraiApplication, Session, message
from graia.application.message.chain import MessageChain
import asyncio
import aiohttp
from graia.application.group import Group, Member
from graia.application.message.elements.internal import At, Image, Plain, Xml
from graia.application.friend import Friend
from operator import eq
from datetime import datetime
import time as Time
from dateutil import rrule
from PIL import Image as Im

import sys
import requests
import os
from runtimetext import lolicon_key,saucenao_key,admin,hsomap,fl1,fl2,authKey,bot_qq,host_,aks_map,aks_map2,aks_map3,aki_map,helptext

loop = asyncio.get_event_loop() 
bcc = Broadcast(loop=loop) 
app = GraiaMiraiApplication(broadcast=bcc,connect_info=Session(host=host_,authKey=authKey,account=bot_qq,websocket=True)) #机器人启动
def sdir(tdir): #新建目录
    if not os.path.exists(tdir):
        print('目标不存在,新建目录:',tdir)
        os.makedirs(tdir)
try:#初始化
    if not os.path.exists('cfg.json'):
        sdir('./r18')
        sdir('./setu')
        sdir('./chace')
        sdir('./backups')
        if not os.path.exists('./chace/mainbg.png'):
            print('错误:没有找到主界面背景')
        cfg = {}
        cfg['hsolvlist'] = {}
        cfg['hsolv'] = {}
        cfg['qd'] = {}
        cfg['qdlist'] = {}
        cfg['last_setu'] = {}
        cfg['hsolvlist']['0'] = 0
        cfg['hsolv']['0'] = 0
        cfg['qd']['0'] = 0
        cfg['qdlist']['0'] = 0
        cfg['setu_group'] = [0]
        cfg['r18_group'] = [0]
        cfg['last_setu']['0'] = 0
        cfg['time'] = datetime.now().strftime('%Y-%m-%d 10:10:10')
        cfg['setu_l'] = 0
        cfg['xml'] = 0
        jsonfile=open("cfg.json","w")
        json.dump(cfg,jsonfile,indent=4)
        jsonfile.close()
        print('初始化完成，你需要在群聊内输入akra来获取明日方舟的数据')
except Exception:print('初始化出现错误')
try:#配置cfg.json读取与补全
    cfgdlist = ['hsolvlist','hsolv','qd','qdlist','last_setu']
    cfgilist = ['setu_l','xml']
    jsonfile = open("cfg.json","r")
    cfg = json.load(jsonfile)
    jsonfile.close()
    for i in cfgdlist:
        try: 
            load = cfg[i]
        except: 
            print('不存在:',i)
            cfg[i] = {}
    for i in cfgilist:
        try: 
            load = cfg[i]
        except: 
            print('不存在:',i)
            cfg[i] = 0
except:pass
try:#配置cfg.json数据转换
    hsolvlist_data = {}
    hsolvlist_data = cfg['hsolvlist']
    hsolv_data = cfg['hsolv']
    qd_data = cfg['qd']
    qdlist_data = cfg['qdlist']
    setu_group = cfg['setu_group']
    r18_group = cfg['r18_group']
    last_setu = cfg['last_setu']
except:print('严重错误，配置读取失败')
try:#方舟json读取
    jsonfile = open("akm.json","r")
    akm_data = json.load(jsonfile)
    jsonfile.close()
    jsonfile = open("aki.json","r")
    aki_data = json.load(jsonfile)
    jsonfile.close()
    jsonfile = open("aks.json","r")
    aks_data = json.load(jsonfile)
    jsonfile.close()
except:print('错误，方舟数据读取失败')

class DF(object): #下载
    async def adf(url,pach):#异步下载
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
        async with aiohttp.ClientSession() as session:
            response = await session.get(headers=headers, url=url)
            content_img = await response.read()
            tempf = open(pach,'w')
            tempf.close()
            with open(pach, 'wb') as f:
                f.write(content_img)
            await session.close()
class CHS(object): #数据初始化
    def chs(id): 
        datas = [hsolv_data,hsolvlist_data,qd_data,qdlist_data]
        for i in datas :
            if id not in i:
                i[id] = 0
async def tlen(text): #文字宽度测量
    lenTxt = len(text) 
    lenTxt_utf8 = len(text.encode('utf-8')) 
    size = int((lenTxt_utf8 - lenTxt)/2 + lenTxt)
    return size
async def dakm(): #明日方舟m数据获取
    apiurl = 'https://penguin-stats.io/PenguinStats/api/v2/result/matrix'
    print('与api沟通中...')
    async with aiohttp.ClientSession() as session:
        async with session.get(apiurl) as resp:
            res_akm_json = await resp.json()
    ak_m = res_akm_json['matrix']
    akm = []
    for i in ak_m:
        end = False
        print(i)
        for item in i:
            if 'end' in item:
                print(i['stageId'],i['itemId'],'已录入')
                end = True
        if end == False:akm.append(i)
    print('done')
    jsonfile=open("akm.json","w")
    json.dump(akm,jsonfile,indent=4)
    jsonfile.close()
    print('json save done')
async def daki(): #明日方舟i数据获取
    apiurl = 'https://penguin-stats.io/PenguinStats/api/v2/items'
    print('与api沟通中...')
    async with aiohttp.ClientSession() as session:
        async with session.get(apiurl) as resp:
            res_aki_json = await resp.json()
    aki = []
    for i in res_aki_json:
        aki_jsoning = {}
        aki_jsoning['itemId'] = i['itemId']
        aki_jsoning['alias'] = i['alias']['zh']
        aki_jsoning['rarity'] = i['rarity']
        print(aki_jsoning['itemId'],aki_jsoning['alias'][0],'已录入')
        aki.append(aki_jsoning)
    print('done')
    jsonfile=open("aki.json","w")
    json.dump(aki,jsonfile,indent=4)
    jsonfile.close()
    print('json save done')
async def daks(): #明日方舟s数据获取
    apiurl = 'https://penguin-stats.io/PenguinStats/api/v2/stages'
    print('与api沟通中...')
    async with aiohttp.ClientSession() as session:
        async with session.get(apiurl) as resp:
            res_aks_json = await resp.json()
    aks = []
    for i in res_aks_json:
        aks_jsoning = {}
        aks_jsoning['stageId'] = i['stageId']
        aks_jsoning['name'] = i['code_i18n']['zh']
        aks_jsoning['stageType'] = i['stageType']
        try:
            aks_jsoning['apCost'] = i['apCost']
        except:pass
        try:
            aks_jsoning['minClearTime'] = i['minClearTime']
        except:pass
        try:
            aks_jsoning['dropInfos'] = i['dropInfos']
        except:pass
        print(aks_jsoning['stageId'],aks_jsoning['name'],'已录入')
        aks.append(aks_jsoning)
    print('done')
    jsonfile=open("aks.json","w")
    json.dump(aks,jsonfile,indent=4)
    jsonfile.close()
    print('json save done')
async def setu(r18,iid,g): #获取色图
    outmsg = {}
    id = str(iid)
    if id not in hsolvlist_data:
        print('初始化',id)
        hsolv_data[id] = 0
        hsolvlist_data[id] = 0
        qd_data[id] = 0
        qdlist_data[id] = 0
    exmsg = "none"
    if qd_data[id] == 0:
        if qdlist_data[id] == 0:
            stadd = random.randint(10,28)
            exmsg = "这是你第一次获取色图,随机获取色图$张".replace('$',str(stadd))
        else:
            stadd = random.randint(6,15)
            exmsg = "今天第一次获取色图，随机获取色图$张".replace('$',str(stadd))
        hsolv_data[id] = hsolv_data[id] + stadd
        qdlist_data[id] = qdlist_data[id] + 1
        qd_data[id] = 1

    if hsolv_data[id] >= 1 and cfg['setu_l'] == 0:
        apiurl = 'https://api.lolicon.app/setu/?apikey=$APIKEY&r18=$R18&num=$NUM'.replace('$APIKEY',lolicon_key).replace('$R18',str(r18)).replace('$NUM',str(1))
        print('与api沟通中...')
        async with aiohttp.ClientSession() as session:
            async with session.get(apiurl) as resp:
                res_json = await resp.json()
        code = res_json['code']
        if code == 429:
            cfg['setu_l'] = 1
            outmsg['extmsg'] = "429错误，达到色图调用上限，切换至本地色图"
            return outmsg
        for i in res_json['data']:
            url_ing = i['url']
            pid_ing = i['pid']
            if r18 == 1:path_ing = './r18/' + str(pid_ing) + '.png'
            else:path_ing = './setu/' + str(pid_ing) + '.png'
            hsolvlist_data[id] = hsolvlist_data[id] + 1
            hsolv_data[id] = hsolv_data[id] - 1
            print(url_ing,pid_ing,'开始下载')
            try:
                await DF.adf(url_ing,path_ing)
                outmsg['imgpath'] = path_ing
                code = True
            except:
                print('连接错误，正在重试....')
                try:
                    await DF.adf(url_ing,path_ing)
                    outmsg['imgpath'] = path_ing
                    code = True
                except:
                    hsolv_data[id] = hsolv_data[id] + 1
                    hsolvlist_data[id] = hsolvlist_data[id] - 1
                    outmsg['extmsg'] = "连接错误，已退回色图。"
            if code == True :
                print('下载成功',path_ing)
                inputimg = Im.open(path_ing)
                mmx = inputimg.size[0]
                mmy = inputimg.size[1]
                print()
                print('下载成功',path_ing,'图片尺寸:',mmx,'x',mmy)
                if mmx > 1080:
                    print('图片过大，处理中..')
                    xyb = mmx / mmy
                    new_mmx = 1080
                    new_mmy = math.floor(new_mmx / xyb)
                    inputimg = inputimg.resize((new_mmx, new_mmy),Im.ANTIALIAS)
                    mmx = inputimg.size[0]
                    mmy = inputimg.size[1]
                    print('新图片大小:',mmx,'|',mmy)
                    inputimg.save(path_ing, 'png')
        gr = str(g)
        outdata = ""
        datamsg = res_json['data'][0]
        for i in datamsg:
            outdata = outdata + i + str(datamsg[i]) 
        outdata = outdata.replace('pid','pid:').replace('p0',' p0 - ').replace('uid','uid:').replace('title','\n标题:').replace('author','   作者:').replace('url','\n').replace('r18False','').replace('r18True','').replace('width','\n').replace('height','x').replace('tags','\n标签:')
        last_setu[gr] = outdata
    elif hsolv_data[id] >= 1 and cfg['setu_l'] == 1:
        if r18 == 0: setu_ = './setu'
        else: setu_ = './r18'
        folder = os.listdir(setu_)
        pach_chace = []
        All_files_pach = []
        for i in folder:
            pach_chace=setu_ +'/' + i
            All_files_pach.append(pach_chace)
        setulen = len(All_files_pach)
        if All_files_pach == []:print('没有找到色图')
        else:print('色图载入成功')
        x = randint(0,setulen)
        filepach = str(All_files_pach[x])
        filename = filepach.replace(setu_ + '/','')
        print("选中色图" + filepach)
        hsolv_data[id] = hsolv_data[id] - 1
        last_setu[str(g)] = filename
        hsolvlist_data[id] = hsolvlist_data[id] + 1
        outmsg['imgpath'] = filepach
    else:
        outmsg['extmsg'] = "你没有剩余色图或其他错误"
    return outmsg
async def rep(l,text): #文字占位处理
    strnone = ' '
    len_ing = await tlen(text)
    if len_ing > l:
        return
    add = strnone * ( l - len_ing)
    out = text + add
    return out
async def settime(time): #时间格式化
    atime = ''
    time_h = math.floor((time/1000)/60/60)
    if time_h != 0:atime = atime + str(time_h) + ':'
    time_m = math.floor((time/1000)/60) - time_h *60
    if time_m != 0:atime = atime + str(time_m) + ':'
    time_s = (math.floor(time/1000) -time_m *60 ) - time_h*60*60
    if time_s != 0:atime = atime + str(time_s)
    return atime
def restart_program(): #重启
    python = sys.executable
    os.execl(python, python, * sys.argv)
def savecfg(): #保存cfg.json
    try:
        jsonfile=open("cfg.json","w")
        json.dump(cfg,jsonfile,indent=4)
        jsonfile.close()
    except Exception:
        print('save cfg 出现错误')
def toimg(msg,img='./chace/mainbg.png',f1=fl1,f2=fl2): #文字转图片
    inputimg = Im.open(img)
    if img != './chace/mainbg.png' : 
        mmx = inputimg.size[0]
        mmy = inputimg.size[1]
#rs
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
#def1
    for i in msg:
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
#rs2
    ly =  (mmy - my) / 2
    outimg = inputimg.crop((0,ly,mx,ly+my))
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
#def2
    for i in msg:
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
        ImageDraw.Draw(outimg).text((x+2, y+2),i,font=ImageFont.truetype(f,size),fill='#000000',direction=None)
        ImageDraw.Draw(outimg).text((x, y),i,font=ImageFont.truetype(f,size),fill=color,direction=None)
        x += fx
        if x + size / 2 > mmx :
            x = 0
            y += size
    outimg.save('./chace/1.png')
    print("done")

@bcc.receiver("GroupMessage")
async def group_listener(app: GraiaMiraiApplication, MessageChain:MessageChain, group: Group, member:Member): #群聊监听
    msg = MessageChain.asDisplay()
    if MessageChain.has(Plain):
        tmsg = str(MessageChain.get(Plain)[0].text)
#图片
    if MessageChain.has(Image):
        timg = MessageChain.get(Image)[0].url
        print(timg)
        if MessageChain.has(At):
            if MessageChain.get(At)[0].target == bot_qq:
#-以图搜图
                print('以图搜图')
                url = "https://saucenao.com/search.php?output_type=2&api_key=$key&testmode=1&dbmask=999&numres=5&url=$url".replace('$url',timg).replace('$key',saucenao_key)
                text = requests.get(url, headers={}) 
                data = json.loads(text.text)
                data = data['results']
                print(data)
                outdata = []
                n = 0
                for i in data:
                    n += 1
                    try:
                        url_ing = ''
                        url_ing = i["data"]['ext_urls'][0]
                        ps_ing = i['header']['similarity'] + '%'
                        url_ing = url_ing.replace('https://www.','')
                        texting = '$n.($%):$url\n'\
                            .replace('$n',str(n))\
                            .replace('$%',ps_ing)\
                            .replace('$url',url_ing)
                        outdata.append(texting)
                    except:
                        pass
                n = 0
                outmsg = ''
                for i in outdata:
                    outmsg = ''.join(outdata)
                await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
#-表情色图来
        if MessageChain.get(Image)[0].imageId == '{B407F708-A2C6-A506-3420-98DF7CAC4A57}.mirai' and group.id in cfg['setu_group']:
            outmsg = await setu(0,member.id,group.id)
            await app.sendGroupMessage(group,MessageChain.create(outmsg))
#普通色图
    if msg.startswith('色图来') and group.id in cfg['setu_group']:
        msg = msg.replace('色图来','').replace(' ','')
        print(msg)
        if msg == '':
            num = 1
        else:
            try:
                num = int(msg)
            except:num = 0
        print(num)
        if num == 0:pass
        elif num > 10:pass
        else:
            for i in range(num):
                outmsg = await setu(0,member.id,group.id)
                if cfg['xml'] == 1:
                    print(outmsg)
                    chace1 = await app.sendGroupMessage(group,MessageChain.create([Image.fromLocalFile(outmsg['imgpath'])]))
                    await asyncio.sleep(1)
                    await app.revokeMessage(chace1)
                    filepach = outmsg['imgpath']
                    fd = open(filepach, "rb")
                    f = fd.read()
                    pmd5 = hashlib.md5(f).hexdigest()
                    inputimg = Im.open(filepach)
                    mmx = inputimg.size[0]
                    mmy = inputimg.size[1]
                    dxy = str(1000)
                    print(pmd5)
                    textxml = '''<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><msg serviceID="5" templateID="1" action="test" brief="[色图]" sourceMsgId="0" url="" flag="2" adverSign="0" multiMsgFlag="0"><item layout="0"><image uuid="2BFB0CD37435F8F52659435EFB9A8396.png" md5="2BFB0CD37435F8F52659435EFB9A8396" GroupFiledid="0" filesize="38504" local_path="/storage/emulated/0/Android/data/com.tencent.mobileqq/Tencent/MobileQQ/chatpic/chatimg/832/Cache_-18f6a103c6617832" minWidth="$x" minHeight="$y" maxWidth="$mx" maxHeight="$my" /></item><source name="" icon="" action="test" appid="-1" /></msg>'''
                    textxml = textxml.replace('2BFB0CD37435F8F52659435EFB9A8396',pmd5)\
                        .replace('$x',str(mmx))\
                        .replace('$y',str(mmy))\
                        .replace('$mx',str(mmx))\
                        .replace('$my',str(mmy))
                    outxml = [Xml(textxml)]
                    await app.sendGroupMessage(group,MessageChain.create(outxml))
                    try:
                        if outmsg['extmsg'] != '':
                            await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg['extmsg'])]))
                    except:pass
                    return
                await app.sendGroupMessage(group,MessageChain.create([Image.fromLocalFile(outmsg['imgpach'])]))
                try:
                    if outmsg['extmsg'] != '':
                        await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg['extmsg'])]))
                except:pass
                await asyncio.sleep(1)
#R18色图
    elif msg.startswith('不够色') and group.id in cfg['r18_group']:
        msg = msg.replace('不够色','').replace(' ','')
        if msg == '':
            num = 1
        else:
            try:
                num = int(msg)
            except:num = 0
        if num == 0:pass
        elif num > 10:pass
        else:
            for i in range(num):
                outmsg = await setu(1,member.id,group.id)
                await app.sendGroupMessage(group,MessageChain.create(outmsg))
#Experimental_xml_setu
    elif msg.startswith('Experimental_xml_setu'):
        msg = msg.replace('Experimental_xml_setu','').replace(' ','')
        if msg == 'on':cfg['xml'] = 1
        elif msg == 'off':cfg['xml'] = 0
        else :pass
#help
    elif msg.startswith('/帮助'):
        text = helptext
        await app.sendGroupMessage(group,MessageChain.create([Plain(text)]))
#test
    elif msg.startswith('test'):
        print(0)
#restart
    elif msg.startswith('restart') and member.id in admin:
        await app.sendGroupMessage(group,MessageChain.create([Plain('执行重启项目----')]))
        restart_program()
#明日方舟企鹅物流物品查询
    elif msg.startswith('ak'):
        msg = msg.replace('ak','').replace(' ','').replace('－','-')
        if msg.startswith('rm') and member.id in admin:
            await dakm()
            await app.sendGroupMessage(group,MessageChain.create([Plain('企鹅物流 - akm 数据下载完成')]))
        if msg.startswith('ri') and member.id in admin:
            await daki()
            await app.sendGroupMessage(group,MessageChain.create([Plain('企鹅物流 - aki 数据下载完成')]))
        if msg.startswith('rs') and member.id in admin:
            await daks()
            await app.sendGroupMessage(group,MessageChain.create([Plain('企鹅物流 - aks 数据下载完成')]))
        if msg.startswith('ra') and member.id in admin:
            await dakm()
            await daki()
            await daks()
            restart_program()
        if msg.startswith('s'):
            msg = msg.replace('s','')
            outdata = {}
            i = {}
            for i in aks_data:
                if msg == i['name']:outdata = i
            if outdata == {} : outmsg = '无结果'
            else:
                sname = await rep(12,outdata['name'])
                scost = await rep(23,str(outdata['apCost']))
                stime0 = await settime(outdata['minClearTime'])
                stime = await rep(41,str(stime0))
                outmsg = aks_map\
                    .replace('sname(12)///',sname)\
                    .replace('scost(23)//////////////',str(scost))\
                    .replace('stime(41)////////////////////////////////',str(stime))
                msglist = []
                for i in outdata['dropInfos']:
                    rarity = 1
                    name = ''
                    outdata2 = {}
                    for o in aki_data:
                        try:
                            if o['itemId'] == i['itemId']:
                                name = o['alias'][0]
                                rarity = o['rarity']
                                break
                        except:pass
                    if name =='':pass
                    else:
                        if rarity == 0: cl = '#FFFFFF\\'
                        elif rarity == 1: cl = '#DFE961\\'
                        elif rarity == 2: cl = '#1AA5E1\\'
                        elif rarity == 3: cl = '#D282DA\\'
                        elif rarity == 4: cl = '#EDCB26\\'
                        else: cl = '#FFFFFF'
                        dname = cl + await rep(16,name)
                        num = str(i['bounds']['lower']) + '~' + str(i['bounds']['upper'])
                        if i['dropType'] == "EXTRA_DROP":num = num + 'ex'
                        dnum = await rep(6,num)
                        plist = []
                        for p in akm_data:
                            if p['stageId'] == outdata['stageId']:
                                plist.append(p)
                        for a in plist:
                            try:
                                if a['itemId'] == i['itemId']:
                                    outdata2 = a
                                    break
                            except:pass
                        if outdata2 == {}:continue
                        else:
                            quantity = outdata2['quantity']
                            times = outdata2['times']
                            if quantity == 0 or times == 0:
                                continue
                            rate = quantity / times
                            prate = rate * 100
                            drate = await rep(7,str(round(prate,2)))
                            lz = round( outdata['apCost'] / rate ,2)
                            dlz = await rep(8,str(lz))
                            time = outdata['minClearTime'] / rate
                            atime = await settime(time)
                            dtime = await rep(9,str(atime))
                        listp = str(math.floor(round(prate,0))).rjust(3,'0')
                        imsg = listp + aks_map2.replace('#FFFFFF\\name(24)////////',dname)
                        imsg = imsg.replace('num(6)',dnum)
                        imsg = imsg.replace('rate(7)',str(drate + '%'))
                        imsg = imsg.replace('lz(8)////',str(dlz))
                        imsg = imsg.replace('time(9)//',str(dtime))
                        print(name,dnum,drate,dlz,dtime)
                        msglist.append(imsg)
                        msglist.sort(reverse=True)
                for i in msglist:
                    i = i[3:]
                    outmsg = outmsg + i
                outmsg = outmsg + aks_map3
                toimg(outmsg,img = "./chace/ak.png" )
                await app.sendGroupMessage(group,MessageChain.create([Image.fromLocalFile("./chace/1.png")]))
        if msg.startswith('i'):
            msg = msg.replace('i','')
            outdata = {}
            for i in aki_data:
                for o in i['alias']:
                    if o == msg:
                        outdata = i
                        iid = i['itemId']
                        break
            iname = await rep(12,outdata['alias'][0])
            irarity = outdata['rarity']
            alias = outdata['alias']
            del alias[0]
            ialias = await rep(49,str(alias))
            ilist = []
            outmsg = aki_map\
                .replace('iname(12)///',iname)\
                .replace('$r',str(irarity) + ' ')\
                .replace('stime(49)////////////////////////////////////////',str(ialias))
            for i in akm_data:#提取
                if i['itemId'] == outdata['itemId']:
                    ilist.append(i)
            msglist =[]
            for o in ilist:#要处理的akm数据 o
                for p in aks_data:#读取物品此时的aks数据 p
                    if o['stageId'] == p['stageId']:
                        sname = '#FFFFFF' + await rep(16,p['name'])
                        try:
                            cost = p['apCost']
                            stime0 = p['minClearTime']
                        except:continue
                        for a in p['dropInfos']:#读取p此时的dropInfos a
                            try:
                                if a['itemId'] == iid:
                                    num = str(a['bounds']['lower']) + '~' + str(a['bounds']['upper'])
                                    dnum = await rep(6,num)
                            except:pass

                quantity = o['quantity']
                times = o['times']
                if quantity == 0 or times == 0:
                    continue
                rate = quantity / times
                prate = rate * 100
                drate = await rep(7,str(round(prate,2)))
                lz = round( cost / rate ,2)
                dlz = await rep(8,str(lz))
                time = stime0 / rate
                atime = await settime(time)
                dtime = await rep(9,str(atime))
                listp = str(math.floor(round(prate,0))).rjust(3,'0')
                imsg = ''
                imsg = listp + aks_map2.replace('#FFFFFFname(23)////////',sname)
                imsg = imsg.replace('num(6)',dnum)
                imsg = imsg.replace('rate(7)',str(drate + '%'))
                imsg = imsg.replace('lz(8)////',str(dlz))
                imsg = imsg.replace('time(9)//',str(dtime))
                print('获取完毕:',sname,dnum,drate,dlz,dtime)
                msglist.append(imsg)
                msglist.sort(reverse=True)
            for i in msglist:
                i = i[3:]
                outmsg = outmsg  + i + '\n'
            outmsg = outmsg + '\n' + aks_map3
            print(outmsg)
            fontl = f1
            fonty = f2
            ism = 1
            cm = 0
            img = "./chace/ak.png"
            toimg(outmsg,fontl,fonty,ism,img,cm)
            await app.sendGroupMessage(group,MessageChain.create([Image.fromLocalFile("./chace/1.png")]))    
#色图info
    elif msg.startswith('info'):
        outmsg = last_setu[str(group.id)]
        await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
#debug
    elif msg.startswith('debug'):
        id = str(member.id)
        info = 'hsolv_data=' +  str(hsolv_data[id]) + '\nhsolvlist_data=' + str(hsolvlist_data[id]) + '\nqd_data=' + str(qd_data[id]) + '\nqdlist_data=' + str(qdlist_data[id])
        await app.sendGroupMessage(group,MessageChain.create([Plain(info)]))
#hsolv
    elif msg.startswith("hsolv") and member.id in admin:
        msg = msg.replace("hsolv",'')
#-重置色图
        if msg.startswith('r') and member.id in admin:
            outmsg = "所有当天获取色图次数被重置"
            for i in qdlist_data:
                qd_data[i] = 0
            await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
            savecfg()
            srcfile='./cfg.json'
            name = Time.strftime('%Y-%m-%d-%H',Time.localtime(Time.time()))
            dstfile='./backups/'+ name + '.json'
            shutil.move(srcfile,dstfile)
#-增加色图
        elif msg.startswith('+') and member.id in admin:
            id = msg.replace("+","").replace(' ','')
            hsolv_data[id] = hsolv_data[id] + 10
            outmsg = str(id) + "的色图增加了10"
            await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
            savecfg()
#-LSP排行榜
        elif msg.startswith('list'):
            print("list读取")
            groupids = []
            hsolvlist = []
            n = 0
            mlist = await app.memberList(group)
            for i in mlist:
                groupids.append(i.id)
            for item in hsolvlist_data:
                try:
                    if int(item) in groupids != 0:
                        for i in mlist:
                            if i.id == int(item) != 0:
                                itemid = await app.getMember(group,int(item))
                                inmsg = '|$item:$int'.replace('$item',itemid.name).replace('$int',str(hsolvlist_data[item]))
                                hsolvlist.append(str(inmsg))
                except:
                    print('err')
                    await app.sendGroupMessage(group,MessageChain.create([Plain('执行此命令时发生了错误')]))

            res = sorted(hsolvlist, key=lambda x: (lambda y: (int(y[1]), y[0]))(x.split(':')))
            res.reverse()
            out = ''
            for i in res:
                if n == 0:
                    for i in res[n]:
                        r = random.randint(0,18)
                        out = out + '#' + hsomap[r] + ''.join(i)
                    res[n] = '\\b30\\\\#FF0000\\' + out
                elif n == 1:
                    res[n] = '\\b25\\\\#FF0000\\' + res[n]
                elif n == 3:
                    res[n] = '\\b20\\\\#FF3300\\'+ res[n]
                elif n == 6:
                    res[n] = '\\#FF6600\\'+ res[n]
                elif n == 9:
                    res[n] = '\\#FF9900\\'+ res[n]
                elif n == 12:
                    res[n] = '\\#FFCC00\\'+ res[n]
                elif n == 15:
                    res[n] = '\\#FFFF00\\'+ res[n]
                elif n == 18:
                    res[n] = '\\#FFFF66\\'+ res[n]
                elif n == 21:
                    res[n] = '\\#FFFFCC\\'+ res[n]
                elif n == 24:
                    res[n] = '\\#FFFFFF\\'+ res[n]
                n = n + 1
            a = '\\n\\'.join(res)
            msg = "-lsp排行榜:‘\\b20\\" + a + "‘    ‘______________________"
            toimg(msg)
            await app.sendGroupMessage(group,MessageChain.create([Image.fromLocalFile("./chace/1.png")]))
#-显示hsolv等级
        else:
            print("printhsolv")
            id = int(msg.replace("-","").replace(' ',''))
            mid = 0
            mid = int(hsolvlist_data[str(id)])
            outmsg = str(id) + "的hso等级为" + str(mid)
            await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
#排行榜
    elif msg.startswith('排行榜'):
        json_result = api.illust_ranking()
        for i in json_result.illusts[:3]:
            api.download(i.image_urls.large)
#备份
    elif msg.startswith('backup') and member.id in admin:
        savecfg()
        srcfile='./cfg.json'
        name = Time.strftime('%Y-%m-%d-%H',Time.localtime(Time.time()))
        dstfile='./backups/'+ name + '.json'
        shutil.move(srcfile,dstfile)
        outmsg = name + '已备份'
        await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
#色图群权限管理
    elif msg.startswith('sg setu') and member.id in admin:
        if group.id in cfg['setu_group']:
            outmsg = '此群已经是色图群'
            if msg.endswith('-'):
                cfg['setu_group'].remove(group.id);outmsg = '此群不再是色图群'
        else: cfg['setu_group'].append(group.id) ; outmsg = '已变成色图群'
        await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
#r18群权限管理
    elif msg.startswith('sg r18'):
        if group.id in cfg['r18_group'] and member.id in admin:
            outmsg = '此群已经是r18群'
            if msg.endswith('-'):
                cfg['r18_group'].remove(group.id);outmsg = '此群不再是r18群'
        else: cfg['r18_group'].append(group.id) ; outmsg = '已变成r18群'
        await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
#后处理项目
    savecfg()
    initDate = datetime.strptime(cfg['time'],'%Y-%m-%d %H:%M:%S')
    timedata = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    timedata2 = datetime.strptime(timedata,'%Y-%m-%d %H:%M:%S')
    firstDay = datetime(initDate.year,initDate.month,initDate.day)
    endDay = datetime(timedata2.year,timedata2.month,timedata2.day)
    days = rrule.rrule(freq = rrule.DAILY,dtstart=firstDay,until=endDay)
    if days.count() >= 2:
        await app.sendGroupMessage(group,MessageChain.create([Plain('执行自动重启项目----')]))
        daki()
        daks()
        dakm()
        if not os.path.exists('./backups'):
            os.makedirs('./backups')
        srcfile='./cfg.json'
        name = Time.strftime('%Y-%m-%d-%H',Time.localtime(Time.time()))
        dstfile='./backups/'+ name + '.json'
        shutil.move(srcfile,dstfile)
        timenow = datetime.now().strftime('%Y-%m-%d 10:10:10')
        cfg['time'] = timenow
        for i in qd_data:
            qd_data[i] = 0
        cfg['setu_l'] = 0
        savecfg()
        restart_program()

app.launch_blocking()