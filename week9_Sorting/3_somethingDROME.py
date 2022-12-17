# Chapter : 9 - item : 3 - somethingDROME

# รับจำนวนเต็มมา 1 จำนวนแล้วให้แสดงผลดังนี้

# - หาก input ที่รับมานั้นมีการเรียงลำดับจากน้อยไปมาก และไม่มีตัวซ้ำเลยให้แสดงผลว่า "Metadrome"

# - หาก input ที่รับมานั้นมีการเรียงลำดับจากน้อยไปมาก และมีตัวซ้ำให้แสดงผลว่า "Plaindrome"

# - หาก input ที่รับมานั้นมีการเรียงลำดับจากมากไปน้อย และไม่มีตัวซ้ำเลยให้แสดงผลว่า "Katadrome"

# - หาก input ที่รับมานั้นมีการเรียงลำดับจากมากไปน้อย และมีตัวซ้ำให้แสดงผลว่า "Nialpdrome"

# - หาก input ที่รับมานั้นทุกหลักเป็นเลขเดียวกันหมด ให้แสดงผลว่า "Repdrome"

# - หากไม่อยู่ในเงื่อนไขด้านบนเลย ให้แสดงผลว่า "Nondrome"

# ****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง

def bubbleRecurByMin(data, i, j):
    n = len(data) - 1

    if int(data[j]) > int( data[j+1]):
        data[j], data[j+1] = data[j+1], data[j]

    if j == n-i-1:
        i = i+1
        j = -1
        
    if i == n:
        return 
    
    bubbleRecurByMin(data, i, j+1)
    
def bubbleRecurByMax(data, i, j):
    n = len(data) - 1

    if int(data[j]) < int( data[j+1]):
        data[j], data[j+1] = data[j+1], data[j]

    if j == n-i-1:
        i = i+1
        j = -1
        
    if i == n:
        return 
    
    bubbleRecurByMax(data, i, j+1)
    

arr = input("Enter Input : ")
arr = [*arr]
        
counter = [0] * 10
isDuplicate = False
isOnlyOne = True
lastIndexOfDuplicate = -1
        
for i in range(len(arr)):
    counter[int(arr[i])] += 1
    if(counter[int(arr[i])] > 1):
        isDuplicate = True                
    if lastIndexOfDuplicate != -1 and lastIndexOfDuplicate != int(arr[i]):
        isOnlyOne = False

    lastIndexOfDuplicate = int(arr[i])
        
minToMax = arr.copy()
maxToMin = arr.copy()
bubbleRecurByMin(minToMax, 0, 0)
bubbleRecurByMax(maxToMin, 0, 0)
        
arr = "".join(arr)
minToMax = "".join(minToMax)
maxToMin = "".join(maxToMin)
        
if isOnlyOne == False and arr == minToMax:
    if not isDuplicate:
        print("Metadrome")
    else:
        print("Plaindrome")
elif isOnlyOne == False and arr == maxToMin:
    if not isDuplicate:
        print("Katadrome")
    else:
        print("Nialpdrome")
else:
    if isOnlyOne:
        print("Repdrome")
    else:
        print("Nondrome")