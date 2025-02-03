class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1 
class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if not root:
            return Node(key)

        if key < root.data:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        # LL
        if balance > 1 and key < root.left.data:
            return self.right_rotate(root)

        # RR
        if balance < -1 and key > root.right.data:
            return self.left_rotate(root)

        # LR
        if balance > 1 and key > root.left.data:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # RL
        if balance < -1 and key < root.right.data:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def search(self, root, key):
        if root is None or root.data == key:
            return root

        if key < root.data:
            return self.search(root.left, key)

        return self.search(root.right, key)

    def delete(self, root, key):
        
        if not root:
            return root
        
        
        if key < root.data:
            root.left = self.delete(root.left, key)
        elif key > root.data:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.get_min_value_node(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)

        if root is None:
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        # LL
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        # RR
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        # LR
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # RL
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def get_min_value_node(self, root):
        if root is None or root.left is None:
            return root
        return self.get_min_value_node(root.left)

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.data, end=" ")
            self.inorder_traversal(root.right)
            
if __name__ == "__main__":
    avl = AVLTree()

    root = None
    root = avl.insert(root, 20)
    root = avl.insert(root, 30)
    root = avl.insert(root, 10)
    root = avl.insert(root, 5)
    root = avl.insert(root, 15)
    
    print("Inorder traversal after insertion:")
    avl.inorder_traversal(root)
    print()

    key = 20
    found = avl.search(root, key)
    if found:
        print(f"Node with value {key} found in the tree.")
    else:
        print(f"Node with value {key} not found.")

    print("Deleting node with value 10:")
    root = avl.delete(root, 10)

    print("Inorder traversal after deletion:")
    avl.inorder_traversal(root)
    print()
