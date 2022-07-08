import pandas as pd


# df = pd.read_csv('Space_Corrected.csv').fillna(0)
# print(df.shape)
# print(df.head())
# print('Assigning a Particular value to column at index2')
# for items in range(len(df)):
#     df.loc[items, 'Unnamed: 0'] = 'rocketinfo' + str(df.loc[items,
#             'Unnamed: 0'])
# print(df.head())
#
# # adding an new row
#
# print('Adding a new row')
# df.loc[len(df)] = [
#     4599,
#     4599,
#     'Pakistan',
#     'Site 20000, Test dvalue, Kazakhstan',
#     'Fri Oct 04, 1957 19:28 UTC',
#     'just test data',
#     'new column ',
#     29,
#     'failure',
#     ]
#
# # adding an new column
#
# print('adding a new column')
# for items in range(len(df)):
#     df.loc[items, 'Points'] = int(df.loc[items, ' Rocket']) * 5
#
# print(df.head())
# print (df.tail())
#
# # updating a particular value
#
# print('Updating company name for index 4320\n')
# print ('Value before update \n', df['Company Name'][4320])
# df.loc[4320, 'Company Name'] = 'Comsats University islambad'
# print ('Value after update \n', df.loc[4320])
#
# # updating row 2
#
# print('Updating row2')
# for items in range(len(df)):
#     if df['Status Mission'][items] == 'Failure':
#         df.loc[items, 'Unnamed: 0'] = str(df.loc[items, 'Unnamed: 0']) \
#             + '(N.A)'
# print('Dropping rows 0 to 10')
# df.drop(df.index[0:10], inplace=True)
#
# print(df.head())
# df.to_csv('Space_Corrected_2.csv', index=False)
x={1: ('shayan', '12', ['english', 'urdu']), 2: ('ali', '13', ['physics', 'algebra'])}
df=pd.DataFrame(x)
df.reset_index(drop=True, inplace=True)
print(df)
df1=df.T

print(df1)