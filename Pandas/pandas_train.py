import pandas as pd

#Creat a dataframe a json object
data = {
    'Name': ['Amy','Rambo','Pilea','Singa','David','Dambo','Yuva'],
    'Age': [23,24,42,35,45,46,56,],
    'Score': [34,45,54,65,74,67,85],
    'Gender':['F','M','F','M','M','M','M'],
    'id' : [1,2,3,4,5,6,7],
    'Blood_group' : ['A','B','O','B','A','O','A']
}
df1 = pd.DataFrame(data)
print(df1)

#Convert dataframe back to json

json_data = df1.to_json(orient = 'records')
print(json_data)

data_new = {
    'Name': ['Dp','Ap','Pa','Si','Lp','Mp','Yp'],
    'Age': [25,44,62,36,48,45,59,],
    'Score': [44,75,74,85,24,68,15],
    'Gender':['M','M','F','M','F','M','M'],
    'id' : [1,2,3,4,5,6,7],
    'Blood_group' : ['B','B','O','A','B','O','A']
}
df2 = pd.DataFrame(data_new)
print(df2)

#Merge two dataframes
data_merge = pd.merge(df1,df2, on = 'id', suffixes=(' ',' '))
print(data_merge)

#inner join
inner_result = pd.merge(df1,df2, how = 'inner', on = 'Blood_group',suffixes =(' ',' '))
print(inner_result)

#left join
left_result = pd.merge(df1,df2, how = 'left', on = 'Blood_group',suffixes =(' ',' '))
print(left_result)

#right join
right_result = pd.merge(df1,df2, how = 'right', on = 'Blood_group',suffixes =(' ',' '))
print(right_result)

#outer join
outer_result = pd.merge(df1,df2, how = 'outer', on = 'Blood_group',suffixes =(' ',' '))
print(outer_result)

#cross join
cross_result = pd.merge(df1,df2, how = 'cross',suffixes =(' ',' '))
print(cross_result)

#using lambda function to square the age column
df1['square_age'] = df1['Age'].apply(lambda x:x**2)
result = df1['square_age']
print(result)