# รับ input 2 จำนวนโดยที่ input ที่ 1 คือ h เป็นค่าความสูง(เมตร) และ Input ที่ 2 คือ w เป็นค่าน้ำหนัก(กิโลกรัม)
# โดยให้คำนวณหาค่า BMI ที่คำนวณจากสูตร BMI = w / (h^2) โดยให้แสดงผลตามข้อความข้างล่าง
# BMI < 18.50 แสดงผล Less Weight
# 18.50 <= BMI  < 23 แสดงผล Normal Weight
# 23 <= BMI  < 25 แสดงผล Morethan Normal Weight
# 25 <= BMI  < 30 แสดงผล Getting Fat
# BMI  >= 30 แสดงผล Fat

high, weight = input("Enter your High and Weight : ").split()
high = float(high)
weight = float(weight)
BMI = weight / (high**2)

if BMI < 18.50 :
    print("Less Weight")
elif BMI >= 18.50 and BMI < 23 :
    print("Normal Weight")
elif BMI >= 23 and BMI < 25 :
    print("More than Normal Weight")
elif BMI >= 25 and BMI < 30 :
    print("Getting Fat")
elif BMI > 30 :
    print("Fat")