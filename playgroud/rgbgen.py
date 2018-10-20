#! /usr/bin/env python
# -*- coding: utf-8 -*-

# paint algorithms (artificial artist) - RGB generated, v1.0, Python version
# based on my FilterMeister plugin "GDC Singen 1.0" Copyright © 2011 Noniewicz.com
# (c)2018 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz
# cre: 20181020
# upd: 20181021

# see:
# https://pillow.readthedocs.io/en/3.1.x/reference/ImageDraw.html
# http://pillow.readthedocs.io/en/5.1.x/reference/ImageFilter.html
# https://auth0.com/blog/image-processing-in-python-with-pillow/

# TODO:
# - ?

from PIL import Image, ImageDraw, ImageFilter, ImageOps, ImageMath
import random, math, os, sys
from bezier import make_bezier
from datetime import datetime as dt
from drawtools import *


def rgbgen1(params, fn):
    start_time = dt.now()
    random.seed()
    w = params['w']
    h = params['h']
    print('rgbgen1...', fn)
    random.seed()
    im = Image.new('RGB', (w, h), params['bg'])
    draw = ImageDraw.Draw(im)

    # ForEveryPixel
    for y in range(h):
        for x in range(w):
            #r = int(y/2-y/3*math.sin(x*random.randint(1, 8)*math.pi/180))
            #g = int(x/2-x/2*math.cos(y*random.randint(1, 8)*math.pi/180))
            r1 = int(x*y/50)
            g1 = int(x*y/4/50)
            b1 = int(x*y/8/50)
            r2 = int((w-x)*(h-y)/50)
            g2 = int((w-x)*(h-y)/4/50)
            b2 = int((w-x)*(h-y)/8/50)
            # diff w/ mirr+flip!
            r = r1 ^ r2
            g = g1 ^ g2
            b = b1 ^ b2
            draw.point((x, y), fill=(r&255, g&255, b&255))

    #im = im.filter(ImageFilter.BLUR)
    #im = im.filter(ImageFilter.BLUR)
    #im = im.filter(ImageFilter.BLUR)
    #im = im.filter(ImageFilter.SHARPEN)
    im.save(fn)
    show_benchmark(start_time)

def rgbgen(params, fn):
    start_time = dt.now()
    random.seed()
    w = params['w']
    h = params['h']
    s = params['s']
    print('rgbgen...', fn)
    random.seed()
    im = Image.new('RGB', (w, h), params['bg'])
    draw = ImageDraw.Draw(im)

    # ForEveryPixel
    for y in range(h):
        for x in range(w):
            r = int(x*y/50)
            g = int(x*y/4/50)
            b = int(x*y/8/50)
            draw.point((x, y), fill=(r&255, g&255, b&255))
    im2 = ImageOps.flip(ImageOps.mirror(im))
    rgb1 = im.split()
    rgb2 = im2.split()
    r_out = ImageMath.eval(s, a=rgb1[0], b=rgb2[0])
    g_out = ImageMath.eval(s, a=rgb1[1], b=rgb2[1])
    b_out = ImageMath.eval(s, a=rgb1[2], b=rgb2[2])
    bands = [r_out, g_out, b_out]
    im = Image.merge('RGB', bands)
    im.save(fn)
    show_benchmark(start_time)

# ---

start_time = dt.now()

w, h = get_canvas('800')
odir = '!output\\'

params1 = {'w': w, 'h': h, 'bg': (0, 0, 0)}
rgbgen1(params1, odir+'rgbgen1-%dx%d-01-002.png' % (w, h))

params1 = {'w': w, 'h': h, 'bg': (0, 0, 0), 's': "convert(min(a, b), 'L')"}
params2 = {'w': w, 'h': h, 'bg': (0, 0, 0), 's': "convert(max(a, b), 'L')"}
params3 = {'w': w, 'h': h, 'bg': (0, 0, 0), 's': "convert(a-b, 'L')"}
params4 = {'w': w, 'h': h, 'bg': (0, 0, 0), 's': "convert((a+b)/2, 'L')"}
params5 = {'w': w, 'h': h, 'bg': (0, 0, 0), 's': "convert(a*b/42, 'L')"}
rgbgen(params1, odir+'rgbgen-%dx%d-01-001.png' % (w, h))
rgbgen(params2, odir+'rgbgen-%dx%d-01-002.png' % (w, h))
rgbgen(params3, odir+'rgbgen-%dx%d-01-003.png' % (w, h))
rgbgen(params4, odir+'rgbgen-%dx%d-01-004.png' % (w, h))
rgbgen(params5, odir+'rgbgen-%dx%d-01-005.png' % (w, h))


time_elapsed = dt.now() - start_time
print('ALL done. elapsed time: {}'.format(time_elapsed))

