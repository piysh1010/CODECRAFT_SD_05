import requests
from bs4 import BeautifulSoup
import csv

# URL of the e-commerce site (eBay in this case)
url = "https://www.ebay.com/sch/i.html?_nkw=laptop&_ipg=240"

pip install requests BeautifulSoup pandas

# Send GET request to the website
response = requests.get(url)

# If the request is successful, proceed
if response.status_code == 200:
    # Parse the content using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract product information (name, price, rating) from the page
    products = []
    
    # Find each product listing on the page
    listings = soup.find_all('li', {'class': 's-item'})
    
    for listing in listings:
        name = listing.find('h3', {'class': 's-item__title'})
        price = listing.find('span', {'class': 's-item__price'})
        rating = listing.find('span', {'class': 's-item__reviews'})

        # Extract the text from the HTML elements
        product_name = name.text if name else "N/A"
        product_price = price.text if price else "N/A"
        product_rating = rating.text if rating else "N/A"
        
        # Store product details in a list
        products.append([product_name, product_price, product_rating])

    # Write the extracted data to a CSV file
    with open("ebay_products.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(["Product Name", "Price", "Rating"])
        # Write each product's details
        writer.writerows(products)
    
    print("Product data has been written to ebay_products.csv")

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
