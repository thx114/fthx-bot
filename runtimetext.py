######填入信息:
bot_qq = 1000100010 #在此填入bot_qq号
authKey = "qaq1234" #在此填入http api 中的 authKey
host_ = "http://127.0.0.1:8080" #在此填入http api 中的 host

refresh_token = "TNBdsx5vr_aHKp22BNsSqG4uKJFKYyVqIVRSSofdgf4" #你的p站refresh_token (获取方法https://gist.github.com/ZipFile/c9ebedb224406f4f11845ab700124362)


lolicon_key = "12345ioawd" #你的lolicon apikey
saucenao_key = "67890oasof" #你的saucenao apikey

admin = [20002000]  #主人的qq号 
xmlimg_group = 200002000 #为了发xml而让机器人上传图片的群(工具群)
maxx_img = 1080 #下载后的色图最大宽度 0为无限    !!!启用xml色图时此项最好<=1080!!!
maximgpass = 100 #toimg 文字写入图片系统中:单个文字能跨过(图片中的)图片的最多次数

oncesetuadd = 4 #色图补充器一次性补充的色图数 /超过4不会有效率提升
setus = 20 #色图缓存库至少存储色图量

fl1 = "C:/WINDOWS/Fonts/ResourceHanRoundedCN-Heavy.ttf" #你的绘图(默认)中文字体
fl2 = "C:/WINDOWS/Fonts/GenShinGothic-Monospace-Heavy.ttf" #你的绘图(默认)英文字体
#######此文件更新后通常下方内容也会更新

thetypes = [1,2,3,4,5,6,7,8]
hsomap = ['#FFFF00','#FFCC00','#FF9900','#FF6600','#FF3300','#FF0000','#00FF00','#0000FF','#FF00FF','#66FFFF','#6600FF','#6633FF','#6666FF','#6699FF','#66CCFF','#66FFFF','#3300FF','#FFCCFF','#CC9900']
infomap = '''标题:title pid:$pid
作者:author uid:$uid
url
大小: mxxmy
标签:tags
'''
aks_map="""
 ╭ ────────────────── \\b15\ \\b45\关卡掉落\\b15\   \\b30\──────────────────── ╮ \\n\\
 │    \\b15\\by F_thx\\b30\                                   \\b15\\-数据来自企鹅物流 \\b30\\   │\\n\\
 │ \\#99FFFF\关卡名称\\#FFFFFF\:sname(12)/// \\#99FFFF\理智消耗\\#FFFFFF\:scost(23)//////////////│\\n\\
 │ \\#99FFFF\最短通关时间\#FFFFFF\:stime(41)////////////////////////////////│\\n\\
 ├ ───────────────────────────────────────────────────── ┤\\n\\
 │ \\#FFFFFF\名称    \\#FFFFFF\          \\#FFFFFF\数量\\#FFFFFF\    \\#FFFFFF\掉率     期望理智  期望用时 │\\n\\"""

aks_map2 = """ │ \\#FFFFFF\\name(24)////////\\#FFFFFF\│ num(6)│ rate(7)│ lz(8)//// time(9)//│\\n\\"""
aks_map3 = """ ╰ ───────────────────────────────────────────────────── ╯\\n\\"""
aki_map="""
 ╭ ─────────────────── \\b15\ \\b45\ 物品 \\b15\   \\b30\────────────────────── ╮\\n\\
 │    \\b15\\by F_thx\\b30\                                   \\b15\-数据来自企鹅物流 \\b30\   │\\n\\
 │ 图片\\#99FFFF\物品名称\\#FFFFFF\:iname(12)/// \\#99FFFF\稀有度\\#FFFFFF\:$r                   │\\n\\
 │     \\#99FFFF\别名\\#FFFFFF\:stime(41)////////////////////////////////│\\n\\
 ├ ───────────────────────────────────────────────────── ┤\\n\\
 │ \\#FFFFFF\关卡名称\\#FFFFFF\          \\#FFFFFF\数量\\#FFFFFF\    \\#FFFFFF\掉率     期望理智  期望用时 │\\n\\
"""
Search_map = '''
 ╭ ────────────────── \\b15\ \\b45\以图搜图\\b15\   \\b30\──────────────────── ╮ \\n\\
 │    \\b15\\by F_thx\\b30\                            \\b15\-数据来自$from(17)////////\\b30\      │\\n\\
 │ \#99FFFF\搜索图片\#FFFFFF\:\p$s180x360\                                             │\\n\\
 │                                                       \\xx>855\\│\\n\\
 │                                                       \\xx>855\\│\\n\\
 │                                                       \\xx>855\\│\\n\\
 │                                                       \\xx>855\\│\\n\\
 │                                                       \\xx>855\\│\\n\\
 ├ ───────────────────────────────────────────────────── \\xx>855\\┤\\n\\
 │ \#FFFFFF\图片    \#FFFFFF\          \#FFFFFF\标题\#FFFFFF\          \#FFFFFF\作者         来源     \\xx>855\\│\\n\\

'''
Search_map2 = '''
 │ \p$i120x240                 $title(13)/// $user(13)/// $from(9)/\\xx>855\\│\\n\\
 │                                                       \\xx>855\\│\\n\\
 │                                                       \\xx>855\\│\\n\\
 │                                                       \\xx>855\\│\\n\\
'''

helptext = """admin:
  test :test
  restart :重启机器人
  akra :更新全部明日方舟数据并重启机器人
  akri :更新 明日方舟 物品 数据
  akrs :更新 明日方舟 关卡 数据
  akrm :更新 明日方舟 掉落 数据
  hsolvr :重置色图签到
  hsolv+ <qqid> :为<qqid>增加10色图
  backup :备份cfg.json
  sg setu +/- :开启/关闭 此群色图权限
  sg r18 +/- :开启/关闭 此群r18权限

普通:
  /帮助 :帮助
  <@机器人> <图片> :以图搜图
  <图片:色图来> :普通色图
  色图来 <数量/搜索内容> :普通色图
  不够色 :r18色图
  info :获取此群最后一个色图的详细信息
  xml on/off :开启/关闭 全局色图xml
  排行榜 <mode>:获取p站排行榜
    -mode : day week month day_r18 week_r18 week_r18g
  tp <数字1~5> 获取排行榜目标详细信息
  hsolvlist :LSP排行榜
  aks <关卡名字> :查询此关卡
  aki <物品名字> :查询此物品
"""
