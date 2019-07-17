import pandas as pd

#load excel file
excel_file = 'movies.csv'
movies = pd.read_csv(excel_file)

#print(movies.head(10))
#print(movies.tail(10))
#print(movies.sample(3))
#print(movies.columns)
#print(movies.describe())

# Extract specific columns
#sheet_1 = movies[['Genres','Year','Country']]
#print(sheet_1)

#Extract designated rows
#print(movies[0:10])

#Extract Row & Columns
#print(movies.loc[10:40, ['Year','Title']])
#print(movies.iloc[3:5, 0:2])

#Search by conditions
#print(movies[movies.Year>2015])

#insert a new column
#df2 = movies[0:6].copy()
#df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
#print(df2)


#Diretctor = movies.Director
#print(Director)

#Count how much data is missing
#for col in movies.columns:
#    print('columnn : {:>10}\t Percent of NaN value:{:.4f}%'.format(col, 100* (movies[col].isnull().sum()/
#                                                                              movies[col].shape[0])))

#결측치(NaN:non existing data)를 바꿔주고 싶을때
#print(movies.fillna(value=10))

#Count number of the data (frequency)
#print(movies['Director'].value_counts())

#Merging data
'''
left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1,2]})
print(left)
right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4,5]})
print(right)
merged = pd.merge(left, right, on='key')
print(merged)
'''
'''
left = pd.DataFrame({'key': ['foo', 'bar'], 'lval': [1,2]})
print(left)
right = pd.DataFrame({'key': ['foo', 'bar'], 'rval': [4,5]})
print(right)
merged = pd.merge(left, right, on='key')
print(merged)

merged.to_csv('excel_file.csv')
'''

excel = 'part_time.csv'
part = pd.read_csv(excel)
print(part)

df = pd.read_csv(excel)
df['running_time'] = df['End_time'] - df['Start_time']
print(df)

df['time per movie'] = df['Time_make'] / df['Make']
print(df)

df = df.sort_values(by=['Time_make'], ascending=False)
print(df)

df.to_csv('new_time.csv')