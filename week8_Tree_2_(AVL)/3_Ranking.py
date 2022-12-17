# จงเขียนฟังก์ชั่นในการหา Rank ของ input ที่รับเข้ามา โดย Rank คือการแบ่งเป็นชั้นๆตามข้อมูลของ BST โดยจะเริ่มจากค่าที่น้อยกว่าค่าใน BST
# ที่น้อยที่สุดจะมีค่า Rank = 0 และค่าที่อยู่ตั้งแต่ค่าที่น้อยที่สุดจนถึงตัวถัดไปจะมีค่า Rank +=1 ไปเรื่อยๆจนถึงชั้นของตัวสุดท้ายหรือตัวมากสุด เช่น

# จากรูป ค่าที่น้อยที่สุดคือ -2 ดังนั้น rank(-2) จะได้ 1 แต่ rank ของค่าที่น้อยกว่า -2 จะเท่ากับ 0

# และ rank(0) จะเท่ากับ 1 ส่วน rank(1) จะเท่ากับ 2 เป็นต้น

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def insert(root,data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = Node.insert(root.left, data)
        else:
            root.right = Node.insert(root.right, data)
        return root

    def printTree(node, level = 0):
        if node != None:
            Node.printTree(node.right, level + 1)
            print('     ' * level, node)
            Node.printTree(node.left, level + 1)

    def rank(root,data):
        if root is None:
            return 0
        if data < root.data:
            return Node.rank(root.left,data)
        else:
            return 1+ Node.rank(root.left,data) + Node.rank(root.right,data)

    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = Node.insert(self.root,data)
        return self.root


tree = BST()
data,a = input("Enter Input : ").split("/")
for i in data.split():
    tree.insert(int(i))
tree.root.printTree()
print("-"*50)
print(f"Rank of {a} : {tree.root.rank(int(a))}")