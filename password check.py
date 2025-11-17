start = True
password = input("Please enter a password: ")
while start == True:
    retry = input("Please enter the same password: ")
    if password == retry:
        start = False
