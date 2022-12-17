# Chapter : 9 - item : 1 - bubble sort [recursive]

# เขียน function bubble sort เพื่อเรียงข้อมูลใน list จากน้อยไปมาก โดยใช้ recursive

# ***ห้ามใช้ คำสั่งloopต่างๆ เช่น for ,while หรือ Built-in Function ที่เกี่ยวกับ Sort เช่น .sort***

# *** ยกเว้นให้ใช้  for ได้แค่ขั้นตอนรับ input เท่านั้น ***

def bubbleRecur(data, i, j):
    n = len(data) - 1
    
    # print(i, j)
    
    if data[j] > data[j+1]:
        data[j], data[j+1] = data[j+1], data[j]
    
    # 0 == 7 - 0 - 1
    # 1 == 7 - 0 - 1
    # 2 == 7 - 0 - 1
    # 3 == 7 - 0 - 1
    
    # 6 == 7 - 6 - 1
    # 0 == 0
    if j == n-i-1:
        i = i+1
        j = -1
        
    if i == n:
        return 
    
    bubbleRecur(data, i, j+1)
    

array = list(map(int, input("Enter Input : ").split(" ")))
bubbleRecur(array, 0, 0)
print(array)