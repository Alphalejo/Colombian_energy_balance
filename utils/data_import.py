import pandas as pd

# Natural Gas Production
raw_gas_production_df = pd.read_csv("https://ourworldindata.org/grapher/gas-production-by-country.csv?v=1&csvType=filtered&useColumnShortNames=true&time=earliest..2024&country=~COL&overlay=download-data", storage_options = {'User-Agent': 'Our World In Data data fetch/1.0'})

# Natural Gas Consumption
raw_gas_consumption_df = pd.read_csv("https://ourworldindata.org/grapher/gas-consumption-by-country.csv?v=1&csvType=filtered&useColumnShortNames=true&tab=line&country=~COL&mapSelect=~COL&overlay=download-data", storage_options = {'User-Agent': 'Our World In Data data fetch/1.0'})

# Natural Gas Trade (bcf)
raw_gas_trade_df = pd.read_csv("./data/raw/INT-Export-10-21-2025_21-19-22.csv", skiprows=1)
