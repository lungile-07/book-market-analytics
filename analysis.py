import csv

prices = []

with open('books.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        try:
            prices.append(float(row['Price']))
        except:
            continue

print(f"Total books: {len(prices)}")
print(f"Average price: {sum(prices)/len(prices):.2f}")
print(f"Cheapest: {min(prices)}")
print(f"Most expensive: {max(prices)}")

with open('books.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    cheapest_book = min(rows, key=lambda x: float(x['Price']))
    expensive_book = max(rows, key=lambda x: float(x['Price']))
    print(f"Cheapest book: {cheapest_book['Title']}")
    print(f"Most expensive: {expensive_book['Title']}")