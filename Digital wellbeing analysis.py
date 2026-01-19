notifications = [34, 28, 55, 40, 60, 22, 18]
notifications_2 = [12, 23, 54, 86, 23, 43, 31]

print(notifications[0])
print(notifications[1])
print(notifications[2])
print(notifications[3])
print(notifications[4])
print(notifications[5])
print(notifications[6])

highest_Day = max(notifications)
lowest_Day = min(notifications)
total = sum(notifications)

print(highest_Day, lowest_Day, total)

avg = total/(len(notifications))
print(round(avg,2))

notifications.append(int(input("Input value to append: ")))
print(notifications)

total_2 = (sum(notifications_2))

if total > total_2:
    print(f"User 1 has more notifications")
else:
    print(f"User 2 has more notifications")
