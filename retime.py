# -*- coding:utf-8 -*-
import os
import threading
import time
cancel_tmr = False

def heart_beat():
    # 打印当前时间
    print(time.strftime('%Y-%m-%d %H:%M:%S'))
    if not cancel_tmr:
        start()
        # 每隔10分钟执行一次
        # threading.Timer(600, heart_beat).start()
        # 每隔600秒执行一次
        threading.Timer(600, heart_beat).start()
def start():
    os.system('python matchinfo.py')
if __name__ == '__main__':
    heart_beat()
    # 300分钟后停止定时器
    time.sleep(172000)
    # 30秒后停止定时器
    # time.sleep(30)
    cancel_tmr = True
