import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

df = pd.read_csv('books.csv')
rating_map = {'One':1, 'Two':2, 'Three':3, 'Four':4, 'Five':5}
df['RatingNum'] = df['Rating'].map(rating_map)
df['TitleLength'] = df['Title'].apply(lambda x: len(str(x)))

X = df[['RatingNum', 'TitleLength']]
y = df['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
pred = model.predict(X_test)

print(f"Model: Price = {model.intercept_:.2f} + {model.coef_[0]:.2f}*Rating + {model.coef_[1]:.2f}*TitleLength")
print(f"R2 Score: {r2_score(y_test, pred):.3f}")
print(f"MSE: {mean_squared_error(y_test, pred):.2f}")
print("This model can estimate book prices from features")