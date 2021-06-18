#! /usr/bin/env python
# -*- coding: utf-8 -*-

# PyArtForms - Python generative art forms paint algorithms (artificial artist)
# FLOWERS (brush paint test), v1.0
# (c)2017-2021 MoNsTeR/GDC, Noniewicz.com, Noniewicz.art.pl, Jakub Noniewicz
# cre: 20180505
# upd: 20180929
# upd: 20181020
# upd: 20210507, 15
# upd: 20210618

# see:
# https://auth0.com/blog/image-processing-in-python-with-pillow/

# TODO:
# - ?

from PIL import Image, ImageDraw
import random, math, os, sys
from bezier import make_bezier
from datetime import datetime as dt
from drawtools import *


def brush1(params, fn):
    start_time = dt.now()
    w = params['w']
    h = params['h']
    print('brush...', fn)
    random.seed()
    im = Image.new('RGB', (w, h), params['bg'])
    draw = ImageDraw.Draw(im)
    imc = Image.open(params['brush'])
    print('imc.size:', imc.size)

    img = [[None for x in range(3)] for y in range(3)]
    for x in range(3):
        for y in range(3):
            x0 = x * 128
            y0 = y * 128
            box = (x0, y0, x0+128-1, y0+128-1)
            img[y][x] = imc.crop(box)

    w2 = w/2
    h2 = h/2
    cnt = random.randint(0, 300)
    for c in range(cnt):
        x = random.randint(0, 3-1)
        y = random.randint(0, 3-1)
        position = (random.randint(w2-w2/2-64, w2+w2/2), random.randint(h2-h2/2-64, h2+h2/2))
        imc_rot = img[y][x].rotate(random.randint(-30, 30))
        im.paste(imc_rot, position, imc_rot)

    im.save(fn)
    show_benchmark(start_time)

# ---

def do_brush(cnt, w, h, odir):
    params1 = {'w': w, 'h': h, 'bg': (255, 255, 255), 'brush': '.\\data\\brush-flowers-01.png'} # 3x red, 3x yellow, 3x white
    params2 = {'w': w, 'h': h, 'bg': (255, 255, 255), 'brush': '.\\data\\brush-weggies-01.png'}

    for n in range(cnt):
        brush1(params1, odir+'flowers1-%dx%d-01-%03d.png' % (w, h, n+1))
        brush1(params2, odir+'weggies1-%dx%d-01-%03d.png' % (w, h, n+1))

# ---

start_time = dt.now()
cnt = 4
w, h = get_canvas('1024')
odir = '!output\\'
do_brush(cnt, w, h, odir)
time_elapsed = dt.now() - start_time
print('ALL done. elapsed time: {}'.format(time_elapsed))

