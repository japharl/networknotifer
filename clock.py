#!/usr/bin/env python

from PIL import ImageFont
import sys
from datetime import datetime

import inkyphat

colour = "red"

try:
    inkyphat.set_colour(colour)
except ValueError:
    print('Invalid colour "{}" for V{}\n'.format(colour, inkyphat.get_version()))
    if inkyphat.get_version() == 2:
        sys.exit(1)
    print('Defaulting to "red"')

font_file = inkyphat.fonts.FredokaOne
inkyphat.arc((0, 0, 212, 104), 0, 180, 2)

top = 0
left = 0
offset_left = 0
now = datetime.now()
dt = now.strftime("%m/%d/%Y %H:%M")
text = "Current Date & Time:\n"
text += dt
font_size=20
font = inkyphat.ImageFont.truetype(font_file, font_size)
width, height = font.getsize(text)
inkyphat.text((0, top), text, 1, font=font)

inkyphat.show()
