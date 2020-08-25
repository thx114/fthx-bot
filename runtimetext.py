######填入信息:
bot_qq = 11111111 #在此填入bot_qq号
authkey = "87654321" #在此填入http api 中的 authkey
host_ = "http://127.0.0.1:8080" #在此填入http api 中的 host
pixiv_name = "" #在此填入你的pixiv账号
pixiv_pw = "" #在此填入你的pixiv密码

setu_ = 'C:/outsetu/'  #你的色图文件夹路径
setu_remove_ = 'C:/setu/' #你的移除暂存文件夹路径
setu_add_ = 'C:/setuadd/' #你的增加色图文件夹
apikey = "" #你的saucenao apikey 没有请注册
admin = []  #主人的qq号 
op = [] #可移除色图的op的qq号

f1 = "C:/WINDOWS/Fonts/ResourceHanRoundedCN-Heavy.ttf" #你的绘图中文字体
f2 = "C:/WINDOWS/Fonts/GenShinGothic-Monospace-Heavy.ttf" #你的绘图英文字体
hash2= "1101100001010100100000101100001010000010111001011100000010100000" #色图来表情的哈希值
#######此文件更新后通常下方内容也会更新

thetypes = [1,2,3,4,5,6,7,8]
stag = ['10000users入り','5000users入り','1000users入り','500users入り','100users入り','']
stag2 = ['进行[10000收藏]搜索....','进行[5000收藏]搜索....','进行[1000收藏]搜索....','进行[500收藏]搜索....','进行[100收藏]搜索....','进行[无收藏]搜索....']
resotypes = ['zhihu','weibo','weixin','baidu','toutiao','163','xl','36k','hitory','sspai','csdn','juejin','bilibili','douyin','52pojie','v2ex','hostloc']
listtype = ["1",'2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19',"20"]
istomsg = {"\\n":"‘","##":"’#","\\b":"；","：":':','【':'[','】':']','《':'<','》':'>','？':'?','”':'"','“':'"','\\[':'【','\\]':'】',"\\d":"："}
hsomap = ['#FFFF00','#FFCC00','#FF9900','#FF6600','#FF3300','#FF0000','#00FF00','#0000FF','#FF00FF','#66FFFF','#6600FF','#6633FF','#6666FF','#6699FF','#66CCFF','#66FFFF','#3300FF','#FFCCFF','#CC9900']
mainmap="""
╭ ──────────────── ；20  ；40菜单；20  ；30─────────────── ╮‘
│    ；15by F_thx；30                  ；15-使用’#99FFFFh ’#CCFF33[指令]’#FFFFFF:查看相应用法；30   │‘
│ ’#99FFFFping’#FFFFFF    :ping ip    ’#99FFFFimg’#FFFFFF     :生成文字图片│‘
│ ’#99FFFF来份色图’#FFFFFF:获取色图  ’#99FFFF 统计色图’#FFFFFF:统计色图个数│‘
│ ’#99FFFF舔狗日记’#FFFFFF:舔狗日记 ’#99FFFF  历史’#FFFFFF    :历史上的今天│‘
│ ’#99FFFF百科 ’#CCFF33[信息]’#FFFFFF:查找百科’#99FFFFrep’#CCFF33 [id]’#FFFFFF:这图不够色  │‘
│ ’#99FFFF直链 ’#CCFF33[链接]’#FFFFFF:网盘直链’#99FFFF网抑云’#FFFFFF  :网易云热评  │‘
│’#99FFFF 热榜’#CCFF33 [接口/id]’#FFFFFF:热榜’#99FFFF tp’#CCFF33[id]’#FFFFFF  :搜图跳转详情│‘
│’#99FFFF 签到’#FFFFFF:签到获取色图  ’#99FFFF @我 ’#CCFF33[图片]’#FFFFFF:以图搜图  │‘
│’#99FFFF 搜’#CCFF33 [信息]’#FFFFFF:p站搜图   ’#99FFFF群直链’#CCFF33 [id]’#FFFFFF:加群链接 │‘
│ ’#99FFFF短链 ’#CCFF33[接口] [链接]’#FFFFFF:生成短链 (接口选填)   │‘
╰ ──────────────────────────────────────── ╯‘
╭ ──────────── ；20  ；40管理员功能；20  ；30─────────── ╮‘
│    ；15        ；30                                  │‘
│ ’#99FFFFhsolv’#FFFFFF:色图限制相关,’#99FFFFh hsolv’#FFFFFF 查看用法      │‘
│ ’#99FFFFsg+’#FFFFFF/’#99FFFFsg-’#FFFFFF’#FFFFFF:给予或删除某群的色图权限         │‘
│ ’#99FFFFban’#FFFFFF:禁用某人色图权限  ’#99FFFFbackup’#FFFFFF:备份cfg.json│‘
│ ##99FFFFsetu+ ##CCFF33[pid]##FFFFFF:从pid添加色图                │‘
│ ##99FFFFsetu+sf##CCFF33[pid]##FFFFFF:从缓存直接添加色图          │‘
│ ##99FFFF@我 setu+ ##CCFF33[图片]##FFFFFF:从以图搜图直接添加色图  │‘
╰ ──────────────────────────────────────── ╯‘
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
╭ ───────────────────   ；30 热榜帮助；20  ；10 ；20── ╮‘
│                                          │‘
│##99FFFF 热榜 ##FFFFFF:获取Bilibili的每日排行榜           │‘
│##99FFFF 热榜 ##CCFF33[id]##FFFFFF:获取热榜指定id的跳转链接       │‘
│##99FFFF 热榜 ##CCFF33[接口]##FFFFFF:获取指定接口的热榜           │‘
│ 接口:zhihu,weibo,weixin,baidu,toutiao,163│‘
│ xl,36k,hitory,sspai,csdn,juejin,pixiv    │‘
│ bilibili,douyin,52pojie,v2ex,hostloc     │‘
╰ ──────────────────────────────────────── ╯   ‘         
"""

imgh ="""；20
╭ ────────────────────── ；20  ；30img帮助；20  ；10 ；20── ╮‘
│                                          │‘
│ ’#99FFFFimg ’#CCFF33[信息] ’#FFFFFF:将信息内容生成为图像         │‘
│                                          │‘
│ 以下为信息内的内容的解释:                │‘
│ ’#CCFF33#·#’#FFFFFF:修改后面的字体颜色 例: #·#FF0000       │‘
│ ’#CCFF33\·b’#FFFFFF:修改后面的字体的大小 例: \·b20         │‘
│ ’#CCFF33符号(点) ’#FFFFFF:忽略符,阻断检测 例: \(点)n     │‘
│ ’#CCFF33\·d’#FFFFFF:在图片底部输入文字(不可逆)            │‘
│ ’#CCFF33\·[’#FFFFFF:居中文字的起始符 -里面无法改颜色与大小│‘
│ ’#CCFF33\·]’#FFFFFF:居中文字的终止符 例: \·[居中文字\·]     │‘
│ ’#CCFF33\·n’#FFFFFF:换行                                  │‘
╰ ──────────────────────────────────────── ╯   ‘  
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
    '透':'-----',
    '嘤嘤嘤':'嘤嘤嘤?|嘤嘤！|抱走你哦~|想干嘛哦'
    },
    {
    '$符':'主人的对话',
    '喵':'喵喵喵?|舔~|喵?!|唔喵~',
    '摸头':'(乖巧)♡|嘻嘻',
    '透':'-----',
    '嘤嘤嘤':'嘤嘤嘤?|嘤嘤！'
    }






    ]
}
