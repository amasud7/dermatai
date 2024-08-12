import requests
from bs4 import BeautifulSoup

# base url to start from

baseUrl = 'https://skinsort.com/products'

# user agent for scraper
userAgent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}

# gets html content from url
page = requests.get(baseUrl)
soup = BeautifulSoup(page.content, 'lxml')

# finds all products
productList = soup.find_all('span', class_='text-warm-gray-900 font-bold leading-none mt-1.5 text-lg lg:text-xl lg:hover:underline')

productLinks = [] # list of all the product links

# creating the links for each products 
for product in productList: # goes through every span tag
    for link in product.find_all('a', href=True): # finds all <a> tags in the span
        strip = link['href'].removeprefix('/products') # removing "/products/" from the href
        productLinks.append(baseUrl + strip) # concatenates the base url with the href of the <a> tag for each product





# https://skinsort.com/products (page 1)
# https://skinsort.com/products/page/2 (page 2)
# so need to add "/page/" + page number

# when it has filters applied it doesn't use pages, it scrolls and presses button to scroll more
# https://skinsort.com/products/cleansers-for-dry-skin-oily-skin-and-acne?product_filter%5Border_by%5D=score
# https://skinsort.com/products/products-for-oily-skin-and-acne?product_filter%5Border_by%5D=score











