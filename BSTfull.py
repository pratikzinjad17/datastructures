class Node(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BST(object):
    def __init__(self):
        self.root=None

    def Insert(self,data):
        if not self.root:
            self.root=Node(data)
        else:
            self.InsertValue(data,self.root)
    def InsertValue(self,data,node):
        if data>node.data:
            if node.right:
                self.InsertValue(data,node.right)
            else:
                node.right=Node(data)
        else:
            if node.left:
                self.InsertValue(data,node.left)
            else:
                node.left=Node(data)
    def GetMax(self):
        if self.root:
            return self.GetMaxValue(self.root)
    def GetMaxValue(self,node):
        if node.right:
            return self.GetMaxValue(node.right)
        else:
            return node.data
    def GetMin(self):
        if self.root:
            return self.GetMinValue(self.root)

    def GetMinValue(self,node):
        if node.left:
            return self.GetMinValue(node.left)
        else:
            return node.data
    def Remove(self,data):
        if self.root:
            self.root=self.RemoveValue(data,self.root)
    def RemoveValue(self,data,node):
        if not node:
            return node
        if data>node.data:
            node.right=self.RemoveValue(data,node.right)
        elif data<node.data:
            node.left=self.RemoveValue(data,node.left)
        else:
            if not node.left and not node.right:
                print('leaf node deleted:')
                del node
                return None
            if not node.right:
                print('node which has single left child deleted: ')
                temp=node.left
                del node
                return temp
            elif not node.left:
                print('node which has single right child is deleted:')
                temp=node.right
                del node
                return temp
            else:
                print('node deleted which has both left and right child:')
                temp=self.Predecessor(node.left)
                node.data=temp.data
                node.left=self.RemoveValue(temp.data,node.left)

        return node        
    def Predecessor(self,node):
        if node.right:
            return self.Predecessor(node.right)
        
        return node
    def Inorder(self):
        if self.root:
            self.TraverseInorder(self.root)
    def TraverseInorder(self,node):
        if node.left:
            self.TraverseInorder(node.left)
        print("%s " % node.data)
        if node.right:
            self.TraverseInorder(node.right)
    def Preorder(self):
        if self.root:
            self.TraversePreorder(self.root)
    def TraversePreorder(self,node):
        print(node.data)
        if node.left:
            self.TraversePreorder(node.left)
        if node.right:
            self.TraversePreorder(node.right)
         
   #search is pending             









b=BST()
b.Insert(4)
b.Insert(3)
b.Insert(1)
b.Insert(6)
b.Insert(5)
b.Insert(2)

print(b.Preorder())
print('INORDER:')
print(b.Inorder())
print('MIN:',b.GetMin())
print('MAX:',b.GetMax())
b.Remove(6)
print('INORDER:',b.Inorder())
b.Remove(4)
print('INORDER:',b.Inorder())



        
