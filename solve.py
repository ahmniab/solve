import requests
from bs4 import BeautifulSoup

def get_page_title(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        page_title_element = soup.find('h4', class_='ml-2 mb-3')
        
        if page_title_element:
            page_title = page_title_element.text.strip()
            return page_title
        else:
            return False
    else:
        return False

# Example usage
url = 'https://www.codewars.com/kata/5263c6999e0f40dee200059d/train/c'
title = get_page_title(url).replace(" ","_")
print(f"{title}")
