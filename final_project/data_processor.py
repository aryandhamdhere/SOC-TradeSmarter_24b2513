import pandas as pd
import numpy as np

def load_price_data(file_path: str) -> pd.DataFrame:
    """
    Load price data from CSV and set Date as index.
    """
    df = pd.read_csv(file_path, parse_dates=['Date'], index_col='Date')
    return df

# ------------------- ATR ------------------- #
def calculate_true_range(df: pd.DataFrame) -> pd.Series:
    """
    Calculate True Range used in ATR calculation.
    """
    high_low = df['High'] - df['Low']
    high_close = (df['High'] - df['Close'].shift()).abs()
    low_close = (df['Low'] - df['Close'].shift()).abs()

    return pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)

def add_atr_bands(df: pd.DataFrame, ma_period: int = 20, atr_period: int = 14, multiplier: float = 2.0) -> pd.DataFrame:
    """
    Add ATR-based bands and trading signals to the DataFrame.
    """
    # Moving Average of Close
    df['price_ma'] = df['Close'].rolling(window=ma_period).mean()

    # Average True Range
    true_range = calculate_true_range(df)
    df['atr'] = true_range.rolling(window=atr_period).mean()

    # ATR Upper and Lower Bands
    df['atr_upper_band'] = df['price_ma'] + (multiplier * df['atr'])
    df['atr_lower_band'] = df['price_ma'] - (multiplier * df['atr'])

    # Buy Signal: Close below lower band
    df['atr_band_signal'] = (df['Close'] < df['atr_lower_band']).astype(int)

    return df

# ------------------- MACD ------------------- #
def add_macd(df: pd.DataFrame, short_window: int = 12, long_window: int = 26, signal_window: int = 9) -> pd.DataFrame:
    """
    Add MACD and MACD signal line to the DataFrame.
    """
    df['ema_short'] = df['Close'].ewm(span=short_window, adjust=False).mean()
    df['ema_long'] = df['Close'].ewm(span=long_window, adjust=False).mean()
    df['macd'] = df['ema_short'] - df['ema_long']
    df['macd_signal'] = df['macd'].ewm(span=signal_window, adjust=False).mean()

    return df

# ------------------- RSI ------------------- #
def add_rsi(df: pd.DataFrame, period: int = 14) -> pd.DataFrame:
    """
    Add RSI (Relative Strength Index) to the DataFrame.
    """
    delta = df['Close'].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(period).mean()
    avg_loss = loss.rolling(period).mean()

    rs = avg_gain / avg_loss
    df['rsi'] = 100 - (100 / (1 + rs))

    return df