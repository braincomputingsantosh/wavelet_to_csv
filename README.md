# Wavelet Data to CSV Transformation

This Python script demonstrates how to transform wavelet data into CSV format, including the generation of synthetic data for testing purposes.

## Features

- Generate synthetic wavelet data with multiple frequency components
- Perform wavelet transformation using Daubechies wavelets
- Convert wavelet coefficients into a structured CSV format
- Include timestamp information for each data point
- Handle multi-level wavelet decomposition

## Requirements

```
numpy
pywt (PyWavelets)
pandas
```

## Installation

Install the required packages using pip:

```bash
pip install numpy pywt pandas
```

## Usage

The script performs the following operations:

1. Generates synthetic time series data with multiple frequency components (2 Hz, 10 Hz, and 20 Hz)
2. Applies a Wavelet Transform using Daubechies 4 wavelet
3. Organizes the coefficients into a structured DataFrame
4. Saves the results to a CSV file

### Code Structure

```python
import numpy as np
import pywt
import pandas as pd
from datetime import datetime, timedelta

# Generate sample data
def generate_sample_data(n_points=1000):
    t = np.linspace(0, 10, n_points)
    signal = (np.sin(2 * np.pi * 2 * t) +  # 2 Hz component
              0.5 * np.sin(2 * np.pi * 10 * t) +  # 10 Hz component
              0.25 * np.sin(2 * np.pi * 20 * t))  # 20 Hz component
    return t, signal
```

### Output Format

The resulting CSV file contains the following columns:

- `timestamp`: Time of each measurement
- `original_signal`: Raw signal values
- `approximation_L3`: Level 3 approximation coefficients
- `detail_L3`: Level 3 detail coefficients
- `detail_L2`: Level 2 detail coefficients
- `detail_L1`: Level 1 detail coefficients

## Working with Real Data

Instead of synthetic data, you can use real wavelet data from these sources:

1. **PhysioNet** (https://physionet.org/)
   - Extensive collection of biomedical signal databases
   - Includes ECG, EEG, and other physiological signals

2. **UCI Machine Learning Repository** (https://archive.ics.uci.edu/ml/index.php)
   - Various time series datasets
   - Well-documented data formats

3. **PyWavelets Examples** (https://pywavelets.readthedocs.io/en/latest/ref/data.html)
   - Built-in example datasets
   - Perfect for testing and learning

## Customization

You can modify the following parameters in the script:

- `n_points`: Number of data points to generate (default: 1000)
- `wavelet`: Type of wavelet to use (default: 'db4')
- `level`: Decomposition level (default: 3)

Example of customizing parameters:

```python
# Custom parameters
t, signal = generate_sample_data(n_points=2000)  # Generate 2000 points
wavelet = 'db8'  # Use Daubechies 8 wavelet
level = 4  # Use 4 levels of decomposition
```

## Notes

- The script pads shorter coefficient arrays with NaN values to maintain consistent array lengths
- Timestamps are generated starting from the current time with millisecond intervals
- All wavelet coefficients are preserved in the CSV output



## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
