# MovieScriptScrapper
## Overview
The MovieScriptScrapper is a Python-based tool designed to scrape movie scripts from the IMSDb website. It fetches details such as the movie title, rating, genres, and the actual script content.

## Features
- Scrape Movie Links: Extracts links to individual movie pages from the main IMSDb page.
- Parse Movie Scripts: Retrieves the actual script content from the individual movie pages.
- Extract Movie Information: Gathers details like the movie title, rating, and genres.
- Save to CSV: After scraping, the scripts and their associated details are saved to a compressed CSV file named scripts.csv.gz.
## Dependencies
- requests: For making HTTP requests to the website.
- BeautifulSoup: For parsing the HTML content of the website.
- pandas: For data manipulation and saving the scraped data to a CSV file.
## Usage
Ensure you have the required dependencies installed.
Run the main.py script.
The script will scrape the movie details and save them to scripts.csv.gz.
