import pandas as pd

import xlsxwriter

data = pd.read_excel("example.lsx","Sheet1)", encoding = "ISO-8859-1", dtype = 'unicode')

data.columns = data.columns.str.strip().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

data2 = data.groupby('Item').Delivery_Date.apply(' '.join).reset_index() #input multilple dates with same ID into one row

grouped = data.groupby(['Item'])

 

print(data2.head(10)) #showing tat each date in the DeliveryDate column per it's respective Item number is in one row 
