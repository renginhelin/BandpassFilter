import numpy as np
import scipy.signal as signal
import soundfile as sf

# Read the input audio file
input_file = 'africa.wav'
output_file = input_file[:-4] + 'BPF.wav'  # Append 'BPF' to the output file name

# Load the audio data and sampling rate
audio_data, sampling_rate = sf.read(input_file)

f0 = 1550  # Center frequency in Hz
bandwidth = 2900  
gain = 1.778

# Calculate the angular center frequency and normalized bandwidth
omega0 = 2 * np.pi * f0 / sampling_rate
bw = 2 * np.pi * bandwidth / sampling_rate

# Calculate the filter coefficients
# uses the signal.iirnotch() function from the scipy.signal library to calculate the filter coefficients
b, a = signal.iirnotch(omega0, bw, gain)

# Applies the filter to the audio data
filtered_audio = signal.lfilter(b, a, audio_data)

# Write the filtered audio data to a new file
sf.write(output_file, filtered_audio, sampling_rate)

print(f"Filtered audio saved to '{output_file}'")
