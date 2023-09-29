<h1> Excel Data Extraction and Transformation</h1>

This Python script demonstrates how to use the openpyxl library to process an Excel file. In this example, we load an Excel file named `employee.xlsx`, access a specific sheet named 'Sheet1', extract data, and create a new Excel file named `conduct2.xlsx`. 

<h1>Prerequisites</h1>

Before running the script, make sure you have the openpyxl library installed. You can install it using pip:

```bash
pip install openpyxl


<h1>Usage</h1>
Replace 'employee.xlsx' with the path to your Excel file.
Replace 'Sheet1' with your sheet name if it's different.
Run the script. It will create a new Excel file named conduct2.xlsx with extracted data.
Script Explanation
The script loads the specified Excel file.
It accesses the specified sheet.
It extracts rows where the value in column 11 is 'Missing'.
The extracted data is organized in a dictionary where each AKAM ID corresponds to a list of employee names.
The script creates a new Excel file.
It adds headers to the new Excel file.
It appends the extracted data to the new Excel file.
The new Excel file is saved as conduct2.xlsx.
Example
For a better understanding of how this script works, consider the following example:

Suppose your employee.xlsx file has data like this:

| AKAM ID | Employee Name | ... |
| ------- | ------------- | --- |
| 001    | John,Doe    | ... |
| 002    | Alice       | ... |
| 003    | Missing     | ... |
| 004    | Bob
