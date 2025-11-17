arcade = {
    "Pinball Wizard": {"Category": "Pinball", "Status": "Working"},
    "Air hockey": {"Category": "Sport", "Status": "Not Working"},
    "Boxer": {"Category": "Sport", "Status": "Working"}
}

def add_machine(machine, category, status):
    arcade[machine] = {"category": category, "Status": status}

def update_machine(machine, category, status):
    arcade[machine] = {"category": category, "Status": status}



select = int(input("1.View machines, 2.Add machine, 3.Update Status, 4.Delete entry : "))
if select == 1:
    print(*arcade.keys())
elif select == 2:
    machine = input("Input machine name: ")
    category = input("Input machine category: ")
    status = input("Input machine status: ")
    add_machine(machine, category, status)
    print(arcade)
elif select == 3:
    machine = input("Please input the machine to alter: ")
    category = input("Input machine category: ")
    status = input("Please input machine status: ")
    update_machine(machine, category, status)
    print(arcade)
elif select == 4:
    machine = input("Input machine to delete: ")
    del arcade[machine]
    print(arcade)