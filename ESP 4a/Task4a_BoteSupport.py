import pandas as pd
import csv
import matplotlib.pyplot as plt

# Outputs the initial menu and validates the input
def main_menu():
    flag = True

    while flag:

        print("####################################################")
        print("############# Botes Parcels CRM System #############")
        print("####################################################")
        print("")
        print("########### Please select an option ################")
        print("### 1. Total issues by type")
        print("### 2. Time taken to resolve issue")
        print("### 3. Issues based on region")
        choice = input('Enter your number selection here: ')

        try:
            int(choice)
        except:
            print("Sorry, you did not enter a valid option")
            flag = True
        else:    
            print('Choice accepted!')
            flag = False

    return choice

  # Submenu for totals, provides type check validation for the input and returns issue type as a string
def total_menu():
    flag = True

    while flag:

        print("####################################################")
        print("############## Total issues by type ################")
        print("####################################################")
        print("")
        print("########## Please select an issue type ##########")
        print("### 1. Customer Account Issue")   
        print("### 2. Delivery Issue") 
        print("### 3. Collection Issue")  
        print("### 4. Service Complaint")

        choice = input('Enter your number selection here: ')
        
        try:
            int(choice)
        except:
            print("Sorry, you did not enter a valid option")
            flag = True
        else:    
            print('Choice accepted!')
            choice = int(choice)
            flag = False
        

    issueTypeList = ["Customer Account Issue", "Delivery Issue", "Collection Issue", "Service Complaint"]


    issueType = issueTypeList[choice-1]
    
    return issueType     

# Creates a new dataframe then counts the number of occurences of the requested issue type

def get_total_data(total_menu_choice):
    
    issues = pd.read_csv("Task4a_data.csv")
    
    total = issues['Issue Type'].value_counts()[total_menu_choice]

    msg = "The total number of issues logged as a {} was: {}".format(total_menu_choice, total)
    return msg

    
def days_resolve(issue_type):
    
    df = pd.read_csv("Task4a_data.csv")
    filtered = df[df['Issue Type'] == issue_type]

    counts = filtered['Days To Resolve'].value_counts().sort_index()

    plt.figure(figsize=(10, 5))
    counts.plot(kind='bar')

    plt.title(f"Days to Resolve for {issue_type}")
    plt.xlabel("Days to Resolve")
    plt.ylabel("Number of Issues")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()



def based_Region(issue_type):
    df = pd.read_csv("Task4a_data.csv")
    filtered = df[df['Issue Type'] == issue_type]
    regions = filtered['Region'].value_counts().sort_index()

    plt.figure(figsize=(10, 5))
    regions.plot(kind='bar')
    plt.title(f"Issues per region for {issue_type}")
    plt.xlabel("Regions")
    plt.ylabel("Number of Issues")
    plt.xticks(rotation=0, fontsize=6)
    plt.tight_layout()
    plt.show()


main_menu_choice = main_menu()
if main_menu_choice ==  "1":
    total_menu_choice = total_menu()
    issue_type = total_menu()
    print(get_total_data(total_menu_choice))
if main_menu_choice == "2":   
    issue_type = total_menu()
    print(days_resolve(issue_type))
elif main_menu_choice == "3":
    issue_type = total_menu()
    print(based_Region(issue_type))