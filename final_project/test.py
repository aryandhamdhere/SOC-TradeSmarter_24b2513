from data_processor import load_price_data, add_atr_bands, add_macd, add_rsi
from model import load_model
import pandas as pd

# Load test dataset
data = load_price_data("data/BDL_testing.csv")

# Add indicators (same as training)
data = add_atr_bands(data)
data = add_macd(data)
data = add_rsi(data)

# Drop rows with NaN values
data = data.dropna()

# Define features
feature_columns = ['macd', 'macd_signal', 'rsi', 'atr_band_signal']

# Load trained model
nn_model = load_model("models/hybrid_model_weights.h5")

# Make predictions
data['prediction'] = (nn_model.predict(data[feature_columns]) > 0.4).astype(int)
print("🔎 Prediction value counts:\n", data['prediction'].value_counts())

# Calculate strategy performance
data['return'] = data['Close'].pct_change().shift(-1)
strategy = data[data['prediction'] == 1]

success_rate = (strategy['return'] > 0).mean() * 100
avg_return = strategy['return'].mean()
total_trades = len(strategy)

print("📊 Neural Network Strategy Results")
print(f"✅ Success Rate: {success_rate:.2f}%")
print(f"📈 Per-Trade Return: {avg_return:.2f}")
print(f"🔁 Total Trades Executed: {total_trades}")