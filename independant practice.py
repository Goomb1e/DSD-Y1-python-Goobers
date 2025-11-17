def area():
    base = int(input("Please input the base of the rectangle: "))
    height = int(input("Please input the height of the rectangle: "))
    area = base*height
    print(f"You're area is: {area}")

def conversion():
    min = float(input("Please input the minutes: "))
    hours = min // 60
    mins = min % 60
    print(f"total of {min} minutes converts into {hours} hours and {mins} minutes")

def billing():
    bill = float(input("Please enter bill amount: "))
    VAT = 1.2
    print(f"Your total is {int(bill*VAT)} pounds")

