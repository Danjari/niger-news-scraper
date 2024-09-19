# Ethical Considerations for Niger News Scraper

This document outlines the ethical considerations taken into account in the development and use of the Niger News Scraper project.

## Purpose of Data Collection

### Why are we collecting this data?

The Niger News Scraper collects links to news articles about Niger from France24 for the following purposes:

1. To provide easy access to current news about Niger from a reputable international source.
2. To offer a randomized selection of articles, giving users a broad overview of recent events in Niger.
3. To facilitate research and stay informed about events in Niger, a country that might not receive extensive coverage in other international media.

The primary goal is educational and informational, aimed at personal use or academic research.

Data Sources and robots.txt
Respecting website terms and robots.txt

We have chosen to scrape France24 (https://www.france24.com) as it does not explicitly prohibit scraping in its robots.txt file for most user agents.
We have thoroughly reviewed the robots.txt file (https://www.france24.com/robots.txt) to ensure our scraping activities are permitted.
Our scraper respects the directives in the robots.txt file:

We do not access any disallowed areas, particularly the urgent content section (*/_ws/urgent).
Our scraper does not use any of the user agents listed as disallowed in the robots.txt file.
We implement a crawl delay of at least 10 seconds between requests to respect the site's resources, even though this isn't explicitly required for general user agents.



Collection Practices
Limiting scraping to avoid disruption

Our scraper is designed to make a single request per run, minimizing the load on France24's servers.
We implement a delay of at least 10 seconds between requests if multiple requests are made in succession, adhering to the strictest crawl-delay specified in the robots.txt file.
We use a custom User-Agent to identify our scraper, allowing the website to track our activities if needed. Our User-Agent is not listed among the disallowed bots in the robots.txt file.

### Not bypassing password protection

1. Our scraper only accesses publicly available content on France24.
2. We do not attempt to bypass any form of authentication or access restricted areas of the website.

## Data Handling and Privacy

### Not collecting Personally Identifiable Information (PII)

1. Our scraper only collects links to news articles and their titles.
2. We do not collect any user data, comments, or other potentially sensitive information.

### Secure data storage

1. The scraped data is not permanently stored; it's only displayed in the console during script execution.
2. If future versions of the project involve data storage, we will:
   - Add any data files to .gitignore to prevent accidental sharing.
   - Implement secure storage practices appropriate to the sensitivity of the data.

## Data Usage

### Educational and research purposes only

1. The data collected by this scraper is intended for personal educational use or academic research only.
2. We do not use the collected data for commercial purposes.
3. We do not republish or distribute the content of the articles, only the links to them.

## Transparency and Attribution

1. We clearly attribute France24 as the source of the news articles.
2. Our README.md file explicitly states the purpose of the scraper and its data source.

Compliance and Updating

We commit to regularly reviewing these ethical guidelines and updating our practices as necessary.
We will promptly address any concerns raised by France24 or other stakeholders regarding our scraping activities.
We will periodically check the robots.txt file for any changes and adjust our scraping behavior accordingly.

