from transformers import pipeline
import pandas as pd
from openpyxl import load_workbook

# Load the Excel workbook
df = pd.read_excel("/app/Articles.xlsx")
# Access each row (article) using DataFrame indexing
articles = [df.iloc[i, 2][:512] for i in range(len(df))]
data = articles

# Perform sentiment analysis
specific_model = pipeline("text-classification", model="ProsusAI/finbert")
lst = specific_model(data)
sentiment_results = [f"{result['label'].capitalize()}, Score: {result['score']}" for result in lst]

# Load existing workbook for editing
wb = load_workbook("/app/Articles.xlsx")
ws = wb.active
ws.cell(row=1, column=4, value="Sentiment")

# Add sentiment analysis results to a new column (starting from column B)
for idx, result in enumerate(sentiment_results):
    # Add 1 to idx because Excel rows and columns are 1-indexed
    ws.cell(row=idx + 2, column=4, value=result)

# Save the updated workbook
wb.save("Articles.xlsx")
print("Sentiment analysis results appended to Excel file.")
