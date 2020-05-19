import pandas as pd
#this file have dummy datasets for titanic passangers .
file_name = "https://raw.githubusercontent.com/rajeevratan84/datascienceforbusiness/master/titanic.csv"
titanic_df = pd.read_csv(file_name)
print(titanic_df.head(10)) #head returns top 10 records
print(titanic_df.tail(10))#tail returns last 10 records
#How to Save
titanic_df.to_csv("outputs/titanic.csv")
#Save as excel
#titanic_df.to_excel("outputs/titanic.xlsx")
print(titanic_df.info)