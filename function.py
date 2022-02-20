def celsius_to_fah(celsius):
    return(celsius * 9/5)+32
def temperature_table():
    for c in range(0,50,5):
        f = celsius_to_fah(c)
        print("{}C = {}F".format(c,f))

def menu():
    print("1.convert Celsius to Fahrenheit")
    print("2.display temperature table")
    n = input("enter choice :")
    if n == "1":
        celsius = float(input("1enter degree in celsius :"))
        print("{}C = {}F".format(celsius,celsius_to_fah(celsius)))
    elif n == "2":
        temperature_table()
#f = celsius_to_fah(1000)
#print(f)

temperature_table()
menu()