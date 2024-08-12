import requests
from bs4 import BeautifulSoup

# base url to start from
baseUrl = 'https://skinsort.com/products'

# user agent for scraper
userAgent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}

# gets html content from url
r = requests.get(baseUrl)
soup = BeautifulSoup(r.content, 'lxml')

# finds all products
productList = soup.find_all('span', class_='text-warm-gray-900 font-bold leading-none mt-1.5 text-lg lg:text-xl lg:hover:underline')

# crreating product links
for product in productList: # goes through every span tag
    for link in product.find_all('a', href=True): # finds all <a> tags in the span
        print(link['href']) # prints out the link associated with the <a> tag






