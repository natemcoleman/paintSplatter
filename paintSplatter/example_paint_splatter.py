import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFilter
import random

# Create canvas
img = Image.new("RGBA", (800, 600), (255, 255, 255, 0))
draw = ImageDraw.Draw(img)

# Generate a random slash path
numPoints = 50
x = np.linspace(100, 700, numPoints)
y = 300 + 50 * np.sin(np.linspace(0, 3*np.pi, numPoints)) + np.random.normal(0, 10, numPoints)

# Draw the core slash path with variable width
for i in range(numPoints - 1):
    width = int(10 + 10 * np.sin(i / numPoints * np.pi))  # tapered edges
    draw.line([(x[i], y[i]), (x[i+1], y[i+1])], fill=(200, 0, 0, 200), width=width)

# Add splatter
for _ in range(200):
    px = random.uniform(min(x), max(x))
    py = random.uniform(min(y) - 40, max(y) + 40)
    r = random.randint(1, 5)
    draw.ellipse([px-r, py-r, px+r, py+r], fill=(180, 0, 0, random.randint(100, 200)))

# Apply blur for softness
img = img.filter(ImageFilter.GaussianBlur(1.5))

# Show
plt.imshow(img)
plt.axis("off")
plt.show()
