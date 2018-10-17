from threading import Thread
from multiprocessing import Process
import os
import time

def work():
    print('hello')

if __name__ == '__main__':
    print("%s " % (time.ctime(time.time())))

    #在主进程下开启线程
    t=Thread(target=work)
    t.start()
    print('主线程')
    print("%s " % (time.ctime(time.time())))

    #在主进程下开启子进程
    t=Process(target=work)
    t.start()
    print('主进程')
    print("%s " % (time.ctime(time.time())))
