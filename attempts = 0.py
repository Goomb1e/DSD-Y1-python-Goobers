attempts = 0
RFID_Valid = False

Correct_Pin = 1234
Valid_RFID = "M2503106"
Door = "Locked"

while attempts < 3:
    Pin = int(input("Please enter Pin: "))
    if Pin  == Correct_Pin:
        print("Access Granted")
        Door = "Open"
        attempts = attempts + 3
    else:
        print("Access denied")
        Door = "Locked"
        attempts = attempts + 1

if attempts == 3 and Door == "Locked":
    print("Authorities alerted")

RFID = input("Please tap RFID Card: ")
if RFID.lower() != Valid_RFID:
    print("RFID Card accepted")
    RFID_Valid = True
else:
    print("Invalid RFID Card Access denied")


if Door == "Open" and RFID_Valid == True:
    print("Door unlocked - Please enter")

