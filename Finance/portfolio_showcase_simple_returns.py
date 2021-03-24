#Program that showcases daily return, volatility and more
from datetime import datetime
import numpy as np
import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

print("Welcome to your porfolio organizer\n")
#Get the stock symbols for the portfolio for #FAANG
stock_symbols= ["FB", "AMZN", "AAPL", "NFLX", "GOOG"]
#Get the stock starting date
stock_start_date = '2013-01-01'
#Get todays date and fortmat it to the form YYYY-mm-dd
today = datetime.today().strftime('%Y-%m-%d')
print ("Today is: " + str(today))
#Get the numbers of assets in the portfolio
num_assets = len(stock_symbols)
print('You have ' +str(num_assets)+ ' asstes in your portfolio')

#Create function to get the stock prices in the portfolio
def get_my_portfolio(stocks= stock_symbols, start =stock_start_date, end=today, col= 'Adj Close'):
    data = web.DataReader(stocks, data_source='yahoo', start=start, end=end)[col]
    return data
#Get the stocs portfolio Adj, Close price
my_stocks = get_my_portfolio(stock_symbols)
print("The stocks are: \n",my_stocks,'\n')

#Create function to visualize portfolio
def showGraph (stocks= stock_symbols, start =stock_start_date, end=today, col= 'Adj Close'):
    #Create title
    title = 'Portfolio '+col+' Price History'

    #Get the stocks
    my_stocks = get_my_portfolio(stocks = stocks, start = start, end = end, col = col)
    #Give the figure size
    plt.figure(figsize=(12.2,4.5))

    #Loop through each stock and plot the price
    for c in my_stocks.columns.values:
        plt.plot(my_stocks[c], label = c)
    plt.title(title)
    plt.xlabel('Date', fontsize = 18)
    plt.ylabel(col+' Price USD ($)', fontsize = 18)
    plt.legend(my_stocks.columns.values, loc='upper left')
    plt.show()
#Show the adjusted close proce for FAANG
showGraph (stock_symbols)
    
#Calculate the simple returns
daily_simple_returns = my_stocks.pct_change(1)
print('Daily simple returns\n',daily_simple_returns,'\n')
#Calculate the stock correlation
daily_simple_returns.corr()
print('Daily simple stock correlation\n',daily_simple_returns.corr(),'\n')
#Calculate the stock covariance
daily_simple_returns.cov()
print('Daily simple stock variance\n',daily_simple_returns.cov(),'\n')
#Calculate the stock variance
daily_simple_returns.var()
print('Daily simple stock covariance\n',daily_simple_returns.var(),'\n')
#Print the standar deviation for faily simple returns
#print("The stock volatility")
daily_simple_returns.std()
print("Stock Volatility\n",daily_simple_returns.std(),'\n')

#Graph that shows the daily simple return
def show_returns(daily_simple_returns):
    plt.figure(figsize=(12.2,4.5))
    #Loop through each stock and plot the price
    for c in daily_simple_returns.columns.values:
        plt.plot(daily_simple_returns[c], lw=2, label=c)
    plt.legend(loc='upper right', fontsize =10)
    plt.xlabel('Volatility')
    plt.ylabel('Date')
    plt.show()
                   
show_returns(daily_simple_returns)


#Show the mean of the daily simple return
dailyMeanSimpleReturns = daily_simple_returns.mean()
print('Daily Means simple returns')
print(dailyMeanSimpleReturns)

#Calculae the expected porfolio daily reurn
randomWeights = np.array([0.4,0.1,0.3,0.1,0.1])
portfolioSimpleReturn = np.sum(dailyMeanSimpleReturns* randomWeights)
print("Your portfolio expected  daily return is: " +str(portfolioSimpleReturn))
#Get yearly simple return
yearly_simple_return = portfolioSimpleReturn *253
print("Your portfolio Yearly Simple Return is: " +str(yearly_simple_return))
#Calculate growth of the investmens
dailyCumulSimpleReturn = (daily_simple_returns+1).cumprod()
#Visualize the daily cumulative simple returns
def show_cumulative_simple_returns(dailyCumulSimpleReturn):
    plt.figure(figsize=(12.2,4.5))
    #Loop through each stock and plot the price
    for c in dailyCumulSimpleReturn.columns.values:
        plt.plot(dailyCumulSimpleReturn[c], lw=2, label=c)
    plt.legend(loc='upper left', fontsize =10)
    plt.xlabel('Date')
    plt.ylabel('Growth of one dollar investment')
    plt.title("Daily cumulative simple returns")
    plt.show()
      
show_cumulative_simple_returns(dailyCumulSimpleReturn)
