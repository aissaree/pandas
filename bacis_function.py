def rectangle(w,h):  # def คือ function rectangle คือ ชื่อ function ใน () คือ arguments
    return w*h       # return ค่า w*h ไปที่ rectangle

def triangle(w,h):
    return .10*w*h

w = int(input("width= "))
h = int(input("height="))

print(rectangle(w,h))
print(triangle(w,h))