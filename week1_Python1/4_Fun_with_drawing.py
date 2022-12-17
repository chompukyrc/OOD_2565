# เขียนภาษา Python เพื่อวาดรูปหัวใจ ซึ่งจะรับ input เป็นขนาดของรูปหัวใจ โดย input จะมีค่าตั้งแต่ 2 ขึ้นไป

print("*** Fun with Drawing ***")
num = int(input("Enter input : "))
if num >= 2 :

    for i in range(num):
        s=""
        for j in range(num-i-1):
            s+="."
        s+="*"
        for j in range(2*i-1):
            s+="+"
        if i!= 0:
            s+="*"
        for j in range(2*(num-i)-3):
            s+="."
        if i!=num-1:
            s+="*"
        for j in range(2*i-1):
            s+="+"
        if i!=num and i!=0:
            s+="*"  
        for j in range(num-i-1):
            s+="." 
        print(s)

    for i in range(2*num-2):
        s=""
        for j in range(i+1):
            s+="."
        s+="*"
        for j in range(2*num-3-i):
            s+="+"
        for j in range(2*num-4-i):
            s+="+"
        if i!=2*num-3:
            s+="*"
        for j in range(i+1):
            s+="."
        print(s)