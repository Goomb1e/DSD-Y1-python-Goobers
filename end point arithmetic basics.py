# Steps = int(input("Please enter steps take today: "))
# Daily = 10000
# percent = (Steps / Daily)* 100
# left = Daily - Steps
# if percent > 0 and percent <= 100 and left > 0:
#     print(f"You're daily steps taken are completed : {round(percent)}% , You have {left} left")
# elif percent > 100:
#     print("Wow you have exceded the goal")
# else:
#     print("Invalid")

# weight_kg = float(input("Please enter weight in kg: "))
# height_m = float(input("Please enter height in M: "))
# BMI = (weight_kg/(height_m**2))
# if BMI < 18.5:
#     print("Underweight")
# elif BMI > 18.5 and BMI < 25:
#     print("Healthy")
# elif BMI > 25 and BMI < 30:
#     print("Overweight")
# elif BMI > 30:
#     print("Obese")

# def flag_user(daily_screen_minutes, night_screen_minutes, steps):
#     return daily_screen_minutes > 240 and steps < 5000 or night_screen_minutes > 60

# daily_screen_minutes = int(input("Please input daily screen time in minutes: "))
# night_screen_minutes = int(input("Please input screen time at night: "))
# steps = int(input("Please input steps took today: "))

# if flag_user(daily_screen_minutes, night_screen_minutes, steps)== True:
#     print("User flagged")
# else:
#     print("User not flagged")

# water_ml = int(input("Please input water intake in ml: "))
# point = 250
# points = 2000
# ml_point = water_ml // point
# L_point = water_ml // points
# L_points = L_point % 2
# total = ml_point + (L_points*5)
# if L_point >= 1:
#     print(f"You're total points are {total}")
# else:
#     print(f"You're total points are {ml_point}")
 
# def eligible_for_free_class(age, low_income, days_since_last_free):
#     return age > 16 and age <= 25 or low_income.lower() == "yes" and days_since_last_free > 30

# age = int(input("Please input age: "))
# low_income = input("Are you classed as low income: ")
# days_since_last_free = int(input("How many days since last free: "))

# if eligible_for_free_class(age, low_income, days_since_last_free) == True:
#     print("Eligible")
# else:
#     print("You are not eligible")

# def weekly_tier(steps, water_ml):
#     points = (steps // 1000) * 2 + (water_ml // 500) 
#     if points > 0 and points <= 19:
#       print("Bronze")
#     elif points >=20 and points <= 39:
#       print("Silver")
#     elif points >= 40:
#       print("Gold")

# water_ml = int(input("Please enter your water intake in ml: "))
# steps = int(input("Please enter your steps today"))

# print(weekly_tier(steps, water_ml))

