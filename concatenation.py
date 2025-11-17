Name1 = str(input("Please input your First name: "))
Name2 = str(input("Please input your Second name: "))
while len(Name1+Name2) > 20:
    print("Error, name is too long")
    Name1 = str(input("Please input your First name: "))
    Name2 = str(input("Please input your Second name: "))
else:
    print("Your name is", Name1 +Name2)
    print("Your name is", len(Name1+Name2), "Letters long")