# Book Market Analytics - Consulting App

## Project Description
This project analyzes the book market using web scraping and data analytics to provide business insights for retailers and publishers. It scrapes book data from Books to Scrape website, cleans it, visualizes market trends, and builds a predictive model for book pricing.

## Features
1.  **Web Scraping (scape.py):** Scrapes 1000 books from books.toscrape.com including Title, Price, Rating, and Availability.
2.  **Data Cleaning (analysis.py):** Cleans dataset, converts text ratings to numerical values (One to Five -> 1-5), calculates title length, and handles missing values.
3.  **Visualization (3_visualization.py):** Generates 3 professional graphs:
    - Price Distribution (histogram)
    - Average Price by Rating (bar chart)
    - Price vs Rating relationship (scatter plot)
4.  **Modelling (modelling.py):** Uses Linear Regression to predict Price from Rating and Title Length. Evaluates using R2 Score and MSE.
5.  **Reporting (report.py / professional_report.txt):** Generates a professional consulting report with key insights, model outcomes, and business recommendations.

## Technologies Used
- Python
- Pandas, Matplotlib, Scikit-learn, Requests, BeautifulSoup

# How to Run
1. Install dependencies: `pip install pandas matplotlib scikit-learn requests beautifulsoup4`
2. Run scraper: `python scape.py`
3. Run analysis: `python analysis.py`
4. Run visualization: `python 3_visualization.py`
5. Run model: `python modelling.py`
6. Run report: `python report.py`

#Files in this Folder(book_market_analytics)
- books.csv - Dataset (1000 books)
- scape.py - Web scraping code
- analysis.py - Data cleaning
- 3_visualization.py - Graphs
- modelling.py - Predictive model
- report.py - Report generation
- price_distribution.png, price_by_rating.png, price_vs_rating.png - Graphs
- professional_report.txt
- README.md - This file

#GitHub Repository


# Author
#Lungile Nombulelo Mabombo - Book Market Analytics Project -2026