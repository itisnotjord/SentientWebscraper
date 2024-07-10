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
    
    def get_image_url(url):
        response = requests.get(url)
        html_content = response.content
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Find the <meta> tag with property="og:image"
        meta_tag = soup.find('meta', property='og:image')
        
        if meta_tag:
            # Extract the content attribute
            image_url = meta_tag.get('content')
            return image_url
        else:
            return None  # Return None if meta tag not found
    
    texts_with_titles_and_images = []
    links = ["https://cybersecuritynews.com/category/cyber-attack/", "https://cybersecuritynews.com/category/vulnerability/"]  # Insert your URLs here
    for url in links:
        gather_links(url)

    for url in parsed_urls:
        text = get_text(url)
        meta_title = get_meta_title(url)
        image_url = get_image_url(url)
        texts_with_titles_and_images.append({
            'title': meta_title,
            'text': text,
            'image_url': image_url,
            'link': url,
        })

    return texts_with_titles_and_images

# Example usage

