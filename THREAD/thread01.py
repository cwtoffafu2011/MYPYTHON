# encoding=utf-8

import thread
import time

# http://www.runoob.com/python3/python3-multithreading.html
# 为线程定义一个函数
def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s " % ( threadName, time.ctime(time.time())))

# 创建两个线程
try:
    thread.start_new_thread( print_time, ("thread-1", 2, ) )
    thread.start_new_thread( print_time, ("thread-2", 4, ) )
except:
    print("error: 无法启动线程")

while 1:
    pass

