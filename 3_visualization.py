import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('books.csv')

# FIX THE ERROR HERE
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

rating_map = {'One':1, 'Two':2, 'Three':3, 'Four':4, 'Five':5}
df['RatingNum'] = df['Rating'].map(rating_map)

# 1. Price Distribution
plt.figure()
plt.hist(df['Price'], bins=20)
plt.title('Price Distribution - All Catalogue')
plt.xlabel('Price (£)')
plt.ylabel('Number of Books')
plt.savefig('price_distribution.png')
plt.show()

# 2. Avg Price by Rating
plt.figure()
avg_price = df.groupby('RatingNum')['Price'].mean()
avg_price.plot(kind='bar')
plt.title('Average Price by Rating')
plt.xlabel('Rating (1-5)')
plt.ylabel('Average Price (£)')
plt.savefig('price_by_rating.png')
plt.show()

# 3. Price vs Rating
plt.figure()
plt.scatter(df['RatingNum'], df['Price'], alpha=0.5)
plt.title('Price vs Rating')
plt.xlabel('Rating')
plt.ylabel('Price (£)')
plt.savefig('price_vs_rating.png')
plt.show()

print("DONE! All 3 graphs created!")