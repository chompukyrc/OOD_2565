# จงสร้างฟังก์ชัน ManageStack() ในการจัดการตัวเลขที่อยู่ใน Stack โดยที่จะมีคำสั่งดังนี้
# A (add) : ทำการเพิ่มตัวเลขเข้าไปใน Stack
# P (pop) : ทำการนำเลขสุดท้ายใน Stack ออก ( ถ้า Stack ว่างให้แสดงผล -1 )
# D (delete) : ทำการลบตัวเลขที่ต้องการใน Stack ( ถ้า Stack ว่างให้แสดงผล -1 )  
# LD (lessthan delete) : ทำการลบตัวเลขที่น้อยกว่าตัวเลขที่กำหนดทั้งหมดออกจาก Stack และแสดงผลตัวเลขที่ถูกลบไป ( ถ้า Stack ว่างให้แสดงผล -1 )
# MD (Morethan delete) : ทำการลบตัวเลขที่มากกว่าตัวเลขที่ต้องการทั้งหมดออกจาก Stack และแสดงผลตัวเลขที่ถูกลบไป ( ถ้า Stack ว่างให้แสดงผล -1 )
# การ Delete ทุกแบบ ถ้าหากไม่มีเลขที่ถูกลบเลย ไม่ต้องแสดงผลอะไรและให้ทำการแสดงผลค่าที่อยู่ใน Stack เมื่อจบโปรแกรม
# *** Hint ***
# ฟังก์ชัน Delete ต่างๆให้สร้าง Stack ขึ้นมาอีก 1 อันเพื่อใช้เป็น Temp ในการเก็บค่าตัวเลขต่างๆ

class Stack:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop() 
    def size(self):
        return len(self.items)
    def peek(self):
        return self.items
def manageStack(list):
    stack = Stack()
    stack_temp = Stack()
    list = list.split(",")
    for items in list:
        item = items.split()
        keyword = item[0]

        if keyword == 'A':
            number_list = item[1]
            number_list = int(number_list)
            stack.push(number_list)
            print('Add = ' + str(number_list))
        elif keyword == 'P':
            if stack.size() > 0:
                s = str(stack.pop())
                print('Pop = '+s)
            else:
                print('-1')
        elif keyword == 'D':
            number_eraser = item[1]
            number_eraser = int(number_eraser)
            if stack.size() > 0:
                for i in range(0,stack.size()):
                    s = stack.pop()
                    if s == number_eraser:
                        print('Delete = '+ str(s))
                        
                    else:
                        stack_temp.push(s)
                for i in range(0,stack_temp.size()):
                    stack.push(stack_temp.pop()) 
            else:
                print('-1')               
        elif keyword == 'LD':
            number_eraser = item[1]
            number_eraser = int(number_eraser)
            if stack.size() > 0:
                for i in range(0,stack.size()):
                    s = stack.pop()
                    if s < number_eraser:
                        print('Delete = '+ str(s)+' Because '+ str(s) +' is less than ' + str(number_eraser))
                    else:
                        stack_temp.push(s)
                for i in range(0,stack_temp.size()):
                    stack.push(stack_temp.pop())  
            else:
                print('-1')
        elif keyword == 'MD':
            number_eraser = item[1]
            number_eraser = int(number_eraser)
            if stack.size() > 0:
                for i in range(0,stack.size()):
                    s = stack.pop()
                    
                    if s > number_eraser:
                        print('Delete = '+ str(s)+' Because '+ str(s) +' is more than ' + str(number_eraser))
                    else:
                        stack_temp.push(s)
                for i in range(0,stack_temp.size()):
                    stack.push(stack_temp.pop())  
            else:
                print('-1')
    print('Value in Stack = ', end="")
    final_list = [int(x) for x in stack.peek()]
    print(final_list)
x = input('Enter Input : ')
manageStack(x)