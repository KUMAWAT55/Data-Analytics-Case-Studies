import pandas
        # print(pandas.__version__)
        # Create python list
sample_list=[1,2,3,4,5]
        # Now lets convert into series
Series=pandas.Series(sample_list)
print(Series)

#Some basic Operations
print('Min Value:',Series.min())
print('Max Value:',Series.max())
#If you will apply operation without inplace , it will create a copy of object .
print(Series.sort_values(ascending=False))
#If you will apply operation with inplace , it will modify object .
print(Series.sort_values(ascending=False,inplace=True))
print(Series)
print(Series.value_counts())
print(Series[1:4])