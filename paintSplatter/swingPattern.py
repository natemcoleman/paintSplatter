import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFilter

# Create canvas
width, height = 800, 800
img = Image.new("RGBA", (width, height), (255, 255, 255, 0))
draw = ImageDraw.Draw(img)

# Parameters for the pendulum motion
t = np.linspace(0, 20, 200)
amplitude_x = 250
amplitude_y = 200
frequency_x = 1.5
frequency_y = 1.2
phase_shift = np.pi / 4

# Calculate pendulum path
x = width/2 + amplitude_x * np.sin(frequency_x * t)
y = height/2 + amplitude_y * np.sin(frequency_y * t + phase_shift)

# Draw the main path with varying thickness
for i in range(len(t)-1):
    width_var = int(8 + 4 * np.sin(i / len(t) * np.pi))
    draw.line([(x[i], y[i]), (x[i+1], y[i+1])],
              fill=(0, 0, 200, 180), width=width_var)

# Add paint splatters along the path
for i in range(0, len(t), 2):
    for _ in range(5):
        splash_x = x[i] + np.random.normal(0, 20)
        splash_y = y[i] + np.random.normal(0, 20)
        r = np.random.randint(2, 8)
        alpha = np.random.randint(100, 200)
        draw.ellipse([splash_x-r, splash_y-r, splash_x+r, splash_y+r],
                    fill=(0, 0, 200, alpha))

# Apply blur for a more natural look
img = img.filter(ImageFilter.GaussianBlur(1.5))

# Display
plt.figure(figsize=(10, 10))
plt.imshow(img)
plt.axis('off')
plt.show()