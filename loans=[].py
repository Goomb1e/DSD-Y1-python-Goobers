loans=[]
next_loan_id=1
def create_loan():
    global next_loan_id
    print("\n--- Create New Loan ---")
    student_name=input("Student Name: ")
    student_id=input("Student ID: ")
    device_type=input("Device Type (Laptop/Tablet/etc): ")
    device_id=input("Device ID: ")
    date_out=input("Date Out (YYYY-MM-DD): ")
    due_back=input("Due Back (YYYY-MM-DD): ")
    new_loan={"loan_id":next_loan_id,"student_name":student_name,"student_id":student_id,"device_type":device_type,"device_id":device_id,"date_out":date_out,"due_back":due_back,"returned":False}
    loans.append(new_loan)
    print(f"Loan created successfully with ID {next_loan_id}!")
    next_loan_id+=1

def search_loans():
    print("\n--- Search Loans ---")
    keyword=input("Enter student name or ID to search: ").lower()
    found=False
    for loan in loans:
        if keyword in loan["student_name"].lower() or keyword in loan["student_id"].lower():
            print("\nLoan Found:")
            for key,value in loan.items():
                print(f"{key}: {value}")
            print("--------------------------")
            found=True
    if not found:
        print("No matching records found.")

def update_loan():
    print("\n--- Update Loan ---")
    try:
        loan_id=int(input("Enter Loan ID to update: "))
    except ValueError:
        print("Invalid ID.")
        return
    for loan in loans:
        if loan["loan_id"]==loan_id:
            print("Loan found! What would you like to update?")
            print("1. Due Date")
            print("2. Mark as Returned")
            choice=input("Choose an option: ")
            if choice=="1":
                new_due=input("Enter new due back date (YYYY-MM-DD): ")
                loan["due_back"]=new_due
                print("Due date updated successfully!")
            elif choice=="2":
                loan["returned"]=True
                print("Loan marked as returned!")
            else:
                print("Invalid option.")
            return
    print("Loan ID not found.")

create_loan()
search_loans()
update_loan()
