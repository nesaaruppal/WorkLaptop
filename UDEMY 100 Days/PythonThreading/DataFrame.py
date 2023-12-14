import pandas
import DataFrame as df
from pandas import *

df = pandas.DataFrame([[1, 1.5]], columns=['int', 'float'])
row = next(df.iterrows())[1]

print(row['int'].dtype)
print(df['int'].dtype)