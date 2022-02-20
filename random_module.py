import random # import module random
print(random.random()) # random หรือ สุ่ม ข้อมูล 0-1
[print(random.randint(1,6)) for i in range(10)] # สุ่มเลข 1-6 ออกมา 10 ครั้ง
[print(random.choice(["rock","paper","scissors"])) for i in range(5)] # สุ่มข้อมูลใน list ออกมา 5 คร้ง
[print(random.choice("HT")) for i in range(5)] # สุ่มข้อมูล T กับ H ออกมา 5 ครั้ง

flowers =["lily","rose","tulip","jasmine"]
a = random.sample(flowers,2) # สุ่มข้อมูลจาก ตัวแปร flowers ออกมา 2 ตัว
print(a)

