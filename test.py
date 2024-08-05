 
from main import init,start
 
if __name__ == "__main__":
    init(
        path = 'C:/chrome/chrome.exe', #浏览器路径
        userdataDir='c:/chromecache', #浏览器数据目录
        extensions=['C:/chrome/extensions/adblock.crx'], #扩展插件
        httpport=8080, #http端口
        forcerun = True, #浏览器断开后自动重启连接
        )
    # start(3) #启动3个浏览器实例