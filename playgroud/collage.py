#! /usr/bin/env python
# -*- coding: utf-8 -*-

# PyArtForms collage builder, v1.0
# (c)2021 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz
# cre: 20210508

# pip install colorthief

# TODO:
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

# ima = image_resize(ima, height = canvas[1])
# d = ImageDraw.Draw(img)
# cin = src.getpixel((x, y))

# ---

def prepare_map(root, outmap, one):
    # scan folder for src images
    src = []
    for r, d, f in os.walk(root): # r=root, d=directories, f = files
        for file in f:
            if file.endswith("JPG") or file.endswith("PNG") or file.endswith("jpg") or file.endswith("png"): # jpg/png only
                src.append(os.path.join(r, file))
    n = len(src)
    dim = int(math.sqrt(n))+1 #note: +1 fix
    print('total src images:', n, 'box dim:', dim)

    #resize + crop
    bimg = [[None for x in range(dim)] for y in range(dim)]
    dc = [[None for x in range(dim)] for y in range(dim)] # dominating color?
    x = 0
    y = 0
    for i in range(n):
        try:
            image = Image.open(src[i]).convert("RGBA")
            print('loaded', i+1, 'of', n, src[i])
        except:
            print("Error opening source image:", params['infile'])
            continue # skip bad and continue
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
        print('resize:', (w ,h), '->', (nw, nh), 'crop box:', box)
        bimg[y][x] = bimg[y][x].crop(box)

        bimg[y][x].save('tmp-image.png', dpi=(300,300))
        color_thief = ColorThief('tmp-image.png')
        dominant_color = color_thief.get_color(quality=1)
        colour = binascii.hexlify(bytearray(int(c) for c in dominant_color)).decode('ascii')
        print('dominant_color', dominant_color, colour)
        dc[y][x] = dominant_color

        x += 1
        if x == dim:
            x = 0
            y += 1

    # make map
    print('make map')
    w = dim * one
    h = dim * one
    bk = (0, 0, 0)
    img = Image.new('RGBA', (w, h), color = bk)
    for y in range(dim):
        for x in range(dim):
            position = (x*one, y*one)
            item = bimg[y][x]
            if item != None:
                print('paste at:', position)
                img.paste(item, position, item)

    # save map
    print('save...')
    img.save(outmap, dpi=(300,300))
    with open(outmap+"-dominant_color_map.json", 'w') as filehandle:
        json.dump(dc, filehandle)

def get_tile(outmap, outmap_data, cin): # todo: by color, but opt by luminosity
    color_diffs = []
    if len(cin) == 4:
        r, g, b, a = cin # watch out for alpha
    else:
        r, g, b = cin
    for y in range(len(outmap_data)):
        row = outmap_data[y]
        for x in range(len(row)):
            c = outmap_data[y][x]
            if c is None:
                continue
            cr, cg, cb = c
            color_diff = math.sqrt(abs(r - cr)**2 + abs(g - cg)**2 + abs(b - cb)**2)
            color_diffs.append((color_diff, x, y))
            #print('debug:', y, x, c)
    mx = min(color_diffs)[1]
    my = min(color_diffs)[2]
    #print('debug: cin:', cin, mx, my, min(color_diffs)[0])
    return mx, my

def make_collage(params):
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

    srcw = src.width
    srch = src.height
    img = Image.new('RGB', (w, h), color = bk)
    d = ImageDraw.Draw(img)
    dx = w/srcw
    dy = h/srch # todo: opt fix for aspect ratio here?

    for x in range(srcw):
        print('x', x+1, 'of', srcw)
        for y in range(srch):
            #print('pixel', 'x', x, 'y', y)
            cin = src.getpixel((x, y))
            ox, oy = get_tile(outmap, outmap_data, cin) # map color -> college item from outmap
            box = (ox*one, oy*one, (ox+1)*one-1, (oy+1)*one-1)
            b = outmap.crop(box)
            b = b.resize((int(dx), int(dy)), resample=Image.BICUBIC, box=None)
            position = (int(x*dx), int(y*dy))
            img.paste(b, position, b)

    outfile = params['outfile']
    img.save(outfile, dpi=(300,300))

# ---

if __name__ == '__main__':
    folder = '.\\00 src img ideas\\'
    outmap = '.\\outmap.png'
    one = 512

#    prepare_map(root=folder, outmap=outmap, one=one)

    # 'A2': (7015, 4960)
    params = {'w': 7015, 'h': 4960, 'bk': (0, 0, 0), 'infile': '.\\00 src img ideas\\Image2.png', 'outfile': 'mosaic-1.png', 'outmap': outmap, 'one': one}
    make_collage(params)

# EOF
