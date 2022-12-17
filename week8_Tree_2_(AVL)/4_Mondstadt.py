# Jean รักษาการผู้บัญชาการของกองอัศวิน Favonius แห่ง Mondstadt ต้องการทราบถึงขุมพลังของอัศวินในแต่ละกลุ่มภายในเมือง Mondstadt
# แห่งนี้จึงจะทดสอบความแข็งแกร่งของขุมกำลังที่มี โดยจะทำการจัดวางกำลังอัศวินภายในเมือง Mondstadt ดังตัวอย่างต่อไปนี้
#                 พลัง    :   5  4  4  3  2  2  2
#                 ลำดับ  :   0  1  2  3  4  5  6
# จากข้อมูลข้างต้นประกอบด้วยอัศวินทั้งหมด 7 คน เรียงตามลำดับตั้งแต่ลำดับที่ 0 ถึง 6 และพลังของอัศวินแต่ละคนมีข้อกำหนดดังนี้
#     -  อัศวินลำดับที่ n จะมีลูกน้องในสังกัดอยู่ลำดับที่ 2n+1 และ 2n+2 (ลูกน้องของลูกน้องของอัศวินลำดับที่ n ถือว่าเป็นลูกน้องของอัศวินลำดับที่ n ด้วย)
#     -  ค่าพลังของอัศวินมีค่าตั้งแต่ 0 - 5
#     -  กลุ่มของอัศวินกลุ่มที่ i จะมีสมาชิกคือ อัศวินลำดับที่ i และลูกน้องของอัศวินลำดับที่ i (รวมลูกน้องของลูกน้องของอัศวินด้วย)
#     -  พลังของกลุ่มอัศวินลำดับที่ i เป็นพลังรวมของสมาชิกของอัศวินทั้งหมดในกลุ่ม เช่น
#             -  อัศวินกลุ่มที่ 1 หมายถึง กลุ่มของอัศวินลำดับที่ 1 ซึ่งมีสมาชิกประกอบด้วย อัศวินลำดับที่ 1, 3 และ 4 และค่าพลังรวมของอัศวินกลุ่มที่ 1 เท่ากับ 4 + 3 + 2 = 9
#             -  อัศวินกลุ่มที่ 2 หมายถึง กลุ่มของอัศวินลำดับที่ 2 ซึ่งมีสมาชิกประกอบด้วย อัศวินลำดับที่ 2 , 5 และ 6 และค่าพลังรวมของอัศวินกลุ่มที่ 2 เท่ากับ 4 + 2 + 2 = 8

# ดังนั้นเมื่อนำพลังของอัศวินกลุ่มที่ 1 และ 2 มาเทียบกัน จะได้ว่าพลังรวมของอัศวินกลุ่มที่ 1 นั้นมากกว่าพลังรวมของอัศวินกลุ่มที่ 2
# Jean ต้องการทราบว่าค่าพลังรวมของอัศวินภายในเมือง Mondstadt เป็นเท่าใด และถ้าเปรียบเทียบระหว่างอัศวินแต่ละกลุ่มแล้วค่าของพลังรวมของอัศวินในกลุ่มใดมีค่ามากกว่ากัน

class TreeNode(object): 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None
        self.height = 0

    def __str__(self):
        return str(self.val)
  
class AVL_Tree(object): 
    def __init__(self):
        self.root = None
    
    def rr(self,px):
        py = px.right
        px.right = py.left
        py.left = px
        return py
    
    def ll(self,px):
        py = px.left
        px.left = py.right
        py.right = px
        return py
    
    def changeHeight(self,a):
        if a!=None:
            a.height = max(self.changeHeight(a.left),self.changeHeight(a.right))+1
            return a.height
        else:
            return -1
    
    def insert(self,node,data):
        if self.root is None:
            self.root = TreeNode(data)
            return self.root
        else:
            if node != None:
                if data <= node.val:
                    node.left = self.insert(node.left,data)
                else:
                    node.right = self.insert(node.right,data)
            else:
                return TreeNode(data)
            
            
            l = node.left.height if node.left is not None else -1
            r = node.right.height if node.right is not None else -1
            if abs(l-r)>1:
                a = self.root
                if l>r:
                    if data<=node.left.val:
                        a = self.ll(node)
                    else:
                        node.left = self.rr(node.left)
                        node = self.ll(node)
                        a = node
                else:
                    if data<=node.right.val:
                        node.right = self.ll(node.right)
                        node = self.rr(node)
                        a = node
                    else:
                        a = self.rr(node)
                self.changeHeight(a)
                return a
            else:
                node.height = max(l,r)+1
                return node

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

def fillData(node,data,q=[]):
    if node!=None:
        if node.left!=None:q.append(node.left)
        if node.right!=None:q.append(node.right)
        node.val = data.pop(0)
        if len(q)!=0:fillData(q.pop(0),data,q)

def getPower(node):
    if node!=None:return node.val+getPower(node.left)+getPower(node.right)
    return 0

def findNode(node,a,i=0,q=[]):
    if node!=None:
        if node.left!=None:q.append(node.left)
        if node.right!=None:q.append(node.right)
        if i==a:return node
        return findNode(q.pop(0),a,i+1,q)

def compare(root,i,j):
    pI = getPower(findNode(root,i,0,[]))
    pJ = getPower(findNode(root,j,0,[]))
    if pI<pJ:print(str(i)+"<"+str(j))
    elif pI>pJ:print(str(i)+">"+str(j))
    else:print(str(i)+"="+str(j))

tr = AVL_Tree()
root = None
inp,comp = input("Enter Input : ").split('/')
dat = [int(i) for i in inp.split()]
for i in dat:root = tr.insert(root,'x')
fillData(root,dat)
print(getPower(root))
#printTree90(root)
for i in comp.split(','):compare(root,int(i.split()[0]),int(i.split()[1]))