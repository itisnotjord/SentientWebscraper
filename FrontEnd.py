import streamlit as st
import pandas as pd

# Set page title and layout
st.set_page_config(page_title="Cybersecurity News", layout="wide")

# Specify the path to your Excel file
excel_path = "/app/Articles.xlsx"

# Cache data for better performance
@st.cache_resource
def load_data(excel_file, sheet_name):
    df = pd.read_excel(excel_file, sheet_name=sheet_name)
    return df

def main():
    st.markdown("""
        <style>
        .main {
            width: 90%; /* Adjust width as needed */
            margin: 0 auto;
            padding: 1.5rem; /* Adjust padding as needed */
            box-sizing: border-box; /* Ensures padding is included in the width */
        }
        .stSelectbox label {
            display: none;
        }
        .article-container {
            display: flex;
            justify-content: center; /* Center align horizontally */
            align-items: center; /* Center align vertically */
            margin-bottom: 2rem;
            text-align: center; /* Center align text */
        }
        .article-image {
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 50%;
        }
        .article-content {
            flex: 1;
        }
        .article-title {
            font-size: 2rem; /* Adjust title font size */
            margin-bottom: 0.5rem;
            cursor: pointer;
            text-align: center;
        }
        .article-sentiment {
            font-size: 1.2rem; /* Match sentiment font size with title */
            text-align: center;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="main">', unsafe_allow_html=True)
    
    st.markdown("<h1 style='text-align: center;'>Cybersecurity News Summaries and Sentiment Analysis</h1>", unsafe_allow_html=True)

    # Load the Excel file and get sheet names
    xls = pd.ExcelFile(excel_path)
    sheet_names = xls.sheet_names

    # Create a dropdown menu to select the sheet without a label
    sheet_name = st.selectbox("", sheet_names)

    # Load data from the selected sheet
    df = load_data(excel_path, sheet_name)

    # Display radio buttons for sorting options
    sort_option = st.radio("Sort articles by:", ("Positive Sentiment", "Negative Sentiment"))

    if sort_option == "Positive Sentiment":
        df_sorted = df.sort_values(by='Sentiment', ascending=False)
    elif sort_option == "Negative Sentiment":
        df_sorted = df.sort_values(by='Sentiment', ascending=True)

    st.markdown(f"<h1 style='text-align: center;'>News Articles from {sheet_name}</h1>", unsafe_allow_html=True)


    for index, row in df_sorted.iterrows():
        st.markdown('<div class="article-container">', unsafe_allow_html=True)
        
        # Display image on the left
        st.markdown(f'<div class="article-image"><img src="{row["image"]}" style="width:100%;"></div>', unsafe_allow_html=True)
        
        # Display article content on the right
        st.markdown('<div class="article-content">', unsafe_allow_html=True)
        
        # Display clickable title linking to the article
        st.markdown(f"<h3 class='article-title'><a href='{row['link']}' target='_blank'>{row['Title']}</a></h3>", unsafe_allow_html=True)
        
        # Display sentiment value below the title
        st.markdown(f"<p class='article-sentiment'><strong>Sentiment:</strong> {row['Sentiment']}</p>", unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)  # Close article-content
        
        st.markdown('</div>', unsafe_allow_html=True)  # Close article-container
        
        st.markdown("<hr style='border: 1px solid #e0e0e0;'>", unsafe_allow_html=True)  # Divider between articles

    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
