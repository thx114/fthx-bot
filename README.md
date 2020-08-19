# fthx-bot
这是一个基于[`Application/Graia Framework`](https://github.com/GraiaProject/Application)的机器人


### 他能做什么

+ [x] setu相关
+ [x] 发送带自定义文字的图片
+ [x] 签到
+ [x] 极其简陋的聊天系统
+ [ ] 自动重置签到,色图限制
+ [ ] 请求频率限制
+ [ ] 处理添加好友请求
+ [ ] 集中的配置加载/处理系统

**此项目是我边学边做的产物,实际代码可能十分丑陋,会在未来慢慢重写**

### 使用

写的太烂了,不建议您使用此bot

  ```
  1.pip install -r requirements.txt
  
  ```
  
  2.在`bot.py`中输入你的`host`，`authKey`，`account`
 
  3.在`runtimetext.py`里`admin`与`op`中输入`主人qq号`
 
  4.启动

### 关于配置文件:

(配置文件太多了，以后会写配置载入系统的)

runtimetext.py中:

  `f1`:中文字体，将文字写入图片时中文采用的字体 （我使用的是ResourceHanRoundedCN-Heavy

  `f2`:英文字体，将文字写入图片时英文采用的字体，该字体宽度应是中文字体的一半 （我使用的是GenShinGothic-Monospace-Heavy

  `feback`:聊天系统，可以按照例子添加文字

### 许可证

我们使用 [`GNU AGPLv3`](https://choosealicense.com/licenses/agpl-3.0/) 作为本项目的开源许可证
