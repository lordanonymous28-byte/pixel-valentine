
def generate_shadow(grid, scale=1):
    shadows = []
    # Palette
    colors = {
        ' ': 'transparent',
        '.': 'transparent',
        'w': 'var(--pixel-white)',
        'b': 'var(--pixel-black)',
        'r': 'var(--pixel-red)',
        'y': 'var(--pixel-yellow)',
        'p': 'var(--pixel-heart)', # Pink
        'o': '#00aaff',   # Blue Overalls
    }
    
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char in colors and colors[char] != 'transparent':
                shadows.append(f"{x * scale}px {y * scale}px 0 {colors[char]}")
                
    return ",\n        ".join(shadows)

# Final Grids based on 28x32
# Detailed blocky look

# Female with Pink Bow
female_grid = [
    "................................",
    ".......bbbbb..........bbbbb.....",
    "......bwwwwwb.......bbpppppbb...",
    ".....bwwwwwwwb.....bpppppppppb..",
    "....bwwwwwwwwwb...bpppppppppppb.",
    "...bwwwwwwwwwwwb..bpppppppppppb.",
    "...bwwwwwwwwwwwwbbppppppppppppb.",
    "..bwwwwwwwwwwwwwwbpppppbbpppppb.",
    "..bwwwwwwwwwwwwwwwbbbbb..bbbbb..",
    "..bwwwwwwwwwwwwwwwwwwww.........",
    "bbwwwwbwwwwwwbwwwwwwwwww........", # Whisker 1
    "bbwwwwbwwwwwwbwwwwwwwwww........", 
    ".bwwwwbwwwwwwbwwwwwwwwb.........", # Eye
    "bbwwwwbwwwwwwbwwwwwwwwbb...bb...", # Whisker 2
    "bbwwwwwwwwwwwwwwwwwwwwbb...bb...", 
    ".bwwwwwwwwyywwwwwwwwwwb.........", # Nose
    "bbwwwwwwwwyywwwwwwwwwwbb...bb...", # Whisker 3
    ".bwwwwwwwwwwwwwwwwwwwwb.........",
    "..bwwwwwwwwwwwwwwwwwwb..........",
    "...bwwwwwwwwwwwwwwwwb...........",
    "....bbwwwwwwwwwwwwbb............",
    "......bbbbbbbbbbbb..............",
    ".....rrbrrrrrrbrr...............", # Shirt
    "....rrrboooooobrrr..............", # Overalls
    "...wrrroyyllboyyrrw.............", # Buttons
    "...wrrroyyllboyyrrw.............", 
    "...wrrroooooooorrw..............",
    "...wrrroooooooorrw..............",
    "....bbrobbbbborbb...............",
    "......bob....bob................", # Legs
    "......bwb....bwb................",
    "......bbb....bbb................",
]

# Male with Red Bowtie
male_grid = [
    "................................",
    ".......bbbbb..........bbbbb.....",
    "......bwwwwwb.......bbwwwwwbb...",
    ".....bwwwwwwwb.....bwwwwwwwwwb..",
    "....bwwwwwwwwwb...bwwwwwwwwwwwb.",
    "...bwwwwwwwwwwwb..bwwwwwwwwwwwb.",
    "...bwwwwwwwwwwwwbbwwwwwwwwwwwwb.",
    "..bwwwwwwwwwwwwwwwwwwwwwwwwwwwb.",
    "..bwwwwwwwwwwwwwwwwwwwwwwwwwwwb.",
    "..bwwwwwwwwwwwwwwwwwwww.........",
    "bbwwwwbwwwwwwbwwwwwwwwww........", 
    "bbwwwwbwwwwwwbwwwwwwwwww........", 
    ".bwwwwbwwwwwwbwwwwwwwwb.........", 
    "bbwwwwbwwwwwwbwwwwwwwwbb...bb...", 
    "bbwwwwwwwwwwwwwwwwwwwwbb...bb...", 
    ".bwwwwwwwwyywwwwwwwwwwb.........", 
    "bbwwwwwwwwyywwwwwwwwwwbb...bb...", 
    ".bwwwwwwwwwwwwwwwwwwwwb.........",
    "..bwwwwwwwwwwwwwwwwwwb..........",
    "...bwwwwwwwwwwwwwwwwb...........",
    "....bbwwwwwwwwwwwwbb............",
    "......bbbbbbbbbbbb..............",
    ".....rrbrrrrrrbrr...............", # Shirt
    "....rrrbbrrrrrbbrrr.............", # Bowtie outline?
    "...wrrroyyllboyyrrw.............", # No just red bowtie
    "...wrrroyyllboyyrrw.............", 
    "...wrrroooooooorrw..............",
    "...wrrroooooooorrw..............",
    "....bbrobbbbborbb...............",
    "......bob....bob................", 
    "......bwb....bwb................",
    "......bbb....bbb................",
]

# Better Male Bowtie logic
# Red bowtie in the center of neck area
male_grid = [
    "................................",
    ".......bbbbb..........bbbbb.....",
    "......bwwwwwb.......bbwwwwwbb...",
    ".....bwwwwwwwb.....bwwwwwwwwwb..",
    "....bwwwwwwwwwb...bwwwwwwwwwwwb.",
    "...bwwwwwwwwwwwb..bwwwwwwwwwwwb.",
    "...bwwwwwwwwwwwwbbwwwwwwwwwwwwb.",
    "..bwwwwwwwwwwwwwwwwwwwwwwwwwwwb.",
    "..bwwwwwwwwwwwwwwwwwwwwwwwwwwwb.",
    "..bwwwwwwwwwwwwwwwwwwww.........",
    "bbwwwwbwwwwwwbwwwwwwwwww........", 
    "bbwwwwbwwwwwwbwwwwwwwwww........", 
    ".bwwwwbwwwwwwbwwwwwwwwb.........", 
    "bbwwwwbwwwwwwbwwwwwwwwbb...bb...", 
    "bbwwwwwwwwwwwwwwwwwwwwbb...bb...", 
    ".bwwwwwwwwyywwwwwwwwwwb.........", 
    "bbwwwwwwwwyywwwwwwwwwwbb...bb...", 
    ".bwwwwwwwwwwwwwwwwwwwwb.........",
    "..bwwwwwwwwwwwwwwwwwwb..........",
    "...bwwwwwwwwwwwwwwwwb...........",
    "....bbwwwwwwwwwwwwbb............",
    "......bbbbbbbbbbbb..............",
    ".....rrbrrrrrrbrr...............", # Shirt
    "....rrrboooooobrrr..............", # Overalls
    "...wrrroryylro yrrw.............", # Bowtie center?
    "...wrrroryylroyrrrw.............", 
    "...wrrroooooooorrw..............",
    "...wrrroooooooorrw..............",
    "....bbrobbbbborbb...............",
    "......bob....bob................", 
    "......bwb....bwb................",
    "......bbb....bbb................",
]

# Let's keep Male simple - basically same as Female body but no bow on head.
# The red shirt acts as a bowtie/collar effectively.

male_grid = [row.replace('p', 'w') for row in female_grid]

css_content = f"""
/* Female Hello Kitty Shadow */
.pixel-hello-kitty.female::before {{
    box-shadow: 
        {generate_shadow(female_grid)};
}}

/* Male Hello Kitty Shadow */
.pixel-hello-kitty.male::before {{
    box-shadow: 
        {generate_shadow(male_grid)};
}}
"""

with open('shadows.css', 'w') as f:
    f.write(css_content)

print("Shadows generated to shadows.css")
