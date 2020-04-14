class Node(object):
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList(object):
    def __init__(self):
        self.head=None
        self.size=0

    def Insert(self,data):
        self.data=Node(data)
        self.size=self.size+1

        if self.head==None:
            self.head=self.data
        else:
            self.data.next=self.head
            self.head=self.data
    def Size(self):
        return self.size
    def PrintList(self):
        tem=self.head
        while tem is not None:
            print(tem.data)
            tem=tem.next

    def InsertEnd(self,data):
        self.data=Node(data)
        self.size=self.size+1
        if self.head==None:
            self.head=self.data
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=self.data
    def Insertafter(self,prev,data):
        newnode=Node(data)
        newnode.next=prev.next
        prev.next=newnode
    def Search(self,key):
        current=self.head
        found=False
        count=1
        while current and found is False:
            if current.data==key:
                found=True
            else:
                current=current.next
                count=count+1
        if current is None:
            raise ValueError('Data not in list')
        print(current.data,count)

    def Delete(self,key):
        current=self.head
        previous=None
        found=False
        self.size=self.size-1
        while current and found is False:
            if current.data==key:
                found=True
            else:
                previous=current
                current=current.next
        if current is None:
            raise ValueError('data not in the list')
        if previous is None:
            self.head=current.next
        else:
            previous.next=current.next
        
                
            

l=LinkedList()
l.InsertEnd(10)
l.InsertEnd(20)
l.InsertEnd(30)
l.InsertEnd(40)
l.InsertEnd(50)
l.InsertEnd(60)
l.Search(50)
l.Delete(50)
l.PrintList()
print(l.Size())
        
        
