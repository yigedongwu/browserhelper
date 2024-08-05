import time
from config import defaultConfig 
from browser import createBrowser,browsers
from httpserver import start
import threading
import os
import json
 
def doTask(name):
    print("执行任务:",name)
    #新建一个线程
    new_thread = None
    def task(): 
        page = None
        browser = createBrowser(name=name)
        run = True
   
        while run:
            try:
                time.sleep(2)
                 
                
                print("线程执行中",browser)
                
                
                page = browser.page
          
                r= page.run_js('document.title = Date.now();')
                
            except Exception as e:
              
                browser = createBrowser(name=name)
                if browser:
                    page = browser.page
                    #page.get("https://www.baidu.com/discover")
                    print(e, "异常")
                    # 退出整个程序
                    #os._exit(0)

                    
    new_thread = threading.Thread(target=task) 
    new_thread.start()

    
    #执行任务
    return "任务执行完毕"

def loadConfig():
    s = ''
    if not os.path.exists('配置.txt'):
        s = '{\n"浏览器路径": "C:/Program Files/Google/Chrome/Application/chrome.exe",\n "插件目录": ["插件目录1","插件目录2"],\n"端口":6299,\n"启动数量":1\n}'
        with open('配置.txt', 'w', encoding='utf-8') as f:
            f.write(s)
        return json.loads(s)
    with open('配置.txt', 'r', encoding='utf-8') as f:
        config = json.load(f)
        return config
 
if __name__ == "__main__":
    #判断zuds目录是否存在
    if not os.path.exists('zuds'):
        os.mkdir('zuds')
    config = loadConfig()
    print('用户配置',config)
    defaultConfig['path'] = config['浏览器路径']  # "C:/Program Files/Google/Chrome/Application/chrome.exe"
    defaultConfig['extensions'] = config['插件目录'] #["C:/Users/run/Desktop/projects/1youhou/01-douyinhelper/zdist"]
    defaultConfig['httpport'] = config['端口']
    for i in range(config['启动数量']):
        name = '浏览器'+str(i+1) 
        doTask(name)
    start()
 
    