from PIL import Image, ImageDraw, ImageFont

def script_it(draw, xy, font, size, fill):
    fnt = ImageFont.truetype(font, size)
    draw.text(xy, "Noniewicz.art.pl", font=fnt, fill=fill)

img = Image.new('RGB', (800, 600), color = (0, 0, 0))
d = ImageDraw.Draw(img)
# 'arial.ttf'

for i in range (19):
    script_it(d, (4+i*7, 4+i*i*1.6), font='times.ttf', size=10+i*3, fill=(224, 80+i*6, 0))

img.save('pil_text_font2.png')
