from threading import Thread
import time
def sayhi(name):
    time.sleep(1)
    print('%s say hello' %name)

if __name__ == '__main__':
    t=Thread(target=sayhi,args=('egon',))
    t.start()
    print(t.is_alive())
    t.join()
    print('主线程')
    print(t.is_alive())
