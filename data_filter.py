import sqlite3

from webstock_scraper import *
from data_port import *

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

# Example usage:
filter_crypto_data(symbol="BTC-USD")

# filter_crypto_data(name = "Bitcoin USD")