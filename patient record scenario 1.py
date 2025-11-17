total_patients = 0
def add_patient():
     global total_patients
     total_patients += 1
     name = input("Input your name: ") 
     age = int(input("Please input your age: "))
     DOB = input("Please input your Dob in 00/00/0000: ")
     weight = float(input("Please input your weight: "))
     height = float(input("Please enter patient height(m): "))
     print(f"name: {name}, age: {age}, height(cm): {height}, weight(kg): {weight}, DOB: {DOB}")
     
add_patient()
def BMI():
     weight = float(input("Please input your weight: "))
     height = float(input("Please input your height in Metres: "))
     Bmi = weight/(height*height)
     print(f"Your bmi is: {Bmi}")

def dosage():
    limit = 4000
    while limit > 0:
         print(f"Your max dose for today is: {limit}")
         dose = float(input("Please input your dosage that is going to be used: "))
         limit = limit - dose

         print(f"You have took : {dose} mg of paracetamol")
         print(f"Your remaining dosage left is:{limit}")
    if limit < 0:
        print("You have over dosed please seek medical help")
    elif limit == 0:
         print("Please refrain from taking anymore doses")

def billing():
     room_value = 40
     numofstays = int(input("Pleae input the days stayed: "))
     cost = int(input("Please input the cost of your treatments: "))
     total = cost + (room_value * numofstays)
     VAT = (total)/5
     tVAT= total + VAT
     print(f"Your total bill is £{tVAT}")
     print(f"Your included VAT is £{VAT}")

def view_total():
    print("Total patients:", total_patients)
view_total()

