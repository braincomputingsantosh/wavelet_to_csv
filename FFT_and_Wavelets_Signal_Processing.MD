# Understanding FFT and Wavelets in Signal Processing

This guide explains the relationship between Fast Fourier Transform (FFT) and Wavelet Transform, particularly in the context of EEG signal analysis.

## Basic Concept

Think of FFT as taking a photograph (single snapshot) of your signal's frequency content, while wavelets are like recording a video that shows how frequencies change over time. Both tools are valuable but serve different purposes in signal analysis.

## Key Differences

### 1. Time vs. Frequency Resolution

#### FFT
- Provides perfect frequency resolution
- Loses temporal information
- Tells you WHAT frequencies exist
- Best for stationary signals

#### Wavelets
- Provides both time and frequency information
- Adaptive resolution
- Tells you WHAT frequencies exist and WHEN they occur
- Excellent for non-stationary signals

### 2. Window Analysis

#### FFT
```python
from scipy.fft import fft
import numpy as np

# FFT uses fixed window size
def fft_analysis(signal, fs):
    frequencies = fft(signal)
    freq_axis = np.fft.fftfreq(len(signal), 1/fs)
    return frequencies, freq_axis
```

#### Wavelets
```python
import pywt

# Wavelets use adaptive window size
def wavelet_analysis(signal):
    scales = np.arange(1, 128)
    coefficients, frequencies = pywt.cwt(signal, scales, 'morl')
    return coefficients, frequencies
```

## Practical Applications

### Combined Analysis Example
```python
def compare_fft_wavelet(signal, fs=256):
    """
    Analyze signal using both FFT and Wavelet transforms
    
    Parameters:
    signal: Input signal
    fs: Sampling frequency (Hz)
    
    Returns:
    fft_result: Frequency spectrum
    wavelet_result: Time-frequency representation
    """
    # FFT Analysis
    fft_result = np.abs(fft(signal))
    
    # Wavelet Analysis
    scales = np.arange(1, 128)
    wavelet_result, _ = pywt.cwt(signal, scales, 'morl')
    
    return fft_result, wavelet_result
```

## When to Use What

### Use FFT For:
- Spectral analysis of stable signals
- Quick frequency component identification
- Power spectrum calculations
- Frequency-domain filtering

### Use Wavelets For:
- Transient event detection
- Time-varying frequency analysis
- Multi-resolution analysis
- Non-stationary signal processing

## EEG Analysis Example

### Common Applications:

1. **Steady State Analysis (FFT)**
   - Resting state EEG
   - Dominant frequency identification
   - Power band calculation

2. **Dynamic Analysis (Wavelets)**
   - Seizure detection
   - Sleep stage transitions
   - Event-related potentials
   - Artifact removal

## Code Example: EEG Processing Pipeline
```python
def process_eeg_signal(eeg_signal, fs=256):
    """
    Complete EEG processing pipeline using both FFT and wavelets
    
    Parameters:
    eeg_signal: Raw EEG signal
    fs: Sampling frequency
    """
    # FFT Analysis
    spectrum = np.abs(fft(eeg_signal))
    
    # Wavelet Analysis
    coeffs = pywt.wavedec(eeg_signal, 'db4', level=5)
    
    # Extract features
    features = {
        'fft_peaks': find_peaks(spectrum),
        'wavelet_energy': [np.sum(c**2) for c in coeffs]
    }
    
    return features
```

## Best Practices

1. **Signal Preprocessing**
   - Remove baseline drift
   - Filter noise
   - Handle artifacts

2. **Analysis Selection**
   - Use FFT for frequency-domain analysis of stable signals
   - Use wavelets for time-varying patterns
   - Consider using both for comprehensive analysis

3. **Parameter Selection**
   - Choose appropriate window sizes for FFT
   - Select suitable wavelet types and scales
   - Consider computational complexity

## Common Pitfalls to Avoid

1. Using FFT for non-stationary signals
2. Ignoring edge effects in wavelet analysis
3. Inappropriate window size selection
4. Over-reliance on a single analysis method

## Requirements

```bash
pip install numpy scipy pywt matplotlib
```

## References

1. FFT Documentation: https://docs.scipy.org/doc/scipy/reference/fft.html
2. PyWavelets: https://pywavelets.readthedocs.io/
3. Signal Processing Basics: https://scipy-lectures.org/intro/scipy/auto_examples/plot_fftpack.html

## License

This documentation is licensed under the MIT License.
