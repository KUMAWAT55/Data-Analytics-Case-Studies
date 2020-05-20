import pandas as pd
dictionary={'Name':['Rohit','Rahul'],'Age':[23,25]}
DataFrame=pd.DataFrame(dictionary)
print(DataFrame)
#describe gives stat.
print(DataFrame.describe())
# info gives datatypes and all info
print(DataFrame.info())

#DataFrame using List
new_list=[1,2,3,4,5]
list_df=pd.DataFrame(new_list)
print(list_df)
#Get columns list
print(DataFrame.columns)

#How to access a column
print(DataFrame['Name'])

