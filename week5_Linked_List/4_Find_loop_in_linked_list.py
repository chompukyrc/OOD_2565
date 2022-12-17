# ให้ตรวจสอบว่า linked list มีการวนซ้ำหรือไม่ และ แสดงผลลัพธ์ตามตัวอย่าง
# โดยมีการรับ input ดังนี้
# 1. append ->   A <int> คือ เพิ่มข้อมูลต่อท้าย linked list
# 2. set_next -> S <index1(int):index2(str)> คือการ set node.next ของ node index ที่1 ให้ชี้ไป node index ที่2
# ซึ่งหากไม่มี  node index ที่1 ใน linked list ให้แสดง error และหากไม่มี node index ที่2 ใน linked list ให้ทำการ append nodeใหม่เข้าไปใน linked list โดยมี value = index2

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.next = None
        self.tail = None


    def __str__(self) -> str:
        if self.head == None:
            return 'Empty'
        current = self.head.next
        out = str(self.head)
        while current is not None:
            out += '->' + (str(current))
            current = current.next
        return out

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node


    def index(self,i):

        cur = self.head
        for i in range(i):
            cur = cur.next
            if cur.next == None:
                break
        return cur

    def size(self):
        curr = self.head
        count = 0
        while curr != None:
            count += 1
            curr = curr.next
        return count

    def isEmpty(self):
        return self.head == None



l = SinglyLinkedList()
check = False
n = input('Enter input : ').split(',')

for i in n:
    i = i.split()

    if i[0] == 'A':
        l.append(int(i[1]))
        print(l)


    if i[0] == 'S':
        a = i[1].split(':')
        num0 = int(a[0])
        num1 = int(a[1])

        if l.isEmpty():
            print("Error! {list is empty}")

        elif num0 >= l.size() or num0 < 0:
            print("Error! {index not in length}:",num0)

        elif num1 >= l.size() or num1 < 0:
            print("index not in length, append :",num1)
            l.append(num1)
    
        else:
            b1 = l.index(num0)
            b2 = l.index(num1)
            b1.next = b2
            print(f"Set node.next complete!, index:value = {a[0]}:{b1.data} -> {a[1]}:{b2.data}")
            if num0 >= num1:
                check = True 
if check:
    print('Found Loop')

else:
    print("No Loop")
    print(l)