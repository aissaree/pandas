"""
# Tuple
program = ("python","C#","JAVA","ASP.NET","Swift","Kotlin","javascript")
print(program[0]) # print ตัวแปรชื่อ program ตำแน่งที่ 0
print(program[0:6]) # print ตัวแปร program ตำแหน่งที่ 0-5
"""

# List
def demo_basic_operation():
    flowers =["calla","lily","jasmine"]
    print(flowers) # print ข้อมูล เรียงลำดับ
    flowers = flowers +["forget me not","ivy","gypso"] # วิธีเพิ่มข้อมูลเข้าไปใน list
    print(flowers)
    del flowers[1] # ลบข้อมูลในตัวแปร flowers ตำแหน่งที่ 1
    print(flowers)
    flowers.remove("forget me not") # ลบข้อมูลแบบระบุตัวที่ต้องการลบ
    print(flowers)
    sorted_flowers = sorted(flowers) # เรียงลำดับตามตัวอักษร A-Z
    print(sorted_flowers)
    flowers.append("carnation") # เพิ่มข้อมูลเข้าไปต่อท้าย
    print(flowers)

def demo():
    flowers = ['calla', 'lily', 'jasmine', 'forget me not', 'ivy', 'gypso']
    # แบบ slice 
    print(flowers[1:5]) # 1-4
    print(flowers[-1]) # -1 จะเริ่มไล่จากฝั่งขวามือ
    print(flowers[:3]) # 0-2
    print(flowers[1:]) # 1- สุดท้าย
demo()


