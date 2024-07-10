from Cybersecuritynews import cybersecurity
from Bleepingcomputer import bleepingcomputer
import openpyxl

print("Retrieving news")

# Retrieve data from functions
data1 = cybersecurity()
data2 = bleepingcomputer()

# Create a new workbook
wb = openpyxl.Workbook()

# Create worksheets for each source
ws1 = wb.active
ws1.title = "Cybersecurity News"
ws2 = wb.create_sheet(title="BleepingComputer")

# Add headers to each worksheet
ws1.append(["Title", "Text", "image", "link"])
ws2.append(["Title", "Text", "image", "link"])

# Add data from Cybersecurity News
for article in data1:
    ws1.append([article['title'], article['text'], article['image_url'], article['link']])

# Add data from BleepingComputer
for article in data2:
    ws2.append([article['title'], article['text'], article['image_url'], article['link']])

# Save the workbook to /app directory
file_path = "/app/Articles.xlsx"
wb.save(file_path)
print(f"Articles saved successfully at {file_path}!")
