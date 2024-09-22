import streamlit as st
import yfinance as yf
import ta  # For technical indicators
import pandas as pd

def get_nifty_50_symbols():
    return [
    ("ADANIENT.NS", "Metals & Mining"), 
    ("ADANIPORTS.NS", "Services"), 
    ("APOLLOHOSP.NS", "Healthcare"), 
    ("ASIANPAINT.NS", "Consumer Durables"), 
    ("AXISBANK.NS", "Financial Services"), 
    ("BAJAJ-AUTO.NS", "Automobile and Auto Components"), 
    ("BAJFINANCE.NS", "Financial Services"), 
    ("BAJAJFINSV.NS", "Financial Services"), 
    ("BPCL.NS", "Oil Gas & Consumable Fuels"), 
    ("BHARTIARTL.NS", "Telecommunication"), 
    ("BRITANNIA.NS", "Fast Moving Consumer Goods"), 
    ("CIPLA.NS", "Healthcare"), 
    ("COALINDIA.NS", "Oil Gas & Consumable Fuels"), 
    ("DIVISLAB.NS", "Healthcare"), 
    ("DRREDDY.NS", "Healthcare"), 
    ("EICHERMOT.NS", "Automobile and Auto Components"), 
    ("GRASIM.NS", "Construction Materials"), 
    ("HCLTECH.NS", "Information Technology"), 
    ("HDFCBANK.NS", "Financial Services"), 
    ("HDFCLIFE.NS", "Financial Services"), 
    ("HEROMOTOCO.NS", "Automobile and Auto Components"), 
    ("HINDALCO.NS", "Metals & Mining"), 
    ("HINDUNILVR.NS", "Fast Moving Consumer Goods"), 
    ("ICICIBANK.NS", "Financial Services"), 
    ("ITC.NS", "Fast Moving Consumer Goods"), 
    ("INDUSINDBK.NS", "Financial Services"), 
    ("INFY.NS", "Information Technology"), 
    ("JSWSTEEL.NS", "Metals & Mining"), 
    ("KOTAKBANK.NS", "Financial Services"), 
    ("LTIM.NS", "Information Technology"), 
    ("LT.NS", "Construction"), 
    ("M&M.NS", "Automobile and Auto Components"), 
    ("MARUTI.NS", "Automobile and Auto Components"), 
    ("NTPC.NS", "Power"), 
    ("NESTLEIND.NS", "Fast Moving Consumer Goods"), 
    ("ONGC.NS", "Oil Gas & Consumable Fuels"), 
    ("POWERGRID.NS", "Power"), 
    ("RELIANCE.NS", "Oil Gas & Consumable Fuels"), 
    ("SBILIFE.NS", "Financial Services"), 
    ("SHRIRAMFIN.NS", "Financial Services"), 
    ("SBIN.NS", "Financial Services"), 
    ("SUNPHARMA.NS", "Healthcare"), 
    ("TCS.NS", "Information Technology"), 
    ("TATACONSUM.NS", "Fast Moving Consumer Goods"), 
    ("TATAMOTORS.NS", "Automobile and Auto Components"), 
    ("TATASTEEL.NS", "Metals & Mining"), 
    ("TECHM.NS", "Information Technology"), 
    ("TITAN.NS", "Consumer Durables"), 
    ("ULTRACEMCO.NS", "Construction Materials"), 
    ("WIPRO.NS", "Information Technology")
]


def get_nifty_next_50_symbols():
    return [
    ("ABB.NS", "Capital Goods"),
    ("ADANIENSOL.NS", "Power"),
    ("ADANIGREEN.NS", "Power"),
    ("ADANIPOWER.NS", "Power"),
    ("ATGL.NS", "Oil Gas & Consumable Fuels"),
    ("AMBUJACEM.NS", "Construction Materials"),
    ("DMART.NS", "Consumer Services"),
    ("BAJAJHLDNG.NS", "Financial Services"),
    ("BANKBARODA.NS", "Financial Services"),
    ("BERGEPAINT.NS", "Consumer Durables"),
    ("BEL.NS", "Capital Goods"),
    ("BOSCHLTD.NS", "Automobile and Auto Components"),
    ("CANBK.NS", "Financial Services"),
    ("CHOLAFIN.NS", "Financial Services"),
    ("COLPAL.NS", "Fast Moving Consumer Goods"),
    ("DLF.NS", "Realty"),
    ("DABUR.NS", "Fast Moving Consumer Goods"),
    ("GAIL.NS", "Oil Gas & Consumable Fuels"),
    ("GODREJCP.NS", "Fast Moving Consumer Goods"),
    ("HAVELLS.NS", "Consumer Durables"),
    ("HAL.NS", "Capital Goods"),
    ("ICICIGI.NS", "Financial Services"),
    ("ICICIPRULI.NS", "Financial Services"),
    ("IOC.NS", "Oil Gas & Consumable Fuels"),
    ("IRCTC.NS", "Consumer Services"),
    ("IRFC.NS", "Financial Services"),
    ("NAUKRI.NS", "Consumer Services"),
    ("INDIGO.NS", "Services"),
    ("JINDALSTEL.NS", "Metals & Mining"),
    ("JIOFIN.NS", "Financial Services"),
    ("LICI.NS", "Financial Services"),
    ("MARICO.NS", "Fast Moving Consumer Goods"),
    ("PIDILITIND.NS", "Chemicals"),
    ("PFC.NS", "Financial Services"),
    ("PNB.NS", "Financial Services"),
    ("RECLTD.NS", "Financial Services"),
    ("SBICARD.NS", "Financial Services"),
    ("SRF.NS", "Chemicals"),
    ("MOTHERSON.NS", "Automobile and Auto Components"),
    ("SHREECEM.NS", "Construction Materials"),
    ("SIEMENS.NS", "Capital Goods"),
    ("TVSMOTOR.NS", "Automobile and Auto Components"),
    ("TATAPOWER.NS", "Power"),
    ("TORNTPHARM.NS", "Healthcare"),
    ("TRENT.NS", "Consumer Services"),
    ("UNITDSPR.NS", "Fast Moving Consumer Goods"),
    ("VBL.NS", "Fast Moving Consumer Goods"),
    ("VEDL.NS", "Metals & Mining"),
    ("ZOMATO.NS", "Consumer Services"),
    ("ZYDUSLIFE.NS", "Healthcare")
]


def get_bank_nifty_symbols():
    return [
        ('HDFCBANK.NS',"Financial Services"),
        ('ICICIBANK.NS',"Financial Services"),
        ('AXISBANK.NS',"Financial Services"),
        ('KOTAKBANK.NS',"Financial Services"),
        ('SBIN.NS',"Financial Services"),
        ('INDUSINDBK.NS',"Financial Services"),
        ('BANDHANBNK.NS',"Financial Services"),
        ('IDFCFIRSTB.NS',"Financial Services"),
        ('PNB.NS',"Financial Services"),
        ('BANKBARODA.NS',"Financial Services")
    ]


# Function to calculate technical indicators (RSI, MACD, etc.)
def calculate_indicators(df):
    df['RSI'] = ta.momentum.RSIIndicator(df['Close'], window=14).rsi()
    df['MACD'] = ta.trend.MACD(df['Close']).macd_diff()
    df['SMA_20'] = df['Close'].rolling(window=20).mean()
    df['EMA_20'] = df['Close'].ewm(span=20, adjust=False).mean()
    return df

# Function to calculate technical indicators (RSI, MACD, etc.)
def calculate_indicators(df):
    df['RSI'] = ta.momentum.RSIIndicator(df['Close'], window=14).rsi()
    df['MACD'] = ta.trend.MACD(df['Close']).macd_diff()
    df['SMA_20'] = df['Close'].rolling(window=20).mean()
    df['EMA_20'] = df['Close'].ewm(span=20, adjust=False).mean()
    return df

# Function to detect candlestick patterns
# def detect_candlestick_patterns(data):
#     patterns = {
#         "Hammer": talib.CDLHAMMER(data['Open'], data['High'], data['Low'], data['Close']),
#         "Engulfing Pattern": talib.CDLENGULFING(data['Open'], data['High'], data['Low'], data['Close']),
#         # Add more candlestick patterns if needed
#     }
#     return patterns

# Function to generate clickable links for TradingView
def create_stock_link(symbol):
    base_url = f"https://www.tradingview.com/symbols/{symbol.replace('.NS', '')}/"
    return f'<a href="{base_url}" target="_blank">{symbol}</a>'

def get_stock_data(symbol):
    try:
        # stock = yf.Ticker(symbol)
        # data = stock.history(period="1y")
        stock = yf.Ticker(symbol)
        data = stock.history(period="1mo", interval="1d")
        if data.empty:
            st.warning(f"{symbol}: No data found, symbol may be delisted")
            return None
        return data
    except Exception as e:
        st.warning(f"Error fetching data for {symbol}: {e}")
        return None


# Function to apply font style based on RSI value
def apply_font_style(row):
    rsi_value = row['RSI']
    if rsi_value < 30:
        return f'<span style="color: green;">{row["RSI"]}</span>'  # Entry - green color
    elif rsi_value > 70:
        return f'<span style="color: red;">{row["RSI"]}</span>'  # Exit - red color
    return row["RSI"]  # Default font color for values between 30 and 70


# Function to display stock data with clickable symbols
def display_stock_data(stock_list, title):
    st.subheader(title)
    
    stock_data_list = []
    for stock in stock_list:
        data = get_stock_data(stock[0])
        if data is not None:
            data = calculate_indicators(data)
            current_data = data.iloc[-1]  # Get the latest data
            
            # Detect patterns
            # patterns = detect_candlestick_patterns(data)
            # latest_patterns = {name: patterns[name].iloc[-1] for name in patterns}
            # detected_patterns = [name for name, value in latest_patterns.items() if value != 0]
            
            stock_data = {
                "Symbol": create_stock_link(stock[0]),
                "Industry":stock[1],
                "Current Price": current_data['Close'],
                "Open": current_data['Open'],
                "High": current_data['High'],
                "Low": current_data['Low'],
                "Close": current_data['Close'],
                "Volume": current_data['Volume'],
                "52-Week High": data['High'].max(),
                "52-Week Low": data['Low'].min(),
                "RSI": current_data['RSI'],
                "MACD": current_data['MACD'],
                "SMA (20)": current_data['SMA_20'],
                "EMA (20)": current_data['EMA_20']
                # "Candlestick Patterns": ", ".join(detected_patterns) if detected_patterns else "None"
            }
            
            stock_data_list.append(stock_data)
            
    if stock_data_list:
        df = pd.DataFrame(stock_data_list)
        # Apply font style based on RSI value
        df['RSI'] = df.apply(apply_font_style, axis=1)

    # Render the dataframe with links
    st.write(df.to_html(escape=False), unsafe_allow_html=True)

# Streamlit App Layout
st.title("Stock Dashboard with RSI and Candlestick Patterns")

# Displaying three separate tables for Nifty 50, Nifty Next 50, and Bank Nifty
display_stock_data(get_nifty_50_symbols(), "Nifty 50 Stocks")
display_stock_data(get_nifty_next_50_symbols(), "Nifty Next 50 Stocks")
display_stock_data(get_bank_nifty_symbols(), "Bank Nifty Stocks")

# End of Streamlit App