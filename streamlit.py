import streamlit as st
import pandas as pd

# Set page title and layout
st.set_page_config(page_title="Cybersecurity News", layout="wide")

# Specify the path to your Excel file
excel_path = "/app/Articles.xlsx"
# Load data from Excel sheet
@st.cache_resource# Cache data for better performance
def load_data(excel_file):
    df = pd.read_excel(excel_file, usecols=["Title", "Text", "Sentiment"])
    return df

def main():
    st.title("Cybersecurity News Summaries and Sentiment Analysis")

    # Load data from specified Excel file path
    df = load_data(excel_path)

    st.header("News Articles from CybersecurityNewsletter and BleepingComputer")

    for index, row in df.iterrows():
        st.subheader(f"{row['Title']}")
        st.write(f"**Summary:** {row['Text']}")
        st.write(f"**Sentiment:** {row['Sentiment']}")

        st.markdown("---")  # Divider between articles

if __name__ == "__main__":
    main()
print("Streamlit file ran")