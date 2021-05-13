from asyncio.tasks import wait
import random
import threading
import aiohttp
import math
from PIL import ImageFile
from aiohttp.client import ClientSession
from bs4 import BeautifulSoup
from graia.application import group
from graia.application.entities import UploadMethods
import imageio
from moviepy.video.VideoClip import ImageClip
ImageFile.LOAD_TRUNCATED_IMAGES = True
from random import randint
import requests
import hashlib
import json
import shutil
import cv2
import _thread
from PIL import ImageFont,ImageDraw
from graia.broadcast import Broadcast
from graia.application import GraiaMiraiApplication, Session, message
from graia.application.event.messages import GroupMessage
from graia.application.event.mirai import MemberJoinEvent, NewFriendRequestEvent
from graia.application.message.chain import MessageChain
from graia.saya import Saya
from graia.saya.builtins.broadcast import BroadcastBehaviour
import asyncio
import aiohttp
from graia.application.group import Group, Member
from graia.application.message.elements.internal import At, Image, Plain, Poke, Quote, Xml,Json,App,Source
from graia.broadcast.interrupt import InterruptControl
from graia.broadcast.interrupt.waiter import Waiter
from operator import eq
from datetime import datetime
import time as Time
from dateutil import rrule
from PIL import Image as Im
from pixivpy3 import *
import sys
import greenlet
import requests
import os
from os.path import join, getsize
from threading import Thread
import zipfile
from asyncio.subprocess import PIPE, STDOUT
from runtimetext import lolicon_key,saucenao_key,admin,hsomap,fl1,fl2,authKey,bot_qq,host_,aks_map,aks_map2,aks_map3,aki_map\
    ,helptext,refresh_token,maxx_img,infomap,maximgpass,xmlimg_group,oncesetuadd,setus,Search_map,Search_map2,stag,stag2,xmloffline

global is_run
global execout
api = AppPixivAPI()
loop = asyncio.get_event_loop() 
is_run = False
def sdir(tdir): #新建目录
    if not os.path.exists(tdir):
        print('目标不存在,新建目录:',tdir)
        os.makedirs(tdir)

try: #start
    try:#初始化
        if not os.path.exists('cfg.json'):
            if not os.path.exists('./chace/mainbg.png'):print('错误:没有找到主界面背景')
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
            cfg['time'] = math.floor( Time.time() / 60 / 60 / 24 )
            cfg['cooling'] = math.floor( Time.time())
            cfg['setu_l'] = 0
            cfg['xml'] = 0
            cfg['info'] = 0
            cfg['revoke'] = 0
            cfg['debug'] = 0
            jsonfile=open("cfg.json","w")
            json.dump(cfg,jsonfile,indent=4)
            jsonfile.close()
            print('初始化完成，你需要在群聊内输入akra来获取明日方舟的数据')
    except Exception:print('初始化出现错误')
    jsonfile = open("cfg.json","r")
    cfg = json.load(jsonfile)
    jsonfile.close()
    try:#配置补全
        for i in ['setu','chace','backups','listpiv','r18','setu','listpsh']:
            sdir('./'+i)
        for i in ['hsolvlist','hsolv','qd','qdlist','last_setu','plinfodata','setus','last_s']:
            try:load = cfg[i]
            except:cfg[i] = {}
        for i in ['setu_l','xml','revoke','info','debug']:
            try: load = cfg[i]
            except: cfg[i] = 0
        try: load = cfg['cooling']
        except:cfg['cooling'] = math.floor(Time.time())
        try:load = cfg['setus']['r18']
        except:cfg['setus']['r18'] = []
        try:load = cfg['setus']['setu']
        except:cfg['setus']['setu'] = []
    except:print('配置补全错误')
    try:#时间转换
        initDate = datetime.strptime(cfg['time'],'%Y-%m-%d %H:%M:%S')
        cfg['time'] = math.floor( Time.time() / 60 / 60 / 24 )
        print('更新时间配置')
    except:pass
    if type(cfg['time']) == float:
        cfg['time'] = math.floor( Time.time() / 60 / 60 / 24 )
        print('更新时间配置')
    try:
        hsolvlist_data = cfg['hsolvlist']
        hsolv_data = cfg['hsolv']
        qd_data = cfg['qd']
        qdlist_data = cfg['qdlist']
        setu_group = cfg['setu_group']
        r18_group = cfg['r18_group']
        last_setu = cfg['last_setu']
        last_s = cfg['last_s']
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
except:print('err')
class DF(object): #下载
    async def resize(path,mx=0,my=0):
        onlyy = onlyx =False
        inputimg = Im.open(path)
        new_x = mmx = inputimg.size[0]
        new_y = mmy = inputimg.size[1]
        xyb = mmx / mmy
        remove_x = mmx - mx 
        remove_y = mmy - my 
        if mx == 0: onlyy = True
        if my == 0: onlyx = True
        if remove_x >= remove_y or onlyx == True:
            new_x = mx
            rsize = mx / mmx
            new_y = mmy * rsize
        elif remove_y > remove_x or onlyy == True:
            new_y = my
            rsize = my / mmy
            new_x = mmx * rsize
        new_x = math.floor(new_x)
        new_y = math.floor(new_y)
        inputimg = inputimg.resize((new_x, new_y),Im.ANTIALIAS)
        print('├新图片大小:',new_x,'|',new_y)
        inputimg.save(path)
    async def adf(url,path,resize=[],resize_r=False):#异步下载
        debug(url ,">开始下载")
        url = url.replace('i.pximg.net','i.pixiv.cat')
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
        async with aiohttp.ClientSession() as session:
            response = await session.get(headers=headers, url=url)
            content_img = await response.read()
            tempf = open(path,'w')
            tempf.close()
            with open(path, 'wb') as f:
                f.write(content_img)
            await session.close()
            if path.endswith('png') and resize == []:
                await DF.resize(path,maxx_img)
        print('└下载完毕' + path)
        if resize_r == True:shutil.copyfile(path,path.replace('.png','_r.png'))
        if resize != []:await DF.resize(path,resize[0],resize[1])
        return path
class CHS(object): #数据初始化
    def chs(id): 
        datas = [hsolv_data,hsolvlist_data,qd_data,qdlist_data]
        for i in datas :
            if id not in i:
                i[id] = 0
#api = AppPixivAPI()
#api = ByPassSniApi()  # Same as AppPixivAPI, but bypass the GFW
#api.require_appapi_hosts(hostname="public-api.secure.pixiv.net")
#api.set_accept_language('en-us')
#try:api.auth(refresh_token=refresh_token)
#except:
#    try:api.auth(refresh_token=refresh_token)
#    except Exception as e:print('Pixiv登录错误: -\n└' + str(e))


bcc = Broadcast(loop=loop) 
app = GraiaMiraiApplication(broadcast=bcc,connect_info=Session(host=host_,authKey=authKey,account=bot_qq,websocket=True,use_dispatcher_statistics = True,use_reference_optimization = True))
inc = InterruptControl(bcc)
###################################
#如果你想使用saya模块就去除下面的“#” 
###################################
try:
    saya = Saya(bcc)
    saya.install_behaviours(BroadcastBehaviour(bcc))
    
    with saya.module_context():
        for module in os.listdir("modules"):
            try:
                if os.path.isdir(module):
                    saya.require(f"modules.{module}")
                else:
                    saya.require(f"modules.{module.split('.')[0]}")
            except ModuleNotFoundError:
                pass
except Exception as e:
    print('saya加载错误 不使用saya插件可无视:',e)
async def tlen(text): #文字宽度测量
    lenTxt = len(text) 
    lenTxt_utf8 = len(text.encode('utf-8')) 
    size = int((lenTxt_utf8 - lenTxt)/2 + lenTxt)
    return size
def debug(*nums):
    if cfg['debug'] == 1:
        print(*nums)
    else: pass
async def aexec(code):
    # Make an async function with the code and `exec` it
    exec(
        f'async def __ex(): ' +
        ''.join(f'\n {l}' for l in code.split('\n'))
    )

    # Get `__ex` from local variables, call it and return the result
    return await locals()['__ex']()
class Ak:
    async def m(): #明日方舟m数据获取
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
    async def i(): #明日方舟i数据获取
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
    async def s(): #明日方舟s数据获取
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
class Setu:
    async def add(r18=0,just_get=True,s='-'): #为色图池增加色图
        if r18 >= 2:
            print('nom')
            setudata = await pixiv.sh(s,20,r18=r18)
            return setudata
        ext_ing = ''
        outmsg = []
        p_ingdata = {}
        setudata = {}
        apiurl = 'https://api.lolicon.app/setu/?apikey=$APIKEY&r18=$R18'.replace('$APIKEY',lolicon_key).replace('$R18',str(r18)).replace('$NUM',str(1))
        if s != '-':apiurl = apiurl + '&keyword=' + s
        print('与api沟通中...','>',apiurl)
        async with aiohttp.ClientSession() as session:
            async with session.get(apiurl) as resp:
                res_json = await resp.json()
        print('└done')
        code = str(res_json['code'])
        codes = {
        '-1'	:'-1:api内部错误',
        '0'	    :'none',
        '401'	:'401:APIKEY 不存在或被封禁',
        '403'	:'403:由于不规范的操作而被拒绝调用',
        '404'	:'404:找不到符合关键字的色图',
        '429'	:'429:达到色图调用上限，切换至本地色图'}
        if code != '0':
            setudata['img'] = ['.\chace\error.png']
            setudata['info'] = code
            if code == '404' : 
                setudata['info'] = '404找不到指定色图'
                if s != '-':
                    setudata = await pixiv.sh(s,20,r18=r18)
            return setudata
        if code == '429':
            cfg['setu_l'] = 1
            setudata['img'] = ['.\chace\error.png']
            setudata['info'] = '429色图调用上限'
            return setudata
        i = res_json['data'][0]
        url_ing = i['url']
        setudata['url'] = url_ing
        pid_ing = i['pid']
        if r18 == 1:path_ing = './r18/' + str(pid_ing) + '.png'
        else:path_ing = './setu/' + str(pid_ing) + '.png'
        p_ingdata['pid'] = pid_ing
        if cfg['xml'] == 0 or xmloffline == True:
            print('开始下载:',url_ing,pid_ing,)
            try:await DF.adf(url_ing,path_ing)
            except:
                print('└连接错误，正在重试....')
                try:await DF.adf(url_ing,path_ing)
                except:
                    print(" └连接错误")
                    return
        ext =" $title by $author |pid:$pid uid:$uid "\
        .replace('$title',i['title'])\
        .replace('$author',i['author'])\
        .replace('$pid',str(pid_ing))\
        .replace('$uid',str(i['uid']))
        setudata['img'] = [path_ing]
        setudata['ext'] = ext
        tags = ''
        for _ in i['tags']:
            tags = tags +","+ _
        setudata['raw'] = [i['title'],i['author'],str(pid_ing),str(i['uid']),tags]
        outdata = ""
        for item in i:
            outdata = outdata + str(item) + str(i[str(item)])
        outdata = outdata.replace('pid','pid:').replace('p0uid',' p0 - uid').replace('uid','uid:').replace('title','\n标题:').replace('author','   作者:').replace('url','\n').replace('r18False','').replace('r18True','').replace('width','\n').replace('height','x').replace('tags','\n标签:')
        setudata['info'] = outdata
        if just_get == True:
            if r18 == 1:fl = 'r18'
            else:fl = 'setu'
            cfg['setus'][fl].append(setudata)
            print(' └色图数量+1, 目前色图总量为',len(cfg['setus'][fl]))
        else:
            return setudata
    async def xml(setudata): #使用xml发出色图
        path = setudata['img'][0]
        ext = setudata['ext']
        print('intoxml')
        with open(path,'rb') as f:
            img = f.read()
            pmd5 = hashlib.md5(img).hexdigest()
        inputimg = Im.open(path)
        mmx = inputimg.size[0]
        mmy = inputimg.size[1]
        #textxml = '''<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><msg serviceID="5" templateID="1" action="test" brief="[色图]" sourceMsgId="0" url="" flag="2" adverSign="0" multiMsgFlag="0"><item layout="0" advertiser_id="0" aid="0"><image uuid="$md5.png" md5="$md5" GroupFiledid="0" filesize="38504" local_path="" minWidth="$x" minHeight="$y" maxWidth="$mx" maxHeight="$my" /></item><source name="$ext" icon="http://p.qpic.cn/qqshare/0" url="http://gchat.qpic.cn/gchatpic_new/0/0-0-$md5?term=2" action="web" appid="-1" /></msg>'''
        textxml = """<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><msg serviceID="1" templateID="1" action="web" brief="[有色图!!]" sourceMsgId="0" url="$url" flag="3" adverSign="0" multiMsgFlag="0"><item layout="0" mode="2" advertiser_id="0" aid="0"><title size="30" color="#D32F2F" style="3">$title</title><picture cover="$url" w="0" h="0" /><summary size="25" color="#EE9A00" style="1">$user</summary></item><item layout="6" advertiser_id="0" aid="0"><summary size="25" color="#EE9A00">$TEXT</summary><hr hidden="false" style="0" /></item><source name="$lost" icon="" action="-1" appid="0" /></msg>"""
        textxml = textxml.replace('$md5',pmd5)\
            .replace('$x',str(mmx))\
            .replace('$y',str(mmy))\
            .replace('$mx',str(mmx))\
            .replace('$my',str(mmy))\
            .replace('$ext',ext)\
            .replace('$title',setudata['raw'][0])\
            .replace('$TEXT','tags:' + setudata['raw'][4])\
            .replace('$user','by ' + setudata['raw'][2])\
            .replace('$lost','pid:' + setudata['raw'][1] +' | uid:' + setudata['raw'][3])
        if type(setudata['url']) is list: textxml = textxml.replace('$url',str(setudata['url'][0]))
        elif type(setudata['url']) is str: textxml = textxml.replace('$url',str(setudata['url']))
        outxml = [(Xml(textxml))]
        return outxml
    async def offline(r18): #发送离线色图
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
        hsolvlist_data[id] = hsolvlist_data[id] + 1
        outmsg = [(Image.fromLocalFile(filepach))]
        return outmsg
    async def get(r18,qid=110,msg='',xml=cfg['xml']): #获取色图
        isdigit = False
        id = str(qid)
        outmsg = []
        if r18 == 1:fl = 'r18'
        else:fl = 'setu'
        if msg.isdigit() == True:
            num = int(msg)
            if 0 < num < 10:isdigit =True
            else:
                outmsg = [(Plain('色图数量不对劲!'))]
                return outmsg
        else:num = 1
        if id not in hsolvlist_data: #初始化
            print('初始化',id)
            hsolv_data[id] = 0
            hsolvlist_data[id] = 0
            qd_data[id] = 0
            qdlist_data[id] = 0
        if qd_data[id] == 0: #签到
            debug1 = hsolv_data[id]
            if qdlist_data[id] == 0:
                stadd = random.randint(20,56)
                ext_ing = "这是你第一次获取色图,随机获取色图$张".replace('$',str(stadd))
            else:
                stadd = random.randint(15,30)
                ext_ing = "今天第一次获取色图，随机获取色图$张".replace('$',str(stadd))
            outmsg.append(Plain(ext_ing))
            hsolv_data[id] += stadd
            debug2 = hsolv_data[id]
            qdlist_data[id] += 1
            qd_data[id] = 1
        if hsolv_data[id] > num: #有剩余色图并获取色图
            if cfg['setu_l'] == 1: #离线色图
                for i in range(num):
                    offline = await Setu.offline(r18)
                    outmsg.append(offline)
                    hsolvlist_data[id] += 1
                    hsolv_data[id] -= 1
                return outmsg
            if isdigit == True or msg == '': #普通和数量色图
                global loop_ing
                loop_ing = False
                if num < len(cfg['setus'][fl]):
                    for _ in range(num):
                        lsetudata = cfg['setus'][fl]
                        setudata = lsetudata[0]
                        print(xml)
                        if xml == 1:
                            setudata['ext'] = setudata['ext'] + '色图缓存:' + str(len(cfg['setus'][fl]))
                            outxml = await Setu.xml(setudata)
                            outmsg = outxml
                        else:
                            outmsg.append(Image.fromLocalFile(setudata['img'][0]))
                        del lsetudata[0]
                        print('┌色图库 -1')
                        cfg['setus'][fl] = lsetudata
                        if cfg["info"] == 1:outmsg.append(Plain(setudata['info']))
                        hsolvlist_data[id] += 1
                        hsolv_data[id] -= 1
                        print('└色图人剩余色图',hsolv_data[id])
                        cfg['last_setu'][id] = setudata
                else:
                    if is_run == True: outmsg.append(Plain('下载可能卡住了|'))
                    outmsg.append(Plain('色图获取的太多啦，补不上货啦'))
                return outmsg
            else : #搜索色图
                setudata = await Setu.add(r18,False,s=msg)
                print('joinsetudata')
                if xml == 1:
                    setudata['ext'] = setudata['ext'] + '色图缓存:' + str(len(cfg['setus'][fl]))
                    outxml = await Setu.xml(setudata)
                    outmsg = outxml
                else:
                    if r18 >= 2:
                        for _ in setudata['img']:
                            outmsg.append(Image.fromLocalFile(_))
                    else:outmsg.append(Image.fromLocalFile(setudata['img'][0]))
                if cfg["info"] == 1:outmsg.append(Plain(setudata['info']))
                hsolvlist_data[id] += 1
                hsolv_data[id] -= 1
                return outmsg
        else:
            outmsg.append(Plain('你没色图啦'))
            debug(cfg['hsolv'][id],'>',hsolv_data[id],'| id:',id)
            return outmsg
    async def reget(r18 ): #重新补充色图
        global is_run
        if is_run == True: return
        is_run = True
        if r18 == 1:fl = 'r18'
        else:fl = 'setu'
        tasks = []
        setu_ix = len(cfg['setus'][fl])
        for _ in range(10):
            if setu_ix < setus:
                task = asyncio.ensure_future(Setu.add(r18=r18))
                tasks.append(task)
                setu_ix = setu_ix + 1
        try:await asyncio.gather(*tasks)
        except:is_run = False
        is_run = False
    async def tdf(url,path): #
        await DF.adf(url,path)
        shutil.copyfile(path,path.replace('.png','_r.png'))
        await DF.resize(path,240,120)
    async def rm(rmsg,c=False,set=0): #撤回色图
        if cfg['xml'] == 1:return
        if c == False :rtime = cfg['revoke']
        if c == True: rtime = set
        if rtime > 0:
            await asyncio.sleep(rtime)
            await app.revokeMessage(rmsg)
        else:return
    async def gif(path):
        frames = []
        image_list = ["chace/none.png",path]
        for image_name in image_list:
            frames.append(imageio.imread(image_name))
        imageio.mimsave(path.replace('.png','.gif').replace('.jpg','.gif'), frames, 'GIF', duration=200)
        path = path.replace('.png','.gif').replace('.jpg','.gif')
        return path
    async def setudata(pid,uid,pname,uname,w,h,tags):
        pid = str(pid)
        uid = str(uid)
        w = str(w)
        h = str(h)
        setudatatext = '''pid:$pid p0 - uid:$uid\n标题:$pname   作者:$uname\n$url\n$xy\n标签:$tags'''\
            .replace('$pid',pid)\
            .replace('$uid',uid)\
            .replace('$pname',pname)\
            .replace('$uname',uname)\
            .replace('$url',"pixiv.net/artworks/"+pid)\
            .replace('$xy',w + '|' + h)\
            .replace('$tags',''.join(tags))
        return setudatatext
class pixiv:
    async def sh(msg,num,r18=2):
        setudata = {}
        print(math.floor(Time.time()),'|',cfg['cooling'])
        if math.floor(Time.time()) - cfg['cooling'] < 15 :
            setudata['img'] = ['.\chace\error.png']
            setudata['info'] = 'pixiv冷却中'
            return setudata
        cfg['cooling'] = math.floor(Time.time())
        debug('开始搜图：',msg)
        shlist = []
        for i in stag:
            if len(shlist) > num:break
            word = msg + ' ' + i
            raw = api.search_illust(search_target='partial_match_for_tags',word=word)
            try:
                for _ in raw['illusts']:
                    print(len(shlist),'/',num,'|',_['tags'][0]['name'])
                    if len(shlist) > num:break
                    if _['tags'][0]['name'] == 'R-18' and r18 == 2 :shlist.append(_)
                    if _['tags'][0]['name'] != 'R-18' and r18 >= 2 :shlist.append(_)
            except:
                print('error:',raw)
            if len(shlist) > num:break
            await asyncio.sleep(3)
            cfg['cooling'] = math.floor(Time.time())
        debug('搜图完成，处理数据中')
        set = random.randint(0,num-1)
        debug('r:',set)
        data = shlist[set]
        raw_tags = data['tags']
        tags = []
        for tag in raw_tags:tags.append(tag['name'])

        setudata['info'] = await Setu.setudata(
            data['id'],
            data['user']['id'],
            data['caption'],
            data['user']['name'],
            data['width'],data['height'],
            tags
            )
        try:
            print(data['meta_single_page']['original_image_url'],'>>>>')
            url = data['meta_single_page']['original_image_url']
            urls = [url]
            print('-done')
        except:
            n = 0
            urls = []
            for _ in data['meta_pages']:
                n += 1
                print(_['image_urls']['original'],'>>>>')
                urls.append(_['image_urls']['original'])
                if n > 3:break
            n = 0
        print(urls)
        setudata['img'] = []
        tasks=[]
        n = 0
        for _ in urls:
            n += 1
            sdir('./listpsh/'+str(data['id']))
            tasks.append(DF.adf(_,'./listpsh/'+str(data['id'])+'/'+str(n)+'.png'))
            setudata['img'].append('./listpsh/'+str(data['id'])+'/'+str(n)+'.png')
        print(tasks)
        await asyncio.wait(tasks)
        cfg['cooling'] = math.floor(Time.time())
        return setudata

async def rep(l,text): #文字占位处理
    strnone = ' '
    text=text.replace('　',' ')
    len_ing = await tlen(text)
    if len_ing > l:
        remove = (len_ing - l)  + 2
        for _ in range(100):
            if remove > 0:
                i = text[-1:]
                if i >= u'\u4e00' and i <= u'\u9fa5' or i >= u'\u3040' and i <= u'\u31FF':
                    remove -=2
                    text = text[:-1]
                else:
                    remove -=1
                    text = text[:-1]
            else:
                if remove < 0:
                    text = text + ' '
                break
        out = text + '..'
    else:
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
        print(cfg)
        print('保存cfg出现错误，已打印cfg内容')
def toimg(msg,imgpath='./chace/mainbg.png',f1=fl1,f2=fl2,PZ=False,savepath='./chace/out.png',SIZE=30,COLOR = "#ffffff"): #文字转图片
    '''
    input:
      msg:str 输入文字
      imgpath:str 图片路径
      f1:str 字体1路径
      f2:str 字体2路径
    '''
    msg = msg.replace('\n','').replace('\r','')
    img = Im.open(imgpath).convert('RGBA')
    global x,y,mx,my,mmx,mmy,size,color,pz,function_time,for_time,text_time,text_list,function_list,for_list,lispuimg,functionlist
    for i in ['text_list' , 'function_list' , 'for_list' , 'lispuimg' , 'functionlist']:exec(i+'=[]',globals())
    for i in ['y' , 'x' , 'my' , 'mx','function_time','for_time','text_time']:exec(i+'=0',globals())
    pz = PZ
    size = SIZE
    color = COLOR
    mmx = img.size[0]
    mmy = img.size[1]
    efunction = False
    f = ''
    img = Im.open(imgpath)
    textimg = Im.new('RGBA', img.size, (0,0,0,0))
    for i in msg: # 遍历所有文字,探测\指令,输出所有文字占图片最大宽 高
        function_s = Time.time()
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
                elif text.startswith('x'):#x<x/y>(-/>)<int> : xy 绝对/相对值修改
                    text = text[1:]
                    if text.startswith('x'):
                        text = text[1:]
                        if text.startswith('-'):x -= int(text[1:])
                        elif text.startswith('>'):x = int(text[1:])
                        else: x += int(text)
                    elif text.startswith('y'):
                        text = text[1:]
                        if text.startswith('-'):y -= int(text[1:])
                        elif text.startswith('>'):y = int(text[1:])
                        else: x += int(text)
                    if x + size > mx: mx = x + size 
                    if y + size > my: my = y + size
                elif text.startswith('p'): #p<图片路径>: 添加图片
                    print(x,y)
                    putpath = text[1:]
                    putimg =  Im.open(putpath).convert('RGBA')
                    putmx = putimg.size[0]
                    putmy = putimg.size[1]
                    layer = Im.new('RGBA', textimg.size, (0,0,0,0)) #空图层 原图大小
                    layer.paste(putimg,(math.floor(x),math.floor(y))) #空图层插入putimg
                    textimg = Im.composite(layer, textimg, layer) #图层与原图合并
                    if pz == True:
                        putpath = text[1:]
                        xin = x
                        xout = x + putmx
                        yin = y
                        yout = y + putmy
                        if yout > my: my = yout + size
                        if xout > mx: mx = xout + size
                        x = x + putmx + 1
                        putdata = {"xin":xin,"xout":xout,"yin":yin,"yout":yout} #因为该图片而产生的文字禁区:(xin,yin),(xout,yout)
                        print(putdata,x,y)
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
        function_e = Time.time()
        function_list.append(function_e - function_s)
        text_s = Time.time()
        if i >= u'\u4e00' and i <= u'\u9fa5' or i >= u'\u3040' and i <= u'\u31FF':#中文
            fx = size
            f = f1
        else:   #如果是英文，使用英文字体，并每次x跃进时只会跃进半个文字大小
            fx = size / 2 
            f = f2
        ImageDraw.Draw(textimg).text((x+2, y-6),i,font=ImageFont.truetype(f,size),fill="#000000",direction=None)
        ImageDraw.Draw(textimg).text((x, y-8),i,font=ImageFont.truetype(f,size),fill=color,direction=None) #文字
        x += fx
        text_e = Time.time()
        text_list.append(text_e - text_s)
        for_s = Time.time()
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
                if x + size > mx: mx = x + size
                if y + size > my: my = y + size
                x = 0
                y += size
                code = True
            if code == False : break #跳出循环
        for_e = Time.time()
        for_list.append(for_e - for_s)
    if x > mx: mx = x + size
    if y > my: my = y + size
    if my == 0:mx = x + size
    if my == 0:my += size 
    print('mx:' + str(mx) + "|my:" + str(my))
    ly =  (mmy - my) / 2
    img = img.crop((0,ly,mx,ly+my))
    layer = Im.new('RGBA', img.size, (0,0,0,0)) #空图层 原图大小
    layer.paste(textimg,(0,0)) #空图层插入putimg
    img = Im.composite(layer, img, layer) #图层与原图合并
    img.save(savepath)
    for i in for_list:for_time += i
    for i in function_list:function_time += i
    for i in text_list:text_time += i
    print('function用时:',function_time)
    print('写入文字用时:',text_time)
    print('碰撞箱用时:',for_time)
loop.create_future()

@bcc.receiver("GroupMessage")
async def group_listener(app: GraiaMiraiApplication, message:MessageChain, group: Group, member:Member ): #群聊监听
    msg = message.asDisplay()
    if message.has(Xml):
        txml = str(message.get(Xml))
        print(txml)
    if message.has(Json):
        tjson = str(message.get(Json))
        print(tjson)
    if message.has(App):
        tapp = str(message.get(App))
        print(tapp)
    if message.has(Plain):
        tmsg = str(message.get(Plain)[0].text)
#图片
    if message.has(Image):
        timg = message.get(Image)[0].url
        print(timg)
        if message.has(At):
# at机器人功能
            if message.get(At)[0].target == bot_qq and group.id in setu_group:
    #├<@机器人> <Img> |以图搜图          
                await app.sendGroupMessage(group, MessageChain.create([At(member.id), Plain("选择搜索源:\n1.saucenao\n2.ascii2d.net")]))
                @Waiter.create_using_function([GroupMessage])
                def waiter(
                    event: GroupMessage, waiter_group: Group,
                    waiter_member: Member, waiter_message: MessageChain
                ):
        
                    msg = waiter_message.asDisplay()
                    mode = 0
                    if all([
                        waiter_group.id == group.id,
                        waiter_member.id == member.id,
                        msg != ''
                    ]):
                        if all([ len(msg) == 1 , msg.isdigit() ]):
                            mode = int(msg)
                        elif msg.startswith('sau'): mode = 1
                        elif msg.startswith('asc'): mode = 2
                        if mode != 0:
                            return mode
                global stime 
                stime = Time.time()
                mode = await inc.wait(waiter)
                imgpath = './sh.png'
                debug('WITE:',timg)
                await DF.adf(timg,imgpath)
                image = Im.open(imgpath)
                mmx = image.size[0]
                mmy = image.size[1]
                await DF.resize(imgpath,360,180)
                fromt = 'none'
                ilist = []
                if mode == 1:
                    fromt = 'saucenao'
                    print('以图搜图sau')
                    url = "https://saucenao.com/search.php?output_type=2&api_key=$key&testmode=1&dbmask=999&numres=5&url=$url".replace('$url',timg).replace('$key',saucenao_key)
                    async with aiohttp.ClientSession() as session:
                        async with session.get(url) as resp:
                            data = await resp.json()
                    data = data['results']
                    ilist = []
                    n = 0
                    for i in data:
                        idata = {}
                        n += 1
                        outlinks = []
                        linkdata = {}
                        try:linkdata['str'] = i['data']['title']
                        except:linkdata['str'] = 'none'
                        try:linkdata['url'] = i['data']['ext_urls'][0]
                        except:linkdata['url'] = 'none'
                        outlinks.append(linkdata)
                        linkdata = {}
                        try:linkdata['str'] = i['data']['member_name']
                        except:linkdata['str'] = 'none'
                        try:linkdata['url'] = 'https://www.pixiv.net/users/uid'.replace('uid',i['data']['member_id'])
                        except:linkdata['url'] = 'none'
                        outlinks.append(linkdata)
                        idata['from'] = i['header']['index_name'][10:]
                        idata['links'] = outlinks
                        idata['img'] = i['header']['thumbnail']
                        ilist.append(idata)
                elif mode == 2:
                    fromt = 'ascii2d'
                    url = 'https://ascii2d.net/search/url/$url'.replace('$url',timg)
                    print('请求api:',url)
                    async with aiohttp.ClientSession() as session:
                        async with session.get(url) as resp:
                            data = await resp.text()
                    soup = BeautifulSoup(data,'html.parser') #html.parser是解析器，也可是lxml
                    a = soup.find_all('div',attrs={"class": "row item-box"},limit=10)
                    ilist = []
                    n = 0
                    for i in a:
                        if n == 0 :
                            n += 1
                            continue
                        idata = {}
                        outlinks = []
                        try:outi = i.find_all('img',attrs={"loading": "eager"})[0]['src']
                        except:outi = i.find_all('img',attrs={"loading": "lazy"})[0]['src']
                        try:outlink = i.find_all('a',attrs={'target':"_blank"})
                        except:outlink = 'none'
                        try:small = i.find_all('small')[-1].string
                        except:small = 'none'
                        small = small.replace('\n','').replace('\r','').replace(' ','')
                        for _ in outlink:
                            linkdata = {}
                            linkdata['str'] = _.string
                            linkdata['url'] = _['href']
                            if linkdata == {} : linkdata['str'] = '详情不存在'
                            outlinks.append(linkdata)
                        idata['img'] = outi
                        idata['links'] = outlinks
                        idata['from'] = small
                        ilist.append(idata)
                startmap = Search_map\
                    .replace('$from(17)////////',await rep(17,fromt))\
                    .replace('$s180x360', imgpath)
                n = 0
                outmsg = startmap
                n = 0
                tasks = []
    
                for i in ilist:
                    n += 1
                    url = i['img']
                    if url.startswith('/thumbnail/'):url = 'https://ascii2d.net' + url
                    img_ing = './chace/' + str(n) + '.png'

                    task = asyncio.ensure_future(DF.adf(url,img_ing,resize=[240,120],resize_r=True))
                    tasks.append(task)
        
                    try:title = await rep(13,i['links'][0]['str'])
                    except:title =await rep(13,'None')
                    try:user = await rep(13,i['links'][1]['str'])
                    except:user =await rep(13,'None')
                    try:fromi = await rep(9,i['from'])
                    except:fromi =await rep(9,'None')
                    map_ing = Search_map2\
                        .replace('$i120x240',img_ing + '\\' + str(n) + '.')\
                        .replace('$title(13)///','\\xx>300\\'+ title)\
                        .replace('$user(13)///','\\xx>510\\'+ user)\
                        .replace('$from(9)/','\\xx>720\\'+fromi)
                    outmsg = outmsg + map_ing
                outmsg = outmsg + aks_map3
                path = './chace/bg_l.png'
                path2 ='./chace/bg_d.png'
                await asyncio.gather(*tasks)
                await DF.resize(path,915,1560)
                img = cv2.imread(path, -1) 
                fx = fy = 1
                img = cv2.resize(img, (0, 0), fx=fx, fy=fy, interpolation=cv2.INTER_CUBIC)  
                img = cv2.GaussianBlur(img,(13,13),0)
                cv2.imwrite(path2, img)
                cv2.waitKey(0)  
                toimg(outmsg,path2)
                #if cfg['xml'] == 1:
                #    setudata = {}
                #    setudata['img'] = './chace/out.png'
                #    setudata['ext'] = '发送<数字>来查看详情'
                #    outxml = await Setu.xml(setudata)
                #    await app.sendGroupMessage(group,MessageChain.create(outxml))
                #else:
                await app.sendGroupMessage(group,MessageChain.create([Image.fromLocalFile("./chace/out.png")]))
                await app.sendGroupMessage(group, MessageChain.create([At(member.id), Plain("发送<数字>来查看详情")]))
                global tic
                tic = Time.time()
                @Waiter.create_using_function([GroupMessage])
                async def waiter(event: GroupMessage, waiter_group: Group,waiter_member: Member, waiter_message: MessageChain):
                    toc = Time.time()
                    if toc - tic > 60:
                        return event
                    if all([waiter_message.has(Image),waiter_message.has(At)]):
                        if message.get(At)[0].target == bot_qq:
                            return event
                    msg = waiter_message.asDisplay()
                    if all([waiter_group.id == group.id,len(msg) == 1 , msg.isdigit()]):
                        if int(msg)<10:
                            infodata = ilist[int(msg) - 1]
                            try:title = infodata['links'][0]['str']
                            except:title = 'none'
                            try:user = infodata['links'][1]['str']
                            except:user  = 'none'
                            try:link1 = infodata['links'][0]['url']
                            except:link1 = 'none'
                            try:link2 = infodata['links'][1]['url']
                            except:link2 = 'none'
                            infomsg = '''$title by $user\n原图链接:$link1\n作者链接:$link2'''\
                            .replace('$title',title)\
                            .replace('$user',user)\
                            .replace('$link1',link1)\
                            .replace('$link2',link2)
                            img_ing = './chace/' + msg + '_r.png'
                            outmsg = [Image.fromLocalFile(img_ing),Plain(infomsg)]
                            await app.sendGroupMessage(group, MessageChain.create(outmsg))
                outmsg = await inc.wait(waiter)
                print('nooo')
    #└<Img> |表情色图来
        if message.get(Image)[0].imageId == '{B407F708-A2C6-A506-3420-98DF7CAC4A57}.mirai' and group.id in cfg['setu_group']:
            outmsg = await Setu.get(0,qid=member.id)
            rmsg = await app.sendGroupMessage(group,MessageChain.create(outmsg),quote=message[Source][0].id)
            if cfg['revoke'] > 0 :
                await asyncio.sleep(cfg['revoke'])
                await app.revokeMessage(rmsg)
            await Setu.reget(0)
#管理员指令
    if member.id in admin:
    #├toimg <Str> |文字写入图片
        if msg.startswith('toimg'):
            msg = msg.replace('toimg ','').replace('toimg','')
            input = msg.split(',')
            t_s = Time.time()
            if len(input) > 1:toimg(input[0],input[1])
            else:toimg(input[0])
            await app.sendGroupMessage(group,MessageChain.create([Image.fromLocalFile("./chace/out.png")]))
            t_e = Time.time()
            print(t_e-t_s)
    #├撤回时间 <Int> |设置色图撤回时间
        elif msg.startswith('撤回时间'):
            cfg['revoke'] = int(msg.replace(' ','').replace('撤回时间',''))
            await app.sendGroupMessage(group,MessageChain.create(
                [(Plain('撤回时间已改为'+str(cfg['revoke'])))]),quote=message[Source][0].id)
    #├test |test
        elif msg.startswith('test'):
            testxml = """<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><msg serviceID="1" templateID="1" action="web" brief="test" sourceMsgId="0" url="https://i.pixiv.cat/img-original/img/2021/04/06/04/20/34/88967403_p0.jpg" flag="3" adverSign="0" multiMsgFlag="0"><item layout="0" mode="2" advertiser_id="0" aid="0"><title size="30" color="#D32F2F" style="3"> test</title><picture cover="https://i.pixiv.cat/img-original/img/2021/04/06/04/20/34/88967403_p0.jpg" w="0" h="0" /><summary size="25" color="#EE9A00" style="1"></summary></item><item layout="6" advertiser_id="0" aid="0"><summary size="25" color="#EE9A00">第一行 第二行 第三行 第四行 第五行</summary><hr hidden="false" style="0" /></item><source name="擎天机器人" icon="http://t.cn/RVIeaZK" action="-1" appid="0" /></msg>"""
            outxml = [(Xml(testxml))]
            print(testxml)
            await app.sendGroupMessage(group,MessageChain.create(outxml))
    #├exec <Str> |运行函数
        elif msg.startswith('exec') and member.id in admin:
            mlist = await app.memberList(group)
            global execout
            global test_
            async def test_():
                print("qaq")
            execout = 'None'
            msg = 'global execout\n' + msg.replace('exec\n','')
            print(msg)
            await aexec(msg)
            if execout != "None":
                if isinstance(execout,list):await app.sendGroupMessage(group,MessageChain.create(execout))
                if isinstance(execout,str):await app.sendGroupMessage(group,MessageChain.create([(Plain(execout))]),quote=message[Source][0].id)
                else:await app.sendGroupMessage(group,MessageChain.create([(Plain(str(execout)))]),quote=message[Source][0].id)
    #├restart |重启机器人
        elif msg.startswith('restart') :
            await app.sendGroupMessage(group,MessageChain.create([Plain('执行重启项目----')]))
            restart_program()
    #├hsolvr |重置色图
        elif msg.startswith("hsolvr"):
            outmsg = "所有当天获取色图次数被重置"
            for i in qd_data:
                qd_data[i] = 0
            await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
            savecfg()
            srcfile='./cfg.json'
            name = Time.strftime('%Y-%m-%d-%H',Time.localtime(Time.time()))
            dstfile='./backups/'+ name + '.json'
            shutil.move(srcfile,dstfile)
    #├hsolv+ <Int/None>|增加色图
        elif msg.startswith('hsolv+'):
            
            id = msg.replace("hsolv+","").replace(' ','')
            if id == '': id = str(member.id)
            hsolv_data[id] = hsolv_data[id] + 10
            outmsg = str(id) + "的色图增加了10"
            await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
            savecfg()
    #├sg setu <+/-> |色图群权限管理
        elif msg.startswith('sg setu'):
            if group.id in cfg['setu_group']:
                if msg.endswith('-'):
                    cfg['setu_group'].remove(group.id)
                    outmsg = '此群不再是色图群'
                else:outmsg = '此群已经是色图群'
            else: 
                if msg.endswith('-'):
                    outmsg = '此群本来就不是色图群'
                else:
                    cfg['setu_group'].append(group.id)
                    outmsg = '已变成色图群'
            await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
    #├sg r18 <+/-> |r18群权限管理
        elif msg.startswith('sg r18') :
            if group.id in cfg['r18_group'] :
                if msg.endswith('-'):
                    cfg['r18_group'].remove(group.id)
                    outmsg = '此群不再是r18群'
                else:
                    outmsg = '此群已经是r18群'
            else: 
                if msg.endswith('-'):
                    outmsg = '此群本来就不是r18群'
                else:
                    cfg['r18_group'].append(group.id)
                    outmsg = '已变成r18群'
            await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
    #├ak <rm/ri/rs/ra> |明日方舟企鹅物流手动数据更新
        elif msg.startswith('ak'):
            msg = msg.replace('ak','').replace(' ','').replace('－','-')
            if msg.startswith('rm') :
                await Ak.m()
                await app.sendGroupMessage(group,MessageChain.create([Plain('企鹅物流 - akm 数据下载完成')]))
            if msg.startswith('ri') :
                await Ak.i()
                await app.sendGroupMessage(group,MessageChain.create([Plain('企鹅物流 - aki 数据下载完成')]))
            if msg.startswith('rs') :
                await Ak.s()
                await app.sendGroupMessage(group,MessageChain.create([Plain('企鹅物流 - aks 数据下载完成')]))
            if msg.startswith('ra') :
                await Ak.m()
                await Ak.i()
                await Ak.s()
                restart_program()
            else:msg = 'ak' + msg
    #└清除色图缓存 |清除色图缓存
        elif msg.startswith('清除色图缓存'):
            if not msg.replace('清除色图缓存','').startswith('setu'):
               cfg["setus"]['r18'] = []
               print('rip r18')
            if not msg.replace('清除色图缓存','').startswith('r18'):
               cfg["setus"]['setu'] = []
               print('rip setu')
    if msg != "":print(msg)
#普通指令 
#├<色图来/不够色> <Int/Str/None> |色图功能
    if msg.startswith('不够色') == 1 or msg.startswith('色图来') == 1:
        if msg.startswith('色图来') == 1 and group.id in setu_group: is_r18 = 0
        elif msg.startswith('不够色') == 1 and group.id in r18_group: is_r18 = 1
        else: return
        msg = msg.replace('不够色','').replace('色图来','').replace(' ','')
        debug('r18:',is_r18,'xml:',cfg['xml'])
        ##xml特殊设置：
        if is_r18 == 0:outmsg = await Setu.get(is_r18,msg=msg,xml = cfg['xml'],qid=member.id)
        if is_r18 == 1:outmsg = await Setu.get(is_r18,msg=msg,xml = 1,qid=member.id)
        print(outmsg)
        if MessageChain.create(outmsg).has(Xml):rmsg = await app.sendGroupMessage(group,MessageChain.create(outmsg))
        else:rmsg = await app.sendGroupMessage(group,MessageChain.create(outmsg),quote=message[Source][0].id)
        tasks = [(asyncio.ensure_future(Setu.rm(rmsg))),(asyncio.ensure_future(Setu.reget(is_r18)))]
        await asyncio.gather(*tasks)
    elif msg.startswith('来点') and msg.endswith('色图'):
        msg = msg.replace('来点','').replace('色图','').replace(' ','')
        if group.id in setu_group : r18 = 3
        if group.id in r18_group : r18 = 2
        if len(msg) == 0:
            return
        outmsg = await Setu.get(r18,qid=member.id,msg=msg,xml=0)
        rmsg = await app.sendGroupMessage(group,MessageChain.create(outmsg),quote=message[Source][0].id)
        await Setu.rm(rmsg)
#├详情 <+/-> |开关色图详情
    elif msg.startswith('详情') :
            msg = msg.replace('详情','').replace(' ','')
            if cfg["info"] == 1 :
                if msg.endswith('-'):
                    cfg['info'] = 0
                    outmsg = '详情已关闭'
                else:
                    outmsg = '详情本来就开着'
            else: 
                if msg.endswith('-'):
                    outmsg = '详情本来就关着'
                else:
                    cfg["info"] = 1
                    outmsg = '已开启详情 详情可能在缓存色图用完之后才会生效'
            await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
#├xml <on/off> |开关色图xml模式
    elif msg.startswith('xml') and hsolvlist_data[str(member.id)] >30:
        msg = msg.replace('xml','').replace(' ','')
        if msg == 'on':
            cfg['xml'] = 1
            await app.sendGroupMessage(group,MessageChain.create([(Plain('已开启'))]))
        elif msg == 'off':
            cfg['xml'] = 0
            await app.sendGroupMessage(group,MessageChain.create([(Plain('已关闭'))]))
        else :pass
#├/help |获取帮助
    elif msg.startswith('/help'):
        text = helptext
        await app.sendGroupMessage(group,MessageChain.create([Plain(text)]))
#├排行榜 <day_r18/week_r18/week_r18g/week/month/None>|p站排行榜
    elif msg.startswith('排行榜') and group.id in setu_group:
        msg = msg.replace('排行榜','').replace(' ','')
        mo = 'day'
        if group.id in r18_group:
            if msg.startswith('day_r18'):mo = 'day_r18'
            if msg.startswith('week_r18'):mo = 'week_r18'
            if msg.startswith('week_r18g'):mo = 'week_r18g'
        else:
            if msg.startswith('week'):mo = 'week'
            if msg.startswith('month'):mo = 'month'
        rank_list = api.illust_ranking(mode=mo)
        rank_list = rank_list['illusts']
        n = 0
        msglist = [[(Plain('pixiv排行榜:'))]]
        cfg['plinfodata'][str(group.id)] = []
        for i in rank_list :
            p_ing = {}
            p_ing['url'] = []
            print(i)
            if n == 5 : break
            n = n + 1
            p_ing['pid'] = i['id']
            p_ing['uid'] = i['user']['id']
            p_ing['title'] = i['title']
            p_ing['user'] = i['user']['name']
            p_ing['tags'] = []
            for tag in i['tags']:
                p_ing['tags'].append(tag['name'])
            try:
                p_ing['url'].append(i['meta_single_page']["original_image_url"])
            except :
                for u in i['meta_pages']:
                    p_ing['url'].append( u["image_urls"]['original'])
            savepath = './listpiv/'+ str(group.id) + '/' + str(n) + '.png'
            savefl = './listpiv/'+ str(group.id) 
            sdir(savefl)
            p_ing['path'] = savepath
            print(p_ing['url'])

            await DF.adf(p_ing['url'][0],savepath)
            fd = open(savepath, "rb")
            f = fd.read()
            pmd5 = hashlib.md5(f).hexdigest()
            p_ing['md5'] = pmd5 
            cfg['plinfodata'][str(group.id)].append(p_ing)
            print(str(p_ing))
            ioutmsg = (Plain('\n' + str(n) + '.' + p_ing['title']))
            iimg = (Image.fromLocalFile(savepath))
            msglist.append([ioutmsg,iimg])
            p_ing = {}
        msglist.append([(Plain('使用tp 1~5来查看色图详情'))])
        for i in msglist:
            await app.sendGroupMessage(group,MessageChain.create(i))
            await asyncio.sleep(3)
    elif msg.startswith('tp'):
        msg = msg.replace(' ','').replace('tp','')
        try:
            mint = int(msg) - 1
        except:return
        p_ing = cfg['plinfodata'][str(group.id)][mint]
        tags = ' '.join(p_ing['tags'])
        inputimg = Im.open(p_ing['path'])
        mmx = inputimg.size[0]
        mmy = inputimg.size[1]
        if cfg['xml'] == 1:
            textxml = '''<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><msg serviceID="5" templateID="1" action="test" brief="[色图]" sourceMsgId="0" url="" flag="2" adverSign="0" multiMsgFlag="0"><item layout="0"><image uuid="$md5.png" md5="$md5" GroupFiledid="0" filesize="38504" local_path="" minWidth="$x" minHeight="$y" maxWidth="$mx" maxHeight="$my" /></item><source name="$ext" icon="" action="web" url="$url" appid="-1" /></msg>'''
            ext =" $title by $author |pid:$pid uid:$uid |tags:$tags"\
                    .replace('$title',p_ing['title'])\
                    .replace('$author',p_ing['user'])\
                    .replace('$pid',str(p_ing['pid']))\
                    .replace('$uid',str(p_ing['user']))\
                    .replace('$tags',tags)
            textxml = textxml.replace('$md5',p_ing['md5'])\
                .replace('$x',str(mmx))\
                .replace('$y',str(mmy))\
                .replace('$mx',str(mmx))\
                .replace('$my',str(mmy))\
                .replace('$ext',ext)\
                .replace('$url',p_ing['url'])
            outmsg = [Xml(textxml)]
        else:
            print(len(p_ing['url']))
            outmsg = []
            if len(p_ing['url']) > 1:
                n = 0
                for i in p_ing['url']:
                    n += 1
                    savepath = p_ing['path'].replace('.png','_' + str(n) + '.png')
                    print(savepath)
                    await DF.adf(i,savepath)
                    outmsg.append((Image.fromLocalFile(savepath)))
            else:outmsg = [].append((Image.fromLocalFile(p_ing['path'])))
            urlstr = p_ing['url'][0]
            urlstr = urlstr[:-3]
            outmsg.append((Plain(infomap\
                .replace('title',p_ing['title'])\
                .replace('author',p_ing['user'])\
                .replace('$uid',str(p_ing['uid']))\
                .replace('$pid',str(p_ing['pid']))\
                .replace('tags',tags)\
                .replace('mx',str(mmx))\
                .replace('my',str(mmy))\
                .replace('url',urlstr))))
        print(outmsg)
        for i in outmsg:
            await app.sendGroupMessage(group,MessageChain.create([i]))
            await asyncio.sleep(2)
#├ak <s/i> <Str> |明日方舟企鹅物流物品查询
    elif msg.startswith('ak'):
        print('ak')
        msg = msg.replace('ak','').replace(' ','').replace('－','-')
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
                        else: cl = '#FFFFFF\\'
                        try:
                            aimg = '\\p./aki_30/id.png\\  '.replace('id',i['itemId'])
                            aimg_p = './aki_30/id.png'.replace('id',i['itemId'])
                            img = Im.open(aimg_p)
                        except:
                            aimg = '  '
                        dname = cl + aimg + await rep(14,name)
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
                print(outmsg)
                toimg(outmsg,imgpath = "./chace/ak.png" )
                await app.sendGroupMessage(group,MessageChain.create([Image.fromLocalFile("./chace/out.png")]))
        if msg.startswith('i'):
            print('aki')
            cost = 1
            stime0 = 1
            sname = ''
            dnum = 0
            iid = ''
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
            ialias = await rep(45,str(alias))
            ilist = []
            try:
                aimg = '\\p./aki_60/id.png\\    '.replace('id',iid)
                aimg_p = './aki_60/id.png'.replace('id',iid)
                img = Im.open(aimg_p)
            except:
                aimg = '  '
            outmsg = aki_map\
                .replace('图片',aimg)\
                .replace('iname(12)///',iname)\
                .replace('$r',str(irarity) + ' ')\
                .replace('stime(41)////////////////////////////////',str(ialias))
            for i in akm_data:#提取
                if i['itemId'] == outdata['itemId']:
                    ilist.append(i)
            msglist =[]
            for o in ilist:#要处理的akm数据 o
                for p in aks_data:#读取物品此时的aks数据 p
                    if o['stageId'] == p['stageId']:
                        sname = '#FFFFFF\\' + await rep(16,p['name'])
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
                imsg = listp + aks_map2.replace('#FFFFFF\\name(24)////////',sname)
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

            img = "./chace/ak.png"
            toimg(outmsg,img)
            await app.sendGroupMessage(group,MessageChain.create([Image.fromLocalFile("./chace/out.png")]))    
#├info |获取上一个色图详情
    elif msg.startswith('info') and group.id in setu_group:
        outmsg = last_setu[str(member.id)]
        await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
#├debug |获取个人debug信息
    elif msg.startswith('debug') and group.id in setu_group:
        id = str(member.id)
        info = 'hsolv_data=' +  str(hsolv_data[id]) + '\nhsolvlist_data=' + str(hsolvlist_data[id]) + '\nqd_data=' + str(qd_data[id]) + '\nqdlist_data=' + str(qdlist_data[id])
        await app.sendGroupMessage(group,MessageChain.create([Plain(info)]))
#├hsolv <Int/list>| hsolv等级获取(qq) / lsp排行榜
    elif msg.startswith("hsolv"):
        print('hsolv')
        msg = msg.replace("hsolv",'')
        if msg.startswith('list') and group.id in setu_group:
            print('list')
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
                                inmsg = '$item:$int'.replace('$item',itemid.name).replace('$int',str(hsolvlist_data[item]))
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
                        out = out + '\\' + hsomap[r] + '\\' + ''.join(i)
                    
                    res[n] = '\\b20\\ \\b30\\' + out + '\\b25\\\\#FF0000\\'
                elif n == 1:
                    res[n] = res[n] + '\\b20\\\\#FF3300\\'
                elif n == 3:
                    res[n] =  res[n] + '\\#FF6600\\'
                elif n == 6:
                    res[n] = res[n] + '\\#FF9900\\'
                elif n == 9:
                    res[n] = res[n] + '\\#FFCC00\\'
                elif n == 12:
                    res[n] = res[n] + '\\#FFFF00\\'
                elif n == 15:
                    res[n] = res[n] + '\\#FFFF66\\'
                elif n == 18:
                    res[n] = res[n] + '\\#FFFFCC\\'
                elif n == 21:
                    res[n] = res[n] + '\\#FFFFFF\\'

                res[n] = res[n] + ' \\n\\ '
                n = n + 1
            a = ''.join(res)
            msg = "-lsp排行榜:\\#FF0000\\ \\n\\" + a + "\\n\\    \\xx>0\\ \\xy>0\\\\b20\\\\#FFFFFF\\ "
            for i in res:
                msg = msg + '\\n\\|'
            for i in range(3):
                msg = msg + '\\n\\|'
            print(msg)
            toimg(msg)
            await app.sendGroupMessage(group,MessageChain.create([Image.fromLocalFile("./chace/out.png")]))
    #-显示hsolv等级
        else:
            try:
                print("printhsolv")
                id = int(msg.replace("-","").replace(' ',''))
                mid = 0
                mid = int(hsolvlist_data[str(id)])
                outmsg = str(id) + "的hso等级为" + str(mid)
                await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))
            except:pass
#└backup |备份
    elif msg.startswith('backup') and member.id in admin:
        savecfg()
        srcfile='./cfg.json'
        name = Time.strftime('%Y-%m-%d-%H',Time.localtime(Time.time()))
        dstfile='./backups/'+ name + '.json'
        shutil.move(srcfile,dstfile)
        outmsg = name + '已备份'
        await app.sendGroupMessage(group,MessageChain.create([Plain(outmsg)]))


#后处理项目
    savecfg()
    timenow = math.floor( Time.time() / 60 / 60 / 24 )
    ltime = cfg['time']
    if timenow - ltime >= 1:
        cfg['time'] = math.floor( Time.time() / 60 / 60 / 24 )
        await app.sendGroupMessage(xmlimg_group,MessageChain.create([Plain('执行自动重启项目----')]))
        srcfile='./cfg.json'
        name = Time.strftime('%Y-%m-%d-%H',Time.localtime(Time.time()))
        dstfile='./backups/'+ name + '.json'
        shutil.move(srcfile,dstfile)
        print(timenow)
        for i in qd_data:
            qd_data[i] = 0
        savecfg()
        await Ak.i()
        await Ak.s()
        await Ak.m()
        restart_program()

@bcc.receiver("MemberJoinEvent")
async def member_join(app: GraiaMiraiApplication,event: MemberJoinEvent):
    print(event.member.id,'加入了本群')

@bcc.receiver("NewFriendRequestEvent")
async def friend_request(app: GraiaMiraiApplication,event: NewFriendRequestEvent):
    mid = event.supplicant
    try:
        if hsolvlist_data[str(mid)] > 30 : await event.accept('喵~')
        else : await event.reject('哼~不给加好友')
    except:await event.reject('哼~不给加好友')


app.launch_blocking()

try:
    loop.run_forever()
except KeyboardInterrupt:
    exit()