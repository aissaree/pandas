def loop1():
    for a in range(11): # 0-10
        print(a)
#loop1()

def loop2():
    for i in range(1,11): # 1-10
        print(i)
#loop2()

def loop3():
    for i in range(1,11,2): # เริ่มตำแหน่งที่ 1 โดย บวกเพิ่มทีละ 2 จนถึงตำแหน่งที่ 10
        print(i)
        print("------------------")
    print('Bye')
loop3()

def loop_string():
    s = "over the rainbow"
    for i in s:
        print(i.upper())# ตัวพิมพ์ใหญ่ทั้งหมด
#loop_string()

def loop_tuple():
    flowers = ("lily","jasmine","rose","ivy")
    for f in flowers:
        print(f.capitalize())# ตัวพิมพ์ใหญ่เฉพาะตัวแรก
loop_tuple()
