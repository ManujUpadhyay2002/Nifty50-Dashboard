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
        ('HDFCBANK.NS', "Financial Services"),
        ('ICICIBANK.NS', "Financial Services"),
        ('AXISBANK.NS', "Financial Services"),
        ('KOTAKBANK.NS', "Financial Services"),
        ('SBIN.NS', "Financial Services"),
        ('INDUSINDBK.NS', "Financial Services"),
        ('BANDHANBNK.NS', "Financial Services"),
        ('IDFCFIRSTB.NS', "Financial Services"),
        ('PNB.NS', "Financial Services"),
        ('BANKBARODA.NS', "Financial Services")
    ]


# Function to calculate technical indicators (RSI, MACD, etc.)
def calculate_indicators(symbol,df):
    df = detect_macd_crossover(symbol,df)
    df['RSI'] = ta.momentum.RSIIndicator(df['Close'], window=14).rsi()
    df['SMA_20'] = df['Close'].rolling(window=20).mean()
    df['EMA_20'] = df['Close'].ewm(span=20, adjust=False).mean()
    df['Volume_Trend_Daily'] = detect_volume_trend(df, window=20, threshold=1.5)
    df['Volume_Trend_Weekly'] = detect_weekly_volume_trend(symbol, window=5, threshold=1.5)
    return df


def create_stock_link(symbol):
    base_url = f"https://www.tradingview.com/symbols/{symbol.replace('.NS', '')}/"
    return f'<a href="{base_url}" target="_blank">{symbol}</a>'


def get_stock_data(symbol):
    try:
        stock = yf.Ticker(symbol)
        data = stock.history(period="1y")
        # stock = yf.Ticker(symbol)
        # data = stock.history(period="1mo", interval="1d")
        if data.empty:
            st.warning(f"{symbol}: No data found, symbol may be delisted")
            return None
        return data
    except Exception as e:
        st.warning(f"Error fetching data for {symbol}: {e}")
        return None

# Function to apply font style based on RSI value
def apply_font_style(row):
    rsi_value = row['RSI_Daily']
    if rsi_value < 30:
        # Entry - green color
        return f'<span style="color: green;">{row["RSI_Daily"]}</span>'
    elif rsi_value > 70:
        # Exit - red color
        return f'<span style="color: red;">{row["RSI_Daily"]}</span>'
    return row["RSI_Daily"]  # Default font color for values between 30 and 70


def apply_weekly_rsi_font_style(row):
    rsi_value = row['RSI_Weekly']
    if rsi_value < 30:
        # Entry - green color
        return f'<span style="color: green;">{row["RSI_Weekly"]}</span>'
    elif rsi_value > 70:
        # Exit - red color
        return f'<span style="color: red;">{row["RSI_Weekly"]}</span>'
    return row["RSI_Weekly"]

def apply_macd_font_style(row):
    macd_value = row['MACD Crossover']
    if macd_value == "Bullish Crossover":
        # Entry - green color
        return f'<span style="color: green;">{row["MACD Crossover"]}</span>'
    elif macd_value == "Bearish Crossover":
        # Exit - red color
        return f'<span style="color: red;">{row["MACD Crossover"]}</span>'
    return row['MACD Crossover']

# Function to detect daily volume trend
def detect_volume_trend(df, window=10, threshold=1.5):
    df = df.copy()
    df['Volume_Avg'] = df['Volume'].rolling(window=window).mean()
    latest_volume = df['Volume'].iloc[-1]
    avg_volume = df['Volume_Avg'].iloc[-1]
    
    if avg_volume == 0:
        return "Normal Volume"
    
    if latest_volume > avg_volume * threshold:
        return "Increasing Volume"
    elif latest_volume < avg_volume / threshold:
        return "Decreasing Volume"
    else:
        return "Normal Volume"

# Function to detect weekly volume trend
def detect_weekly_volume_trend(symbol, window=10, threshold=1.5):
    stock = yf.Ticker(symbol)
    data_weekly = stock.history(period="1y", interval="1wk")
    if data_weekly.empty:
        return "Normal Volume"
    avg_volume = data_weekly['Volume'].rolling(window=window).mean().iloc[-1]
    latest_volume = data_weekly['Volume'].iloc[-1]
    
    if avg_volume == 0:
        return "Normal Volume"
    
    if latest_volume > avg_volume * threshold:
        return "Increasing Volume"
    elif latest_volume < avg_volume / threshold:
        return "Decreasing Volume"
    else:
        return "Normal Volume"

# Function to apply font style based on Volume Trend
def apply_volume_trend_font_style(row, trend_column):
    trend = row[trend_column]
    if trend == "Increasing Volume":
        return f'<span style="color: green;">{trend}</span>'
    elif trend == "Decreasing Volume":
        return f'<span style="color: red;">{trend}</span>'
    return trend  # Normal Volume

def identify_candlestick_patterns(symbol,data):
    stock = yf.Ticker(symbol)
    data_weekly = stock.history(period="1y", interval="1wk")
    
    # Bullish Engulfing Pattern
    data["Bullish_Engulfing"] = int(
        (data_weekly['Open'].shift(1).iloc[-1] > data_weekly['Close'].shift(1).iloc[-1]) and
        (data_weekly['Open'].iloc[-1] < data_weekly['Close'].iloc[-1]) and
        (data_weekly['Open'].iloc[-1] < data_weekly['Close'].shift(1).iloc[-1]) and
        (data_weekly['Close'].iloc[-1] > data_weekly['Open'].shift(1).iloc[-1])
    )

    # Bearish Engulfing Pattern
    data["Bearish_Engulfing"] = int(
        (data_weekly['Open'].shift(1).iloc[-1] < data_weekly['Close'].shift(1).iloc[-1]) and
        (data_weekly['Open'].iloc[-1] > data_weekly['Close'].iloc[-1]) and
        (data_weekly['Open'].iloc[-1] > data_weekly['Close'].shift(1).iloc[-1]) and
        (data_weekly['Close'].iloc[-1] < data_weekly['Open'].shift(1).iloc[-1])
    )

    # Doji Pattern
    data["Doji"] = int(abs(data_weekly['Open'].iloc[-1] - data_weekly['Close'].iloc[-1]) < (data_weekly['High'].iloc[-1] - data_weekly['Low'].iloc[-1]) * 0.1)

    # Hammer Pattern
    data["Hammer"] = int(
        (data_weekly['Close'].iloc[-1] > data_weekly['Open'].iloc[-1]) and
        ((data_weekly['Low'].iloc[-1] - data_weekly['Open'].iloc[-1]) > 2 * abs(data_weekly['Open'].iloc[-1] - data_weekly['Close'].iloc[-1])) and
        (abs(data_weekly['High'].iloc[-1] - data_weekly['Close'].iloc[-1]) < 0.1 * abs(data_weekly['Open'].iloc[-1] - data_weekly['Low'].iloc[-1]))
    )
    
    # Inverted Hammer Pattern
    data["Inverted_Hammer"] = int(
        (data_weekly['Close'].iloc[-1] > data_weekly['Open'].iloc[-1]) and
        ((data_weekly['High'].iloc[-1] - data_weekly['Close'].iloc[-1]) > 2 * abs(data_weekly['Open'].iloc[-1] - data_weekly['Close'].iloc[-1])) and
        (abs(data_weekly['Low'].iloc[-1] - data_weekly['Open'].iloc[-1]) < 0.1 * abs(data_weekly['High'].iloc[-1] - data_weekly['Close'].iloc[-1]))
    )
    
    # Shooting Star Pattern
    data["Shooting_Star"] = int(
        (data_weekly['Open'].iloc[-1] > data_weekly['Close'].iloc[-1]) and
        ((data_weekly['High'].iloc[-1] - data_weekly['Open'].iloc[-1]) > 2 * abs(data_weekly['Open'].iloc[-1] - data_weekly['Close'].iloc[-1])) and
        (abs(data_weekly['Low'].iloc[-1] - data_weekly['Close'].iloc[-1]) < 0.1 * abs(data_weekly['High'].iloc[-1] - data_weekly['Close'].iloc[-1]))
    )

    # Morning Star Pattern (3 candles)
    data["Morning_Star"] = int(
        (data_weekly['Close'].shift(2).iloc[-1] > data_weekly['Open'].shift(2).iloc[-1]) and  # First candle is bullish
        (data_weekly['Close'].shift(1).iloc[-1] < data_weekly['Open'].shift(1).iloc[-1]) and  # Second candle is bearish
        (data_weekly['Open'].iloc[-1] < data_weekly['Close'].shift(1).iloc[-1]) and  # Third candle opens above second
        (data_weekly['Close'].iloc[-1] > data_weekly['Open'].iloc[-1]) and  # Third candle is bullish
        (data_weekly['Close'].iloc[-1] > (data_weekly['Close'].shift(2).iloc[-1] + data_weekly['Open'].shift(2).iloc[-1]) / 2)  # Third candle closes above midpoint of first candle
    )

    # Evening Star Pattern (3 candles)
    data["Evening_Star"] = int(
        (data_weekly['Close'].shift(2).iloc[-1] < data_weekly['Open'].shift(2).iloc[-1]) and  # First candle is bearish
        (data_weekly['Close'].shift(1).iloc[-1] > data_weekly['Open'].shift(1).iloc[-1]) and  # Second candle is bullish
        (data_weekly['Open'].iloc[-1] > data_weekly['Close'].shift(1).iloc[-1]) and  # Third candle opens below second
        (data_weekly['Close'].iloc[-1] < data_weekly['Open'].iloc[-1]) and  # Third candle is bearish
        (data_weekly['Close'].iloc[-1] < (data_weekly['Close'].shift(2).iloc[-1] + data_weekly['Open'].shift(2).iloc[-1]) / 2)  # Third candle closes below midpoint of first candle
    )

    return data

# Function to calculate weekly RSI
def calculate_weekly_rsi(symbol):
    stock = yf.Ticker(symbol)
    data_weekly = stock.history(period="1y", interval="1wk")
    if not data_weekly.empty:
        data_weekly['RSI_Weekly'] = ta.momentum.RSIIndicator(data_weekly['Close'], window=14).rsi()
        # Get the most recent weekly RSI value
        return data_weekly['RSI_Weekly'].iloc[-1]
    return None

# Add MACD Crossover Detection Function
def detect_macd_crossover(symbol,df):
    stock = yf.Ticker(symbol)
    weekly_df = stock.history(period="1y", interval="1wk")
    df['MACD_line'] = ta.trend.MACD(weekly_df['Close']).macd()
    df['Signal_line'] = ta.trend.MACD(weekly_df['Close']).macd_signal()
    # Detect crossover points
    df['MACD_Crossover'] = (df['MACD_line'] > df['Signal_line']) & (
        df['MACD_line'].shift(1) <= df['Signal_line'].shift(1))
    df['MACD_Crossunder'] = (df['MACD_line'] < df['Signal_line']) & (
        df['MACD_line'].shift(1) >= df['Signal_line'].shift(1))
    return df


# Function to display stock data with clickable symbols
def display_stock_data(stock_list, title):
    st.subheader(title)

    stock_data_list = []
    for stock in stock_list:
        data = get_stock_data(stock[0])
        RSI_Weekly = calculate_weekly_rsi(stock[0])
        if data is not None:
            data = calculate_indicators(stock[0],data)
            data = identify_candlestick_patterns(stock[0],data)
            current_data = data.iloc[-1]  # Get the latest data
            stock_data = {
                "Symbol": create_stock_link(stock[0]),
                "Industry": stock[1],
                "RSI_Daily": current_data['RSI'],
                "RSI_Weekly": RSI_Weekly,
                "MACD Crossover": "Bullish Crossover" if current_data['MACD_Crossover'] else "Bearish Crossover" if current_data['MACD_Crossunder'] else "No Crossover",
                "Volume Trend Daily": current_data['Volume_Trend_Daily'],
                "Volume Trend Weekly": current_data['Volume_Trend_Weekly'],
                "Bullish_Engulfing": 'Bullish_Engulfing' if current_data['Bullish_Engulfing'] else 0,
                "Bearish_Engulfing": 'Bearish_Engulfing' if current_data['Bearish_Engulfing'] else 0,
                "Doji": 'Doji' if current_data['Doji'] else 0,
                "Hammer": 'Hammer' if current_data['Hammer'] else 0,
                "Inverted_Hammer":'Inverted_Hammer' if current_data['Inverted_Hammer'] else 0,
                "Shooting_Star": 'Shooting_Star' if current_data['Shooting_Star'] else 0,
                "Morning_Star": 'Morning_Star' if current_data['Morning_Star'] else 0,
                "Evening_Star": 'Evening_Star' if current_data['Evening_Star'] else 0,
                "Current Price": current_data['Close'],
                "Open": current_data['Open'],
                "High": current_data['High'],
                "Low": current_data['Low'],
                "Close": current_data['Close'],
                "Volume": current_data['Volume'],
                "52-Week Low": data['Low'].min(),
                "52-Week High": data['High'].max(),
                # "MACD": current_data['MACD_line'],
            }
            stock_data_list.append(stock_data)

    if stock_data_list:
        df = pd.DataFrame(stock_data_list)
        # Apply font style based on RSI value
        df['RSI_Daily'] = df.apply(apply_font_style, axis=1)
        df['RSI_Weekly'] = df.apply(apply_weekly_rsi_font_style, axis=1)
        df['MACD Crossover'] = df.apply(apply_macd_font_style,axis=1)
        df['Volume Trend Daily'] = df.apply(lambda row: apply_volume_trend_font_style(row, 'Volume Trend Daily'), axis=1)
        df['Volume Trend Weekly'] = df.apply(lambda row: apply_volume_trend_font_style(row, 'Volume Trend Weekly'), axis=1)
        
    # # Render the dataframe with links
    st.write(df.to_html(escape=False), unsafe_allow_html=True)

# Streamlit App Layout
st.title("Stock Dashboard with RSI and Candlestick Patterns")

# Displaying three separate tables for Nifty 50, Nifty Next 50, and Bank Nifty
display_stock_data(get_nifty_50_symbols(), "Nifty 50 Stocks")
display_stock_data(get_nifty_next_50_symbols(), "Nifty Next 50 Stocks")
display_stock_data(get_bank_nifty_symbols(), "Bank Nifty Stocks")

# End of Streamlit App
