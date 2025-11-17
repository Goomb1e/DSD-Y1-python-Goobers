def safety():
    age = int(input("Please enter patient age: "))
    weight = float(input("Please input patient weight: "))
    if age > 12 and weight > 40:
        print("Safe to medicate")
    else:
        print("Unsafe to medicate")

def fitness():
    age = int(input("Please enter individuals age: "))
    clear = input("Do you have medical clearance? ")
    if age >= 18 and clear == "yes":
        print("You can access the intesive zone")
    else:
        print("You cannot access the intensive zone")

def sleep():
    asleep = input("Are you asleep? ")
    heart = float(input("What is your heart rate? "))
    if asleep == "no" and heart >= 100:
        print("Get to bed")
    else:
        print("Good ")

run = True

while run == True:
    start = input("\n Options: \n1. safety in medication \n2. Fitness tracker \n3. sleep tracker \n 4. Exit menu \n")
    if start == "1":
     safety()
    elif start == "2":
        fitness()
    elif start == "3":
        sleep()
    elif start == "4":
        run = False