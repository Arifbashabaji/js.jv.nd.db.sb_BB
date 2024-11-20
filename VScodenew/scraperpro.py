import requests
from bs4 import BeautifulSoup
import openai
import time
from urllib.parse import urljoin
import var

# Create an OpenAI client instance with the API key
client = openai.Client(api_key=var.openaikey)

def get_all_links(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Get all hyperlinks on the page
        links = []
        for a in soup.find_all('a', href=True):
            full_url = urljoin(url, a['href'])  # Handle relative URLs
            links.append(full_url)
        
        return links
    except Exception as e:
        print(f"Error fetching links from {url}: {e}")
        return []

def extract_text_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract text from paragraphs
        paragraphs = soup.find_all('p')
        text = ' '.join([p.get_text() for p in paragraphs])
        
        return text
    except Exception as e:
        print(f"Error extracting text from {url}: {e}")
        return ""

def summarize_text(text):
    try:
        # Using `client.chat.completions.create()` with the updated API interface
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"Please summarize the following text: {text}"}],
            max_tokens=100  # Adjust token limit as needed
        )
        return response.choices[0].message['content']
    except Exception as e:
        print(f"Error summarizing text: {e}")
        return ""

def main(start_url):
    visited = set()
    to_visit = [start_url]
    
    while to_visit:
        current_url = to_visit.pop(0)
        
        if current_url not in visited:
            visited.add(current_url)
            print(f"Visiting: {current_url}")
            
            # Extract links and text
            links = get_all_links(current_url)
            text = extract_text_from_url(current_url)
            
            # Summarize the text if there's any
            if text:
                summary = summarize_text(text)
                print(f"Summary of {current_url}:\n{summary}\n")
            else:
                print(f"No text found for {current_url}\n")
            
            # Add new links to the to_visit list
            for link in links:
                if link.startswith(start_url) and link not in visited:
                    to_visit.append(link)

            # Sleep to avoid overwhelming the server
            time.sleep(1)

if __name__ == "__main__":
    start_url = input("Give me the URL of the website: ")  # Prompt the user for the target website
    main(start_url)
