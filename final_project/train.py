from data_processor import load_price_data, add_atr_bands, add_macd, add_rsi
from model import build_model, save_model

# Load training dataset
data = load_price_data("data/BDL_training.csv")
print("➡️ Loaded data columns:", data.columns.tolist())

# Add technical indicators
data = add_atr_bands(data)
print("✅ After ATR:", data.columns.tolist())

data = add_macd(data)
print("✅ After MACD:", data.columns.tolist())

data = add_rsi(data)
print("✅ After RSI:", data.columns.tolist())

# Drop rows with NaN values caused by rolling calculations
data = data.dropna()
print("✅ Final columns (before training):", data.columns.tolist())

# Define input features for the neural network
feature_columns = ['macd', 'macd_signal', 'rsi', 'atr_band_signal']

# Input (X) and output (y) variables
print("\n➡️ Columns present:", data.columns.tolist())
print("\n➡️ Sample data:\n", data.head())
X = data[feature_columns]
y = (data['Close'].shift(-1) > data['Close']).astype(int)

# Build and train the neural network model
nn_model = build_model()
nn_model.fit(X, y)

# Save the trained model to disk
save_model(nn_model, "models/hybrid_model_weights.h5")

# Build and train the neural network model
nn_model = build_model()
nn_model.fit(X, y, epochs=50, batch_size=32, verbose=1)

# Save the trained model to disk
save_model(nn_model, "models/hybrid_model_weights.h5")

# Debug: Show class balance
print("🔎 Training target balance:\n", y.value_counts())