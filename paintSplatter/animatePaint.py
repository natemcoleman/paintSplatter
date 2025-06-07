import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from PIL import Image, ImageDraw, ImageFilter
import random

# Canvas dimensions
width, height = 800, 800
background_color = (200, 200, 200, 255)
# Change the pendulum line color
pendulum_color = (0, 0, 200)  # Blue color to match original


# Parameters for the pendulum motion
t = np.linspace(0, 20, 200)
amplitude_x = 250
amplitude_y = 200
frequency_x = 1.5
frequency_y = 1.2
phase_shift = np.pi / 4

# Calculate pendulum path
x = width / 2 + amplitude_x * np.sin(frequency_x * t)
y = height / 2 + amplitude_y * np.sin(frequency_y * t + phase_shift)

# Initialize figure
fig, ax = plt.subplots(figsize=(8, 8))
ax.axis("off")
image = None

# Store splatter information
splatter_history = []


# Animation update function
def update(frame):
    global image, splatter_history
    # Create a new canvas for each frame
    img = Image.new("RGBA", (width, height), background_color)
    draw = ImageDraw.Draw(img)

    # Draw the pendulum path up to the current frame
    for i in range(frame):
        if i < len(t) - 1:
            width_var = int(8 + 4 * np.sin(i / len(t) * np.pi))
            draw.line([(x[i], y[i]), (x[i + 1], y[i + 1])],
                      fill=(0, 0, 200, 180), width=width_var)

    # Generate new splatters for current frame
    colors = [(200, 0, 0), (0, 200, 0), (0, 0, 200), (200, 200, 0), (200, 0, 200), (0, 200, 200)]
    new_splatters = []
    for _ in range(10):
        splash_x = x[frame] + np.random.normal(0, 20)
        splash_y = y[frame] + np.random.normal(0, 20)
        r_width = np.random.randint(2, 10)
        r_height = np.random.randint(2, 10)
        alpha = np.random.randint(100, 200)
        # color = random.choice(colors) + (alpha,)
        color = pendulum_color + (alpha,)  # Use the same blue color with random alpha
        new_splatters.append((splash_x, splash_y, r_width, r_height, color))

    # Add new splatters to history
    splatter_history.extend(new_splatters)

    # Draw all splatters from history
    for splash_x, splash_y, r_width, r_height, color in splatter_history:
        draw.ellipse([splash_x - r_width, splash_y - r_height,
                      splash_x + r_width, splash_y + r_height], fill=color)

    # Apply blur for smoother look
    img = img.filter(ImageFilter.GaussianBlur(1))

    # Convert the PIL image to matplotlib format
    image = np.array(img)
    ax.clear()
    ax.imshow(image)
    ax.axis("off")
    return ax,


# Create animation
ani = FuncAnimation(fig, update, frames=len(t), interval=50, repeat=False)

# Save animation as GIF
# writer = PillowWriter(fps=20)
# ani.save('pendulum_paint.gif', writer=writer)

# Show animation
plt.show()