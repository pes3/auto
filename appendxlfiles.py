import glob
import pandas as pd
import xlrd 
all_data = pd.DataFrame()
for f in glob.glob(r'\\--\--------\-\-------\ ----\----\*'): # loop through folder
    df = pd.read_excel(f)# store each file as df
    all_data = all_data.append(df,ignore_index=True) #append each file in folder
    writer = pd.ExcelWriter('appen.xlsx', engine='xlsxwriter')
    df.to_excel(writer) # write dataframe to excel file
    writer.save()
