
# paint algorithms (artificial artist) - CITY (yet lame), v1.0, Python version
# (c)2018 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz
# cre: 20180505
# upd: 20180506

# see:
# https://pillow.readthedocs.io/en/3.1.x/reference/ImageDraw.html
# http://pillow.readthedocs.io/en/5.1.x/reference/ImageFilter.html
# https://auth0.com/blog/image-processing-in-python-with-pillow/

# TODO:
# - ?
# - opt: clouds / diff buildings (styles) / no-flat land / roofs / chimneys / doors / details / day-night
# - from images? also like silver skyscrapers? also photoreallistic?
# - also 3d (perspective) / also 'nice' small towns


from PIL import Image, ImageDraw, ImageFilter
import random, math, string, os, sys
from bezier import make_bezier
from datetime import datetime as dt
from drawtools import *

def draw_one_block(draw, params, x0, y0, wn, hn, color):

    # main fill
    po = [(x0, y0),
          (x0, y0-hn),
          (x0+wn, y0-hn),
          (x0+wn, y0)]
    draw.polygon(po, fill=color, outline=None)

    v = params['v']
    v2 = 10

    cwx = 5
    cwy = 5
    winx = wn/(cwx+cwx+1)
    winy = hn*0.7/(cwy+cwy+1)

    # windows
    for n in range(cwy):
        for m in range(cwx):
            xw = x0+winx+winx*m*2
            yw = y0-hn*0.3-winy-winy*n*2
            po_w = [(xw, yw),
                  (xw, yw-winy),
                  (xw+winx, yw-winy),
                  (xw+winx, yw)]
            draw.polygon(po_w, fill=(0,0,0), outline=None)
            for m in range(4):
                po_w[:] = [(xy[0]+random.randint(0, v2)-random.randint(0, v2), xy[1]+random.randint(0, v2)-random.randint(0, v2)) for xy in po_w]
                rr = random.randint(0, 48)
                draw.line(po_w, fill=(rr, rr, rr), width=params['pw'])

    # door/entry
    dw = wn/4
    dh = hn/9
    po_w = [(x0+dw*1.5, y0),
          (x0+dw*1.5, y0-dh),
          (x0+dw*1.5+dw, y0-dh),
          (x0+dw*1.5+dw, y0)]
    draw.polygon(po_w, fill=(0,0,0), outline=None)
    for m in range(4):
        po_w[:] = [(xy[0]+random.randint(0, v2)-random.randint(0, v2), xy[1]+random.randint(0, v2)-random.randint(0, v2)) for xy in po_w]
        rr = random.randint(0, 48)
        draw.line(po_w, fill=(rr, rr, rr), width=params['pw'])

    # contour
    for m in range(params['m']):
        po[:] = [(xy[0]+random.randint(0, v)-random.randint(0, v), xy[1]+random.randint(0, v)-random.randint(0, v)) for xy in po]
        rr = random.randint(0, 48)
        draw.line(po, fill=(rr, rr, rr), width=params['pw'])

def city1(params, fn):
    start_time = dt.now()
    w = params['w']
    h = params['h']
    print('city1...', fn)
    random.seed()
    im = Image.new('RGB', (w, h), params['bg'])
    draw = ImageDraw.Draw(im)

    x0 = -w*0.05
    y0 = h*0.85

    imc = Image.open('cloud001.png')
    cc = random.randint(0, 50)
    for c in range(cc):
        position = (random.randint(-200, w*2+200), random.randint(-200, int(h/2)))
        r = random.randint(-10, 10)
        imc_rot = imc.rotate(r)
        im.paste(imc_rot, position, imc_rot)

    for n in range(params['n']):
        wn = random.randint(500, 1000)
        hn = random.randint(500, 1500)
        r = 0
        g = 0
        b = 0
        if params['r1'] > 0:
            r = random.randint(params['r0'], params['r1'])
        if params['g1'] > 0:
            g = random.randint(params['g0'], params['g1'])
        if params['b1'] > 0:
            b = random.randint(params['b0'], params['b1'])
        color = (r, g, b)
        draw_one_block(draw, params, x0, y0, wn, hn, color)
        if random.randint(0, 100) > 80:
            spc = random.randint(0, 250)
        else:
            spc = 0
        x0 = x0 + wn + spc

    draw.polygon([(0,h), (0,y0), (w,y0), (w,h)], fill=(60,60,60), outline=None)

    im.save(fn)
    time_elapsed = dt.now() - start_time
    print('done. elapsed time: {}'.format(time_elapsed))


#        circle(draw, po[0][0], po[0][1], random.randint(200, 800), fill=color, outline=None)
#        triangle(draw, po, fill=color, outline=None)
#        draw.polygon(po, fill=color, outline=None)

# ---

def do_city1(cnt, w, h, odir):

    params1 = {
        'w': w, 'h': h, 'bg': (24, 224, 255),
        'pw': 5,
        'v': 20,
        'n': 20,
        'm': 10,
        'r0': 128,
        'g0': 192,
        'b0': 64,
        'r1': 256,
        'g1': 256,
        'b1': 192,
    }

    for n in range(cnt):
        city1(params1, odir+'city1-%dx%d-01-%03d.png' % (w, h, n+1))

# ---

def main():
    start_time = dt.now()
    cnt = 5
    ca = get_canvas('A3')
    w = ca[0]
    h = ca[1]
    do_city1(cnt, w, h, '')

    #do_city1(1, 16384, 2200, '')
    
    time_elapsed = dt.now() - start_time
    print('ALL done. elapsed time: {}'.format(time_elapsed))


if __name__ == '__main__':
    main()
