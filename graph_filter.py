import sqlite3

from webstock_scraper import *
from data_port import *
import matplotlib.pyplot as plt

def filter_crypto_data(symbol = None, name = None):
    conn = sqlite3.connect('Stock_performance.db')
    c = conn.cursor()

    query = "SELECT * FROM Stock_performance"

    conditions = []
    params = []
    if symbol:
        conditions.append("Symbol = ?")
        params.append(symbol)
    if name:
        if ' ' in name:
            name_parts = name.split()
            name_condition = " AND " .join(["Name = ?"] * len(name_parts))
            conditions.append("("+ name_condition+ ")")
            params.extend(name_parts)
        else:
            conditions.append("Name = ?")
            params.append(name)

    if conditions:
        query += " WHERE " + " AND " .join(conditions)

    print("Query:", query)
    print("Params:", params)

    c.execute(query, tuple(params))
    results = c.fetchall()
    print(results)

    conn.close

def data_graph():
    # Open new connection
    conn = sqlite3.connect('Stock_performance.db')
    c = conn.cursor()
    '''
    For reference of table data
    '''
    # c.execute('''CREATE TABLE IF NOT EXISTS Stock_Performance(
        #   ID INTEGER PRIMARY KEY,
        #   Symbol TEXT,
        #   Name TEXT, 
        #   Price_Intraday DECIMAL, 
        #   Change DECIMAL, 
        #   Percent_Change DECIMAL(5,4), 
        #   Market_Cap  TEXT, 
        #   Vol_in_Curr_0000_UTC TEXT,
        #   Vol_in_Curr_24Hr TEXT,
        #   Total_vol_Curr_24Hr TEXT,
        #   Circ_Supply TEXT,
        #   DateTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
        #   ''')
    c.execute("SELECT Symbol, Price_Intraday, DateTime FROM Stock_performance")

    # Extract data into local object.
    data = c.fetchall()

    # Data format
    symbols = []
    prices = []
    dates = []
    for row in data:
        symbols.append(row[1])
        prices.append(row[3])
        dates.append(datetime.strftime(row[11], '%Y-%m-%d %H:%M:%S')) #Formatted date stored in database

    plt.figure(figsize= (12, 8))
    for i, symbol in enumerate(set(symbols)):
        x = [dates[j] for j in range(len(symbols)) if symbols[j] == symbol]
        y = [prices[j] for j in range(len(symbols)) if symbols[j] == symbol]
        plt.plot(x, y, label = symbol)

    plt.xlabel('Date')
    plt.ylabel('Price per crypto')
    plt.title('Price trend over Time')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
# Example usage:

def main():
    filter_crypto_data(symbol="BTC-USD") 
    data_graph() 

# filter_crypto_data(name = "Bitcoin USD")

# Create a JS front end to interface with user. 