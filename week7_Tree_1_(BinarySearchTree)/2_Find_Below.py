# ให้น้องรับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input ตัวแรกสุดจะเป็น Root เสมอ
# และหาค่าที่น้อยกว่าค่าที่รับเข้ามาของ Binary Search Tree

# ***** ห้ามใช้ Built-in Function เช่น min() , max() , sort() , sorted()

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = BST._insert(self.root,data)
        return self.root
        
    def _insert(root,data):
        if root == None:
            return Node(data)
        if data < root.data:
            root.left = BST._insert(root.left,data)
        else:
            root.right = BST._insert(root.right,data)
        return root
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    
    v = ''
    def less_than(self, node, n):
        
        if node == None:
            return 
        if node.left!=None:
            self.less_than(node.left, n)
        if int(node.data) < n:
            self.v+=str(node.data)+' '
          #print(str(node.data),end=' ')
        if node.right!=None:
            self.less_than(node.right, n)
        if self.v =='':
            return "Not have"
        else :
            return self.v

T = BST()
inp, k = input('Enter Input : ').split('|')
inp = [int(i) for i in inp.split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
print('--------------------------------------------------')
print("Below {0} : ".format(k),end='')
below = T.less_than(root, int(k))
print(below)