#!/usr/bin/env python3
"""Draw entry.png for make.fun news-image-20261125.
One 1024x1024 infographic summarising world news of Wed 25 Nov 2026.
News verified 25 Nov 2026 (CST) against: Japan Times, SCMP, The Hindu
(NYT), Yeni Safak, Daily Summary of World, Principia News, Open Chronicle.
Run: python3 build_image.py  -> writes entry.png (1024x1024, <1 MiB).
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BG = (246, 241, 231)      # cream paper
INK = (16, 35, 63)        # navy
RED = (178, 34, 34)
GOLD = (176, 141, 87)
GREY = (74, 74, 74)
CARD = (255, 255, 255)
NAVY = (16, 35, 63)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

def wrap(draw, text, fnt, max_w):
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

STORIES = [
    ("SPACE", (31, 111, 183),
     "China flies first Pakistani astronaut to Tiangong",
     "Shenzhou-24 carries Zeeshan Ali, the first Pakistani \u2014 and first "
     "foreign astronaut \u2014 to China's Tiangong station."),
    ("CHINA", (178, 34, 34),
     "Beijing investigates Shanghai party chief",
     "Chen Jining, a Politburo member and rising star, is probed for "
     "\u201csevere violations of discipline and laws\u201d."),
    ("MIDDLE EAST", (176, 120, 20),
     "Riyadh tower hit again; 11 injured",
     "A second Houthi strike in under a week hits the Saudi capital's "
     "tallest tower. The Saudi-led coalition hits Hodeidah port."),
    ("EUROPE", (90, 60, 140),
     "Overnight strikes kill 3 in Russia and Ukraine",
     "Attacks hit Kyiv, Kharkiv, Zaporizhzhia and Samara. Kyiv says it "
     "needs \u20ac115bn in foreign aid for 2027."),
    ("AMERICAS", (0, 128, 96),
     "Colombia frees all supermarket hostages",
     "Security forces storm a Cartagena supermarket, rescue every "
     "remaining hostage and kill one captor."),
    ("TECH & TRADE", (200, 80, 20),
     "US jury convicts Huawei of trade-secret theft",
     "Huawei is found guilty of conspiring to steal trade secrets and "
     "of bank fraud; it is acquitted of racketeering."),
]

FOOTER = ("ALSO ON 25 NOVEMBER:  Bangladesh raises the garment wage "
          "36% to 17,000 taka  \u2022  Rescuers search for miners in a flooded "
          "Indonesian mine  \u2022  North Korea expels Swiss envoy in Pyongyang")

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# --- masthead ---
d.rectangle([0, 0, W, 148], fill=NAVY)
d.text((36, 22), "THE WORLD IN ONE DAY", font=font(BOLD, 52), fill=(255, 255, 255))
d.text((36, 92), "WEDNESDAY  \u00b7  25 NOVEMBER 2026", font=font(BOLD, 30), fill=(232, 197, 120))
d.rectangle([0, 148, W, 154], fill=RED)
d.text((36, 168), "Six stories that defined the day \u2014 space, power, war, rescue and trade",
       font=font(REG, 22), fill=GREY)

# --- story grid: 2 cols x 3 rows ---
x0, y0 = 28, 212
cw, ch, gx, gy = 474, 208, 20, 16
for i, (tag, colour, head, body) in enumerate(STORIES):
    x = x0 + (i % 2) * (cw + gx)
    y = y0 + (i // 2) * (ch + gy)
    d.rounded_rectangle([x, y, x + cw, y + ch], radius=10, fill=CARD,
                        outline=(210, 200, 180), width=1)
    d.rectangle([x, y + 10, x + 9, y + ch - 10], fill=colour)
    d.text((x + 26, y + 16), tag, font=font(BOLD, 18), fill=colour)
    hl = wrap(d, head, font(BOLD, 27), cw - 52)
    yy = y + 46
    for ln in hl[:2]:
        d.text((x + 26, yy), ln, font=font(BOLD, 27), fill=INK)
        yy += 33
    bl = wrap(d, body, font(REG, 20), cw - 52)
    for ln in bl[:3]:
        d.text((x + 26, yy), ln, font=font(REG, 20), fill=(40, 40, 40))
        yy += 27

# --- footer ---
fy = y0 + 3 * ch + 2 * gy + 18  # 886
d.rectangle([0, fy, W, fy + 96], fill=NAVY)
d.text((36, fy + 12), "ALSO ON 25 NOVEMBER", font=font(BOLD, 19), fill=(232, 197, 120))
fl = wrap(d, FOOTER[len("ALSO ON 25 NOVEMBER:  "):], font(REG, 19), W - 72)
yy = fy + 40
for ln in fl[:2]:
    d.text((36, yy), ln, font=font(REG, 19), fill=(255, 255, 255))
    yy += 25
d.text((36, H - 26), "Sources: Japan Times, South China Morning Post, The Hindu, Yeni Safak, "
       "Daily Summary of World, Principia \u2014 25 Nov 2026",
       font=font(REG, 13), fill=(120, 110, 95))

img.save("entry.png", optimize=True)
print("saved entry.png", img.size)
