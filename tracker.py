#TODO: 
# 1 Import necessary libraries (csv, datetime)
# 2 Define the product_data dictionary with product IDs, names, and unit prices
# 3 Read the "product_sales.txt" file and store the product IDs in a list
# 4 Loop through the list of product ID's
# 5 Appdn lists containing the data points for each product ID to a "list of lists"
   # 5.1 Create a current_date variaable outside of the loop and set it equal to today
   # 5.2 Create a counter variable outside the loop, and set it to 1
   # 5.3 Strip the newline chracters off the end of the product IDs, and fetch...
   
import csv
import datetime

product_data = {
    "P001": ["Wireless Headphones", 100],
    "P002": ["Laptop Backpack", 60],
    "P003": ["Bluetooth Speaker", 50],
    "P004": ["USB Flash Drive", 20],
    "P005": ["Mobile Phone Case", 15],
    "P006": ["Wireless Mouse", 30],
    "P007": ["Laptop Stand", 40],
    "P008": ["HDMI Cable", 15],
    "P009": ["Smartphone", 600],
    "P010": ["External Hard Drive", 100],
}

