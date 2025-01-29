# EEG Signal Analysis Using Wavelets

This documentation describes the application of wavelet transforms for EEG (Electroencephalogram) signal analysis, including preprocessing, feature extraction, and event detection.

## Overview

Wavelet transforms are particularly powerful for EEG analysis because they provide:
- Multi-resolution analysis of different frequency bands
- Effective artifact removal
- Superior time-frequency resolution compared to Fourier transforms
- Ability to analyze non-stationary signals
- Preservation of signal characteristics during noise reduction

## Requirements

```bash
pip install numpy pywt mne pandas
```

## Core Functionality

### Basic EEG Processing

```python
import numpy as np
import pywt
import mne
import pandas as pd

def process_eeg_with_wavelets(eeg_signal, sampling_rate=256):
    """
    Process EEG signal using wavelet decomposition
    
    Parameters:
    eeg_signal: Raw EEG signal
    sampling_rate: Sampling frequency in Hz
    
    Returns:
    DataFrame containing separated frequency bands
    """
    wavelet = 'db4'
    coeffs = pywt.wavedec(eeg_signal, wavelet, level=5)
    
    # Reconstruct individual bands
    reconstructed = []
    for i in range(len(coeffs)):
        coeff_copy = [np.zeros_like(c) for c in coeffs]
        coeff_copy[i] = coeffs[i]
        reconstructed.append(pywt.waverec(coeff_copy, wavelet))
    
    # Create DataFrame with separated bands
    bands = pd.DataFrame({
        'raw_signal': eeg_signal,
        'delta': reconstructed[-1],  # 0.5-4 Hz
        'theta': reconstructed[-2],  # 4-8 Hz
        'alpha': reconstructed[-3],  # 8-13 Hz
        'beta': reconstructed[-4],   # 13-30 Hz
        'gamma': reconstructed[-5]   # >30 Hz
    })
    
    return bands
```

### Artifact Removal

```python
def remove_eeg_artifacts(eeg_signal, wavelet='db4', threshold=0.3):
    """
    Remove artifacts from EEG signal using wavelet thresholding
    
    Parameters:
    eeg_signal: Raw EEG signal
    wavelet: Wavelet type (default: 'db4')
    threshold: Threshold for coefficient suppression (default: 0.3)
    
    Returns:
    Cleaned EEG signal
    """
    coeffs = pywt.wavedec(eeg_signal, wavelet, level=5)
    
    # Apply thresholding to detail coefficients
    for i in range(1, len(coeffs)):
        coeffs[i] = pywt.threshold(coeffs[i], threshold*np.max(coeffs[i]))
    
    return pywt.waverec(coeffs, wavelet)
```

## Advanced Applications

### Feature Extraction

```python
def extract_eeg_features(eeg_signal):
    """
    Extract wavelet-based features from EEG signal
    
    Parameters:
    eeg_signal: EEG signal
    
    Returns:
    Dictionary of features including energy, entropy, and variance
    """
    coeffs = pywt.wavedec(eeg_signal, 'db4', level=5)
    
    features = {
        'energy': [np.sum(c**2) for c in coeffs],
        'entropy': [np.sum(-c**2 * np.log(c**2 + 1e-10)) for c in coeffs],
        'variance': [np.var(c) for c in coeffs]
    }
    return features
```

### Event Detection

```python
def detect_events(eeg_signal, threshold):
    """
    Detect significant events in EEG signal
    
    Parameters:
    eeg_signal: EEG signal
    threshold: Detection threshold
    
    Returns:
    Boolean array indicating event locations
    """
    coeffs, freqs = pywt.cwt(eeg_signal, 
                            scales=np.arange(1, 128), 
                            wavelet='morl')
    
    energy = np.sum(coeffs**2, axis=0)
    events = energy > threshold
    
    return events
```

## Common Analysis Tasks

### 1. Preprocessing
- Signal denoising
- Artifact removal (eye movements, muscle activity)
- Baseline correction

### 2. Frequency Band Analysis
- Delta (0.5-4 Hz): Deep sleep
- Theta (4-8 Hz): Drowsiness
- Alpha (8-13 Hz): Relaxed wakefulness
- Beta (13-30 Hz): Active thinking
- Gamma (>30 Hz): Information processing

### 3. Clinical Applications
- Sleep stage classification
- Seizure detection
- Brain-computer interfaces
- Cognitive state assessment

## Best Practices

1. **Preprocessing**
   - Always check signal quality before analysis
   - Remove baseline drift
   - Apply appropriate filtering

2. **Wavelet Selection**
   - Daubechies wavelets (db4, db6) work well for EEG
   - Consider signal characteristics when choosing wavelets
   - Test multiple wavelet types if unsure

3. **Parameter Tuning**
   - Adjust decomposition levels based on sampling rate
   - Fine-tune thresholds for artifact removal
   - Validate results with known markers

## Common Pitfalls

1. Edge effects in wavelet transformation
2. Inappropriate threshold selection
3. Over-filtering leading to signal distortion
4. Incorrect frequency band separation

## References

1. Continuous Wavelet Transform: https://pywavelets.readthedocs.io/en/latest/ref/cwt.html
2. MNE-Python: https://mne.tools/stable/index.html
3. PyWavelets Documentation: https://pywavelets.readthedocs.io/

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
