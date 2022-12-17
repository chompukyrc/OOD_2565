# ****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )
# หา Factorial ของ input ที่รับมา โดยใช้ Recursive

def fac(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fac(n-1)
        

n=int(input("Enter Number : "))
print(str(n)+"! =",fac(n))