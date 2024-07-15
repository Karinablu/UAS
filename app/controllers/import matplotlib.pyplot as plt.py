import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Function to create an arrowed annotation
def create_arrow(ax, start, end, text="", text_offset=(0, 0)):
    ax.annotate(text, xy=start, xytext=end, 
                arrowprops=dict(facecolor='black', shrink=0.05),
                fontsize=10, ha='center', va='center')
    if text:
        ax.text((start[0] + end[0]) / 2 + text_offset[0], 
                (start[1] + end[1]) / 2 + text_offset[1], text, 
                fontsize=10, ha='center', va='center')

fig, ax = plt.subplots(figsize=(10, 8))

# Create boxes for flowchart
boxes = {
    "start": (0.5, 0.9),
    "analisis_kebutuhan": (0.5, 0.75),
    "desain_sistem": (0.5, 0.6),
    "pengembangan": (0.5, 0.45),
    "pengujian": (0.5, 0.3),
    "implementasi": (0.5, 0.15),
    "pemeliharaan": (0.5, 0.05)
}

# Add boxes
for box, pos in boxes.items():
    if box == "start":
        ax.add_patch(patches.Ellipse(pos, 0.3, 0.1, edgecolor='black', facecolor='lightgray'))
        ax.text(pos[0], pos[1], "Start", fontsize=12, ha='center', va='center')
    else:
        ax.add_patch(patches.Rectangle((pos[0] - 0.15, pos[1] - 0.05), 0.3, 0.1, edgecolor='black', facecolor='lightgray'))
        ax.text(pos[0], pos[1], box.replace('_', ' ').capitalize(), fontsize=12, ha='center', va='center')

# Create arrows
create_arrow(ax, (0.5, 0.85), (0.5, 0.8))
create_arrow(ax, (0.5, 0.7), (0.5, 0.65))
create_arrow(ax, (0.5, 0.55), (0.5, 0.5))
create_arrow(ax, (0.5, 0.4), (0.5, 0.35))
create_arrow(ax, (0.5, 0.25), (0.5, 0.2))
create_arrow(ax, (0.5, 0.1), (0.5, 0.05))

# Set limits and hide axes
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

plt.show()
