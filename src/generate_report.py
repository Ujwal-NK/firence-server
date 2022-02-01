import xlsxwriter
from pysqlitecipher import sqlitewrapper
from datetime import date

# Creating a sqlite object to get data from the database
obj = sqlitewrapper.SqliteCipher(dataBasePath="../data/attendance.db" , checkSameThread=False , password="B3774405ED2198EDA392267CC1C17C6A6017ABA5870C6777EC86CF17CABE05FB")

# Getting the data
db_out = obj.getDataFromTable(str(date.today()), raiseConversionError = True , omitID = False)

table_data_dict = {}
table_data_list = []

# Sorting out the duplicate data
for x in db_out[1]:
    try:
        table_data_dict[x[2]] = [x[1], x[3], x[4], x[5]]
    except:
        table_data_dict[x[2]] = [x[1], x[3], x[4]]

for x in table_data_dict:
    if(len(table_data_dict[x]) == 3):
        table_data_list.append([x, *table_data_dict[x], ''])
    else:
        table_data_list.append([x, *table_data_dict[x]])
  
# Creating a workbook
workbook = xlsxwriter.Workbook("../data/tmp/" + str(date.today()) + ".xlsx")

# Adding a worksheet to the Workbook
worksheet = workbook.add_worksheet()

# Adding the date to the first row
worksheet.write(0, 0,"date:")
worksheet.write(0, 1, str(date.today()))
          
# Entering the data into the worksheet
worksheet.add_table('A2:E'+str(len(table_data_list) + 2), {'style': 'Table Style Light 11' ,'data': table_data_list, 'banded_rows': True, "columns":[{"header": "SRN"}, {"header": "Class Number"}, {"header": "Subject"}, {"header": "Status"}, {"header": "Query"}]})

# Red fill with dark red text.
red_format = workbook.add_format({'bg_color': '#FFC7CE', 'font_color': '#9C0006'})
# Green fill with dark green text.
green_format = workbook.add_format({'bg_color': '#C6EFCE', 'font_color': '#006100'})
# Light yellow fill with dark yellow text.
yellow_format = workbook.add_format({'bg_color': '#FFEB9C', 'font_color': '#9C6500'})

# Conditional Formatting
worksheet.conditional_format('D3:D' + str(len(table_data_list) + 3), {'type': 'cell', 'criteria': 'equal to', 'value': '"r"','format': red_format})
worksheet.conditional_format('D3:D' + str(len(table_data_list) + 3), {'type': 'cell', 'criteria': 'equal to', 'value': '"-"','format': yellow_format})
worksheet.conditional_format('D3:D' + str(len(table_data_list) + 3), {'type': 'cell', 'criteria': 'equal to', 'value': '"+"','format': green_format})

# Close the workbook
workbook.close()