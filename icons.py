# osu! Mod Icons Generator

import yaml
from PIL import Image, ImageDraw, ImageFont, ImageOps

def draw_text_border(draw, x, y, text, font, color):
    draw.text((x-1, y-1), text, font=font, fill=color)
    draw.text((x+1, y+1), text, font=font, fill=color)
    draw.text((x-1, y-1), text, font=font, fill=color)
    draw.text((x+1, y+1), text, font=font, fill=color)
    return draw

with open('input.yaml', 'r') as f:
    config = yaml.load(f)

for name, mode in config['icons'].items():
    icon = Image.open('template.png').convert('RGBA')

    WIDTH = icon.size[0]
    HEIGHT = icon.size[1]

    draw = ImageDraw.Draw(icon)
    draw.rectangle([0, 0, 75, 75], mode['bg_color'])

    font = ImageFont.truetype('fonts/{}'.format(config['font']), 45)
    w, h = font.getsize(mode['text'])

    # For some reason the font won't center correctly 
    x = (WIDTH - w)/2
    y = (HEIGHT - h)/2 - config['center_adj']
    draw_text_border(draw, x, y, mode['text'], font, mode['text_shadow_color'])
    draw.text((x, y), mode['text'], font=font, fill=mode['text_color'])

    icon = ImageOps.expand(icon, border=config['border_thickness'], fill=mode['border_color'])


    icon.save('output/selection-mod-{}.png'.format(mode['name']))
