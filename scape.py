import requests
from bs4 import BeautifulSoup
import csv

base_url = "https://books.toscrape.com/catalogue/page-{}.html"
headers = {"User-Agent": "Mozilla/5.0"}

all_books = []

for page in range(1, 51):
    url = base_url.format(page)
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.find_all('article', class_='product_pod')

    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text.replace('£', '')
        rating = book.find('p', class_='star-rating')['class'][1]
        availability = book.find('p', class_='instock availability').text.strip()
        all_books.append([title, price, rating, availability])

    print(f"Scraped page {page} - Total: {len(all_books)}")

with open('books.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Title', 'Price', 'Rating', 'Availability'])
    writer.writerows(all_books)

print(f"DONE! Total books scraped: {len(all_books)}")

