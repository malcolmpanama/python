#This program scrapes stocks tickers and thier company name from a website

import requests
import pandas as pd
from bs4 import BeautifulSoup
import string

#Create two empty list for the company name  and the ticker
company_name = []
company_ticker = []

#Create a funcetion to scrape the data
def scrape_stock_symbols(Letter):
    Letter = Letter.upper()
    URL = 'https://www.advfn.com/nyse/newyorkstockexchange.asp?companies='+Letter
    page = requests.get(URL)
    soup = BeautifulSoup(page.text,'html.parser')
    odd_rows = soup.find_all('tr', attrs={'class':'ts0'})
    even_rows = soup.find_all('tr', attrs={'class':'ts1'})

    for i in odd_rows:
        row = i.find_all('td')
        company_name.append(row[0].text.strip()) #Company name
        company_ticker.append(row[1].text.strip()) # Ticker

    for i in even_rows:
        row = i.find_all('td')
        company_name.append(row[0].text.strip()) #Company name
        company_ticker.append(row[1].text.strip()) # Ticker

    return(company_name, company_ticker)

#Loop through every letter in the alphabet to get all of the tickers
#and companies names from the websiste
all_letters = string.ascii_uppercase
for char in all_letters:
    (tname,tticker) = scrape_stock_symbols(char)

#print(*tname, sep = "\n")
#print(*tticker, sep = "\n")
#Create a dataFrame that contains the company name and company ticker
data =pd.DataFrame(columns= ['company_name', 'company_ticker'])
data['company_name'] =tname
data['company_ticker'] =tticker
#Clean the data
data = data[data['company_name'] !='']
#Save as CSV
data.to_csv (r'C:/Users/b_jim/python for finance/export_dataframe.csv', index = False, header=True)

