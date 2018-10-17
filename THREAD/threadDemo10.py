from threading import Thread
import os,time
def work():
    global n
    temp=n
    time.sleep(0.1)
    n=temp-1
if __name__ == '__main__':
    n=100
    l=[]
    for i in range(100):
        p=Thread(target=work)
        l.append(p)
        p.start()
    for p in l:
        p.join()

    print(n) #结果可能为99