# รับ string มาเข้าคิวหา secret code โดยรับ input คือ
# code เป็น string ยาว
# hint คือตัวแรกของรหัสที่ถูกต้อง
# **คำใบ้**
# ascii ของ "f" มีค่า = 102
# ascii ของ "g" มีค่า = 103
# ascii ของ "h" มีค่า = 104
# ascii ของ "i" มีค่า = 105
# ascii ของ "j" มีค่า = 106

class Queue:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def front(self):
        return self.items[0] if self.size()>0 else -1
    
    def enqueue(self,tmp):
        self.items.append(tmp)
    
    def dequeue(self):
        return self.items.pop(0)
    
q=Queue()
w,h = input("Enter code,hint : ").split(",")
s=ord(h)-ord(w[0])
for i in w:
    q.enqueue(chr(ord(i)+s))
    print(q.items)