import numpy as np
import matplotlib.pyplot as plt

# Parameters for the pendulum motion
t = np.linspace(0, 20, 5000)  # Time array
amplitude_x = 200  # Amplitude of swing in x-direction
amplitude_y = 150  # Amplitude of swing in y-direction
frequency_x = 1.5  # Frequency of swing in x-direction
frequency_y = 1.2  # Frequency of swing in y-direction
phase_shift = np.pi / 4  # Phase shift between x and y

# Parametric equations for the pendulum motion
x = amplitude_x * np.sin(frequency_x * t)
y = amplitude_y * np.sin(frequency_y * t + phase_shift)

# Create the figure and plot
plt.figure(figsize=(8, 8))
plt.plot(x, y, color="blue", linewidth=1.5, alpha=0.8)

# Add labels and styling
plt.title("Swinging Pendulum with Spirograph-like Motion", fontsize=14)
plt.axis("equal")
plt.axis("off")

# Display the plot
plt.show()