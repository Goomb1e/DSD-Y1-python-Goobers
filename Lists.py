Energy_Levels = [1,3,5,7,9]

Username = [
    "ozzar",
    "goombie", 
    "exe",
    "DB095",
    "Vince",
    "Weegemation",
    "Cyrus",
    "Dom",
    "mrballz"
    ]

Steps = [1212, 2154, 3512, 5313, 1231, 8523, 9231]

def findMiddle(input_list):
    middle = float(len(input_list))/2
    if middle % 2 != 0:
        return input_list[int(middle - .5)]
    else:
        return (input_list[int(middle)], input_list[int(middle-1)])


print(Energy_Levels, Username, Steps)

print(Energy_Levels[0])
print(findMiddle(Energy_Levels))
print(Energy_Levels[-1])

print(Username[0])
print(findMiddle(Username))
print(Username[-1])

print(Steps[0])
print(findMiddle(Steps))
print(Steps[-1])