from PIL import Image, ImageDraw, ImageFilter
import random, math, string, os, sys
from datetime import datetime as dt
#from drawtools import get_canvas, circle, box, triangle, gradient, gradient2

# drawing life in Python
# (c)2018 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz
# https://pillow.readthedocs.io/en/3.1.x/reference/ImageDraw.html
# cre: 20180503
# upd; 2018????

# TODO:
# - ?


def f1(x):
    if random.randint(0, 100) >= 90:
        return 1
    return 0

def f2a(x, row):
    z = 0
    if x > 1+1 and x < len(row)-1-1:
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

def f2b(x, row):
    z = 0
    if x > 1 and x < len(row)-1:
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

def f2c(x, row):
    z = 0
    if x > 1+1 and x < len(row)-1-1:
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

def f2d(x, row):
    z = 0
    if x > 1+1 and x < len(row)-1-1:
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


def life(draw, params):
    c = math.pi/180
    random.seed()
    row = []
    row[:] = [f1(x) for x in range(params['w'])]

    if params['f'] == 'f2a':
        myfun = f2a
    if params['f'] == 'f2b':
        myfun = f2b
    if params['f'] == 'f2c':
        myfun = f2c
    if params['f'] == 'f2d':
        myfun = f2d
    
    y = 0
    for y in range(params['h']):
        points = []
        for i in range(params['w']):
            if row[i] == 1:
                points.extend((i, y))
        draw.point(points, fill=params['LineColor'])
        rownew = []
        rownew[:] = [myfun(x, row) for x in range(params['w'])]
        row = rownew
        y += 1

def call_painter(params, png):
    start_time = dt.now()
    print('drawing life...', png)
    im = Image.new('RGB', (params['w'], params['h']), params['Background'])
    draw = ImageDraw.Draw(im)
    life(draw, params)
    im.save(png, dpi=(300,300))
    time_elapsed = dt.now() - start_time
    print('done. elapsed time: {}'.format(time_elapsed))

# ---

#w = 4960
#h = 3507
w = 640
h = 480

params1 = {
    'w': w, 'h': h,
    'Background': (0, 0, 0),
    'LineColor': (255,255,255),
    'f': 'f2a',
}
call_painter(params1, 'life-0001.png')
call_painter(params1, 'life-0002.png')
params1 = {
    'w': w, 'h': h,
    'Background': (0, 0, 0),
    'LineColor': (255,255,255),
    'f': 'f2b',
}
call_painter(params1, 'life-0003.png')
call_painter(params1, 'life-0004.png')
params1 = {
    'w': w, 'h': h,
    'Background': (0, 0, 0),
    'LineColor': (255,255,255),
    'f': 'f2c',
}
call_painter(params1, 'life-0005.png')
call_painter(params1, 'life-0006.png')
params1 = {
    'w': w, 'h': h,
    'Background': (0, 0, 0),
    'LineColor': (255,255,255),
    'f': 'f2d',
}
call_painter(params1, 'life-0007.png')
call_painter(params1, 'life-0008.png')
