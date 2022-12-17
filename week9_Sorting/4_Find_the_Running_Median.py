# Chapter : 9 - item : 4 - Find the Running Median

# เขียนโปรแกรมที่ทำการรับข้อมูลเป็น list เพื่อหาค่ามัธยฐานของข้อมูลใน list โดยจะเริ่มต้นจากข้อมูลใน list 
# เพียง 1 ตัวจากนั้นค่อยๆเพิ่มไปเรื่อยๆจนครบ โดยในการหาค่ามัธยฐานเราต้องจัดเรียงข้อมูลตามลำดับจากน้อยไปหามากเสียก่อน จากนั้นแสดงผลตามตัวอย่าง

# ***ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort เช่น sort, min, max,ฯลฯ***

# l = [e for e in input("Enter Input : ").split()]
# if l[0] == 'EX':
#     Ans = "xxx"
#     print("Extra Question : What is a suitable sort algorithm?")
#     print("   Your Answer : "+Ans)
# else:
#     l=list(map(int, l))
#     #code here

# ***test case พิเศษเพิ่มเติม ไม่คิดคะแนน และไม่มีผลต่อการผ่านโจทย์ข้อนี้หรือไม่***

# พี่มีคำถามมาถามน้องๆว่าในกรณีโจทย์แบบนี้ ถ้าหากจำนวน  input มีจำนวนมากกว่าหมื่นตัวขึ้นไป เราสามารถ sort algorithm 
# แบบใดมาประยุกต์ใช้จึงจะเหมาะสม และ ทำเวลาได้ดี

# - bubble sort

# - straight selection sort

# - insertion sort

# - shell sort

# - merge sort

# - quick sort

# - minHeap and maxHeap

# พิมพ์คำตอบลงในช่อง Ans = "xxx"

# ***ยกมือถามได้นะถ้าสงสัยว่าทำไมเป็นอันนี้***
    

def insertSort(l):
    for i in range(1, len(l)):
        key = l[i]
        j   = i - 1
        
        # print("key:", key, "j:", j)
        
        while j >= 0 and key < l[j]:
            # print("check key and l[j]", key, l[j])
            l[j+1] = l[j]
            # print("==>", l[j+1], l[j])
            j      = j - 1
            
        # print("======>", l[j+1], key)
        l[j+1] = key
        # print("after:", l)
        # print("====")
    
def calMedian(arr):
    if len(arr)%2 == 0:
        mid = int(len(arr)/2)
        med = (arr[mid]+arr[mid-1])/2
        print(" median =", med)
    else:
        mid = int(len(arr)/2)
        print(" median =", float(arr[mid]))
    

# l = [4, 3, 1, 5, 2, 7, 9, 8]
l = [e for e in input("Enter Input : ").split()]
# if l[0] == 'EX':
#     Ans = "merge sort"
#     print("Extra Question : What is a suitable sort algorithm?")
#     print("   Your Answer : "+Ans)
# else:
l=list(map(int, l))

# print("ori:", l)
temp =[]
for i in range(len(l)):
    # list = [4] : median = 4.0
    temp.append(l[i])
            
    print("list =", temp, ":", end="")
            
    temp2 = temp.copy()
    insertSort(temp2)
    calMedian(temp2)
    # print(temp)
            
# print(l)

