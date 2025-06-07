import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from PIL import Image, ImageDraw, ImageFilter
import random

# Canvas dimensions
width, height = 800, 800
background_color = (255, 255, 255, 255)

# Define colors for each pendulum
pendulum_colors = [
    (200, 0, 0),    # Red
    # (0, 200, 0),    # Green
    (200, 200, 0),  # Green
    (0, 0, 200)     # Blue
]
# pendulum_colors = [
#     (156, 67, 92),    # Matte rose
#     (85, 140, 134),   # Sage green
#     (76, 106, 147),   # Dusty blue
# ]

# Parameters for the pendulum motions
t = np.linspace(0, 20, 200)
# Different parameters for each pendulum
pendulums = [
    {
        'x': width/2 + 250 * np.sin(1.5 * t),
        'y': height/2 + 200 * np.sin(1.2 * t + np.pi/4)
    },
    {
        'x': width/2 + 200 * np.sin(1.2 * t + np.pi/3),
        'y': height/2 + 250 * np.sin(1.4 * t + np.pi/3)
    },
    {
        'x': width/2 + 220 * np.sin(0.7 * t + np.pi/6),
        'y': height/2 + 250 * np.sin(1.7 * t + np.pi/2)
    }
]

# Initialize figure
fig, ax = plt.subplots(figsize=(8, 8))
ax.axis("off")
image = None

# Store splatter information for each pendulum
splatter_histories = [[], [], []]


def update(frame):
    global image
    img = Image.new("RGBA", (width, height), background_color)
    draw = ImageDraw.Draw(img)

    # First draw all pendulum paths
    for idx, (pendulum, color) in enumerate(zip(pendulums, pendulum_colors)):
        for i in range(frame):
            if i < len(t) - 1:
                width_var = int(8 + 4 * np.sin(i / len(t) * np.pi))
                draw.line(
                    [(pendulum['x'][i], pendulum['y'][i]),
                     (pendulum['x'][i + 1], pendulum['y'][i + 1])],
                    fill=color + (180,),
                    width=width_var
                )

    # Generate new splatters for each pendulum
    for idx, (pendulum, color) in enumerate(zip(pendulums, pendulum_colors)):
        new_splatters = []
        for _ in range(7):
            splash_x = pendulum['x'][frame] + np.random.normal(0, 20)
            splash_y = pendulum['y'][frame] + np.random.normal(0, 20)
            r_width = np.random.randint(2, 10)
            r_height = np.random.randint(2, 10)
            alpha = np.random.randint(100, 200)
            splatter_color = color + (alpha,)
            # Add frame number to track when splatter was created
            new_splatters.append((frame, splash_x, splash_y, r_width, r_height, splatter_color))
        splatter_histories[idx].extend(new_splatters)

    # Draw all splatters from all pendulums sorted by creation time
    all_splatters = []
    for history in splatter_histories:
        all_splatters.extend(history)

    # Sort splatters by frame number (oldest first)
    all_splatters.sort(key=lambda x: x[0])

    # Draw splatters in order
    for _, splash_x, splash_y, r_width, r_height, splatter_color in all_splatters:
        draw.ellipse(
            [splash_x - r_width, splash_y - r_height,
             splash_x + r_width, splash_y + r_height],
            fill=splatter_color
        )

    # Apply blur
    img = img.filter(ImageFilter.GaussianBlur(1))

    # Update display
    image = np.array(img)
    ax.clear()
    ax.imshow(image)
    ax.axis("off")
    return ax,

# Create animation
ani = FuncAnimation(fig, update, frames=len(t), interval=50, repeat=False)

# Save animation
# writer = PillowWriter(fps=20)
# ani.save('triple_pendulum_paint.gif', writer=writer)

plt.show()