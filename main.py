import requests
from bs4 import BeautifulSoup
import random

# url to scrape. Niger info from France24
URL = "https://www.france24.com/en/tag/niger/" # page decidated to niger. 

# Request the page content, avoid getting flagged as a bot!!! 
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
response = requests.get(URL, headers=headers)


if response.status_code == 200: # if status 200 we can parse, else failed to retrieve the page. 
    # beatifullSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all <a> tags within the div with class m-item-list-article__wrapper [what we are interested in]
    article_links = []
    for wrapper in soup.find_all('div', class_='m-item-list-article__wrapper'):
        a_tag = wrapper.find('a', href=True)
        if a_tag:
            full_link = f"https://www.france24.com{a_tag['href']}"
            article_links.append(full_link)

    # Randomly select 5 links from the list [ news per day ]
    if len(article_links) >= 5:
        random_links = random.sample(article_links, 5)
    else:
        random_links = article_links  # If there are fewer than 5 links

    # Display the selected links
    print("Today's 5 random News from Niger [source:France24] :")
    for i, link in enumerate(random_links, 1):
        print(f"{i}. {link}")
else:
    print(f"Failed to retrieve the Page. Status code: {response.status_code}")