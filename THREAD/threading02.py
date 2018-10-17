# encoding=utf-8
import threading
import time

# http://www.runoob.com/python3/python3-multithreading.html
# 说明：需要安装模块 thread-queue thread threading
# pip3 install thread-queue thread threading

# 线程同步  使用队列来实现线程间的同步

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print ("开启线程： " + self.name)
        # 获取锁，用于线程同步
        threadLock.acquire()
        # print_time(self.name, 1, self.counter)
        print_time(self.name, self.counter, 3)
        # 释放锁，开启下一个线程
        threadLock.release()

def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

threadLock = threading.Lock()
threads = []

# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()
print("开启新线程完了")

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)
print("添加线程到线程列表完了")

# 等待所有线程完成
for t in threads:
    t.join()
print ("退出主线程")