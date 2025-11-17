
def Conversion():
    NUM1 = 0.0555
    NUM2 = 18.018
    NUM3 = 0.0259
    NUM4 = 38.6
    type = input("What test would you like glucose or cholesterol? ")
    if type == "glucose":  
     value = float(input("What is the value that you will convert? "))
     mid = input("What unit is this currently stored in mg/dL or mmol/L? ")
     out = input("What unit would you like this displayed in mg/dL or mmol/L? ")
     RIGHT = value * NUM1
     OHH = value * NUM2
     if mid == "mg/dL" and out == "mmol/L":
        print(f"Your value will be {RIGHT} mmol/L ")
     if mid == "mmol/L" and out == "mg/dL":
        print(f"Your value will be {OHH} mg/dL")
    elif type == "cholesterol":
     value = float(input("What is the value that you will convert? "))
     mid = input("What unit is this currently stored in mg/dL or mmol/L? ")
     out = input("What unit would you like this displayed in mg/dL or mmol/L? ")
     RIGHT = value * NUM3
     OHH = value * NUM4
     if mid == "mg/dL" and out == "mmol/L":
        print(f"Your value will be {RIGHT} mmol/L ")
     if mid == "mmol/L" and out == "mg/dL":
        print(f"Your value will be {OHH} mg/dL")
    else:
     print("Please use a different converter!!")


def Tempaverage():
    FEVER =  38
    print("Please enter your temperatures in degrees celcius")
    Num1 = float(input("Input your first temperature: "))
    Num2 = float(input("Input your second temperature: "))
    Num3 = float(input("Input your third temperature: "))
    average = (Num1 + Num2 +Num3)/3
    print (f"your average is {round(average, 2)} in degrees celcius")
    if average >= FEVER:
       print("Fever warning please administor treatment!")
    elif average > 36 and average < FEVER:
       print("Please keep an eye on the patient, near fever temp")
    else:
       print("Safe, fever free")

def heartmonitor():
   MAX = 220
   Class = ""
   age = int(input("Please input your age: "))
   resting = int(input("Please enter your resting heart rate: "))
   safe = MAX - age
   if resting <= safe:
    Class = "High"
   if resting <= 100:
    Class = "Med"
   elif resting <= 60:
    Class = "Low"
   print(f"Your safe heart rate is {safe}, this means your heart rate is {Class}")

def hydratetracker():
    DAILY = 3.7
    intake = float(input("Please enter your water intake in Litres? "))
    current = DAILY - intake
    if current < DAILY:
      print(f"You need to drink {round(current,2)} more litres to meet the daily optimal water intake")
    else:
      print("Good job u met the optimal consumption of 3.5 litres of water a day!!")
      
