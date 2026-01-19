import random 

name = input("Please enter name: ")

randomnum = random.random()

with open("NameRandom.txt", "a") as file:
    file.write(f"{name} {str(randomnum)}")