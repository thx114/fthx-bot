bot_qq = qq  #机器人的qq
authkey = "key"  #你在http api配置中设置的authkey 
host_ = "http://127.0.0.1:8080" #你在http api设置的host
setu_ = 'C:/qaq/' #你的色图文件夹地址
setu_remove_ = 'C:/qaq2/' #你的色图移除暂存文件夹


admin = [1764362678] #主人的qq
op = [1764362678,1256779787,2922150732,3370171857,2538723194] #可移除色图的op
thetypes = [1,2,3,4,5,6,7,8]
f1 = "C:\\WINDOWS\\Fonts\\ResourceHanRoundedCN-Heavy.ttf"
f2 = "C:\\WINDOWS\\Fonts\\GenShinGothic-Monospace-Heavy.ttf"
resotypes = ['zhihu','weibo','weixin','baidu','toutiao','163','xl','36k','hitory','sspai','csdn','juejin','bilibili','douyin','52pojie','v2ex','hostloc']
listtype = ["1",'2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19',"20"]
istomsg = {"\\n":"‘","##":"’#","\\b":"；",'【':'[','】':']','《':'<','》':'>','？':'?','”':'"','“':'"'}
mainmap="""
╭ ──────────────── ；20  ；40菜单；20  ；30──────────────── ╮‘
│    ；15by F_thx；30                  ；15-使用’#99FFFFh ’#CCFF33[指令]’#FFFFFF:查看相应用法；30    │‘
│ ’#99FFFFping’#FFFFFF    :ping ip    ’#99FFFFimg’#FFFFFF     :生成文字图片 │‘
│ ’#99FFFF来份色图’#FFFFFF:获取色图  ’#99FFFF 统计色图’#FFFFFF:统计色图个数 │‘
│ ’#99FFFFh 扫雷’#FFFFFF  :扫雷游戏  ’#99FFFF setu+’#CCFF33[图片]’#FFFFFF:加入色图库│‘
│ ’#99FFFF舔狗日记’#FFFFFF:舔狗日记 ’#99FFFF  历史’#FFFFFF    :历史上的今天 │‘
│ ’#99FFFF百科 ’#CCFF33[信息]’#FFFFFF:查找百科’#99FFFFrep’#CCFF33 [id]’#FFFFFF:这图不够色   │‘
│ ’#99FFFF直链 ’#CCFF33[链接]’#FFFFFF:网盘直链’#99FFFF群直链’#CCFF33 [id]’#FFFFFF:加群链接  │‘
│’#99FFFF 热榜’#CCFF33 [接口/id]’#FFFFFF:热榜’#99FFFF 网抑云’#FFFFFF:网易云热评     │‘
│ ’#99FFFF短链 ’#CCFF33[接口] [链接]’#FFFFFF:生成短链 (接口选填)    │‘
╰ ───────────────────────────────────────── ╯‘
╭ ──────────── ；20  ；40管理员功能；20  ；30──────────── ╮‘
│    ；15        ；30                                   │‘
│ ’#99FFFF更新色图’#FFFFFF:从服务器更新色图                 │‘
│ ’#99FFFFhsolv’#FFFFFF:色图限制相关,’#99FFFFh hsolv’#FFFFFF 查看用法       │‘
│ ’#99FFFFsg+’#FFFFFF/’#99FFFFsg-’#FFFFFF ’#CCFF33[群号]’#FFFFFF:给予或删除某群的色图权限   │‘
│ ’#99FFFFban’#FFFFFF:禁用某人色图权限   ’#99FFFFrun’#FFFFFF:运行def        │‘
╰ ───────────────────────────────────────── ╯‘
"""
sl = """；20##FFFFFF
╭ ──────────────────── ；20  ；40扫雷；20  ；20─ ╮‘
│ 欢迎游玩扫雷小游戏                 │‘
│ ##99FFFFm 开始 ##ffffff:即可开始游戏               │‘
│ ##99FFFFm 中级##ffffff/##99FFFF高级 ##ffffff:开始不同难度游戏      │‘
│ ##99FFFFm ##CCFF33[长] [宽] [雷数] ##ffffff:开始自定义游戏 │‘
│ ##99FFFFm d ##CCFF33[位置1] ... ##ffffff:来挖开多个方快    │‘
│ ##99FFFFm t ##CCFF33[位置1] ... ##ffffff:来标记多个方块    │‘
│ ##99FFFFm show ##ffffff:来重新查看游戏盘           │‘
│ ##99FFFFm help ##ffffff:来查看帮助                 │‘
│ ##99FFFFm exit ##ffffff:退出游戏                   │‘
╰ ────────────────────────────────── ╯‘        
"""

hsolvtext = """；20##FFFFFF
╭ ─────────────────── ；20  ；30hsolv帮助；20  ；10─；20─ ╮‘
│ ##99FFFFhsolvlist##FFFFFF:获取lsp榜单                   │‘
│ ##99FFFFhsolv- ##CCFF33[qq号]##FFFFFF:将指定qq hso等级清零      │‘
│ ##99FFFFhsolvch ##CCFF33[数字]##FFFFFF:设置色图的撤回时间       │‘
│ ##99FFFFhsolv ##CCFF33[qq号]##FFFFFF:查看指定qq的 hso等级       │‘
│ ##99FFFFhsolvmax ##CCFF33[数字]##FFFFFF:设置色图请求上限        │‘
╰ ─────────────────────────────────────── ╯   ‘       

"""

dlmsg = """；20##FFFFFF
╭ ─────────────────── ；20  ；30 短链帮助；20  ；10 ；20── ╮‘
│                                          │‘
│ ##99FFFF短链 ##CCFF33[地址]##FFFFFF:获取地址的t.cn短链           │‘
│ ##99FFFF短链 ##CCFF33[接口] [地址]##FFFFFF:获取地址的指定接口短链│‘
│   1     返回 t.cn 短网址                 │‘
│   2     返回 url.cn 短网址               │‘
│   3     返回 dwz.mk 短网址               │‘
│   4     返回 suo.im 短网址               │‘
│   5     返回 u.nu 短网址                 │‘
│   6     返回 mrw.so 短网址               │‘
│   7     返回 suo.nz 短网址               │‘
│   8     返回 sohu.gg 短网址              │‘
╰ ──────────────────────────────────────── ╯   ‘        
"""

rb= """；20##FFFFFF
╭ ─────────────────── ；20  ；30 热榜帮助；20  ；10 ；20── ╮‘
│                                          │‘
│##99FFFF 热榜 ##FFFFFF:获取Bilibili的每日排行榜           │‘
│##99FFFF 热榜 ##CCFF33[id]##FFFFFF:获取热榜指定id的跳转链接       │‘
│##99FFFF 热榜 ##CCFF33[接口]##FFFFFF:获取指定接口的热榜           │‘
│ 接口:zhihu,weibo,weixin,baidu,toutiao    │‘
│ 163,xl,36k,hitory,sspai,csdn,juejin      │‘
│ bilibili,douyin,52pojie,v2ex,hostloc     │‘
╰ ──────────────────────────────────────── ╯   ‘         
"""

imgh ="""；20
╭ ─────────────────── ；20  ；30img帮助；20  ；10─；20── ╮‘
│                                       │‘
│ ’#99FFFFimg ’#CCFF33[信息] ’#FFFFFF:将信息内容生成为图像          │‘
│                                       │‘
│ 以下为信息内的内容的解释：             │‘
│ ’#CCFF33#·#’#FFFFFF:修改后面的字体颜色 例: #·#FF0000    │‘
│ ’#CCFF33\·b’#FFFFFF:修改后面的字体的大小 例: \·b20      │‘
│ ’#CCFF33符号(点) ’#FFFFFF:忽略符,阻断检测 例: \(点)n  │‘
│ ’#CCFF33\·n’#FFFFFF:换行                               │‘
╰ ───────────────────────────────────── ╯   ‘  
"""

feback={
    'data':[{
    '$符':'等级一的对话:',
    '喵':'喵~|喵呜|喵喵喵|唔喵~|摸~|喵喵~~',
    '摸头':'唔~|喵~QAQ|~~|要摸秃啦(#ﾟДﾟ)|(*๓´╰╯`๓)',
    '透':'人家还小QAQ|嘤嘤嘤不要呀',
    '嘤嘤嘤':'嘤嘤嘤|为什么要学狐狸叫呀|嘤！|摸摸头|啊这',
    },
    {
    '$符':'lsp的对话',
    '喵':'喵喵喵?|舔~|喵?!',
    '摸头':'(乖巧)|嘻嘻',
    '透':'哇唔...轻点嘛♡|嘤嘤嘤..|唔喵 ..还想要♡|要坏掉惹..♡',
    '嘤嘤嘤':'嘤嘤嘤?|嘤嘤！|抱走你哦~|想干嘛哦'
    },
    {
    '$符':'主人的对话',
    '喵':'喵喵喵?|舔~|喵?!|唔喵~',
    '摸头':'(乖巧)♡|嘻嘻',
    '透':'嘤嘤嘤♡..|还想要♡~|好...好舒服♡|要坏掉惹♡....|主人好棒呀~♡',
    '嘤嘤嘤':'嘤嘤嘤?|嘤嘤！'
    }






    ]
}
