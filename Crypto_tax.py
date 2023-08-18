'''Q1. https://etherscan.io/tx/0xe48a42dc70619677d1db41663896a960ca55c659ad468f705bcd3c7475b11df4 scrape the entire page into excel'''

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Defining the URL
url = "https://etherscan.io/tx/0xe48a42dc70619677d1db41663896a960ca55c659ad468f705bcd3c7475b11df4"

# Sending a GET request to the URL
response = requests.get(url)

# Parsing the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extracting data from the page 
transaction_hash_elem = soup.find("div", {"class": "hash-tag text-truncate"})
transaction_hash = transaction_hash_elem.text.strip() if transaction_hash_elem else "N/A"

from_address_elem = soup.find("span", {"id": "ContentPlaceHolder1_maintxnsrow_2"})
from_address = from_address_elem.text.strip() if from_address_elem else "N/A"

# Creating a DataFrame from the extracted data
data = {
   "Transaction Hash": [transaction_hash],
   "From Address": [from_address]
}
df = pd.DataFrame(data)

# Displaying the DataFrame
print(df)

'''The two files are an excel file and an html file made to also store the data in tabluar as well as html tags form in the respective files'''