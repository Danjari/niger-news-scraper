# Niger News Scraper

## Description

This project is a web scraper designed to fetch the latest news about Niger from France24's English website. It randomly selects five recent articles about Niger, providing users with a quick overview of current events in the country.

### Data Uncovered

The scraper extracts:
- Links to recent news articles about Niger from France24
- Article titles (indirectly, through the links)

### Purpose

The purpose of this scraper is to:
1. Provide easy access to current news about Niger from a reputable international source
2. Offer a randomized selection of articles to give a broad overview of recent events
3. Automate the process of checking for news updates about Niger

## Website Choice

The scraper targets [France24's Niger tag page](https://www.france24.com/en/tag/niger/).

Reasons for choosing this website:
1. France24 is a reputable international news source
2. It provides regular updates on Niger, a country that might not receive extensive coverage in other international media and where I was born
3. The website structure is suitable for scraping, with clearly defined article sections
4. And no mention of Robots in the terms in use. 

## Installation and Usage

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/danjari/niger-news-scraper.git
   cd niger-news-scraper
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

### Usage

Run the script using Python:

```
python main.py
```

The script will output links to five randomly selected recent articles about Niger from France24.

## Code Overview

The script does the following:
1. Sends a GET request to the France24 Niger tag page
2. Parses the HTML content using BeautifulSoup
3. Extracts links to articles from the parsed HTML
4. Randomly selects 5 articles (or all articles if fewer than 5 are available)
5. Prints the selected article links

## Ethical Considerations

- The script uses a custom User-Agent to identify itself
- The scraper is designed for personal use and should not be used to republish content without permission

## Dependencies

- requests
- beautifulsoup4


These can be installed using the provided `requirements.txt` file.

## Disclaimer

This project is for educational purposes only. Users should respect France24's terms of service and copyright when using this tool.

