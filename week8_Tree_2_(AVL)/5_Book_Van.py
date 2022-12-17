# บริษัทแห่งหนึ่งมีรถตู้ K คันที่ลูกค้าสามารถเช่าไปใช้งานได้ โดยรถตู้แต่ละคันมีรหัสประจำตัวรถเป็นหมายเลขจำนวนเต็มบวกตั้งแต่ 1 จนถึง K
# ข้อกำหนดในการเลือกรถตู้ให้ลูกค้ามีอยู่ว่า ลูกค้าจะต้องทำการจองรถตู้ก่อน โดยคำสั่งจองจะต้องระบุจำนวนวันที่จะใช้
# จากนั้นผู้จองจะได้รถตู้ที่ว่างให้ใช้เร็วที่สุดเท่าที่จะหาได้จากรถตู้ทั้งหมด

# ในกรณีที่มีรถตู้ว่างให้ใช้เร็วที่สุดมากกว่า 1 คัน คันที่มีรหัสประจำรถน้อยกว่าจะถูกเลือกก่อน เช่นถ้าหากมีรถตู้ที่ว่างให้ใช้เร็วที่สุด 3 คัน 
# ซึ่งมีรหัสประจำรถเป็น 5 , 7 และ 20 รถตู้ที่มีหมายเลข 5 จะถูกเลือกก่อน นอกจากนี้การจองจะให้ความสำคัญกับคำสั่งจองที่มาก่อนเสมอ
# สำหรับการจองแต่ละครั้ง ผู้จองจะได้รับคำตอบกลับมาว่าได้ใช้รถตู้หมายเลขใด  โดยในตอนแรกรถตู้ทุกคันจะว่างและพร้อมใช้งานทั้งหมด

# อธิบาย Input โดย Input จะแบ่งเป็น 2 ฝั่งด้วย /
# -  ฝั่งซ้ายเป็น K ซึ่งหมายถึงเลขประจำตัวรถ โดยเริ่มตั้งแต่ 1 ถึง K
# -  ฝั่งขวาเป็น List จำนวนวันที่จองรถตู้ของลูกค้าที่สั่งจองเข้ามา

# คำใบ้ :  Min Heap

def printTree(data, index, size, level):
    if  index < size:
        printTree(data, 2 * index + 2, size, level + 1)
        print('        ' * level, data[index])
        printTree(data, 2 * index + 1, size, level + 1)


inp = input('Enter Input : ').split('/')

data = []
van = {}

for name in range(int(inp[0])):
    van[name + 1] = van.get(name + 1, 0)
    data.append(int(name) + 1)

for cus, key in enumerate(inp[1].split()):
    print(f'Customer {cus + 1} Booking Van {data[0]} | {key} day(s)')
    temp = data.pop(0)
    van[temp] = van.get(temp, 0) + int(key)
    for index, key in enumerate(data):
        if  van[temp] < van[key] or (van[temp] == van[key] and temp < key):
            data.insert(index, temp)
            temp = None
            break
    if temp:
        data.append(temp)