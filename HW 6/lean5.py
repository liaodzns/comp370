def load(file_path):
    pass

def sum_sales(book_sales, game_sales):
    pass

# get all the sales data by product type 
book_sales_2022 = load("data/book_sales_2022.csv") 
book_sales_2023 = load("data/book_sales_2023.csv") 
book_sales_2024 = load("data/book_sales_2024.csv") 
 
game_sales_2022 = load("data/game_sales_2022.csv") 
game_sales_2023 = load("data/game_sales_2023.csv") 
game_sales_2024 = load("data/game_sales_2024.csv") 
 
# calculate the total sales for each year 
total_sales_2022 = sum_sales(book_sales_2022, game_sales_2022) 
total_sales_2023 = sum_sales(book_sales_2023, game_sales_2023) 
total_sales_2024 = sum_sales(book_sales_2024, game_sales_2024)


# Practice again for midterm:

years = [2022, 2023, 2024]
products = [ 'book', 'game']
sales_data = {}

for product in products: 
    sales_data[product] = {}
    for year in years:
        file_name = f'data/{product}_sales_{year}.csv'
        sales_data[product][year] = load(file_name)

total_sales = {}
for year in years:
    total_sales[year] = sum_sales(sales_data['book'][year], sales_data['game'][year])


# Refactored code:

years = [2022, 2023, 2024]
product_types = ['book', 'game']

sales_data = {}
for product in product_types:
    sales_data[product] = {}
    for year in years:
        file_path = f"data/{product}_sales_{year}.csv"
        sales_data[product][year] = load(file_path)

# total sales for each year
total_sales = {}
for year in years:
    total_sales[year] = sum_sales(sales_data['book'][year], sales_data['game'][year])
