#! /usr/bin/env python
# -*- coding: utf-8 -*-

# PyArtForms - Python generative art forms paint algorithms (artificial artist)
# collage builder, v1.0
# (c)2021 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz
# cre: 20210508, 09, 10, 15

# pip install colorthief

# TODO:
# - manage pool of 'same' map pix - swap randomly from the same
# - issue with round err and lame lines - de facto ratio issue
# - issue with ratio src v dst
# - some collor scalling to better fit?
# - ?

"""
IDEA:
+1. scan img folder
+- get all / resize + crop / build new x*y mosaic
+- map of dominant color
+- save
2. get src image / get mosaic
3. foreach pix src
- find best match in moisac
- put big pixel
4. save
"""

from PIL import Image, ImageDraw
import numpy as np
import random, math, string, os, sys
from os import walk
import binascii
import json
from colorthief import ColorThief # for dominant color, https://github.com/fengsp/color-thief-py



def prepare_map(params):
    print('prepare_map:', params)
    root = params['folder']
    outmap = params['outmap']
    one = int(params['one'])
    # scan folder for src images
    src = []
    for r, d, f in os.walk(root): # r=root, d=directories, f = files
        for file in f:
            if file.endswith("JPG") or file.endswith("PNG") or file.endswith("jpg") or file.endswith("png"): # jpg/png only
                src.append(os.path.join(r, file))
    n = len(src)
    dim = int(math.sqrt(n))+1 #note: +1 fix
    print('total src images:', n, 'box dim:', dim)

    #resize + crop + map
    bimg = [[None for x in range(dim)] for y in range(dim)]
    dc = [[None for x in range(dim)] for y in range(dim)] # dominating color?
    x = 0
    y = 0
    for i in range(n):
        msg = ""
        try:
            image = Image.open(src[i]).convert("RGBA")
            msg += 'loaded %d/%d [%s]' % (i+1, n, src[i])
        except:
            print("Error opening source image:", params['infile'])
            continue # just skip bad and continue
        w = image.size[0]
        h = image.size[1]
        d = w
        if h < d:
            d = h
        sc = 1.0
        if d > one:
            sc = one/float(d)
        else:
            if d < one:
                sc = one/float(d)
        bimg[y][x] = image
        image = None
        nw = int(bimg[y][x].width*sc)
        nh = int(bimg[y][x].height*sc)
        bimg[y][x] = bimg[y][x].resize((nw, nh), resample=Image.BICUBIC, box=None)
        dw = int((nw - one) / 2)
        dh = int((nh - one) / 2)
        box = (dw, dh, dw+one-1, dh+one-1)
        bimg[y][x] = bimg[y][x].crop(box)
        msg += ' resize: (%dx%d)->(%dx%d)->(%dx%d)' % (w, h, nw, nh, bimg[y][x].width, bimg[y][x].height)

        #opt also by average (better in fact)
        if False:
            bimg[y][x].save('tmp-image.png', dpi=(300,300))
            color_thief = ColorThief('tmp-image.png')
            dominant_color = color_thief.get_color(quality=1)
            colour = binascii.hexlify(bytearray(int(c) for c in dominant_color)).decode('ascii')
            print(msg, 'dominant_color', dominant_color, '#'+colour)
            dc[y][x] = dominant_color
        if True:
            img2 = bimg[y][x].resize((1, 1), resample=Image.BICUBIC, box=None)
            dc[y][x] = img2.getpixel((0, 0))
            print(msg, 'avg_color', dc[y][x])

        x += 1
        if x == dim:
            x = 0
            y += 1

    # make map as one big image
    print('make map')
    w = dim * one
    h = dim * one
    img = Image.new('RGBA', (w, h), color = (0, 0, 0))
    for y in range(dim):
        for x in range(dim):
            position = (x*one, y*one)
            item = bimg[y][x]
            if item != None:
                img.paste(item, position, item)

    # save map
    print('save...')
    img.save(outmap, dpi=(300,300))
    with open(outmap+"-dominant_color_map.json", 'w') as filehandle:
        json.dump(dc, filehandle)

def get_tile(outmap, outmap_data, cin): # works by color, or luminosity
    color_diffs = []
    if len(cin) == 4:
        r, g, b, a = cin # watch out for alpha
    else:
        if len(cin) == 3:
            r, g, b = cin
        else: #grayscale?
            r = cin
            g = cin
            b = cin
    for y in range(len(outmap_data)):
        row = outmap_data[y]
        for x in range(len(row)):
            c = outmap_data[y][x]
            if c is None:
                continue
            if len(c) == 4:
                cr, cg, cb, a = c
            else:
                if len(c) == 3:
                    cr, cg, cb = c
            color_diff = math.sqrt(abs(r - cr)**2 + abs(g - cg)**2 + abs(b - cb)**2)
            color_diffs.append((color_diff, x, y))
            #print('debug:', y, x, c)
    mx = min(color_diffs)[1]
    my = min(color_diffs)[2]
    #print('debug: cin:', cin, mx, my, min(color_diffs)[0])
    return mx, my

def make_collage(params):
    print('make_collage:', params)
    random.seed()
    if not 'w' in params or not 'h' in params or not 'one' in params:
        print("No w, h or one in params")
        return
    w = int(params['w'])
    h = int(params['h'])
    one = int(params['one'])
    if h <= 0:
        print("Destination height must be > 0")
        return
    if w <= 0:
        print("Destination width must be > 0")
        return
    if 'bk' in params:
        bk = params['bk']
    else:
        bk = (0,0,0)

    x0 = 0
    y0 = 0
    x1 = 0
    y1 = 0
    if 'x0' in params:
        x0 = params['x0']
    if 'y0' in params:
        y0 = params['y0']
    if 'x1' in params:
        x1 = params['x1']
    if 'y1' in params:
        y1 = params['y1']

    #todo: chk for infile outfile outmap outmap-json

    try:
        src = Image.open(params['infile'])
    except:
        print("Error opening source image:", params['infile'])
        return
    try:
        outmap = Image.open(params['outmap'])
    except:
        print("Error opening outmap image:", params['outmap'])
        return
    try:
        fn_json = params['outmap']+"-dominant_color_map.json"
        with open(fn_json) as f:
          outmap_data = json.load(f)
        #print(outmap_data)
    except:
        print("Error opening outmap json:", fn_json)
        return

    srcw = src.width-x0-x1
    srch = src.height-y0-y1
    print('src:', srcw, srch, 'dst:', w, h, 'map:', outmap.width, outmap.height, 'working...')
    img = Image.new('RGB', (w, h), color = bk)
    d = ImageDraw.Draw(img)
    dx = w/srcw
    dy = h/srch # todo: opt fix for aspect ratio here?

    for x in range(srcw):
        #print('x', x+1, 'of', srcw)
        if x % 10 == 0:
            print('%0.2f %s' % (x/srcw*100, '%'))
        for y in range(srch):
            cin = src.getpixel((x+x0, y+y0))
            if len(cin) >= 3 and cin[0] == bk[0] and cin[1] == bk[1] and cin[2] == bk[2]: # skip bk
                continue
            ox, oy = get_tile(outmap, outmap_data, cin) # map color -> item from outmap
            box = (ox*one, oy*one, (ox+1)*one-1, (oy+1)*one-1)
            b = outmap.crop(box)
            b = b.resize((int(dx), int(dy)), resample=Image.BICUBIC, box=None)
            position = (int(x*dx), int(y*dy))
            img.paste(b, position, b)

    outfile = params['outfile']
    print('saving', outfile, '...')
    img.save(outfile, dpi=(300,300))

# ---

def test():

# - #1

    folder = '.\\map-in-1\\'
    outmap = '.\\outmap.png'
    infile = '.\\repixel-in\\38a.jpg'
    outfile = 'mosaic-1.png'
    one = 80
    w = one*160
    h = one*178

#'A2': (7015, 4960), 'A1': (9933, 7015), 'A0': (14043, 9933),
#14043 / 9933 = 1.41377227423739

    params1 = {'folder': folder, 'outmap': outmap, 'one': one}
    params2 = {'w': w, 'h': h, 'bk': (0, 0, 0), 'infile': infile, 'outfile': outfile, 'outmap': outmap, 'one': one}
#    prepare_map(params1)
#    make_collage(params2)

# - #2

    if True:
        folder = '.\\map-in-2\\'
        outmap = '.\\outmap2.png'
        outfile = 'mosaic-2.png'
        one = 56
        infile = '.\\me-src1.png'
        w = one*238
        h = one*266
        params1 = {'folder': folder, 'outmap': outmap, 'one': one}
        params2 = {'w': w, 'h': h, 'bk': (255, 255, 255), 'infile': infile, 'outfile': outfile, 'outmap': outmap, 'one': one}
        prepare_map(params1)
        make_collage(params2)

# ---

if __name__ == '__main__':
    test()

# EOF
