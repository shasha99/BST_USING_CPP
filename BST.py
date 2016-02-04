class Node:
    def __init__(self,val):
        self.left=None
        self.right=None
        self.value=val
        
class BST:
    def __init__(self):
        self.root=None
        
    def insert(self,val):
        self.root=self._insert(self.root,val)
        
    def _insert(self,ptr,val):
        if ptr is None:
            return Node(val)
        elif ptr.value==val:
            print("Already exists")
        elif ptr.value < val:
            ptr.right=self._insert(ptr.right,val)
        else:
            ptr.left=self._insert(ptr.left,val)
        return ptr
        
    def search(self,val):
        self._search(self.root,val)
        
    def _search(self,ptr,val):
        if ptr is None:
            print("Not found")
        elif ptr.value == val:
            print("Found")
        elif ptr.value < val:
            self._search(ptr.right,val)
        else:
            self._search(ptr.left,val)
        
        
    def delete(self,val):
        self._delete(self.root,val)
        
    def _delete(self,ptr,val):
        if ptr is None:
            print("Not Found")
        elif ptr.value < val:
            ptr.right=self._delete(ptr.right,val)
        elif ptr.value > val:
            ptr.left=self._delete(ptr.left,val)
        else:
            if ptr.left is None or ptr.right is None:
                ptr=ptr.left if ptr.right is None else ptr.right
            else:
                temp=ptr.right
                while(temp1.left is not None):
                    temp=temp.left
                ptr.value=temp.value
                ptr.right=self._delete(ptr.right,temp.value)
        return ptr
        
    def inorder(self):
        self._inorder(self.root)
        
    def _inorder(self,ptr):
        if ptr is not None:
            self._inorder(ptr.left)
            print(" "+str(ptr.value))
            self._inorder(ptr.right)
            
    
def main():
    b=BST()
    b.insert(20)
    b.insert(10)
    b.insert(30)
    b.delete(10)
    b.inorder()
    b.insert(5)
    b.insert(6)
    b.inorder()
    b.insert(35)
    b.delete(30)
    b.inorder()
    b.insert(15)
    b.inorder()
main()