import numpy as np
import pandas as pd
import pandas_datareader as pdr

# -----------------------
# SMI20 (yahoo) tickers
smi = ['SGSN.SW','SCMN.SW','GIVN.SW','ZURN.SW','NOVN.SW',
          'ROG.SW','CSGN.SW','LHN.SW','ABBN.SW','UHR.SW',
          'LONN.SW','SLHN.SW','PGHN.SW','GEBN.SW','NESN.SW',
          'SREN.SW','CFR.SW','UBSG.SW','SIKA.SW','ALC.SW']

# Names of those SMI firms
smi_names = ['SGS','Swisscom','Givaudan','Zurich Insurance Group','Novartis',
         'Roche','Credit Suisse','LafargeHolcim','ABB','Swatch Group',
         'Lonza','Swiss Life Holding','Partners Group','Geberit','Nestle',
         'Swiss Re','Richemont','UBS','Sika','Alcon']

# more_ticks = ['ADEN.SW','BAER.SW','CLN.SW','GIVN.SW','KNIN.SW','SOON.SW']
# more_names = ['Adecco Group','Julius Bär','Clariant','Givaudan','Kuehne + Nagel International','Sonova']

# -----------------------
def get_prices(ticks):
    prices = []
    for i in ticks:
        try:
            closing_price = pdr.DataReader(i,data_source='yahoo').iloc[:,-1]
            prices.append(closing_price)
        except KeyError:
            pass
    prices = pd.concat(prices,axis=1)
    return prices

def get_volumes(ticks):
    volumes = []
    for i in ticks:
        try:
            vol = pdr.DataReader(i,data_source='yahoo').iloc[:,-2]
            volumes.append(vol)
        except KeyError:
            pass
    volumes = pd.concat(volumes,axis=1)
    return volumes

# -----------------------
# SMI stocks prices - last 5 years
smi_prices = get_prices(smi)
smi_prices.columns = smi_names
# SMI stocks volumes - last 5 years
smi_volumes = get_volumes(smi)
smi_volumes.columns = smi_names

# --> For Alcon the data starts from 8th April 2019

# Swiss Market Index - Aggregate
smi20_prices = pdr.DataReader('^SSMI','yahoo').iloc[:,-1]
smi20_prices.name = 'SMI20' 
# SP500 Index
sp500_prices = pdr.DataReader('^GSPC','yahoo').iloc[:,-1]
sp500_prices.name = 'SP500' 

# -----------------------
# Export the data
smi_prices.to_csv('data/smi_prices.csv')
smi_volumes.to_csv('data/smi_volumes.csv')
smi20_prices.to_csv('data/smi_index_prices.csv')
sp500_prices.to_csv('data/sp500_index_prices.csv')
