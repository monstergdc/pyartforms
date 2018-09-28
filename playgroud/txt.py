from PIL import Image, ImageDraw, ImageFont

def script_it(draw, xy, font, size, fill):
    fnt = ImageFont.truetype(font, size)
    draw.text(xy, "Noniewicz.art.pl", font=fnt, fill=fill)

img = Image.new('RGB', (300, 50), color = (0, 0, 0))
d = ImageDraw.Draw(img)
# 'arial.ttf'
script_it(d, (2, 0), font='times.ttf', size=42, fill=(255, 255, 0))

img.save('pil_text_font.png')
