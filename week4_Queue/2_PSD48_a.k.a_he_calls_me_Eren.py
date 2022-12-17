# PSD48 (P-Saderd 48 Group) เป็นวงไอดอลวงหนึ่งที่กระแสกำลังมาแรง ณ ตอนนี้โดยเพลงที่ได้รับความนิยมอย่างมากคือเพลงจี่หอย
# โดยวง PSD48 กำลังจะจัดงานจับมือขึ้น โดยมีกฎอยู่ว่าถ้าหากคนที่กำลังต่อแถวอยู่เป็นคนจาก กองกำลังสำรวจ จะได้สิทธิพิเศษในการแทรกแถวไปข้างหน้าสุดทันที
# (แต่ถ้าหากคนหน้าสุดก็เป็นคนของกองกำลังสำรวจก็ต้องต่อหลังเขาอยู่ดี)
# PSD48 อยากให้คุณช่วยเขียนโปรแกรมสำหรับหาว่าจะมีโอตะ id ใดบ้างที่ได้จับมือ
# เพลงประกอบ : https://youtu.be/Jd4Hd-HFgls
# Input :
# EN <value>  เป็นโอตะธรรมดา  id = value
# ES <value>  เป็นโอตะของกองกำลังสำรวจ  id = value
# D           เป็นคำสั่งแสดงผล value ของหัวแถว ถ้าหากในแถวไม่มีคนจะแสดงคำว่า Empty

class Queue:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def enQueue(self, value):
        self.items.append(value)

    def deQueue(self):
        if not self.isEmpty():
            return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

if __name__ == '__main__':
    qEN = Queue()
    qES = Queue() 
    value = input("Enter Input : ").split(",")
    for i in value:
        key = i.split(" ")
        if key[0] == 'EN':
            qEN.enQueue(key[1])
        elif key[0] == 'ES':
            qES.enQueue(key[1])
        elif key[0] == 'D':
            if qEN.isEmpty() and qES.isEmpty():
                print("Empty")
            elif not qES.isEmpty():
                key = qES.deQueue()
                print(str(key))
            else:
                key = qEN.deQueue() 
                print(str(key))