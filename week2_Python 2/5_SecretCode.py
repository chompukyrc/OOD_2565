# ตึกลึกลับแห่งหนึ่งเมื่อเดินไปข้างหลังจะมีคนบอกรหัสลับมาจงสร้างฟังชั่นคำนวณรหัส
# โดยรหัสจะประกอบไปด้วย english word that have repeat character
# เช่น bon("ball") = 48 หรือ bon("aah") = 4
# def bon(w):
# 	### Enter Your Code Here ###
# secretCode = input("Enter secret code : ")
# print(bon(secretCode))

def bon(w):
    x = " "
    for i in range(len(w)):
        if (w[i] == w[i+1]):
            x = (ord(w[i])-96)*4
            return x

secretCode = input("Enter secret code : ")
print(bon(secretCode))