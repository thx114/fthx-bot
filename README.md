# fthx-bot
这是一个使用Mirai,[`Application/Graia Framework`](https://github.com/GraiaProject/Application)编写的机器人


### 他能做什么

+ [x] setu相关
+ [x] 发送带自定义文字的图片
+ [x] 签到
+ [x] 极其简陋的聊天系统
+ [x] 以图搜图
+ [x] 其他基于api的一些功能:舔狗日记，历史上的今天等

###todos:

+ [x] 集中的配置加载/处理系统
+ [ ] 自动重置签到,色图限制
+ [ ] 请求频率限制
+ [ ] 处理添加好友请求


**此项目是我边学边做的产物,实际代码可能十分丑陋,会在未来慢慢重写**

### 使用

写的太烂了,不建议您使用此bot

  安装[Application](https://github.com/GraiaProject/Application)以及他的前置包括mirai等

  1.`git clone https://github.com/voidf/bot_irori.git`

  2.```pip install -r requirements.txt```
  
  3.在`runtimetext.py`里按照注释写入相应的信息
 
  4.启动

### 关于配置文件:

(配置文件太多了，以后会写配置载入系统的)

runtimetext.py中:

  `f1`:中文字体，将文字写入图片时中文采用的字体 （我使用的是ResourceHanRoundedCN-Heavy

  `f2`:英文字体，将文字写入图片时英文采用的字体，该字体宽度应是中文字体的一半 （我使用的是GenShinGothic-Monospace-Heavy

  `feback`:聊天系统，可以按照例子添加文字

### 许可证

我们使用 [`GNU AGPLv3`](https://choosealicense.com/licenses/agpl-3.0/) 作为本项目的开源许可证
