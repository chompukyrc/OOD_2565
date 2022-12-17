# Chapter : 9 - item : 5 - Sort Subset

# ให้น้องรับ input มา 2 อย่างโดยคั่นด้วย /

# 1. ด้านซ้าย เป็นผลลัพธ์
# 2. ด้านขวา เป็น list ของจำนวนเต็ม

# โดยผลลัพธ์ให้แสดงเป็น subset ของ input ด้านขวาที่มีผลรวมได้เท่ากับ input ด้านซ้าย และมี Pattern การแสดงผลลัพธ์ดังนี้

# 1. ให้เรียงลำดับจากขนาดของ subset จากน้อยไปมาก
# 2. ถ้าหาก subset มีขนาดเท่ากันให้เรียงลำดับจำนวนเต็มใน subset จากน้อยไปมาก

# ถ้าหากไม่มี subset ไหนที่ผลรวมเท่ากับ input ด้านซ้าย ให้แสดงว่า No Subset



# ****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง และห้าม Import

# อธิบาย Test Case 1:

# [2]
# [-1, 3]
# [0, 2]  # [-1, 3] กับ [0, 2] มีขนาดเท่ากัน แต่ -1 < 0 ดังนั้น [-1, 3] จึงแสดงผลก่อน [0, 2]
# [-3, 2, 3]
# [-2, 1, 3]
# [-1, 0, 3]
# [-1, 1, 2]
# [-3, 0, 2, 3]
# [-2, -1, 2, 3]
# [-2, 0, 1, 3]   # [-2, -1, 2, 3] กับ [-2, 0, 1, 3] มีขนาดและตัวแรกสุดเท่ากัน แต่ตัวที่สอง -1 < 0 
                    # ดังนั้น [-2, -1, 2, 3] จึงแสดงผลก่อน [-2, 0, 1, 3]
# [-1, 0, 1, 2]
# [-3, -1, 1, 2, 3]
# [-2, -1, 0, 2, 3]
# [-3, -1, 0, 1, 2, 3]

def bubbleSort(data):
    for i in range(len(data)):
        for j in range(len(data)-i-1):
            # print(array[j], array[j+1])
            if len(data[j]) > len(data[j+1]):
                # print("swap", array[i], array[j])
                data[j], data[j+1] = data[j+1], data[j]
        # print("========================================")
        # print(array[len(array)-i-1])
        
# def bubbleSort2(data):
#     for i in range(len(data)):
#         for j in range(len(data)-i-1):
#             # print(array[j], array[j+1])
#             if data[j][0] > data[j+1][0]:
#                 # print("swap", array[i], array[j])
#                 data[j], data[j+1] = data[j+1], data[j]
        # print("========================================")
        # print(array[len(array)-i-1])
    
    
def bubbleRecur2(data, i, j):
    if(len(data) == 1):
        return
    
    n = len(data) - 1
    
    if data[j] > data[j+1]:
        data[j], data[j+1] = data[j+1], data[j]
    
    if j == n-i-1:
        i = i+1
        j = -1
        
    if i == n:
        return 
    
    bubbleRecur2(data, i, j+1)
    
# needed = 2
# arr = [-2,3,1,-1,0,-3,2]
# permuted =[]

# n = len(arr)

# for i in range(1, 2**n):

#     binary = bin(i)[2:].zfill(n) # 0b100 => 100
#     # print(bin(i)[2:])
    
#     temp = []
    
#     for j in range(len(binary)):
#         # print(binary[j], end="")
#         if(binary[j] == '1'):
#             print(arr[j], end="")
#             temp.append(arr[j])
    
#     permuted.append(temp)
        
#     print("\n====")
    
#     # print(permuted)
    

def sortSubset(needed, arr):
    permuted =[]

    n = len(arr)

    # for i in range(1, 2**n):
    for i in range(2**n-1, 0, -1):

        binary = bin(i)[2:].zfill(n) # 0b100 =>
        # print(bin(i)[2:])
        
        temp = []
        sum = 0
        
        for j in range(len(binary)):
            # print(binary[j], end="")
            if(binary[j] == '1'):
                # print(arr[j], end=" + ")
                sum += int(arr[j])
                temp.append(arr[j])
        
        # print(" = ",sum)
        if(sum == needed):
            # bubbleRecur2(temp, 0, 0)
            permuted.append(temp)
            
        # print("\n====")
    
    # print("===>", permuted, " -- ",  len(permuted))
        
    if len(permuted) == 0:
        print("No Subset")
    else:
        # bubbleSort2(permuted)
        # print("=============")
        bubbleSort(permuted)
        for k in permuted:
            print(k)
    

# needed = 2
# arr = [-2,3,1,-1,0,-3,2]
needed, arr = input("Enter Input : ").split("/")
needed = int(needed)
arr = list(map(int, arr.split(" ")))
bubbleRecur2(arr, 0, 0)
# print(arr)
# print(needed, arr)
sortSubset(needed, arr)