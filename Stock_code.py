import pandas as pd
import numpy as np
from nsepy import get_history, get_index_pe_history
from datetime import date
import matplotlib.pyplot as plt
import datetime
import yfinance as yf
import calendar
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR

def findDay(date):
    day = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    return (calendar.day_name[day])

class stock:
    def __init__(self, ticker):
        self.ticker = ticker
        self.data = yf.download(tickers=self.ticker)  # to download real-time data
        self.datayf = self.data.reset_index(level=0)
        self.start_date = min(self.data['Date'])  # ipo start date
        self.end_date = max(self.data['Date'])  # public for today

    def basic_details(self):
        plt.plot(self.data['Date'], self.data['Close'], color='green', linewidth=3)
        plt.xlabel('Date')
        plt.ylabel('Close (In Rs)')
        plt.title("Stock History " % self.ticker)
        plt.show()
        print("The min price is %f " % min(self.data['Low']))
        print("The max price is %f " % max(self.data['High']))

    def min_price(self):
        return min(self.data['Low'])

    def max_price(self):
        return max(self.data['High'])

    def pe_value(self, date1=date.today()):  # profit-loss value
    nifty_pe = get_index_pe_history(symbol=self.ticker, start=self.start_date, end=date1)
    nifty_pe = nifty_pe.reset_index(level=0)
    for i in range(0, nifty_pe['P/E'].count()):
        if nifty_pe['P/E'][i] != 'P/E':
            pe = nifty_pe['P/E'][i]
            div_yield = nifty_pe['Div Yield'][i]
    print("P/E=%f" % pe + "P/Dic Yield:" % div_yield)
    print("P/E:%f" % pe + "Div Yield:" % div_yield)

def realtime_details(self, period='5d'):
    datayf = yf.download(tickers=self.ticker, period=period, interval='1m')
    plt.style.context('ggplot')
    plt.figure(figsize=(15, 8))
    plt.plot(datayf['Close'], color='green', linewidth=3)
    plt.xlabel('Date')
    plt.ylabel('Close (In Rs)')
    plt.title("Stock History " % self.ticker)
    plt.show()
    print("The min price is %f " % min(datayf['Low']))
    print("The max price is %f " % max(datayf['High']))

def other_details(self):
    datayf.Ticker(self.ticker)
    choice = input("Enter your choice \n 1)Dividends \n 2)Splits \n 3)Financials \n 4)Major Share Holders\n5)Balance Sheet \n6)Earnings \n7)Analysts Recommendations)")

    if choice == 1:
        print(datayf.dividends)  # stock share per person
    elif choice == 2:
        print(datayf.splits)  # SHARES
    elif choice == 3:
        print(datayf.shares)  # No. of shares
    elif choice == 4:
        print(datayf.major_holders)  # the one who bought the maximum shares on a particular stock
    elif choice == 5:
        print(datayf.balance_sheet)  # analyzing the stock shares profits in loss details, spend details
    elif choice == 6:
        print(datayf.earnings)
    elif choice == 7:
        print(datayf.recommendations)
# Applying Multi Linear Regression Algorithm

# Initialize variables
init_range = 0.1
weights = np.random.uniform(-init_range, init_range, size=(6, 1))
biases = np.random.uniform(-init_range, init_range, size=1)
learning_rate = 0.02

# Calculate the number of observations
observations = int(np.size(training_X, 0))

# Training loop for 100 iterations
for i in range(100):
    # Calculate the predicted outputs
    outputs = np.dot(training_X, weights) + biases

    # Calculate the difference between predicted and actual values
    deltas = outputs - training_Y

    # Calculate the loss (Mean Squared Error)
    loss = np.sum(deltas**2) / 2 / observations

    # Calculate the scaled deltas for updating weights
    deltas_scaled = deltas / observations

    # Update weights and biases using gradient descent
    weights = weights - learning_rate * np.dot(training_X.T, deltas_scaled)
    biases = biases - learning_rate * np.sum(deltas_scaled)

# Store the final loss value
mlr_loss = loss

# Make predictions on the test set
y_pred = np.dot(Test_X, weights) + biases

# Convert predictions to a JSON format
predictionResult = pd.Series(y_pred.flatten()).to_json(orient='values')

﻿

else:
confidence=str(Ir_confidence*100)
predicted_data=pd.dataFrame(svm_prediction, Nextdate) confidence-str(svm_confidence*100)
print("The prediction data for next "+ str(days)+" is given in the below table") print(predicted_data)
print("The data provided in the above table is "+confidence+" percent accurate") plt.style.context(['ggplot'])
plt.figure(figsize=(15,6))
plt.plot(predicted_data)
plt.xlabel('Date')
plt.ylabel('Predicted Amount')
plt.title("%s Stock Analytics" % self.ticker)
plt.show()
ticker=input("Enter the Stock Name")
print("The Realtime details of the "+ticker+" is given below") stock_details=stock(ticker)
stock_details.realtime_details()
choice=int(input("Enter the choice: \n 1)Basic details of the stock \n 2)Minimum price \n3) Maximum price \n4)P/E value \n5)Real Time data\n6)other Details\n7)Predict))
while choice>e and choice<8:
if choice==1:
stock_details.basic_details()
elif choice==2:
stock_details.min_price()
elif choice ==3:
stock_details.max_price()
elif choice==4:
stock_details.pe_value()
elif choice==5:
stock_details.realtime_details()
elif choice==6:
stock_deatils.other_details()
elif choice == 7:
days=int(input("Enter the number of days"))
stock_details.predict(days)
choice=int(input("Enter the choice: \n 1)Basic details of the stock \n 2)Minimum price \n3) Maximum price \
\n4)P/E value \n5)Real Time data \n6)Other Details"))
    