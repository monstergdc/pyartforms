#! /usr/bin/env python
# -*- coding: utf-8 -*-

# paint algorithms (artificial artist) - XOR, v1.0, Python version
# based on my FilterMeister plugin "GDC XORizator 1.0" Copyright © 2011 Noniewicz.com
# (c)2018 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz
# cre: 20181020
# upd: 201810??

# see:
# https://pillow.readthedocs.io/en/3.1.x/reference/ImageDraw.html
# http://pillow.readthedocs.io/en/5.1.x/reference/ImageFilter.html
# https://auth0.com/blog/image-processing-in-python-with-pillow/

# TODO:
# - ?

from PIL import Image, ImageDraw
import random, math, os, sys
from bezier import make_bezier
from datetime import datetime as dt
from drawtools import *


def xor(params, fn):
    start_time = dt.now()
    w = params['w']
    h = params['h']
    xfloatmul = params['xfloatmul']
    yfloatmul = params['yfloatmul']
    tfloatmul = params['tfloatmul']
    print('xor...', fn)
    random.seed()
    im = Image.new('RGB', (w, h), params['bg'])
    draw = ImageDraw.Draw(im)

    # ForEveryPixel
    for y in range(h):
        for x in range(w):
            fx = int(x*xfloatmul)
            fy = int(y*yfloatmul)
            va = int((fx^fy) * tfloatmul) & 255
            if params['red'] == True:
                R = va
            else:
                R = 0
            if params['green'] == True:
                G = va
            else:
                G = 0
            if params['blue'] == True:
                B = va
            else:
                B = 0
            draw.point((x, y), fill=(R, G, B))

    im.save(fn)
    show_benchmark(start_time)

# ---

start_time = dt.now()

w, h = get_canvas('640')
odir = '!output\\'
params1 = {'w': w, 'h': h, 'bg': (0, 0, 0), 'n': 1, 'red': True, 'green': True, 'blue': True, 'xfloatmul': 1.0, 'yfloatmul': 1.0, 'tfloatmul': 1.0}
params2 = {'w': w, 'h': h, 'bg': (0, 0, 0), 'n': 2, 'red': True, 'green': False, 'blue': False, 'xfloatmul': 1.0, 'yfloatmul': 1.0, 'tfloatmul': 1.0}
params3 = {'w': w, 'h': h, 'bg': (0, 0, 0), 'n': 2, 'red': False, 'green': True, 'blue': False, 'xfloatmul': 1.0, 'yfloatmul': 1.0, 'tfloatmul': 0.2}
params4 = {'w': w, 'h': h, 'bg': (0, 0, 0), 'n': 2, 'red': False, 'green': False, 'blue': True, 'xfloatmul': 0.5, 'yfloatmul': 0.5, 'tfloatmul': 8.0}

xor(params1, odir+'xor-%dx%d-01-001.png' % (w, h))
xor(params2, odir+'xor-%dx%d-01-002.png' % (w, h))
xor(params3, odir+'xor-%dx%d-01-003.png' % (w, h))
xor(params4, odir+'xor-%dx%d-01-004.png' % (w, h))

time_elapsed = dt.now() - start_time
print('ALL done. elapsed time: {}'.format(time_elapsed))

