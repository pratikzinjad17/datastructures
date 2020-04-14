class Stack(object):
    def __init__(self):
        self.stack=[]

    def Push(self,data):
        self.stack.append(data)
    def StackSize(self):
        return len(self.stack)
    def Pop(self):
        data=self.stack[-1]
        self.stack.pop()
        return data
    def Peek(self):
        data=self.stack[-1]
        return data
    def PrintStack(self):
        print(self.stack)

s=Stack()
s.Push(1)
s.Push(2)
s.Push(3)
s.Push(4)
s.Push(5)
print(s.StackSize())
s.PrintStack()
print('poped:',s.Pop())
print('poped:',s.Pop())
s.PrintStack()
