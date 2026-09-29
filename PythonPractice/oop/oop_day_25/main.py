
import csv
import pandas




data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

squirrel_count = {'Black' :[len(data[data['Primary Fur Color'] == 'Black'])],
'Cinnamon' :[len(data[data['Primary Fur Color'] == 'Cinnamon'])],
'Gray' :[len(data[data['Primary Fur Color'] == 'Gray'])]}
print(squirrel_count)
df = pandas.DataFrame(squirrel_count)
df.to_csv('newcsv.csv')