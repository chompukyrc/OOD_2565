# เขียนโปรแกรมคลุกคำ (scramble) สร้าง singly linked list ของคำในจดหมาย scramble จดหมายโดยทำคล้ายตัด ไพ่และกรีดไพ่
# ผู้รับจดหมาย descramble กรีดกลับและตัดกลับจนได้จดหมายฉบับเดิมที่อ่านได้(หากออกแบบดีๆ สามารถ scramble กี่ครั้งก็ได้ ขึ้นแรกให้ทำ ครั้งเดียวก่อน)  

# ***** รูปแบบ input *****

# แบ่งเป็น 2 ฝั่ง ได้แก่ ฝั่งซ้าย (Linked List เริ่มต้น  ความยาวขั้นต่ำของ Linked List รับประกันว่าขั้นต่ำคือ 10)  |  ฝั่งขวา BottomUp กับ Riffle โดยการแทนด้วย B กับ R
# ซึ่งการรับ R กับ B สามารถสลับที่กันได้ เช่น   R 40,B 60  <->  B 60,R 40

# 1.  B   < percentage >  :  bottomUp ตัด ยกส่วนบน (lift) ออกตาม % input ที่รับเข้ามา นำส่วนล่างมาซ้อนทับส่วนบน

# 2.  R   < percentage >  :  riffleShuffle กรีด (จากด้านบน) lift ตาม % นำ node ของแต่ละลิสต์มาสลับกันทีละ node จากต้นลิสต์ ส่วนเกินนำมาต่อท้าย

# ***** ถ้าหากคิดเปอร์เซ็นของความยาว Linked List แล้วได้ทศนิยม ให้ปัดลงทั้งหมด *****

# ***** การแสดงผลมี Pattern เป็น   Bottomup  ->  Riffle  ->  Deriffle  -> Debottomup นะครับ



# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

#     def __str__(self):
#         return str(self.value)

# def createLL(LL):
#     # Code Here

# def printLL(head):
#     # Code Here

# def SIZE(head):
#     # Code Here

# def scarmble(head, b, r, size):
#     # Code Here

# inp1, inp2 = input('Enter Input : ').split('/')
# print('-' * 50)
# h = createLL(inp1.split())
# for i in inp2.split('|'):
#     print("Start : {0}".format(printLL(h)))
#     k = i.split(',')
#     if k[0][0] == "B" and k[1][0] == "R":
#         scarmble(h, float(k[0][2:]), float(k[1][2:]), SIZE(h))
#     elif k[0][0] == "R" and k[1][0] == "B":
#         scarmble(h, float(k[1][2:]), float(k[0][2:]), SIZE(h))
#     print('-' * 50)

class ListNode:
    def __init__(self, value=None):
        self.value = value
        self.next = None

def createLinkedList(raw_list):
    head = ListNode()
    node = head
    while True:
        node.value = raw_list.pop(0)
        if len(raw_list) == 0:
            break
        node.next = ListNode()
        node = node.next
    return head

def printLinkedList(head):
    ret = []
    tail = head
    while tail != None:
        ret.append(str(tail.value))
        tail = tail.next
    return " ".join(ret)

def size(head):
    size = 0
    node = head
    while node != None:
        node = node.next
        size += 1
    return size

def bottomup(head, b, size):
    cut_index = int(size * (b/100))
    first = head
    node = head
    if cut_index > 1:
        while True:
            node = node.next
            cut_index -= 1
            if cut_index == 1:
                head = node.next
                node.next = None
                break
    else:
        head = node.next
        node.next = None

    node = head
    if node.next != None:
        while True:
            node = node.next
            if node.next == None:
                break
    node.next = first

    return head

def riffle(head, r, size):
    if int(r/10) == 0 or int(r/10) == 10:
        return head

    cut_index = int(size * (r/100))

    first_head = head
    second_head = None

    node = head
    if cut_index > 0:
        while True:
            cut_index -= 1
            if cut_index == 0:
                second_head = node.next
                node.next = None
                break
            node = node.next
    else:
        second_head = node.next
        node.next = None

    first_node = first_head
    second_node = second_head

    head = ListNode()
    result = head
    while True:
        result.value = first_node.value
        if first_node.next != None:
            result.next = ListNode()
        else:
            result.next = second_node
            break

        if first_node.next != None:
            first_node = first_node.next
        result = result.next

        result.value = second_node.value
        if second_node.next != None:
            result.next = ListNode()
        else:
            result.next = first_node
            break

        if second_node.next != None:
            second_node = second_node.next
        result = result.next

    return head

def deriffle(head, r, size):
    cut_index = min(size - int(size * (r/100)), int(size * r/100))
    if cut_index == 0:
        return head

    first_head = ListNode()
    second_head = ListNode()
    first_node = first_head
    second_node = second_head

    node = head
    while True:
        first_node.value = node.value
        if cut_index > 1:
            first_node.next = ListNode()
            first_node = first_node.next
        node = node.next

        second_node.value = node.value
        if cut_index > 1:
            second_node.next = ListNode()
            second_node = second_node.next
        node = node.next

        cut_index -= 1
        if node == None:
            break
        elif cut_index == 0:
            if r >= 50:
                first_node.next = node
            else:
                second_node.next = node
            break

    tail = first_head
    while True:
        if tail.next == None:
            break
        tail = tail.next
    tail.next = second_head

    return first_head

def debottomup(head, b, size):
    cut_index = size - int(size * (b/100))
    first = head
    node = head

    if cut_index > 1:
        while True:
            node = node.next
            cut_index -= 1
            if cut_index == 1:
                head = node.next
                node.next = None
                break
    else:
        head = node.next
        node.next = None

    node = head
    if node.next != None:
        while True:
            node = node.next
            if node.next == None:
                break
    node.next = first

    return head

def scramble(head, b, r, size):
    print("Start :", printLinkedList(head))
    head = bottomup(head, b, size)
    print("BottomUp %.3f %% :" % (b), printLinkedList(head))
    head = riffle(head, r, size)
    print("Riffle %.3f %% :" % (r), printLinkedList(head))
    head = deriffle(head, r, size)
    print("Deriffle %.3f %% :" % (r), printLinkedList(head))
    head = debottomup(head, b, size)
    print("Debottomup %.3f %% :" % (b), printLinkedList(head))
    return head

raw_list, commands = tuple(input("Enter Input : ").split("/"))

head = createLinkedList(raw_list.split())
print("--------------------------------------------------")
for e in commands.split("|"):
    x, y = tuple(e.split(","))
    if x[0] == "B":
        b, r = float(x.split()[1]), float(y.split()[1])
    else:
        r, b = float(x.split()[1]), float(y.split()[1])
    head = scramble(head, b, r, size(head))
    print("--------------------------------------------------")