# รับจำนวนเต็ม 3 จำนวนจากแป้นพิมพ์
# เก็บในตัวแปร h, m และ s ซึ่งแทนจำนวน ชั่วโมง นาที และ วินาที
# แล้วแสดงผลเป็น วินาที
# แสดงผลตามตัวอย่าง

print("*** Converting hh.mm.ss to seconds ***")
hh, mm, ss = input("Enter hh mm ss : ").split()
hh = int(hh)
mm = int(mm)
ss = int(ss)

if hh < 0 :
    print("hh("+str(hh)+") is invalid!")
elif mm < 0 or mm > 59:
    print("mm("+str(mm)+") is invalid!")
elif ss < 0 or ss > 59:
    print("ss("+str(ss)+") is invalid!")
else :
    sec = hh*3600 + mm*60 + ss
    sec = "{:,}".format(sec)

    if hh < 10 and mm < 10 and ss < 10 :
        print("0"+str(hh)+":0"+str(mm)+":0"+str(ss),"= " +str(sec), "seconds")
    elif hh < 10 and mm < 10 :
        print("0"+str(hh)+":0"+str(mm)+":"+str  (ss),"= " +str(sec), "seconds")
    elif mm < 10 and ss < 10 :
        print(""+str(hh)+":0"+str(mm)+":0"+str(ss),"= " +str(sec), "seconds")
    elif hh < 10 and ss < 10 :
        print("0"+str(hh)+":"+str(mm)+":0"+str(ss),"= " +str(sec), "seconds")
    elif hh < 10 :
        print("0"+str(hh)+":"+str(mm)+":"+str(ss),"= " +str(sec), "seconds")
    elif mm < 10:
        print(str(hh)+":0"+str(mm)+":"+str(ss),"= " +str(sec), "seconds")
    elif ss < 10:
        print(str(hh)+":"+str(mm)+":0"+str(ss),"= " +str(sec), "seconds")
    else :
        print(str(hh)+":"+str(mm)+":"+str(ss),"= " +str(sec), "seconds")