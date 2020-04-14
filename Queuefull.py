class Queue(object):
    def __init__(self):
        self.queue=[]
    def Enqueue(self,data):
        self.queue.append(data)
    def Dequeue(self):
        data=self.queue[0]
        self.queue.pop(0)
        print('deleted:',data)
    def Peek(self):
        data=self.queue[0]
        print(data)
    def QueueSize(self):
        print('size:',len(self.queue))
    def PrintQueue(self):
        for i in range(len(self.queue)):
            print(self.queue[i])

q=Queue()
q.Enqueue(1)
q.Enqueue(2)
q.Enqueue(3)
q.Enqueue(4)
q.Enqueue(5)
q.PrintQueue()
q.QueueSize()
q.Dequeue()
q.Dequeue()
q.PrintQueue()
q.QueueSize()
