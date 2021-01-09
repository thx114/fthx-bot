# fthx-bot
这是一个使用Mirai,[`Application/Graia Framework`](https://github.com/GraiaProject/Application)编写的机器人


# 他能做什么

+ [x] 色图相关(lolicon + 本地) 
+ [x] 以图搜图
+ [x] 明日方舟关卡掉落，物品查询(企鹅物流,自动做表格)
+ [x] 十分优美的文字转图片系统

# todos:

+ [x] 集中的配置加载/处理系统
+ [x] 签到系统已经被色图吞并
+ [ ] 请求频率限制
+ [ ] 处理添加好友请求
+ [ ] 基于好感度的养成聊天系统



**此项目是我边学边做的产物,实际代码可能看了会吐血,会在未来慢慢重写**

# 使用


  1.安装[**Graia Application**](https://github.com/GraiaProject/Application)以及前置包括mirai等

  2.`git clone https://github.com/thx114/fthx-bot.git`

  3.`pip install -r requirements.txt`
  
  4.在`runtimetext.py`里按照注释写入相应的信息
 
  5.启动`bot.py`

# 关于配置文件:

runtimetext.py中:

  `fl1`:中文字体，将文字写入图片时中文采用的字体 （我使用的是*ResourceHanRoundedCN-Heavy

  `fl2`:英文字体，将文字写入图片时英文采用的字体，该字体宽度应是中文字体的一半 （我使用的是*GenShinGothic-Monospace-Heavy
  
  `lolicon_key` 与 `saucenao_key` 需要自行获取并填入

cfg.json中:

  这里的东西基本不用太动，大部分都是用指令修改
  
色图:

  获取的色图会第一时间发出去，并存放在文件夹中，当300张色图用完时使用本地色图
 
# 许可证

使用 [`GNU AGPLv3`](https://choosealicense.com/licenses/agpl-3.0/) 作为本项目的开源许可证
