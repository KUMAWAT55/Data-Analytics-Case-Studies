import pandas as pd
dictionary={'Name':['Rohit','Rahul'],'Age':[23,25]}
DataFrame=pd.DataFrame(dictionary)
#Method 1
print(DataFrame['Name'])
#Method 2
print(DataFrame.loc[:,'Name'])
print(DataFrame.loc[:,['Name','Age']])
print(DataFrame.loc[1,'Name'])

#Using iloc
print(DataFrame.iloc[:,:])
#Or
print(DataFrame.iloc[:,:])