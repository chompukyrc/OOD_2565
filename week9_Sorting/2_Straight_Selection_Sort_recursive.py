# Chapter : 9 - item : 2 - Straight Selection Sort [recursive]

# เขียน function Straight Selection Sort เพื่อเรียงข้อมูลใน list จากน้อยไปมาก โดยใช้ recursive

# และแสดงขั้นตอนของ Straight Selection Sort ตามตัวอย่าง

# ***ห้ามใช้ คำสั่งloopต่างๆ เช่น for ,while หรือ Built-in Function ที่เกี่ยวกับ Sort เช่น .sort***

# *** ยกเว้นให้ใช้  for ได้แค่ขั้นตอนรับ input เท่านั้น ***


def selectSort(arr, i, j, max_index):
    
    if j == -1:
        # swap 1 <-> 2 : [1, 2, 3, 4, 5]
        # Swap
        if i != max_index:
            arr[i], arr[max_index] = arr[max_index], arr[i]
            print("swap", arr[max_index], "<->", arr[i], ":", arr)
        
        i = i-1
        j = i-1
        max_index = i
        
    if i==0:
        return
    
    if arr[j] > arr[max_index]:
        max_index = j
        
   
    selectSort(arr, i, j-1, max_index)


inp = list(map(int, input("Enter Input : ").split(" ")))
    
# arr = [40 20 30 10 50]
n = len(inp)
#                i   j  max_index
selectSort(inp, n-1, n-2, n-1)
print(inp)