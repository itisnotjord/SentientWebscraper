import requests
from bs4 import BeautifulSoup
import re
import time

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

    def get_image_url_from_url(url):
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            # Fetch the HTML content with headers
            response = requests.get(url, headers=headers)
            
            if response.status_code == 200:
                html_content = response.text
                
                # Parse HTML with BeautifulSoup
                soup = BeautifulSoup(html_content, 'html.parser')
                
                # Find the image URL using regex (or other methods if more complex)
                pattern = re.compile(r'"image":\s*{\s*"@type":\s*"ImageObject",\s*"url":\s*"([^"]+)"')
                match = re.search(pattern, html_content)
                if match:
                    image_url = match.group(1)
                    return image_url
                else:
                    return None
            
            else:
                print(f"Failed to retrieve HTML content. Status code: {response.status_code}")
                return None
        
        except requests.exceptions.RequestException as e:
            print(f"Request exception occurred: {e}")
            return None
        except Exception as e:
            print(f"Error: {e}")
            return None

    def get_article_data(url):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            html_content = response.content
            soup = BeautifulSoup(html_content, 'html.parser')
            
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
            'text': article_text,
            'link': url,
            'image_url': get_image_url_from_url(url)  # Call the image scraping function here
        }

    links = get_urls()
    articles_data = []

    for link in links:
        article_data = get_article_data(link)
        if article_data['image_url']:  # Check if image URL is valid
            articles_data.append(article_data)
        else:
            print(f"Skipping article without valid image URL: {link}")

        # Introduce a delay to avoid rate limiting
        time.sleep(0.8)  # Adjust delay as needed

    return articles_data

