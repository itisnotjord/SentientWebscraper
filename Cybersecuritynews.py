import requests
from bs4 import BeautifulSoup


def cybersecurity():
    parsed_urls = []
    
    def gather_links(link):
        url = link
        response = requests.get(url)
        html_content = response.content
        soup = BeautifulSoup(html_content, 'html.parser')
        divs = soup.find_all('div', class_='td-read-more')
        links = []
        for div in divs:
            a_tag = div.find('a')
            if a_tag and 'href' in a_tag.attrs:
                links.append(a_tag['href'])
        for link in links:
            parsed_urls.append(link)

    def get_text(link):
        url = link
        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")
        result = doc.find_all("p")
        paragraph_texts = [p.get_text() for p in result]
        all_paragraph_text = ' '.join(paragraph_texts)
        return all_paragraph_text
    
    def get_meta_title(url):
        response = requests.get(url)
        html_content = response.content
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Find all meta tags
        meta_tags = soup.find_all('meta')
        
        # Search for meta tag with property="og:title"
        for tag in meta_tags:
            if tag.get('property') == 'og:title':
                return tag.get('content')
        
        return None  # Return None if meta tag not found
    
    texts_with_titles = []
    links = ["https://cybersecuritynews.com/category/cyber-attack/"]  # Insert your URLs here
    for url in links:
        gather_links(url)

    for url in parsed_urls:
        text = get_text(url)
        meta_title = get_meta_title(url)
        texts_with_titles.append({
            'title': meta_title,
            'text': text
        })

    return texts_with_titles

# Example usage
