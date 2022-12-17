# เขียนโปรแกรมแก้ปัญหา หอคอยแห่งฮานอย โดยเราจะมีแทงไม้อยู่3แท่งคือ A B C และรับ input
# เป็นจำนวนแผ่นไม้ที่วางซ้อนกันให้แสดงลำดับการย้ายแผ่นไม้ทั้งหมดจากแท่ง A ไปยัง แท่งC
# โดยแผ่นไม้ที่มีขนาดเล็กกว่าจะอยู่ข้างบนแผ่นไม้ที่มีขนาดใหม่กว่าเสมอ(ห้ามวางแผ่นเล็กกว่าไว้ข้างล่าง)

# ****ห้ามใช้คำสั่ง for, while, do while*****

# หมายเหตุ ทุกฟังก์ชันต้องมี parameter มากที่สุดไม่เกิน 5 ตัว

# คำแนะนำ ให้สร้างฟังก์ชันสำหรับแสดงผล แยกต่างหาก และใช้ list ในการเก็บข้อมูลของแท่งไม้แต่ละแท่ง
# และให้ระวังเรื่องการสลับ list ให้ดีๆ

# หากมีข้อสงสัยเกี่ยวกับ หอคอยแห่งฮานอย สามารถสอบถาม TA เพิ่มเติม หรือ ลองเล่นได้ที่
# https://www.mathsisfun.com/games/towerofhanoi.html

# def move(n,A,B,C,maxn):
#     #code here
# n = int(input("Enter Input : "))

def display(i, a, b, c):
    if i == 0:
        return
    if i < len(a):
        print(a[i], end="  ")
    else:
        print("|", end="  ")
    if i < len(b):
        print(b[i], end="  ")
    else:
        print("|", end="  ")
    if i < len(c):
        print(c[i])
    else:
        print("|")
    i -= 1
    display(i, a, b, c)

def move(n, m, a, b, c):
    if n == 1:
        if a[0] == "A" and c[0] == "B":
            b.append(a.pop())
        elif a[0] == "B" and c[0] == "C":
            c.append(b.pop())
        elif a[0] == "A" and c[0] == "C":
            c.append(a.pop())
        elif a[0] == "C" and c[0] == "B":
            b.append(c.pop())
        elif a[0] == "B" and c[0] == "A":
            a.append(b.pop())
        elif a[0] == "C" and c[0] == "A":
            a.append(c.pop())
        print("move 1 from  %s to %s" % (a[0], c[0]))
        print("|  |  |")
        display(m, a, b, c)

        b[0], c[0] = c[0], b[0]
        return a, b, c
    else:
        bb, cc = b.copy(), c.copy()
        bb[0], cc[0] = c[0], b[0]
        a, b, c = move(n-1, m, a, bb, cc)

        if a[0] == "A" and c[0] == "B":
            b.append(a.pop())
        elif a[0] == "B" and c[0] == "C":
            c.append(b.pop())
        elif a[0] == "A" and c[0] == "C":
            c.append(a.pop())
        elif a[0] == "C" and c[0] == "B":
            b.append(c.pop())
        elif a[0] == "B" and c[0] == "A":
            a.append(b.pop())
        elif a[0] == "C" and c[0] == "A":
            a.append(c.pop())
        print("move %d from  %s to %s" % (n, a[0], c[0]))
        print("|  |  |")
        display(m, a, b, c)

        aa, bb = a.copy(), b.copy()
        aa[0], bb[0] = b[0], a[0]
        a, b, c = move(n-1, m, aa, bb, c)

        a[0], c[0] = c[0], a[0]
        return a, b, c

n = int(input("Enter Input : "))
a = ["A"]
b = ["B"]
c = ["C"]
a += list(range(n, 0, -1))

print("|  |  |")
display(n, a, b, c)

move(n, n, a, b, c)