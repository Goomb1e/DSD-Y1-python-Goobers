def Burn():
    perminute = int(input("Please input your calories burnt per minute: "))
    workout = int(input("How long have you worked out for? "))
    burnt = perminute * workout
    print(f"Your total calories burnt is {burnt}")

def step_conversion():
    steps = int(input("Please input the number of steps taken: "))
    DIST = 1300
    km = steps / DIST
    print(f"Your total distance in km is: {km}")

def medication_timing():
    minutes = int(input("Please input your total minutes left until next medication: "))
    hours = minutes // 60
    minute = minutes % 60
    print(f"Your time is: {hours} hours and {minute} minutes")

def medicine_pack_usage():
    packet = 10
    start = int(input("Please input how many tablets you have taken: "))
    remain = round(10-start)
    print(f"You have {remain} tablets left")






calculation = int(input("Which operation would you like : 1.Calorie burn 2.Step conversion 3.Medication timing 4.Medicine pack usage, Please input the number: "))
if calculation == 1:
    Burn()
if calculation == 2:
    step_conversion()
if calculation == 3:
    medication_timing()
if calculation == 4:
    medicine_pack_usage()

















