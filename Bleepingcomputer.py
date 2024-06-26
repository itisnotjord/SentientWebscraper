import requests
from bs4 import BeautifulSoup

def bleepingcomputer():
    def get_urls():
        url = "https://www.bleepingcomputer.com/news/security/"

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            main_content_section = soup.find('section', class_='bc_main_content')
            
            if main_content_section:
                h4_tags = main_content_section.find_all('h4')
                
                links = []
                for h4 in h4_tags:
                    link = h4.find('a')['href']
                    links.append(link)
                
                return links
            else:
                print("Main content section not found.")
        else:
            print("Failed to fetch the webpage. Status code:", response.status_code)

    def get_article_data(url):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract title
            title_tag = soup.find('title')
            if title_tag:
                title = title_tag.text.strip()
            else:
                title = "Title not found"
            
            # Extract article body text
            article_body = soup.find('div', class_='articleBody')
            
            if article_body:
                paragraphs = article_body.find_all(['p', 'h3'])
                article_text = []
                continue_parsing = True
                
                for element in paragraphs:
                    if "Related Articles:" in element.get_text():
                        continue_parsing = False
                        break
                    
                    if continue_parsing:
                        article_text.append(element.get_text().strip())
                
                article_text = " ".join(article_text)
            else:
                article_text = "Article body not found."
        else:
            title = "Failed to fetch the webpage. Status code: " + str(response.status_code)
            article_text = ""

        return {
            'title': title,
            'text': article_text
        }

    links = get_urls()
    articles_data = []

    for link in links:
        article_data = get_article_data(link)
        articles_data.append(article_data)

    return articles_data

# Example usage
