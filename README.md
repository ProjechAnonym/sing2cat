# clash-singbox
一款能够将机场的clash配置文件自动转换为singbox配置文件的软件,singbox需要支持clashAPI以及gvisor支持。目前支持的协议有:
* vmess
* ss
* trojan
均为机场常见协议,需要新的协议可以自己添加,代码是模块化的,添加新的协议对于有一点点编程基础的人不是很难。
# 说明
## 关于DNS
* 国内DNS:223.5.5.5
* 国外DNS:8.8.8.8
* 查询节点IPDNS:1.1.1.1
以上DNS均使用https加密,强烈建议使用加密DNS,不要用原始的UDP的DNS,QoS不说还泄露。
## host劫持
singbox支持出站覆写IP和端口,基于此编写配置文件的出站和路由规则可以实现host劫持的效果,在程序中有提示host劫持该如何编写,这里不再赘述。
## clash支持
* 默认端口:9090
* 密码:123456
* 访问url:http://ip:9090
clashAPI的支持使得singbox可以任意切换节点,这在看流媒体的时候很有意义
## 关于编译
使用python写的代码,pyinstaller打包的,mac用户需要自行打包一下,作者过于贫穷买不起mac,虚拟机又非常卡于是就把mac程序暂时不列入考虑范围,mac用户需要编译的话下载main.spec文件,修改pathex和hiddenimports,另外python需要安装有yaml和pyside6包。
* pathex = ["你的项目路径"]
* hiddenimports = ["你的项目路径/Gui","你的项目路径/jsProcess"]

