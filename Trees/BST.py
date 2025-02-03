class BinarySearchTreeNode():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def add_child(self,data):
        if self.data==data:
            return data
        if data<self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left=BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right=BinarySearchTreeNode(data)
    def in_order_traversal(self):
        elements=[]
        if self.left:
            elements+=self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements+=self.right.in_order_traversal()
            
        return elements
    def search(self,val):
        if val==self.data:
            return True
        if val<self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val>self.data:
            if self.right:
                return self.right.search(val)
            else: return False
    def min(self):
        if self.left is None: return self.data
        else: return self.left.min()
    def max(self):
        if self.right is None:
            return self.data
        else: return self.right.max
    def delete(self,val):
        if val <self.data:
            if self.left:
                self.left=self.left.delete(val)
        elif val>self.data:
            if self.right:
                self.right=self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            min_val =self.right.min()
            self.data=min_val
            self.right=self.right.delete(min_val)
        return self
            
def build_tree(elements):
    root=BinarySearchTreeNode(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root 
if __name__=='__main__':
    arr=[18,1,5,4,21,19,20]
    number_tree=build_tree(arr)
    print(number_tree.in_order_traversal())
    i=21
    number_tree.delete(i)
    print("remove",i,"->",number_tree.in_order_traversal())