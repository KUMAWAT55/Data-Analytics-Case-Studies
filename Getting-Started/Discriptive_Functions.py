import pandas as pd
dictionary={'Name':['Rohit','Rahul','A','B'],'Age':[23,25,26,25]}
DataFrame=pd.DataFrame(dictionary)
#Unique
print(DataFrame['Age'].unique())
print("######")
# count
print(DataFrame.count())
print("######")
# Mean
print(DataFrame.mean())
#Max can be
#Min can be
#value_count


