class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
    def add_child(self,child):
        child.parent = self
        self.children.append(child)
    def get_level(self):
        level = 0
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level
    def print_tree(self):
        spaces=' '*self.get_level()*3
        print(spaces+self.data)
        if self.children:
            for child in self.children:
                child.print_tree()
def build_tree():
    root=TreeNode("Root")
    
    laptop = TreeNode("Laptop")
    dell=TreeNode('del')
    laptop.add_child(dell)
    laptop.add_child(TreeNode('hp'))
    
    tv=TreeNode('TV')
    samsung=TreeNode("samsung")
    tv.add_child(samsung)
    tv.add_child(TreeNode('sony'))
    
    root.add_child(tv)
    root.add_child(laptop)
    
    
    #print(samsung.get_level())
    return root

    
if __name__=="__main__":
    root=build_tree()
    root.print_tree()
    pass