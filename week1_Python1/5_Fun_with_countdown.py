# อยากให้นักศึกษาช่วยหาลำดับการ Countdown จาก Input ที่รับเข้ามา
# โดยลำดับการ Countdown จะเป็นเลขเรียงลำดับ เช่น 2->1 , 3->2->1 โดยจะสิ้นสุดด้วย 1 เสมอ
# โดยผลลัพธ์ให้แสดง List ของ จำนวนลำดับที่เจอ และ แต่ละลำดับเป็นอย่างไร

print("*** Fun with countdown ***")
num = [int(x) for x in input("Enter List : ").split()]
mainList = []
num.append(0)
temList = []
count = 0
for i in range(len(num)):
    if i < len(num)-1:
        if (num[i]-num[i+1] == 1 or num[i] == 1):
            temList.append(num[i])
            if (num[i] == 1):
                mainList.append(temList)
                temList = []
                count += 1
print([count, mainList])