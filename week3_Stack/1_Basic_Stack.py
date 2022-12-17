# ให้น้องๆเขียนโปรแกรมโดยรับ input 2 แบบ โดยใช้ STACK ในการแก้ปัญหา
# A  <value>  ให้นำ value ไปใส่ใน STACK และทำการแสดงผล Size ปัจจุบันของ STACK
# P   ให้ทำการแสดงผลของvalueที่อยู่ท้ายสุดและindexของvalueนั้นจากนั้นทำการ Pop_Stack ถ้าหากไม่มี value อยู่ใน Stack ให้แสดงผลเป็น  -1
# *** ในตอนสุดท้ยถ้าหากใน Stack ยังมี Value อยู่ให้แสดงผลออกมา  ถ้าหากไม่มีแล้วให้แสดงคำว่า  Empty

class Stack :
    def __init__(self) :
        self.data = []
    def push(self,e):
        self.data.append(e)
    def is_Empty(self):
        return self.data == []
    def pop(self):
        return self.data.pop()
    def top(self) :
        return self.data[-1]
    def size(self):
        return len(self.data)
    def st(self,i):
        return self.data[i]
s=Stack()
x = input("Enter Input : ").split(",")
for i in x :
    inp=i.split()
    if inp[0]=="A" :
        s.push(inp[1])
        temp = inp[1]
        temp1 = s.size()
        print(f"Add = {temp} and Size = {temp1}")
    elif inp[0]=="P" :
        if s.size()>0:
            temp2 = s.top()
            s.pop()
            temp3 = s.size()
            print(f"Pop = {temp2} and Index = {temp3}" )
        else:
            print("-1")
print('Value in Stack = ',end='')
if s.size()>0:
    for i in range(s.size()):
        print(int(s.st(i)),end=' ')
else :
    print("Empty")