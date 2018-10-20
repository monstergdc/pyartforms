#! /usr/bin/env python
# -*- coding: utf-8 -*-

# paint algorithms (artificial artist) - RGB generated, v1.0, Python version
# based on my old FilterMeister plugins
# (c)2018 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz
# cre: 20181020
# upd: 20181021

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
    im = Image.new('RGB', (w, h), params['Background'])
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

def rgbgen2(params, fn):
    start_time = dt.now()
    random.seed()
    w = params['w']
    h = params['h']
    s = params['s']
    print('rgbgen2...', fn)
    random.seed()
    im = Image.new('RGB', (w, h), params['Background'])
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

def rgbgen3(params, fn):
    start_time = dt.now()
    random.seed()
    w = params['w']
    h = params['h']
    s = params['s']
    green = params['green']
    print('rgbgen3...', fn)
    random.seed()
    im = Image.new('RGB', (w, h), params['Background'])
    draw = ImageDraw.Draw(im)

    # ForEveryPixel
    for y in range(h):
        for x in range(w):
            if green == True:
                r = 0
            else:
                r = int(x*y/50/4)
            g = int( x*math.cos(y*math.pi/180) + y*math.sin(x*math.pi/180) )
            b = 0
            draw.point((x, y), fill=(r&255, g&255, b&255))
    im2 = ImageOps.flip(ImageOps.mirror(im))
    rgb1 = im.split()
    rgb2 = im2.split()
    r_out = ImageMath.eval(s, a=rgb1[0], b=rgb2[0])
    g_out = ImageMath.eval(s, a=rgb1[1], b=rgb2[1])
    b_out = ImageMath.eval(s, a=rgb1[2], b=rgb2[2])
    bands = [r_out, g_out, b_out]
    im = Image.merge('RGB', bands)
    im = im.filter(ImageFilter.BLUR)
    im = im.filter(ImageFilter.SHARPEN)
    im.save(fn)
    show_benchmark(start_time)

# GDC #7 - Stupid modern art generator
def rgbsam(params, fn):
    start_time = dt.now()
    random.seed()
    w = params['w']
    h = params['h']
    print('rgbsam...', fn)
    random.seed()
    im = Image.new('RGB', (w, h), params['Background'])
    draw = ImageDraw.Draw(im)

    # ForEveryPixel
    for y in range(h):
        for x in range(w):
            r = 0
            g = 0
            b = 0
            if y > 0:
                r = x%y
            if x > 0:
                g = (w-x)%x
            if h-y > 0:
                b = (w-x)%(h-y)
            draw.point((x, y), fill=(r&255, g&255, b&255))
    im.save(fn)
    show_benchmark(start_time)

# GDC #8 - grid
def rgbgdc8(params, fn):
    start_time = dt.now()
    random.seed()
    w = params['w']
    h = params['h']
    print('rgbgdc8...', fn)
    random.seed()
    im = Image.new('RGB', (w, h), params['Background'])
    draw = ImageDraw.Draw(im)

    # ForEveryPixel
    for y in range(h):
        for x in range(w):
            c = ((x%40) > 20 and (y%40) > 20) or ((x%40) < 20 and (y%40) < 20)
            if c == True:
                r = 255
            else:
                r = 0
            g = r
            b = r
            draw.point((x, y), fill=(r&255, g&255, b&255))
    im.save(fn)
    show_benchmark(start_time)

# GDC #9 - grid2
def rgbgdc9(params, fn):
    start_time = dt.now()
    random.seed()
    w = params['w']
    h = params['h']
    print('rgbgdc8...', fn)
    random.seed()
    im = Image.new('RGB', (w, h), params['Background'])
    draw = ImageDraw.Draw(im)

    # ForEveryPixel
    for y in range(h):
        for x in range(w):
            c1 = ((x%40) >= 20 and (y%40) >= 20) or ((x%40) <= 20 and (y%40) <= 20)
            c2 = ((x%80) >= 40 and (y%80) >= 40) or ((x%80) <= 40 and (y%80) <= 40)
            c3 = ((x%120) >= 60 and (y%120) >= 60) or ((x%120) <= 60 and (y%120) <= 60)
            if c1 == True:
                r = 127
            else:
                r = 0
            if c2 == True:
                g = 127
            else:
                g = 0
            if c3 == True:
                b = 127
            else:
                b = 0
            draw.point((x, y), fill=(r&255, g&255, b&255))
    im.save(fn)
    show_benchmark(start_time)

# GDC #11 - Bar/grid genenrator
def rgbgdc11(params, fn):
    start_time = dt.now()
    random.seed()
    w = params['w']
    h = params['h']
    print('rgbgdc11...', fn)
    random.seed()
    im = Image.new('RGB', (w, h), params['Background'])
    draw = ImageDraw.Draw(im)
    w1 = params['w1']
    w2 = params['w2']
    ctl = params['ctl']

    # ForEveryPixel
    for y in range(h):
        for x in range(w):
            c = 0
            # ctl[2]: "mode (|||,---,###,///,***)", val=3, size=(*,6), range=(1,5)
            if ctl == 1:
                c = (x%w2) >= w1
            if ctl == 2:
                c = (y%w2) >= w1
            if ctl == 3:
                c = ((x%w2) >= w1 and (y%w2) >= w1) or ((x%w2) <= w1 and (y%w2) <= w1)
            if ctl == 4:
                c = ((y+x)%w2) >= w1
            if ctl == 5:
                c = ((y*x)%w2) >= w1
            if c == True:
                r = 255
            else:
                r = 0
            g = r
            b = r
            draw.point((x, y), fill=(r&255, g&255, b&255))
    im.save(fn)
    show_benchmark(start_time)

# GDC #12 - ambient
def rgbgdc12(params, fn):
    start_time = dt.now()
    random.seed()
    w = params['w']
    h = params['h']
    print('rgbgdc12...', fn)
    random.seed()
    im = Image.new('RGB', (w, h), params['Background'])
    draw = ImageDraw.Draw(im)

    # ForEveryPixel
    for y in range(h):
        for x in range(w):
            r = int(x/w*255)
            g = int(y/h*255)
            b = 0
            draw.point((x, y), fill=(r&255, g&255, b&255))
    im.save(fn)
    show_benchmark(start_time)

# ---

start_time = dt.now()

w, h = get_canvas('800')
odir = '!output\\'

params1 = {'w': w, 'h': h, 'Background': (0, 0, 0)}
rgbgen1(params1, odir+'rgbgen-%dx%d-01-002.png' % (w, h))

params1 = {'w': w, 'h': h, 'Background': (0, 0, 0), 's': "convert(min(a, b), 'L')"}
params2 = {'w': w, 'h': h, 'Background': (0, 0, 0), 's': "convert(max(a, b), 'L')"}
params3 = {'w': w, 'h': h, 'Background': (0, 0, 0), 's': "convert(a-b, 'L')"}
params4 = {'w': w, 'h': h, 'Background': (0, 0, 0), 's': "convert((a+b)/2, 'L')"}
params5 = {'w': w, 'h': h, 'Background': (0, 0, 0), 's': "convert(a*b/42, 'L')"}
rgbgen2(params1, odir+'rgbgen-%dx%d-02-001.png' % (w, h))
rgbgen2(params2, odir+'rgbgen-%dx%d-02-002.png' % (w, h))
rgbgen2(params3, odir+'rgbgen-%dx%d-02-003.png' % (w, h))
rgbgen2(params4, odir+'rgbgen-%dx%d-02-004.png' % (w, h))
rgbgen2(params5, odir+'rgbgen-%dx%d-02-005.png' % (w, h))

params1 = {'w': w, 'h': h, 'Background': (0, 0, 0), 's': "convert(min(a, b), 'L')", 'green': True}
params2 = {'w': w, 'h': h, 'Background': (0, 0, 0), 's': "convert(max(a, b), 'L')", 'green': True}
params3 = {'w': w, 'h': h, 'Background': (0, 0, 0), 's': "convert(a-b, 'L')", 'green': True}
params4 = {'w': w, 'h': h, 'Background': (0, 0, 0), 's': "convert((a+b)/2, 'L')", 'green': True}
params5 = {'w': w, 'h': h, 'Background': (0, 0, 0), 's': "convert(a*b/42, 'L')", 'green': True}
rgbgen3(params1, odir+'rgbgen-%dx%d-03g-001.png' % (w, h))
rgbgen3(params2, odir+'rgbgen-%dx%d-03g-002.png' % (w, h))
rgbgen3(params3, odir+'rgbgen-%dx%d-03g-003.png' % (w, h))
rgbgen3(params4, odir+'rgbgen-%dx%d-03g-004.png' % (w, h))
rgbgen3(params5, odir+'rgbgen-%dx%d-03g-005.png' % (w, h))

params1 = {'w': w, 'h': h, 'Background': (0, 0, 0), 's': "convert(min(a, b), 'L')", 'green': False}
params2 = {'w': w, 'h': h, 'Background': (0, 0, 0), 's': "convert(max(a, b), 'L')", 'green': False}
params3 = {'w': w, 'h': h, 'Background': (0, 0, 0), 's': "convert(a-b, 'L')", 'green': False}
params4 = {'w': w, 'h': h, 'Background': (0, 0, 0), 's': "convert((a+b)/2, 'L')", 'green': False}
params5 = {'w': w, 'h': h, 'Background': (0, 0, 0), 's': "convert(a*b/42, 'L')", 'green': False}
rgbgen3(params1, odir+'rgbgen-%dx%d-03-001.png' % (w, h))
rgbgen3(params2, odir+'rgbgen-%dx%d-03-002.png' % (w, h))
rgbgen3(params3, odir+'rgbgen-%dx%d-03-003.png' % (w, h))
rgbgen3(params4, odir+'rgbgen-%dx%d-03-004.png' % (w, h))
rgbgen3(params5, odir+'rgbgen-%dx%d-03-005.png' % (w, h))

# pixel math does not scale well with size
w, h = get_canvas('2000')
params5 = {'w': w, 'h': h, 'Background': (0, 0, 0), 's': "convert(a*b/42, 'L')", 'green': False}
rgbgen3(params5, odir+'rgbgen-%dx%d-03-005.png' % (w, h))

w, h = get_canvas('800')
params = {'w': w, 'h': h, 'Background': (0, 0, 0)}
rgbsam(params, odir+'rgbsam-%dx%d-01-001.png' % (w, h))

w, h = get_canvas('800')
params = {'w': w, 'h': h, 'Background': (0, 0, 0)}
rgbgdc8(params, odir+'rgbgdc8-%dx%d-01-001.png' % (w, h))
rgbgdc9(params, odir+'rgbgdc9-%dx%d-01-001.png' % (w, h))
rgbgdc12(params, odir+'rgbgdc12-%dx%d-01-001.png' % (w, h))

params1 = {'w': w, 'h': h, 'Background': (0, 0, 0), 'ctl': 1, 'w1': 10, 'w2': 40}
params2 = {'w': w, 'h': h, 'Background': (0, 0, 0), 'ctl': 2, 'w1': 10, 'w2': 40}
params3 = {'w': w, 'h': h, 'Background': (0, 0, 0), 'ctl': 3, 'w1': 10, 'w2': 40}   # this
params4 = {'w': w, 'h': h, 'Background': (0, 0, 0), 'ctl': 4, 'w1': 10, 'w2': 40}
params5 = {'w': w, 'h': h, 'Background': (0, 0, 0), 'ctl': 5, 'w1': 10, 'w2': 40}
rgbgdc11(params1, odir+'rgbgdc11-%dx%d-01-001.png' % (w, h))
rgbgdc11(params2, odir+'rgbgdc11-%dx%d-01-002.png' % (w, h))
rgbgdc11(params3, odir+'rgbgdc11-%dx%d-01-003.png' % (w, h))
rgbgdc11(params4, odir+'rgbgdc11-%dx%d-01-004.png' % (w, h))
rgbgdc11(params5, odir+'rgbgdc11-%dx%d-01-005.png' % (w, h))

time_elapsed = dt.now() - start_time
print('ALL done. elapsed time: {}'.format(time_elapsed))

