from tensorflow.keras.models import Sequential, load_model as keras_load_model
from tensorflow.keras.layers import Dense
import os

# Build a simple feed-forward neural network
def build_model(input_dim=4):
    model = Sequential()
    model.add(Dense(16, input_dim=input_dim, activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

# Save model weights to a file
def save_model(model, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    model.save(path)

# Load a previously saved model
def load_model(path):
    return keras_load_model(path)