name = input("Please enter patient name: ")
age = int(input("Please enter patient age: "))
bill = float(input("Please enter the bill amount: "))
tbill = bill*1.2
discount = False
if age < 18:   
    dicount = True
    print("Discount applied")
elif age > 18:
    print("Discount not applied")
print(f"Patient : {name}, age : {age}, outstanding bill: {tbill}")
if (tbill) > 1000:
    plans = input("Would you like to start a plan: ")
    if plans == "Yes":
        time = input("Weeks or Months: ")
        if time == "Months":
            much = float(input("How much would you like to pay a month: "))
            total = tbill / much
            print(f"It will take {round(total, 2)} months to pay")
        elif time == "Weeks":
            wmuch = float(input("How much would you like to pay a month: "))
            totalw = tbill / wmuch
            print(f"It will take {totalw} weeks to pay")
    else:
        print("Ok")