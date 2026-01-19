import pandas as pd
data = {
    "Name":["Alex", "Jamie","Sam","Bob"],
    "Attendence":[92,85,78,89],
    "Grade":["B","C","D","B"],
    "Passed":[True,True,False,True]
}

df = pd.DataFrame(data)
print(df)

df0 = pd.read_csv("students.csv") 
print(len(df0["ID"]))
print(df0["Attendence"].mean)
print(df0["Attendence"].min)
print(df0["Attendence"].max)

