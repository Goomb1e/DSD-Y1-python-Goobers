name = input("Please input the name: ")
add = input("Would you like to add to the balance: ")
balance = 0
while add.upper() == "YES":
    adding = float(input("Please input what you would like to add: "))  
    balance = balance + adding
    add = input("Would you like to add to the balance: ")
    print(f"Your new balance is :{balance}")
