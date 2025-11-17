def hospital():
    name = input("enter Patient Name: ")
    age = int(input("enter patient Age: "))
    height = float(input("enter patient height(m): "))
    weight= float(input("enter patient weight(kg): "))
    bmi= float(weight)/(float(height)*float(height))
    if bmi>30:
        print("you are obese")
    elif bmi > 25 and bmi < 29.9:
        print("You are overweight")
    elif bmi > 18.5 and bmi < 24.9:
        print("You are healthy weight")
    elif bmi < 18.5:
        print("You are underweight")          
    
    if age > 65:
        print("Old person discount applied")
    print(f"Patient:{name}, has bmi of{bmi}")
hospital()