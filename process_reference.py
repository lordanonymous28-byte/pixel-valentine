import sys
try:
    from PIL import Image
except ImportError:
    print("PIL not found. Please install Pillow.")
    sys.exit(1)

def extract_pixel_art(image_path, output_path):
    img = Image.open(image_path).convert('RGBA')
    
    # Trim whitespace
    bbox = img.getbbox()
    if bbox:
        img = img.crop(bbox)
        
    # Resize to target grid
    target_width = 30
    ratio = img.width / img.height
    target_height = int(target_width / ratio)
    
    small_img = img.resize((target_width, target_height), resample=Image.NEAREST)
    print(f"Resized to target grid: {target_width}x{target_height}")
    
    w, h = small_img.size
    
    # Flood fill to find background
    # Start from corners
    background_mask = set()
    queue = [(0,0), (w-1, 0), (0, h-1), (w-1, h-1)]
    
    # Get corner colors to verify they align (simple heuristic)
    # If all corners are different, we might have an issue, but usually it's uniform.
    bg_color = small_img.getpixel((0,0))
    
    visited = set()
    for q in queue:
        if q[0] >= 0 and q[0] < w and q[1] >= 0 and q[1] < h:
            visited.add(q)
            
    # Simple BFS flood fill for background
    idx = 0
    # Add valid corners to actual queue
    bfs_queue = []
    for q in queue:
        if 0 <= q[0] < w and 0 <= q[1] < h:
           bfs_queue.append(q)
           background_mask.add(q)

    while bfs_queue:
        x, y = bfs_queue.pop(0)
        curr_color = small_img.getpixel((x, y))
        
        # Check neighbors
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < w and 0 <= ny < h:
                if (nx, ny) not in background_mask:
                    neighbor_color = small_img.getpixel((nx, ny))
                    # Tolerance for compression artifacts?
                    # For pixel art, exact match is usually best, or very close.
                    if neighbor_color == curr_color:
                        background_mask.add((nx, ny))
                        bfs_queue.append((nx, ny))

    # CSS Generation
    shadows_female = []
    shadows_male = []
    
    def get_color_code(r, g, b, a):
        if a < 10: return None
        
        # Detect Red
        if r > 200 and g < 100 and b < 100: return "var(--pixel-red)"
        # Detect Yellow
        if r > 200 and g > 200 and b < 100: return "var(--pixel-yellow)"
        # Detect Teal/Blue (Overalls)
        if b > 150 and r < 100: return "#00aaff" 
        
        # Detect Pink (Bow)
        if r > 200 and g < 150 and b > 100: return "var(--pixel-heart)"
            
        # Detect Black (Outline/Eyes)
        if r < 80 and g < 80 and b < 80: return "var(--pixel-black)"
        
        # Detect White
        if r > 200 and g > 200 and b > 200: return "var(--pixel-white)"
        
        return None

    for y in range(h):
        for x in range(w):
            if (x, y) in background_mask:
                continue
                
            r, g, b, a = small_img.getpixel((x, y))
            
            # Additional check: if alpha is transparent
            if a < 10:
                continue
                
            color = get_color_code(r, g, b, a)
            
            if color:
                shadows_female.append(f"{x}px {y}px 0 {color}")
                
                # Male Logic
                if color == "var(--pixel-heart)": 
                    # Convert Bow to Black outline or White or Transparent?
                    # Usually removing the bow reveals the ear.
                    # This is hard to automate perfectly. 
                    # Let's try to assume the bow covers the ear.
                    # We'll just make it transparent for now, or maybe White if inside?
                    # Safe bet: Transparent.
                    pass
                else:
                    shadows_male.append(f"{x}px {y}px 0 {color}")

    css_female = ",\n        ".join(shadows_female)
    css_male = ",\n        ".join(shadows_male)
    
    template = f"""/* Auto-extracted from reference with background removal */
.pixel-hello-kitty.female::before {{
    width: 1px; height: 1px;
    box-shadow: 
        {css_female};
}}

.pixel-hello-kitty.male::before {{
    width: 1px; height: 1px;
    box-shadow: 
        {css_male};
}}
"""
    
    with open(output_path, 'w') as f:
        f.write(template)
    print(f"Generated CSS to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 process_reference.py <image_file>")
        sys.exit(1)
        
    extract_pixel_art(sys.argv[1], 'shadows_extracted.css')
