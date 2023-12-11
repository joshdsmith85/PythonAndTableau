# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 21:42:12 2023

@author: joshd
"""



import pandas as pd
 
 # file_name = pd.read_csv('file.csv') <--- format of read_csv

data = pd.read_csv('transaction2.csv', sep=';')

#summary of the data
data.info()

#working with calculations

#defining variables

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemsPurchased = 6

#Mathematical Operations on Tableau

ProfitPerItem = 21.11 * 11.73
ProfitPerItem = SellingPricePerItem - CostPerItem
ProfitPerTransAction = ProfitPerItem * NumberOfItemsPurchased
CostPerTransaction = CostPerItem * NumberOfItemsPurchased
SellingPricePerTransaction = SellingPricePerItem * NumberOfItemsPurchased


#CostPerTransaction = CostPerITem * NumberOfItemsPurchased
# variable = dataframe['column_name']

CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']

CostPerTransaction = CostPerItem * NumberOfItemsPurchased

#Adding new column to dataframe

data['CostPerTransaction'] = CostPerTransaction

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

data['ProfitPerTransaction'] = ((data['SellingPricePerItem'] - data['CostPerItem']) * data['NumberOfItemsPurchased'])

data['Markup'] = ((data['SellingPricePerItem'] - data['CostPerItem'])/ data['CostPerItem'])

# rounding marking

roundmarkup = round(data['Markup'],2)

data['Markup'] = round(data['Markup'],2)

# Combining data fields

my_name = 'Josh' + 'Smith'
my_day = 'Day' + '-' + 'Month' + '-' + 'Year'

#my_date = data['Day']+ '-' this wont work without changing the data type to string

#Checking columns data type
print(data['Day'].dtype)

#change column data type
day = data['Day'].astype(str)
Year = data['Year'].astype(str)
print(day.dtype)
my_date = day + '-' + data['Month'] + '-' + Year

data['Date'] = my_date

# using iloc to view specific columns/rows
data.iloc[0] #views the row with the index 0
data.iloc[0:3] #views the first 3 rows
data.iloc[-5:] #views the last 5 rows

data.head(5) # brings in first 5 rows

data.iloc[:,2] #brings in all rows on secound column

data.iloc[4,2] #brings in 4th row, 2nd column

# using split to split clients keyword field
# new_var= column.str.split('seperator type' , expand = true)




split_col = data['ClientKeywords'].str.split(',' , expand=True )

#Creating new columns for the split columns

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthOfContract'] = split_col[2]

#using replace to remove certain characters

data['ClientAge'] = data['ClientAge'].str.replace('[', '')

data['LengthOfContract'] = data['LengthOfContract'].str.replace(']', '')

# Using lower function to change item to lowercase
data['ItemDescription'] = data['ItemDescription'].str.lower()

#how to merge files

#bring in a new data set
season = pd.read_csv('value_inc_seasons.csv', sep=';')

#merging files: merge_df = pd.merge(df_old, df_new, ON = 'KEY')

data = pd.merge(data, season, on = 'Month')

#dropping columns 

# df= df.drop['ColumnName', axis = 1]
data = data.drop('ClientKeywords', axis = 1)
data = data.drop(['Day', 'Month', 'Year'], axis = 1)
                 
# Export into csv

data.to_csv('ValueInc_Cleaned.csv', index = False)
