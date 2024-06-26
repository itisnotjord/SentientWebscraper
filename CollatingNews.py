from Cybersecuritynews import cybersecurity
from Bleepingcomputer import bleepingcomputer
import openpyxl

# Retrieve data from functions
data1 = cybersecurity()
data2 = bleepingcomputer()

# Combine data from both sources
combined_data = data1 + data2

# Create a new workbook
wb = openpyxl.Workbook()

# Create a worksheet
ws = wb.active
ws.title = "Combined Articles"

# Add headers
ws.append(["Source", "Title", "Text"])

# Add data from both sources
for source, articles in [("Cybersecurity News", data1), ("BleepingComputer", data2)]:
    for article in articles:
        ws.append([source, article['title'], article['text']])

# Save the workbook
wb.save("Articles.xlsx")
print("Articles saved successfully!")
