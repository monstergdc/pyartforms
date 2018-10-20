#! /usr/bin/env python
# -*- coding: utf-8 -*-

# drawing life in Python
# (c)2018 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz
# https://pillow.readthedocs.io/en/3.1.x/reference/ImageDraw.html
# cre: 20180503
# upd; 20180504
# upd; 20181019, 20

# TODO:
# - ?

from PIL import Image, ImageDraw, ImageFilter
import random, math, string, os, sys
from datetime import datetime as dt
from drawtools import *



def f1(x):
    if random.randint(0, 100) >= 90:
        return 1
    return 0

def f2a(x, row, n):
    z = 0
    if x > 1+1 and x < n-1-1:
        suma = row[x-2] + row[x-1] + row[x] + row[x+1] + row[x+2]
        if suma == 0:
            z = 0
            if random.randint(0, 100) >= 95:
                z = 1
        if suma == 1:
            z = 1
        if suma == 2:
            z = row[x]
        if suma == 3:
            z = row[x] ^ 1
        if suma == 4:
            z = row[x] ^ 1
        if suma == 5:
            z = 0
    return z

def f2b(x, row, n):
    z = 0
    if x > 1 and x < n-1:
        suma = row[x-1] + row[x] + row[x+1]
        if suma == 0:
            z = 0
        if suma == 1:
            z = row[x] ^ 1
        if suma == 2:
            z = row[x]
        if suma == 3:
            z = 0
    return z

def f2c(x, row, n):
    z = 0
    if x > 1+1 and x < n-1-1:
        suma = row[x-2] + row[x-1] + row[x] + row[x+1] + row[x+2]
        if suma == 0:
            z = 0
        if suma == 1:
            z = row[x]
        if suma == 2:
            z = 1
        if suma == 3:
            z = row[x] ^ 1
        if suma == 4:
            z = row[x]
        if suma == 5:
            z = 0
    return z

def f2d(x, row, n):
    z = 0
    if x > 1+1 and x < n-1-1:
        suma = row[x-2] + row[x-1] + row[x] + row[x+1] + row[x+2]
        if suma == 0:
            z = 0
        if suma == 1:
            z = row[x]
        if suma == 2:
            z = 1
        if suma == 3:
            z = row[x-1]
        if suma == 4:
            z = row[x+1]
        if suma == 5:
            z = 0
    return z

def f2e(x, row, n):
    z = 0
    if x > 1+1+1 and x < n-1-1-1:
        suma = row[x-3] + row[x-2] + row[x-1] + row[x] + row[x+1] + row[x+2] + row[x+3]
        if suma == 0:
            z = 0
        if suma == 1:
            z = 0
        if suma == 2:
            z = row[x]
        if suma == 3:
            z = 1
        if suma == 4:
            z = 1
        if suma == 5:
            z = row[x]
        if suma == 6:
            z = 0
        if suma == 7:
            z = 0
    return z

def f2f(x, row, n):
    z = 0
    if x > 1 and x < n-1:
        suma = row[x]
        for i in range(3):
            pm = x - random.randint(0, 5)
            pp = x + random.randint(0, 5)
            if pm > 1:
                suma += row[pm]
            if pp < n-1:
                suma += row[pp]
        if suma == 0:
            z = 0
        if suma == 1:
            z = 0
        if suma == 2:
            z = row[x]
        if suma == 3:
            z = 1
        if suma == 4:
            z = 1
        if suma == 5:
            z = row[x]
        if suma >= 6:
            z = 0
    return z


def life(draw, params):
    random.seed()
    row = []
    row[:] = [f1(x) for x in range(params['w'])]
    n = len(row)

    if params['f'] == 'f2a':
        myfun = f2a
    if params['f'] == 'f2b':
        myfun = f2b
    if params['f'] == 'f2c':
        myfun = f2c
    if params['f'] == 'f2d':
        myfun = f2d
    if params['f'] == 'f2e':
        myfun = f2e
    if params['f'] == 'f2f':
        myfun = f2f
    
    y = 0
    for y in range(params['h']):
        points = []
        for i in range(params['w']):
            if row[i] == 1:
                points.extend((i, y))
        draw.point(points, fill=params['LineColor'])
        rownew = []
        rownew[:] = [myfun(x, row, n) for x in range(params['w'])]
        row = rownew
        y += 1

def call_painter(params, png_file='example.png', output_mode='save'):
    start_time = dt.now()
    print('drawing life...', png_file)
    im = Image.new('RGB', (params['w'], params['h']), params['Background'])
    draw = ImageDraw.Draw(im)
    life(draw, params)
    if output_mode == 'save':
        im.save(png_file, dpi=(300,300))
        show_benchmark(start_time)
    else:
        im2cgi(im)

# ---

ca = get_canvas('640')
params1 = {
    'w': ca[0], 'h': ca[1],
    'Background': (0, 0, 0),
    'LineColor': (255,255,255),
    'f': '',
}

# tmp: to call from CGI (remove print!)
#p1 = cgiart.get_cgi_par()
#params1['w'] = p1["w"]
#params1['h'] = p1["h"]
#params1['f'] = p1["f"]
#call_painter(params1, '')


params1['f'] = 'f2a'
call_painter(params1, 'life-0001.jpg')
call_painter(params1, 'life-0001.gif')
call_painter(params1, 'life-0001.png')
call_painter(params1, 'life-0002.png')
params1['f'] = 'f2b'
call_painter(params1, 'life-0003.png')
call_painter(params1, 'life-0004.png')
params1['f'] = 'f2c'
call_painter(params1, 'life-0005.png')
call_painter(params1, 'life-0006.png')
params1['f'] = 'f2d'
call_painter(params1, 'life-0007.png')
call_painter(params1, 'life-0008.png')
params1['f'] = 'f2e'
call_painter(params1, 'life-0009.png')
call_painter(params1, 'life-0010.png')
params1['f'] = 'f2f'
call_painter(params1, 'life-0011.png')
call_painter(params1, 'life-0012.png')
