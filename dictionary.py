def demo(): # ฟังก์ชั่น
    d = {"hello":"สวัสดี","thank you": "ขอบคุณ","toilet":"ห้องน้ำ"}
    # dictionary ข้อมูลจะถูกเก็บเป็นคู่ๆ แบบ key : value
    d["one"] = "หนึ่ง" # เพิ่มข้อมูลในตัวแปร d โดย one คือ key หนึ่ง คือ value
    print(d) # print ออกมาข้อมูลจะไม่จัดตามลำดับ
    del d["toilet"] # ลบข้อมูลจากตัวแปร d ที่มี key คือ toilet
    print(d)

def demo2(): # ฟังก์ชั่น
    m = {"th":[5,3,7],"sg":[3,1,2]}
    print(m) # print ข้อมูลที่อยู่ในตัวแปร m ออกมา
    print(m["th"]) # print ข้อมูล จากตัวแปร m โดย print value จาก key th ออกมา
    print(m["th"][2]) # print ข้อมูล ในตัวแปร m โดย print value จาก key th ในตำแหน่งที่ 2
    print(m["th"][0]+(m["th"][1]) +(m["th"][2])) # นำ value ตำแหน่งที่ 0,1,2 จาก key th มาบวกกัน

demo2()