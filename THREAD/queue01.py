# encoding=utf-8
import queue
import threading

# 先进先出
fifoQueue = queue.Queue()
# 后进先出
lifoQueue = queue.LifoQueue()

# 队列数据初始化
for i in range(5):
    fifoQueue.put(i)
    lifoQueue.put(i)

# 打印队列数据
while not fifoQueue.empty():
    print("first int first out = {fifo}，last in first out = {lifo}  ，".format(  fifo = str(fifoQueue.get()) ,  lifo = str(lifoQueue.get())))