import os
import pandas as pd
cwd = os.path.abspath('') 
files = os.listdir(cwd)  
import glob

## Method 1 gets the first sheet of a given file
# df = pd.DataFrame()
# for file in files:
#     if file.endswith('.xls'):
#         df = df.append(pd.read_excel(file), ignore_index=True) 
# df.head() 
# df.to_excel('combined_file.xlsx')



## Method 2 gets all sheets of a given file
df_total = pd.DataFrame()
for file in files:   
    if file.endswith('.xls'):
        print(file)                      # loop through Excel files
        excel_file = pd.ExcelFile(file)
        sheets = excel_file.sheet_names
        for sheet in sheets:               # loop through sheets inside an Excel file
            df = excel_file.parse(sheet_name = sheet)
            df_total = df_total.append(df)
writer = pd.ExcelWriter(r'combined_file.xlsx', engine='xlsxwriter',options={'strings_to_urls': False})
df_total.to_excel(writer)
writer.close()
# df_total.to_excel('combined_file.xlsx',engine='xlsxwriter',options={'strings_to_urls': False})

## Method 3 using glob
# all_data = pd.DataFrame()
# for f in glob.glob("*.xls"):
#     df = pd.read_excel(f)
#     all_data = all_data.append(df,ignore_index=True)
#     all_data.to_excel('combined_file.xlsx')