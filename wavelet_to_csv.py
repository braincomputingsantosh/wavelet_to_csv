import numpy as np
import pywt
import pandas as pd
from datetime import datetime, timedelta

# Create synthetic time series data
def generate_sample_data(n_points=1000):
    t = np.linspace(0, 10, n_points)
    # Create a signal with multiple frequency components
    signal = (np.sin(2 * np.pi * 2 * t) +  # 2 Hz component
              0.5 * np.sin(2 * np.pi * 10 * t) +  # 10 Hz component
              0.25 * np.sin(2 * np.pi * 20 * t))  # 20 Hz component
    return t, signal

# Generate sample data
t, signal = generate_sample_data()

# Perform wavelet transform
wavelet = 'db4'  # Daubechies 4 wavelet
level = 3  # Decomposition level
coeffs = pywt.wavedec(signal, wavelet, level=level)

# Create DataFrame for coefficients
# First, let's create timestamps for our data
start_time = datetime.now()
timestamps = [start_time + timedelta(milliseconds=i) for i in range(len(signal))]

# Create a dictionary to store all coefficients
coef_dict = {
    'timestamp': timestamps,
    'original_signal': signal
}

# Add wavelet coefficients to dictionary
for i, coef in enumerate(coeffs):
    if i == 0:
        coef_dict[f'approximation_L{level}'] = np.pad(coef, 
            (0, len(signal) - len(coef)), 'constant', constant_values=np.nan)
    else:
        coef_dict[f'detail_L{level-i+1}'] = np.pad(coef, 
            (0, len(signal) - len(coef)), 'constant', constant_values=np.nan)

# Create DataFrame
df = pd.DataFrame(coef_dict)

# Save to CSV
df.to_csv('wavelet_data.csv', index=False)

# Display first few rows
print("First few rows of the CSV:")
print(df.head())

# Display basic information about the data
print("\nDataFrame Info:")
print(df.info())
