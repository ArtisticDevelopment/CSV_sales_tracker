#TODO: 
# 1 Import necessary libraries (csv, datetime)
# 2 Define the product_data dictionary with product IDs, names, and unit prices
# 3 Read the "product_sales.txt" file and store the product IDs in a list
# 4 Loop through the list of product ID's
# 5 Append lists containing the data points for each product ID to a "list of lists"
   # 5.1 Create a current_date variaable outside of the loop and set it equal to today
   # 5.2 Create a counter variable outside the loop, and set it to 1
   # 5.3 Strip the newline chracters off the end of the product IDs, and fetch...
   
import csv
import datetime

#product number matches (object literal)
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

#empty csv list
csv_data = []

#opens file in read mode(immutable) to collect product_ids
#"with as" will close the file after exiting block
with open('product_sales.txt', 'r') as file:
  product_ids = file.readlines()
  
#duh 
current_date = datetime.date.today()

#loop through product_ids, match against product_data
#extract product_name&price and set to variables
for sale_id, product_id in enumerate(product_ids, start=1):
  product_id = product_id.strip()
  product_name = product_data[product_id][0]
  product_price = product_data[product_id][1]
  
  #row template,prepping for entry to csv file
  row = [current_date, sale_id, product_id, product_name, f"${product_price}"]
  #initially empty list appends rows
  csv_data.append(row)

  
with open('product_sales.csv', 'w', newline ='') as csv_file:
  csv_writer = csv.writer(csv_file)
  #writerow sets the header, writerows sets the data afterwords
  csv_writer.writerow(['current date', 'sale_id', 'product_id', 'product_name', 'product_price'])
  csv_writer.writerows(csv_data)