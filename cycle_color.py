import os
import re

svg_path = r"C:\Users\shuvr\.config\yasb\time_bg.svg"
css_path = r"C:\Users\shuvr\.config\yasb\styles.css"

colors = [
    "#4ecdc4", "#ff7bac", "#f9d423", "#a3bffa", "#ff6b6b", "#b620e0",
    "#00e5ff", "#ff9100", "#52f1d2", "#d031ff", "#ff7f50", "#2ecc71"
]

try:
    with open(svg_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find current color
    match = re.search(r'fill="([^"]+)"', content)
    if match:
        current_color = match.group(1).lower()
        try:
            # Convert colors to lower for safe matching
            lower_colors = [c.lower() for c in colors]
            idx = lower_colors.index(current_color)
            next_color = colors[(idx + 1) % len(colors)]
        except ValueError:
            next_color = colors[0]
    else:
        next_color = colors[0]

    # Replace color
    content = re.sub(r'fill="[^"]+"', f'fill="{next_color}"', content)
    content = re.sub(r'stroke="[^"]+"', f'stroke="{next_color}"', content)

    with open(svg_path, 'w', encoding='utf-8') as f:
        f.write(content)

    # Touch styles.css to trigger YASB reload
    if os.path.exists(css_path):
        os.utime(css_path, None)

except Exception as e:
    pass
