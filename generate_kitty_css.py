def generate_box_shadow(grid, pixel_size=4):
    shadows = []
    height = len(grid)
    width = len(grid[0])
    
    colors = {
        '.': 'transparent',
        'w': 'var(--pixel-white)',
        'b': 'var(--pixel-black)',
        'r': '#ff0000',
        'y': '#ffcc00',  # Yellow for nose/buttons
        'p': '#ff1493',  # Pink for bow
        'l': '#00aaff',  # Blue for overalls
    }
    
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char in colors and colors[char] != 'transparent':
                # grid x,y maps to x*size, y*size
                shadows.append(f"{x * pixel_size}px {y * pixel_size}px 0 {colors[char]}")
                
    return ",\n        ".join(shadows)

# Reference based strictly on the user's provided Hello Kitty pixel art image
# Head: Wide oval, black eyes far apart, yellow nose, whiskers (black lines)
# Body: Red shirt, Blue overalls, Yellow buttons
# Female: Pink bow
# Male: No bow (or red bowtie if requested, but standard HK male often just looks like HK or has different hair/outfit. User asked for Male/Female HK. I'll give Male a blue hat or just plain).
# Actually, standard "Daniel" (Dear Daniel) has spiky hair. But user just said "Male Hello Kitty". I'll stick to Red Bowtie for Male.

# 30x26 grid roughly
common_body = [
    "..............................",
    "..............................",
    "..............................",
    "..............................",
    ".........bbbbbbbbbb...........",
    ".......bbwwwwwwwwwwbb.........",
    "......bwwwwwwwwwwwwwwb........",
    ".....bwwwwwwwwwwwwwwwwb.......",
    ".....bwwwwwwwwwwwwwwwwb.......",
    "....bwwwwwwwwwwwwwwwwwwb......",
    "....bwwwwwwwwwwwwwwwwwwb......",
    "bb..bwwwwwwwwwwwwwwwwwwb..bb..", # Whiskers start
    "bb..bwwbwwwwwwwwwwwwbwwb..bb..", # Eyes
    "....bwwbwwwwwwwwwwwwbwwb......", # Eyes
    "bb..bwwwwwwwwwwwwwwwwwwb..bb..", # Whiskers
    "bb..bwwwwwwwwwyywwwwwwwb..bb..", # Nose (yellow)
    "....bwwwwwwwwwyywwwwwwwb......",
    "bb..bwwwwwwwwwwwwwwwwwwb..bb..", # Whiskers
    "....bwwwwwwwwwwwwwwwwwwb......",
    ".....bwwwwwwwwwwwwwwwwb.......",
    "......bwwwwwwwwwwwwwwb........",
    ".......bbwwwwwwwwwwbb.........", # Neck
    ".........bbbbbbbbbb...........",
    ".........rrrrrrrrrr...........", # Shirt
    ".......rrbbbbbbbbbbrr.........",
    "......rrbllllllllllbrr........", # Overalls
    ".....wbblyyllllllyylbbw.......", # Buttons
    "....wwblyyllllllyylbww......",
    "....wwbllllllllllllbww......",
    "....wwbllllllllllllbww......",
    ".....bbbllbbbbbbllbbb.......", # Legs start
    ".......bllb....bllb.........",
    ".......bllb....bllb.........",
    ".......bbbb....bbbb.........",
]

# Female Head Modifier (Bow)
female_grid = [x for x in common_body]
# Add bow on right ear area (indices roughly x=18-26, y=2-8)
# I'll overlay the bow manually or adjust the grid. 

# Let's define the full grids explicitly to be safe.

# FEMALE HELLO KITTY (with Pink Bow)
female_art = [
    "..............................",
    "...........bbbbb.......bbbb...",
    ".........bbwwwwwbb...bbppppbb.",
    ".......bbwwwwwwwwwbb.bppppppb.",
    "......bwwwwwwwwwwwwwbppppppppb",
    ".....bwwwwwwwwwwwwwwwbppppppb.",
    ".....bwwwwwwwwwwwwwwbppppppbb.",
    "....bwwwwwwwwwwwwwwbppppppppbb",
    "....bwwwwwwwwwwwwwwbppppppbb..",
    "....bwwwwwwwwwwwwwwwbqqqqb....", # q is placeholder, just overwrote head line
    "bb..bwwbwwwwwwwwwwwwbmmb..bb..", # m is bow knot
    "bb..bwwbwwwwwwwwwwwwbwwb..bb..", 
    "....bwwbwwwwwwwwwwwwbwwb......", 
    "bb..bwwwwwwwwwwwwwwwwwwb..bb..", 
    "bb..bwwwwwwwwwwyywwwwwwb..bb..", 
    "....bwwwwwwwwwwyywwwwwwb......",
    "bb..bwwwwwwwwwwwwwwwwwwb..bb..", 
    "....bwwwwwwwwwwwwwwwwwwb......",
    ".....bwwwwwwwwwwwwwwwwb.......",
    "......bwwwwwwwwwwwwwwb........",
    ".......bbwwwwwwwwwwbb.........",
    "......rrbbbbbbbbbbrr..........",
    ".....rrrbrrrrrrrrbrrr.........", # Red Body/Arms
    "....wrrrbllllllllbrrww........", # Blue Overalls
    "....wrrbyyllllllyybrww........", # Buttons
    "....wrrbyyllllllyybrww........",
    "....wrrllllllllllllrrw........",
    "....wrrllllllllllllrrw........",
    ".....bbllbbbbbbllbbbb.........",
    ".......bllb....bllb...........",
    ".......bllb....bllb...........",
    ".......bbbb....bbbb...........",
]

# Fix the grid manually to be perfect
female_fixed = [
    "..............................",
    "......bbbbb..........bbbb.....", # Ears
    ".....bwwwwwb.......bbppppbb...", # Bow starts
    "....bwwwwwwwb.....bppppppppb..",
    "...bwwwwwwwwwb...bppppppppppb.",
    "..bwwwwwwwwwwwb..bppppppppppb.",
    "..bwwwwwwwwwwwwb..bppppppppb..",
    ".bwwwwwwwwwwwwwwb..bbppppbb...",
    ".bwwwwwwwwwwwwwwwb...bbbb.....",
    ".bwwwwwwwwwwwwwwwwb...........",
    "bbwwwwbwwwwwwbwwwwwbb...bb....", # Eyes and Whiskers
    "bbwwwwbwwwwwwbwwwwwbb...bb....", # Eyes and Whiskers
    ".bwwwwwwwwwwwwwwwwwb..........",
    "bbwwwwwwwwwwwwwwwwwbb...bb....", # Whiskers
    "bbwwwwwwwwyywwwwwwwbb...bb....", # Nose
    ".bwwwwwwwwyywwwwwwwb..........",
    "bbwwwwwwwwwwwwwwwwwbb...bb....", # Whiskers
    ".bwwwwwwwwwwwwwwwwwb..........",
    "..bwwwwwwwwwwwwwwwb...........",
    "...bwwwwwwwwwwwwwb............",
    "....bbwwwwwwwwwbb.............",
    "......bbbbbbbbb...............", # Neck
    ".....rrbrrrrbrr...............", # Shirt
    "....rrrrblllbrrrr.............", # Overalls start
    "...wrrrbyyllyybrrrw...........", # Buttons (yellow)
    "...wrrrbyyllyybrrrw...........",
    "...wrrrlllllllllrrw...........",
    "...wrrrlllllllllrrw...........",
    "....bbrllbbbbllrbb............",
    "......bllb..bllb..............", 
    "......bllb..bllb..............",
    "......bbbb..bbbb..............",
]

# Create mirrored male (no bow)
male_fixed = [
    "..............................",
    "......bbbbb..........bbbbb....", 
    ".....bwwwwwb........bwwwwwb...", 
    "....bwwwwwwwb......bwwwwwwwb..",
    "...bwwwwwwwwwb....bwwwwwwwwwb.",
    "..bwwwwwwwwwwwb..bwwwwwwwwwwwb",
    "..bwwwwwwwwwwwwbbwwwwwwwwwwwwb",
    ".bwwwwwwwwwwwwwwwwwwwwwwwwwwwwb",
    ".bwwwwwwwwwwwwwwwwwwwwwwwwwwwwb",
    ".bwwwwwwwwwwwwwwwwwwwwwwwwwwwwb",
    "bbwwwwbwwwwwwbwwwwwbwwwwbb..bb", 
    "bbwwwwbwwwwwwbwwwwwbwwwwbb..bb", 
    ".bwwwwwwwwwwwwwwwwwwwwwwb.....",
    "bbwwwwwwwwwwwwwwwwwwwwwwbb..bb", 
    "bbwwwwwwwwyywwwwwwwwwwwwbb..bb", 
    ".bwwwwwwwwyywwwwwwwwwwwwb.....",
    "bbwwwwwwwwwwwwwwwwwwwwwwbb..bb", 
    ".bwwwwwwwwwwwwwwwwwwwwwwb.....",
    "..bwwwwwwwwwwwwwwwwwwwwb......",
    "...bwwwwwwwwwwwwwwwwwwb.......",
    "....bbwwwwwwwwwwwwwwbb........",
    "......bbbbbbbbbbbbbb..........", 
    ".....rrbrrrrrrrrbrr...........", 
    "....rrrrbllllllbrrrr..........", 
    "...wrrrbyylyylbybrrrw.........", # Blue bowtie in middle? Or just overalls
    "...wrrrbyylyylbybrrrw.........",
    "...wrrrllllllllllrrw..........",
    "...wrrrllllllllllrrw..........",
    "....bbrllbbbbbbllrbb..........",
    "......bllb....bllb............", 
    "......bllb....bllb............",
    "......bbbb....bbbb............",
]


# I'll construct a simplified 24x26 approx version that is guaranteed to look cute
# Using a known "Hello Kitty" pixel pattern
# Reference: https://www.pinterest.com/pin/331929610162584852/ (visual memory)

def get_hk_grid(gender='female'):
    # H = Head/White, B = Border, S = Shirt/Red, O = Overalls/Blue, Y = Yellow, P = Pink Bow, T = Tie/Red
    
    # Common Head Shape
    head = [
        "      BBBBBB        BBBBBB      ",
        "     BHHHHHHB      BHHHHHHB     ",
        "    BHHHHHHHHB    BHHHHHHHHB    ",
        "   BHHHHHHHHHHB  BHHHHHHHHHHB   ",
        "  BHHHHHHHHHHHHBBHHHHHHHHHHHHB  ",
        "  BHHHHHHHHHHHHHHHHHHHHHHHHHHB  ",
        " BHHHHHHHHHHHHHHHHHHHHHHHHHHHHB ",
        " BHHHHHHHHHHHHHHHHHHHHHHHHHHHHB ",
        "BHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHB",
        "BHHHHHBBHHHHHHHHHHHHBBHHHHHHHHHB", # Eyes
        "BHHHHHBBHHHHHHHHHHHHBBHHHHHHHHHB",
        "BHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHB",
        "WHHHHHHHHHHHHYYHHHHHHHHHHHHHHHWH", # Nose + Whiskers (W=Whisker)
        " BHHHHHHHHHHHYYHHHHHHHHHHHHHHB ",
        "WHHHHHHHHHHHHHHHHHHHHHHHHHHHHHWH",
        " BHHHHHHHHHHHHHHHHHHHHHHHHHHHHB ",
        "  BHHHHHHHHHHHHHHHHHHHHHHHHHHB  ",
        "   BHHHHHHHHHHHHHHHHHHHHHHHHB   ",
        "    BBBBBBBBBBBBBBBBBBBBBBBB    ",
    ]
    
    # Body
    body = [
        "      BBBBSSSSSSSSSSSSBBBB      ",
        "    BBSSSSBHOOOOOOOOHBSSSSBB    ",
        "   BHHSSSSSBYYYYYYYYBSSSSSHHB   ", # Button
        "   BHHSSSSSOOOOOOOOOOSSSSSHHB   ",
        "   BHHSSSSSOOOOOOOOOOSSSSSHHB   ",
        "    BSSSSSSOOOOOOOOOOSSSSSSB    ",
        "     BBBBBBOOBBBBBBOOBBBBBB     ",
        "          BOOB    BOOB          ",
        "          BBBB    BBBB          ",
    ]
    
    # This is getting too complex to type.
    # Let's use a smaller, cuter 18x16 type grid.
    
    return []

# NEW STRATEGY: 
# Generating the CSS directly in the response using a proven pixel art string.

pixel_art_female = [
    "...........................",
    "...........XXXX......XXXX..", # Ears
    "..........XWWWWX....XXPPPPX", # W=White, P=Pink
    ".........XWWWWWWX..XPPPPPPX",
    "........XWWWWWWWWXXPPPPPPPX",
    "........XWWWWWWWWXPPPPPPPX.",
    ".......XWWWWWWWWXXPPPPPPX..",
    ".......XWWWWWWWWX..XPPXX...",
    "......XWWWWWWWWWWX..XX.....",
    "XX...XW.WXXXXWWWWWX........", # Eye (Left)
    "XX...XW.WXXXXWWWWWX........", 
    ".....XWWWWWWWWWWWWX........",
    "XX...XWWWWWWYYWWWWX........", # Nose
    "XX...XWWWWWWYYWWWWX........",
    ".....XWWWWWWWWWWWWX........",
    "XX...XWWWWWWWWWWWWX........", # Whiskers
    "XX...XW.WXXXXWWWWWX........", # Eye (Right) - wait eyes should be symmetrical
    # Backtrack. 
    # Let's use the code content to generate the exact CSS string.
]

print("Script placeholder")
