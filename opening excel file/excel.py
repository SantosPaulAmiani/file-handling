write ReadMe.md for from openpyxl import load_workbook, Workbook

# Replace 'employee.xlsx' with the path to your Excel file
excel_file = 'employee.xlsx'

# Load the Excel file
workbook = load_workbook(filename=excel_file)

# Access a specific sheet (replace 'Sheet1' with your sheet name)
sheet = workbook['Sheet1']

data = {}
keys = []
# Iterate through rows
for row in sheet.iter_rows(values_only=True):
    if row[10] == 'Missing':
        data[row[0]] = row[1].split(',')
        keys.append(row[1])
#print(data)
# Close the loaded workbook
workbook.close()

# Create a new workbook
new_workbook = Workbook()
new_sheet = new_workbook.active

# Add headers to the first row
new_sheet.append(['AKAM ID', 'Employee Name'])

# Append data to the new sheet
for employee_id, employee_names in data.items():
    for employee_name in employee_names:
        new_sheet.append([employee_id, employee_name])


# Save the new Excel file to a specified location
new_workbook.save('conduct2.xlsx')
new_workbook.close()
