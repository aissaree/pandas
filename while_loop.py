"""
get = 0
answer = 5
while answer != get: # answer ไม่เท่ากับ get
    get = int(input("get number :")) # get number คือ ค่าที่ใส่เข้าไปในตัวแปร get
else: # ถ้า ค่า get เท่ากับ answer จะ print Done ออกมา
    print("Done")
"""
def demo():
    i = 11
    while i <= 10:
        print(i)
        i += 1 # i += 1 คือ i = i+1
    print("Bye")
#demo()

def sum_input_repeat_unit():
    total = 0
    while True: # ถ้าเป็นจริงทำการวน loop ซ้ำ
        n = int(input("enter number ")) # ค่าตัวแปร n ที่ key เข้าไป
        if n != 0: # ถ้า n = 0 จะทำการ break และแสดง total ออกมาเป็น 0 ถ้าเป็นค่าอื่นดูต่อ
            total += n # total = total+n เช่น 0+1=1 วน loop ซ้ำ เช่น total =1+2(n)=3 วนไปเรื่อยๆ ถ้าเจอ 0 จะทำการ break และแสดง total ออกมา
        else:
            break #
    print("total =",total)
sum_input_repeat_unit()







