import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Define the transfer function
numerator = [1.778, 0]
denominator = [3.35, 1/3.35, 9708.16**2]

# Create the transfer function object
transfer_function = signal.TransferFunction(numerator, denominator)

# Generate the frequency response
frequency, magnitude, phase = signal.bode(transfer_function, np.logspace(1, 4, num=1000))

# Plot the phase response
plt.subplot(2, 1, 2)
plt.semilogx(frequency, phase)
plt.title('Bode Plot - Phase Response')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Phase (degrees)')
plt.xlim([10, 10000])
plt.ylim([-180, 180])
plt.grid(True)

# Convert magnitudes to dB
magnitudes_db = 20 * np.log10(np.abs(magnitude))

# Plot the magnitude response
plt.subplot(2, 1, 1)
plt.semilogx(frequency, magnitudes_db)
plt.title('Magnitude Response Bode Plot')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.xlim([10, 10000])
plt.grid(True)

# Adjust subplots spacing
plt.tight_layout()

plt.show()

