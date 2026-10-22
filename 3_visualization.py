import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('books.csv')

df['Price'] = df['Price'].astype(str).str.replace('£', '', regex=False).str.replace('Â', '', regex=False)
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
df = df.dropna(subset=['Price'])

plt.figure()
plt.hist(df['Price'], bins=20)
plt.title('Price Distribution')
plt.xlabel('Price (£)')
plt.ylabel('Frequency')
plt.savefig('price_distribution.png')
plt.show()

plt.figure()
df.boxplot(column='Price', by='Rating')
plt.title('Price by Rating')
plt.xlabel('Rating')
plt.ylabel('Price (£)')
plt.savefig('price_by_rating.png')
plt.show()

plt.figure()
plt.scatter(df['Rating'], df['Price'])
plt.title('Price vs Rating')
plt.xlabel('Rating')
plt.ylabel('Price (£)')
plt.savefig('price_vs_rating.png')
plt.show()

print('DONE! All 3 graphs created!')