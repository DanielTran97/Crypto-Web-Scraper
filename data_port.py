import sqlite3
from webstock_scraper import *

conn = sqlite3.connect('Stock_performance.db')
c = conn.cursor()

# Database already created

c.execute('''CREATE TABLE IF NOT EXISTS Stock_Performance(
          ID INTEGER PRIMARY KEY,
          Symbol TEXT,
          Name TEXT, 
          Price_Intraday DECIMAL, 
          Change DECIMAL, 
          Percent_Change DECIMAL(5,4), 
          Market_Cap  TEXT, 
          Vol_in_Curr_0000_UTC TEXT,
          Vol_in_Curr_24Hr TEXT,
          Total_vol_Curr_24Hr TEXT,
          Circ_Supply TEXT,
          DateTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
          ''')

for data in crypto_scrape_data:
    c.execute('''INSERT INTO Stock_Performance (Symbol, Name, Price_Intraday, Change, Percent_Change, Market_Cap, Vol_in_Curr_0000_UTC, Vol_in_Curr_24Hr, Total_vol_Curr_24Hr, Circ_Supply, DateTime) 
              VALUES(?,?,?,?,?,?,?,?,?,?,?)''',(data['item_selector'], 
                                                data['name_selector'], 
                                                data['price_selector'], 
                                                data['change_selector'],
                                                data['changePercentage_selector'],
                                                data['marketCap_selector'],
                                                data['Vol_InCurrencyUTC_selector'],
                                                data['Vol_InCurrencyHour_selector'],
                                                data['TotalVol_InCurrencyHour_selector'],
                                                data['Circul_Supply_selector'],
                                                data['DateTime']))

# conn.commit()

# conn.close()

c.execute('''SELECT * FROM Stock_Performance''')
results = c.fetchall()
print(results)

# c.execute('''DELETE FROM Stock_Performance''')

conn.close()

# STEP 1: FILTER DATA BY CRYPTO NAME OR TYPE (SQLITE)
# RESULTS: DONE

# STEP 2: FORMULATE PERFORMANCE GRAPH OF DATA'S CAPTURED WEEKLY BASED OFF STEP 1 (MACHINE LEARNING)


# STEP 3: PERFORM DATA ANALYSIS ON EACH CRYPTO'S DATA BASED OFF WEEKLY PERFORMANCES (MACHINE LEARNING)

