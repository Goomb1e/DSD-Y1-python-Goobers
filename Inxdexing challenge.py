Screen_times = [120, 95, 140, 160, 80, 100, 200]

day_1 = Screen_times[0]
day_2 = Screen_times[1]
day_3 = Screen_times[2]

print(day_3)

avg = (day_1 + day_2 + day_3)//3
print(avg)

Screen_times[-1] = 210

print(min(Screen_times), max(Screen_times))