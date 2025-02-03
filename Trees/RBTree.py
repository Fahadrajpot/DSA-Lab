class RBTreeNode:
    def __init__(self, key, color ="RED"):
        self.key = key
        self.left = None
        self.right = None
        self.parent =  None
        self.color = color
        
class RBTree:
    def __init__(self):
        self.NIL = RBTreeNode(None, "BLACK")
        self.root = self.NIL
        
    def leftRotate(self,x):
         y = x.right
         x.right = y.left
         if  y.left != self.NIL:
             y.left.parent = x
         y.parent = x.parent
         if x.parent == None:
             self.root = y
         elif x == x.parent.left:
             x.parent.left = y
         else:
             x.parent.right = y
         y.left = x
         x.parent = y
         
    def rightRotate(self,x):
        y= x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif  x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.right = x
        x.parent = y
    def insert(self,data):
        node = RBTreeNode(data)
        node.left = self.NIL
        node.right = self.NIL
        parent = None
        current = self.root
        while current != self.NIL:
            parent = current
            if node.key < current.key:
                current = current.left
            else:
                current = current.right
        node.parent = parent
        if node.parent is None:
            self.root = node
            self.root.parent = self.NIL
        elif node.key < parent.key:
            parent.left = node
        else:
            parent.right = node
            
        node.color = "RED"
        self.fixInsert(node)
    def fixInsert(self,z):
        while z.parent and z.parent.color == "RED":
            if z.parent.parent is None:
               break 
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right or self.NIL
                if  y.color == "RED":
                    z.parent.color = "BLACK"
                    y.color = "BLACK"
                    z.parent.parent.color = "RED"
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z= z.parent
                        self.leftRotate(z)
                    z.parent.color = "BLACK"
                    z.parent.parent.color = "RED"
                    self.rightRotate(z.parent.parent)
            else:
                y = z.parent.parent.left  or self.NIL

                if y.color == "RED":
                    z.parent.color = "BLACK"
                    y.color = "BLACK"
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.rightRotate(z)
                    z.parent.color = "BLACK"
                    z.parent.parent.color = "RED"
                    self.leftRotate(z.parent.parent)
                    
    def treeMinimum(self,node):
        while node.left != self.NIL:
            node = node.left
        return node
    def transplant(self,u,v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent
        
    def delete(self,key):
        node = self.search(self.root,key)
        if node is None:
            return
        y = node
        yOriginalColor =  y.color
        if node.left == self.NIL:
            x = node.right 
            self.transplant(node, node.right)
        elif node.right == self.NIL:
            x = node.left
            self.transplant(node, node.left)
        else:
            y = self.treeMinimum(node.right)
            yOriginalColor = y.color
            x = y.right
            if y.parent == node:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = node.right
                y.right.parent = y
            self.transplant(node, y)
            y.left = node.left
            y.left.parent = y
            y.color = node.color
            if yOriginalColor == "BLACK":
                self.fixDelete(x)
    def fixDelete(self,x):
        while x != self.root and x.color == "BLACK":
              if x == x.parent.left:
                  w = x.parent.right
                  if w.color == "RED":
                      w.color = "BLACK"
                      x.parent.color = "RED"
                      self.leftRotate(x.parent)
                      w = x.parent.right
                  else:
                      if w.left.color == "BLACK" and w.right.color == "BLACK":
                          w.color = "RED"
                          x = x.parent
                      else:
                          if w.right.color == "BLACK":
                              w.left.color = "BLACK"
                              w.color = "RED"
                              self.rightRotate(w)
                              
                              w = x.parent.right
                          w.color = x.parent.color
                          x.parent.color = "BLACK"
                          w.right.color = "BLACK"
                          self.leftRotate(x.parent)
                          x = self.root
              else:
                    w = x.parent.left
                    if w.color == "RED":
                        w.color = "BLACK"
                        x.parent.color = "RED"
                        self.rightRotate(x.parent)
                        w  = x.parent.left
                    else:
                        if  w.right.color == "BLACK" and w.left.color == "BLACK":
                            w.color = "RED"
                            x = x.parent
                            
                        else:
                            if w.left.color == "BLACK":   
                                w.right.color =  "BLACK"
                                w.color = "RED"
                                self.leftRotate(w)
                                w = x.parent.left
                            w.color = x.parent.color
                            x.parent.color = "BLACK"
                            w.left.color = "BLACK"
                            self.rightRotate(x.parent)
                            x = self.root
        x.color = "BLACK"

    def search(self,node,key):
        while  node!= self.NIL and  node.key != key:
            if key < node.key:
                node = node.left
            else:
                node = node.right
        return node        

    def inorder_traversal(self, node):
        if node != self.NIL:
            self.inorder_traversal(node.left)
            print(f"{node.key} ({node.color})", end=" ")
            self.inorder_traversal(node.right)
            
if __name__ == "__main__":
    rb_tree = RBTree()
    elements = [20, 15, 25, 10, 5, 30, 35]
    
    for element in elements:
        rb_tree.insert(element)

    print("In-order traversal after insertion:")
    rb_tree.inorder_traversal(rb_tree.root)
    i=10
    rb_tree.delete(i)
    print(f"\nDeleting {i} ...")
    rb_tree.inorder_traversal(rb_tree.root)             

