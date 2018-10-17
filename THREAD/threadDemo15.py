from threading import Thread,Lock
import time
mutexA=Lock()
mutexB=Lock()

class MyThread(Thread):
    def run(self):
        self.func1()
        self.func2()
    def func1(self):
        mutexA.acquire()
        print('\033[41m%s func1 拿到A锁\033[0m' %self.name)

        mutexB.acquire()
        print('\033[42m%s func1 拿到B锁\033[0m' %self.name)
        mutexB.release()
        print('\033[42m%s func1 释放B锁\033[0m' % self.name)
        mutexA.release()
        print('\033[41m%s func1 释放A锁\033[0m' % self.name)

    def func2(self):
        mutexB.acquire()
        print('\033[43m%s func2 拿到B锁\033[0m' %self.name)
        time.sleep(2)

        mutexA.acquire()
        print('\033[44m%s func2 拿到A锁\033[0m' %self.name)
        mutexA.release()
        print('\033[44m%s func2 释放A锁\033[0m' % self.name)

        mutexB.release()
        print('\033[43m%s func2 释放B锁\033[0m' % self.name)

if __name__ == '__main__':
    for i in range(10):
        t=MyThread()
        t.start()

'''
Thread-1 拿到A锁
Thread-1 拿到B锁
Thread-1 拿到B锁
Thread-2 拿到A锁
然后就卡住，死锁了
'''