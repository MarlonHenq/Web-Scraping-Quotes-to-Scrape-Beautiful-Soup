from bs4 import BeautifulSoup
import requests

# URL of the page we want to scrape
url = 'https://quotes.toscrape.com/page/'

initial_page = 1;
end_page = 10;

author = "Albert Einstein"

quotes = []

# Loop through the pages
for page in range(initial_page, end_page):
    
    # Get the HTML content
    response = requests.get(url + str(page))

    # Create a BeautifulSoup object
    soup = BeautifulSoup(response.text, 'html.parser')

    # Get the quotes
    page_quotes = soup.find_all('div', class_='quote')

    # Verify if the author is in the quote and save it
    for quote in page_quotes:
        if (quote.find('small', class_='author').text == author):
            quote_text = quote.find('span', class_='text').text

            quotes.append(quote_text)
            print("Quote found: " + quote_text)
    

print("Number of quotes: " + str(len(quotes)))