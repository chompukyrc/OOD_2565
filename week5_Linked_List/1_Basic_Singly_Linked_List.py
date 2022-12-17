# ให้เขียนคลาสของ Singly Linked List ซึ่งมีเมท็อดดังนี้
# 1. __init__     สร้าง Head ขึ้นมาเพื่อบอกว่าจุดเริ่มต้นของ Linked List คือตรงไหน
# 2. __str__     คืนค่าเป็นสตริงซึ่งบอกว่า Linked List เราตั้งแต่หัวไปจนท้ายมีตัวอะไรบ้าง
# 3. isEmpty    เช็คว่า Linked List ของเราว่างหรือป่าว คืนค่าเป็น True / False
# 4. append     add Item เข้า Linked List จากด้านหลัง ไม่คืนค่า
# 5. addHead  add Item เข้า Linked List จากด้านหน้า ไม่คืนค่า
# 6. search      ค้นหา Item ที่ต้องการใน Linked List คืนค่าเป็น Found / Not Found
# 7. index        ค้นหา Item ที่ต้องการใน Linked List ว่าอยู่ที่ Index ไหน คืนค่าเป็น Index (0,1,2,3,4,.....) ถ้าหากไม่มีคืนค่าเป็น -1
# 8. size           คืนค่าเป็นขนาดของ Linked List
# 9. pop            นำ Item Index ที่ pos ออกจาก Linked List คืนค่าเป็น Success / Out of Range

# โดยรูปแบบ Input มีดังนี้
# 1. append    ->  AP
# 2. addHead  ->  AH
# 3. search      ->  SE
# 4. index        ->   ID
# 5. size          ->   SI
# 6. pop          ->   PO

# โดยให้เพิ่มเติมจากส่วน #Code Here ของโปรแกรมต่อไปนี้ เพื่อให้สามารถแสดงผลได้ตามที่โจทย์กำหนด
# ********  ห้ามใช้ List ในการทำ Linked List เด็ดขาดถ้าหากพบจะถูกลดเป็น 0 คะแนน ********

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def __str__(self):
#         if self.isEmpty():
#             return "Empty"
#         cur, s = self.head, str(self.head.value) + " "
#         while cur.next != None:
#             s += str(cur.next.value) + " "
#             cur = cur.next
#         return s

#     def isEmpty(self):
#         return self.head == None

#     def append(self, item):
#         # Code Here

#     def addHead(self, item):
#         # Code Here

#     def search(self, item):
#         # Code Here

#     def index(self, item):
#         # Code Here

#     def size(self):
#         # Code Here

#     def pop(self, pos):
#         # Code Here

# L = LinkedList()
# inp = input('Enter Input : ').split(',')
# for i in inp:
#     if i[:2] == "AP":
#         L.append(i[3:])
#     elif i[:2] == "AH":
#         L.addHead(i[3:])
#     elif i[:2] == "SE":
#         print("{0} {1}".format(L.search(i[3:]), i[3:]))
#     elif i[:2] == "SI":
#         print("Linked List size = {0} : {1}".format(L.size(), L))
#     elif i[:2] == "ID":
#         print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
#     elif i[:2] == "PO":
#         before = "{}".format(L)
#         k = L.pop(int(i[3:]))
#         print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
# print("Linked List :", L)

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.data) + " "
        while cur.next != None:
            s += str(cur.next.data) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, data):
        newNode = Node(data)
        if self.isEmpty():
            self.head = newNode
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = newNode


    def addHead(self, data):
        newNode = Node(data)
        cur = self.head
        if self.isEmpty():
            self.append(data)
            return
        else:
            newNode.next = cur
            self.head = newNode


    def search(self, data):
        cur = self.head
        while cur != None:
            if cur.data == data:
                return "Found"
            cur = cur.next
        return "Not Found"
        

    def index(self, data):
        cur = self.head
        id = 0
        while cur != None:
            if cur.data == data:
                return id
            id += 1
            cur = cur.next
        return -1


    def size(self):
        cur = self.head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def pop(self, pos):
        if not (-(self.size()) <= pos < self.size()):
            return "Out of Range"

        if(pos<0):
            pos += self.size()

        if pos == 0:
            cur = self.head
            if cur.next != None:
                self.head = cur.next
            else:
                self.head = None
        elif pos == self.size()-1:
            cur = self.head
            i = 0
            while pos - 1 > i :
                i += 1
                cur = cur.next
            cur.next = None
        else:
            cur = self.head
            i = 0
            while pos - 1 > i :
                i += 1
                cur = cur.next
            cur.next = cur.next.next
        return "Success"

L = LinkedList()
inp = input('Enter Input : ').split(',')           # AP I,AP Love,AP KMITL,AP 2020
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2} ".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
print("Linked List :", L)