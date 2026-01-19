food_menu = {
    "spaghetti":2.50, 
    "Churizzo":2, 
    "Butter":1, 
    "Aardvark":5
    }



drink_menu = {
    "cola":2.50, 
    "fanta":2, 
    "water":1, 
    "milk":5
    }

ordered = {
    "spaghetti":0,
    "churizzo":0,
    "butter":0,
    "aardvark":0,
}




available = [1, 2, 3, 4, 5, 6]

time = [9,10,11,12,13,14,15,16,17,18,19,20]

def bookings():
    name = input("Please input name for the booking: ")
    print(*time)
    times = int(input("Input the desired time: "))
    time.remove(times)
    if times + 1 in time:
        time.remove(times + 1)
    print("List of available lanes:")
    print(*available)
    picked = int(input("Please input the desired lane: "))
    available.remove(picked)
    number_people = int(input("How many people are attending: "))
    print(f"You are booked under {name} for {times} at lane {picked}")
    price_per_booking = 8
    total = number_people*price_per_booking
    print(f"The total price will be {round(total,0)}")


def food():
    print("Here is a list of our food")
    print(*food_menu)
   
    while True:
        Spaghetti = 0
        Churizzo = 0
        Butter = 0
        Aardvark = 0
        selected = input("Please input the item you would like: ")
        many_food = int(input("How many of this food item: "))
        if selected.lower() == "spaghetti":
            Spaghetti = Spaghetti + many_food
            ordered["spaghetti"]=Spaghetti
        elif selected.lower() == "churizzo":
            Churizzo = Churizzo + many_food
            ordered["churizzo"]=Churizzo
        elif selected.lower() == "butter":
            Butter = Butter + many_food
            ordered["butter"]=Butter
        elif selected.lower() == "aardvark":
            Aardvark = Aardvark + many_food
            ordered["aardvark"]=Aardvark
        else:
            print("Item not on menu")
        end = input("Would you like to order more: ")
        if end.lower()== "no":
            break
    print(f"You have ordered {Spaghetti} Spaghettis, {Churizzo} Churizzos, {Butter} sticks of butter and {Aardvark} Aardvarks")
    price_1 = Spaghetti * 2.50
    price_2 = Churizzo * 2
    price_3 = Butter * 1
    price_4 = Aardvark * 5
    total = price_1 + price_2 + price_3 + price_4
    print(f"Your price will be £ {total}")
    print(*ordered)
food()









