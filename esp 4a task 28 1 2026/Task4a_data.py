import pandas as pd
import matplotlib.pyplot as plt

def main_menu():
    flag = True
    while flag:
        print("#################################################")
        print("############## Versere Cars Sales ##############")
        print("#################################################")
        print("")
        print("########### Please select an option #############")
        print("### 1. Total Sales Analysis")
        print("### 2. New and used car sales")
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

def total_menu():
    flag = True
    while flag:
        print("#################################################")
        print("############## Total Sales ##############")
        print("#################################################")
        print("")
        print("########### Please select an option #############")
        print("### 1. All sales by model")   
        print("### 2. Custom selection") 
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

def convert_total_menu_choice(total_menu_choice):
    if total_menu_choice == "1":
        total_choice = "All"
    elif total_menu_choice == "2":
        total_choice = "Model"
    else:
        total_choice = "All" 
    return total_choice

def get_total_data(total_choice):
    df = pd.read_csv("Task4a_data.csv")
    df.columns = df.columns.str.strip()  

    if total_choice == "All":
        total = df['Value'].sum()
        print("The total value of sales for your selection is {}".format(total))
        extract = df
        model_name = "All Models" 
    else:
        flag = True
        while flag:
            print("########### Please select a model #############")
            print("### 1. Ranger")
            print("### 2. Model D Premium Plus")
            print("### 3. Compass")
            print("### 4. Mercury")
            print("### 5. Outback")
            choice = input('Enter your number selection here: ')
            try:
                choice = int(choice)
                flag = False
            except:
                print("Sorry, you did not enter a valid option")

        models = ["Ranger", "Model D Premium Plus", "Compass", "Mercury", "Outback"]   
        custom_choice = models[choice -1]
        extract = df[df['Car Model'] == custom_choice]  
        total = extract['Value'].sum()
        print("The total value of sales for your selection is {}".format(total))
        model_name = custom_choice 

    return extract, model_name  

def plot_new_used(extract, model_name):
    extract.columns = extract.columns.str.strip()
    counts = extract['New/Used'].value_counts()
    plt.figure(figsize=(6, 4))
    counts.plot(kind='bar', color=['skyblue', 'orange'])
    plt.title(f"New vs Used Sales for {model_name}") 
    plt.xlabel("Condition")
    plt.ylabel("Number of Sales")
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

if main_menu_choice == "1":
    total_menu_choice = total_menu()
    total_choice = convert_total_menu_choice(total_menu_choice)
    extract = get_total_data(total_choice)

elif main_menu_choice == "2":
    total_menu_choice = total_menu()
    total_choice = convert_total_menu_choice(total_menu_choice)
    extract, model_name = get_total_data(total_choice)
    plot_new_used(extract, model_name)

else:
    print("This section is under construction")