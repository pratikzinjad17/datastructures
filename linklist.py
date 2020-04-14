class Node(object):
    def __init__(self,data):
        self.data=data
        self.nextNode=None

class LinkedList(object):
    def __init__(self):
        self.head=None
        self.size=0

    def InsertNode(self,data):
        newNode=Node(data)
        self.size=self.size+1

        if(self.head==None):
            self.head=newNode
        else:
            newNode.nextNode=self.head
            self.head=newNode

    def Size(self):
        return self.size
    def PrintList(self):
        temp=self.head
        while temp is not None:
            print(temp.data)
            temp=temp.nextNode


l=LinkedList()
l.InsertNode(8)
l.InsertNode(7)
l.InsertNode(6)
l.InsertNode(5)
l.InsertNode(4)
l.InsertNode(3)
print(l.PrintList())
       
print(l.Size())        

        
