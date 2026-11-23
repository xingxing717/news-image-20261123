#!/usr/bin/env python3
"""Render the front page for Monday 23 November 2026.

Pure Pillow drawing, no network, no randomness, no timestamps:
two runs produce byte-identical output.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (248, 244, 236)
INK = (20, 20, 20)
MUTED = (90, 84, 74)
RED = (163, 22, 33)
NAVY = (31, 58, 95)
TEAL = (15, 118, 110)
GOLD = (176, 132, 52)
RULE = (180, 172, 156)
PANEL = (255, 255, 255)
SEA = (38, 84, 124)
SEA_DARK = (24, 60, 96)
SKY = (214, 228, 238)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"

def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)

F_SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)
F_SANS = lambda s: font("DejaVuSans.ttf", s)
F_SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)

def wrap(text, fnt, max_w, draw):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def draw_icon(draw, kind, cx, cy, s, color):
    """Tiny flat glyph, centred on (cx, cy), size s."""
    if kind == "flame":  # Middle East: oil flame
        draw.polygon([(cx, cy - s), (cx + s * 0.55, cy + s * 0.1),
                      (cx + s * 0.25, cy + s * 0.55), (cx - s * 0.25, cy + s * 0.55),
                      (cx - s * 0.55, cy + s * 0.1)], fill=color)
        draw.ellipse([cx - s * 0.22, cy + s * 0.15, cx + s * 0.22, cy + s * 0.6],
                     fill=(255, 255, 255))
    elif kind == "dome":  # Europe
        draw.pieslice([cx - s * 0.7, cy - s * 0.7, cx + s * 0.7, cy + s * 0.5],
                      180, 360, fill=color)
        draw.rectangle([cx - s * 0.7, cy + s * 0.1, cx + s * 0.7, cy + s * 0.6],
                       fill=color)
        draw.rectangle([cx - s * 0.75, cy + s * 0.6, cx + s * 0.75, cy + s * 0.72],
                       fill=color)
    elif kind == "temple":  # Asia
        draw.polygon([(cx - s * 0.8, cy - s * 0.2), (cx + s * 0.8, cy - s * 0.2),
                      (cx + s * 0.5, cy - s * 0.55), (cx - s * 0.5, cy - s * 0.55)],
                     fill=color)
        draw.rectangle([cx - s * 0.6, cy - s * 0.2, cx + s * 0.6, cy + s * 0.6],
                       fill=color)
        draw.rectangle([cx - s * 0.7, cy + s * 0.6, cx + s * 0.7, cy + s * 0.72],
                       fill=color)
    elif kind == "tree":  # Africa: acacia
        draw.rectangle([cx - s * 0.08, cy - s * 0.1, cx + s * 0.08, cy + s * 0.75],
                       fill=color)
        draw.ellipse([cx - s * 0.85, cy - s * 0.75, cx + s * 0.85, cy - s * 0.05],
                     fill=color)
    elif kind == "star":  # Americas
        pts = []
        import math
        for i in range(10):
            ang = -math.pi / 2 + i * math.pi / 5
            r = s * 0.75 if i % 2 == 0 else s * 0.32
            pts.append((cx + r * math.cos(ang), cy + r * math.sin(ang)))
        draw.polygon(pts, fill=color)
    elif kind == "chart":  # Markets & tech
        bars = [0.45, 0.8, 0.6, 1.0]
        for i, h in enumerate(bars):
            x0 = cx - s * 0.8 + i * s * 0.45
            draw.rectangle([x0, cy + s * 0.6 - h * s * 1.1, x0 + s * 0.3,
                            cy + s * 0.6], fill=color)
    elif kind == "ball":  # Sport & culture
        draw.ellipse([cx - s * 0.7, cy - s * 0.7, cx + s * 0.7, cy + s * 0.7],
                     outline=color, width=3)
        draw.polygon([(cx, cy - s * 0.3), (cx + s * 0.3, cy - s * 0.05),
                      (cx + s * 0.18, cy + s * 0.3), (cx - s * 0.18, cy + s * 0.3),
                      (cx - s * 0.3, cy - s * 0.05)], fill=color)

# ---------------------------------------------------------------- stories
# (lead, detail) — every story happened or was first reported 23 Nov 2026.
SECTIONS = [
    ("MIDDLE EAST", "flame", RED, [
        ("Two tankers hit mines in Hormuz",
         "Shipping attacks at wartime high"),
        ("US, Libya sign aviation, minerals deals",
         "Aviation and rare-minerals deals"),
        ("UN urges probe into Benghazi attacks",
         "Mission calls for independent inquiry"),
        ("Iran says it downed a US drone",
         "20th MQ-1 Predator claimed by IRGC"),
        ("Settler arson is \u201cJewish terrorism\u201d",
         "PM-elect condemns West Bank attacks"),
    ]),
    ("EUROPE", "dome", NAVY, [
        ("Russian strike kills 11 in Dymer",
         "14 missing near Kyiv after attack"),
        ("Russia violated Polish airspace",
         "NATO council meets in Brussels"),
        ("Poland: Russia tried twice to kill rapper",
         "Targeted in Poland and Denmark"),
        ("Russia \u2018plans nuclear-armed satellite\u2019",
         "German media report NATO finding"),
        ("Ukraine hits Russian oil sites",
         "Drones strike Rostov, Perm, Tatarstan"),
        ("Belgrade floods in record rain",
         "12 hours of rain beat monthly norm"),
    ]),
    ("ASIA", "temple", TEAL, [
        ("Seoul minister quits over AI cheating",
         "Exam chaos after AI cheating scam"),
        ("Kospi slides as chip stocks fall",
         "Asian markets hit by Wall Street rout"),
        ("Thai court upholds MP conviction",
         "Royal-defamation term cut to 3 years"),
        ("Bangladesh: Hasina faces jail if she returns",
         "Minister: ex-PM would be arrested"),
        ("China warns citizens off Mt Fuji",
         "$75,000 reward for missing climber"),
        ("South Korea\u2019s Lee reshuffles cabinet",
         "Surprise shake-up announced Monday"),
    ]),
    ("AFRICA", "tree", (122, 90, 20), [
        ("Sudan drones kill 4 near Khartoum",
         "UN building hit; airport targeted"),
        ("Fighting traps Ebola teams in Congo",
         "WHO: staff sheltered over 24 hours"),
        ("Kenya and DR Congo restore ties",
         "Ambassadors return after friction"),
        ("ECOWAS defence chiefs meet",
         "Regional security talks open Monday"),
        ("Rebel attack kills 15 in South Sudan",
         "Civilians, herders die in Warrap"),
    ]),
    ("THE AMERICAS", "star", (90, 40, 110), [
        ("Trump curbs Congress\u2019s access to agencies",
         "Order demands a \u201clegislative purpose\u201d"),
        ("Storms threaten Thanksgiving travel",
         "Airline glitches add to holiday chaos"),
        ("Trump defers to court on Iowa blast",
         "Army told not to detonate chemicals"),
        ("Two states sue SpaceX over AI claims",
         "Oregon, Virginia allege deception"),
        ("Waymo pauses Bay Area service",
         "Stormy Thanksgiving week forecast"),
        ("Amtrak derails in Louisiana",
         "Train hits truck; 5 people injured"),
    ]),
    ("MARKETS & TECH", "chart", GOLD, [
        ("Nasdaq futures jump about 3%",
         "Holiday week opens after Friday rout"),
        ("Epstein probe details Russia links",
         "Expert challenges suicide ruling"),
        ("LS Cable starts $476m New York job",
         "Cables for New York grid expansion"),
    ]),
    ("SPORT & CULTURE", "ball", (168, 60, 90), [
        ("Skubal agrees record $450m Mets deal",
         "Biggest contract ever for a pitcher"),
        ("Tom Jackson dies at 75",
         "Ex-Bronco became ESPN analyst"),
        ("Saudi Arabia stun France 1-0",
         "Late goal wins U-17 group clash"),
        ("Olympians mark 70 years since Melbourne 1956",
         "Ceremony recalls landmark Games"),
        ("Steinfeld back as Kate Bishop",
         "Marvel confirms Doomsday return"),
    ]),
]

HEADLINE_KICKER = "UKRAINE \u2022 LIBYA \u2014 THE BIG STORY"
HEADLINE = "KYIV SAYS ITS SEA DRONES SANK RUSSIAN WARSHIP OFF LIBYA"
HEADLINE_DECK = ("Zelenskyy says seven naval drones sank the corvette Merkury "
                 "at Benghazi; Libyan officials say it was heavily damaged. "
                 "A weapons cargo ship was hit and a Ka-27 helicopter destroyed.")

def draw_headline_art(draw, x0, y0, x1, y1):
    """Flat-vector illustration: a listing warship, a sea drone, the Libyan coast."""
    draw.rectangle([x0, y0, x1, y1], fill=SKY)
    # sun
    draw.ellipse([x1 - 78, y0 + 14, x1 - 34, y0 + 58], fill=(240, 196, 90))
    # distant coast
    draw.polygon([(x0, y0 + 118), (x0 + 90, y0 + 96), (x0 + 190, y0 + 112),
                  (x0 + 260, y0 + 98), (x1, y0 + 116), (x1, y0 + 132),
                  (x0, y0 + 132)], fill=(150, 160, 140))
    # sea
    draw.rectangle([x0, y0 + 132, x1, y1], fill=SEA)
    draw.rectangle([x0, y0 + 132, x1, y0 + 140], fill=(90, 140, 180))
    # wave lines
    for wy, wx0, wx1 in [(y0 + 168, x0 + 20, x0 + 130), (y0 + 186, x1 - 150, x1 - 30),
                         (y0 + 200, x0 + 90, x0 + 210)]:
        draw.line([(wx0, wy), (wx1, wy)], fill=(140, 180, 210), width=3)
    # capsized / listing corvette (hull tilted, bow down)
    hull = [(x0 + 52, y0 + 156), (x0 + 196, y0 + 138), (x0 + 208, y0 + 152),
            (x0 + 176, y0 + 168), (x0 + 66, y0 + 178)]
    draw.polygon(hull, fill=(96, 98, 104))
    draw.line([(x0 + 60, y0 + 168), (x0 + 188, y0 + 152)], fill=RED, width=3)
    draw.polygon([(x0 + 120, y0 + 138), (x0 + 138, y0 + 136),
                  (x0 + 140, y0 + 122), (x0 + 124, y0 + 124)], fill=(70, 72, 78))
    draw.line([(x0 + 132, y0 + 124), (x0 + 132, y0 + 108)], fill=(70, 72, 78), width=3)
    draw.polygon([(x0 + 132, y0 + 108), (x0 + 146, y0 + 116), (x0 + 132, y0 + 118)],
                 fill=RED)
    # smoke plume rising from the ship
    draw.ellipse([x0 + 148, y0 + 96, x0 + 188, y0 + 126], fill=(120, 120, 122))
    draw.ellipse([x0 + 162, y0 + 76, x0 + 198, y0 + 106], fill=(150, 150, 152))
    draw.ellipse([x0 + 176, y0 + 58, x0 + 206, y0 + 84], fill=(178, 178, 180))
    # sea drone boat with wake
    draw.polygon([(x0 + 238, y0 + 176), (x0 + 288, y0 + 176), (x0 + 296, y0 + 186),
                  (x0 + 244, y0 + 186)], fill=(30, 30, 34))
    draw.rectangle([x0 + 258, y0 + 168, x0 + 272, y0 + 176], fill=(30, 30, 34))
    draw.line([(x0 + 238, y0 + 190), (x0 + 210, y0 + 194)], fill=(200, 220, 235), width=3)
    draw.line([(x0 + 244, y0 + 196), (x0 + 222, y0 + 200)], fill=(200, 220, 235), width=2)
    draw.rectangle([x0, y0, x1, y1], outline=INK, width=2)
    draw.rectangle([x0 + 2, y1 - 24, x1 - 2, y1 - 2], fill=NAVY)
    draw.text((x0 + 8, y1 - 21), "SEA DRONES OFF BENGHAZI",
              font=F_SANS_B(11), fill=(255, 255, 255))

def draw_section(draw, x0, y0, x1, y1, name, icon, color, stories):
    draw.rectangle([x0, y0, x1, y1], fill=PANEL, outline=RULE, width=1)
    # header band
    draw.rectangle([x0, y0, x1, y0 + 30], fill=color)
    draw_icon(draw, icon, x0 + 18, y0 + 15, 11, (255, 255, 255))
    draw.text((x0 + 34, y0 + 8), name, font=F_SANS_B(13), fill=(255, 255, 255))
    draw.text((x1 - 34, y0 + 9), str(len(stories)), font=F_SANS_B(12),
              fill=(255, 255, 255))
    y = y0 + 38
    lead_f, det_f = F_SANS_B(11), F_SANS(10)
    for lead, detail in stories:
        draw.rectangle([x0 + 10, y + 4, x0 + 14, y + 8], fill=color)
        lines = wrap(lead, lead_f, (x1 - x0) - 34, draw)
        for ln in lines[:2]:
            draw.text((x0 + 20, y), ln, font=lead_f, fill=INK)
            y += 14
        dlines = wrap(detail, det_f, (x1 - x0) - 34, draw)
        for ln in dlines[:1]:
            draw.text((x0 + 20, y), ln, font=det_f, fill=MUTED)
            y += 12
        y += 5

def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    # ---- masthead ----
    d.rectangle([0, 0, W, 96], fill=NAVY)
    d.text((24, 12), "THE WORLD IN ONE DAY", font=F_SERIF_B(46), fill=(255, 255, 255))
    d.text((24, 66), "MONDAY 23 NOVEMBER 2026", font=F_SANS_B(16), fill=(240, 196, 90))
    d.text((W - 24, 66), "37 STORIES \u2022 7 REGIONS", font=F_SANS_B(13),
           fill=(255, 255, 255), anchor="ra")
    d.line([(0, 96), (W, 96)], fill=GOLD, width=3)
    # ---- headline block ----
    d.text((24, 108), HEADLINE_KICKER, font=F_SANS_B(13), fill=RED)
    hx, hw = 24, 612
    lines = wrap(HEADLINE, F_SERIF_B(33), hw, d)
    y = 130
    for ln in lines:
        d.text((hx, y), ln, font=F_SERIF_B(33), fill=INK)
        y += 38
    y += 4
    for ln in wrap(HEADLINE_DECK, F_SANS(14), hw, d):
        d.text((hx, y), ln, font=F_SANS(14), fill=(52, 52, 52))
        y += 19
    draw_headline_art(d, 656, 112, 1000, 330)
    d.line([(16, 340), (1008, 340)], fill=RULE, width=2)
    # ---- region panels ----
    margin, gap = 16, 10
    row1_y, row1_h = 350, 318
    row2_y, row2_h = 678, 318
    w4 = (W - 2 * margin - 3 * gap) // 4
    w3 = (W - 2 * margin - 2 * gap) // 3
    for i, sec in enumerate(SECTIONS[:4]):
        x0 = margin + i * (w4 + gap)
        draw_section(d, x0, row1_y, x0 + w4, row1_y + row1_h, *sec)
    for i, sec in enumerate(SECTIONS[4:]):
        x0 = margin + i * (w3 + gap)
        draw_section(d, x0, row2_y, x0 + w3, row2_y + row2_h, *sec)
    # ---- footer ----
    d.text((W // 2, 1006),
           "All 37 stories happened or were first reported on Monday 23 November 2026",
           font=F_SANS(11), fill=MUTED, anchor="ma")
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img.save(out, "PNG", optimize=True)

if __name__ == "__main__":
    main()
