import datetime
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Task_4a.csv')


def mainmenu():
    print("\t\t****Welcome to the Dashboard****")
    print('1) Return all current data')
    print('2) Return data for a specific region')
    print('3) size within a region')
    return int(input(""))


def alldata():
    print(df)


def region_check(region, startdate, enddate):  # region, startdate, enddate

    df1 = df.loc[:, startdate:enddate]
    df2 = df.loc[:, 'Region Code':'Rooms']

    result = pd.concat([df2, df1], axis=1, join='inner').where(df2["Region"] == region)
    result = pd.DataFrame(result)
    result.dropna(inplace=True)
    print(result)
    ave = df1.mean()
    ave.plot()
    plt.show()
    return result

def property_region(region, Property_Type):

    filtered = df[(df["Region"] == region) & 
                  (df["Property Type"] == Property_Type)]

    pivot = pd.crosstab(filtered["Rooms"], filtered["Property"])

    pivot = pivot.reindex(range(1,6), fill_value=0) 

    pivot.plot(kind='bar', figsize=(10,6))

    plt.xlabel("Number of Rooms")
    plt.ylabel("Number of Properties")
    plt.title(f"{Property_Type} in {region} by Room Size and Property")
    plt.xticks(rotation=0)
    plt.legend(title='Property')
    plt.show()




while True:
    x = mainmenu()
    if x == 1:
        alldata()

    elif x == 2:
        while True:
            print()

            region = input("Please enter the name of the region you would like to check:")
            region = region.capitalize()
            if region in df.Region.values:
                while True:
                    startdate = input("PLEASE ENTER A START DATE AS MONTH-YEAR e.g. JAN-20")
                    startdate = startdate.capitalize()
                    if startdate not in df.columns:
                        print("Error start date not found")
                    else:
                        while True:
                            enddate = input("PLEASE ENTER AN END DATE AS MONTH-YEAR e.g. JAN-20")
                            enddate = enddate.capitalize()
                            if enddate not in df.columns:
                                print("Error end date not found")
                            else:
                                region_check(region, startdate, enddate)
                                break
                        break
                break
    elif x == 3:
               region = input("Please enter the name of the region you would like to check:\n 1.London\n 2.Bristol\n 3.Leeds \n 4.Cardiff \n 5.Manchester\n 6.Birmingham\n 7.Glasgow\n ")
               region = region.capitalize()
               if region in df.Region.values:
                while True:
                     Property_Type = input("Please enter type of house: \n 1. Bungalow\n 2. Semi-Detached\n 3. Detached\n ")
                     Property_Type = Property_Type.capitalize()
                     property_region(region, Property_Type)
                     if Property_Type not in df["Property Type"].values:
                        print("Error property type not found")
                     else:
                        break
                break
            