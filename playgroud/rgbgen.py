#! /usr/bin/env python
# -*- coding: utf-8 -*-

# PyArtForms - Python generative art forms paint algorithms (artificial artist)
# RGB generated
# based a bit on my old FilterMeister plugins
# (c)2018-2021 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz
# cre: 20181020
# upd: 20181021, 22
# upd: 20181110
# upd: 20190422
# upd: 20210526

# TODO:
# - mazy20 - proper

from PIL import Image, ImageDraw, ImageFilter, ImageOps, ImageMath
import random, math, os, sys
from bezier import make_bezier
from datetime import datetime as dt
from drawtools import *

# ZX colors
C_0 = 192
C_1 = 252
ZXC0 = [(0,0,0), (0,0,C_0), (C_0,0,0), (C_0,0,C_0), (0,C_0,0), (0,C_0,C_0), (C_0,C_0,0), (C_0,C_0,C_0)]
ZXC1 = [(0,0,0), (0,0,C_1), (C_1,0,0), (C_1,0,C_1), (0,C_1,0), (0,C_1,C_1), (C_1,C_1,0), (C_1,C_1,C_1)]
ZXCX = [ZXC0[0], ZXC1[0], ZXC0[1], ZXC1[1], ZXC0[2], ZXC1[2], ZXC0[3], ZXC1[3],
        ZXC0[4], ZXC1[4], ZXC0[5], ZXC1[5], ZXC0[6], ZXC1[6], ZXC0[7], ZXC1[7]
        ]

# ---

def init_common(params):
    random.seed()
    w = params['w']
    h = params['h']
    return w, h

# ---

def rgbgen1(params, fn):
    start_time = dt.now()
    w, h = init_common(params)
    print('rgbgen1...', fn)
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
    w, h = init_common(params)
    print('rgbgen2...', fn)
    s = params['s']
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
    w, h = init_common(params)
    print('rgbgen3...', fn)
    s = params['s']
    green = params['green']
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
    w, h = init_common(params)
    print('rgbsam...', fn)
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
    w, h = init_common(params)
    print('rgbgdc8...', fn)
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
    w, h = init_common(params)
    print('rgbgdc8...', fn)
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
    w, h = init_common(params)
    print('rgbgdc11...', fn)
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
    w, h = init_common(params)
    print('rgbgdc12...', fn)
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

def rgbxxx(params, fn):
    start_time = dt.now()
    w, h = init_common(params)
    c = math.pi/180
    print('rgbxxx...', fn)
    im = Image.new('RGB', (w, h), params['Background'])
    draw = ImageDraw.Draw(im)

    if params['box'] > 1:
        pix = params['box']
        h1 = int(h/pix)
        w1 = int(w/pix)
    else:
        pix = 1
        h1 = h
        w1 = w
    print(w,h,'->',w1,h1,'*',pix)

    # ForEveryPixel
    # size dependent! :(
    for y1 in range(h1):
        y = (y1+1) * pix
        for x1 in range(w1):
            x = x1 * pix
            if params['mode'] == 0:    # kind of color grid
                r = (x-y)
                g = (x+y)
                b = (x)
            if params['mode'] == 1:    # kind of color ?
                r = (x-y)*(x+y)/800
                g = (x+y)*(y)/800
                b = 0
            if params['mode'] == 2:    # kind of interference
                r = 0
                #g = (math.sqrt((x-w)*(x-w)+(y-h)*(y-h))) + (math.sqrt((x-w1)*(x-w1)+(y-h1)*(y-h1)))
                g = (math.sqrt((x-w)*(x-w)+(y-h)*(y-h))) * (math.sqrt((x-w1)*(x-w1)+(y-h1)*(y-h1)))
                b = 0
            if params['mode'] == 3:   # cool red
                r = abs( math.sqrt((x-w)*(x-w)+(y-h)*(y-h)) * (y*math.cos(x/100*c)) * (x*math.sin(y/100*c)) ) / 5000
                g = 0
                b = 0
            if params['mode'] == 4:    # so-so
                sq = math.sqrt((x-w)*(x-w)+(y-h)*(y-h))
                r = abs( sq * (x*math.sin(x/300*c)) ) / 5
                g = abs( sq * (y*math.sin(y/300*c)) ) / 5
                b = abs( sq * (x*math.sin(y/300*c)) ) / 5

            fill = (int(r)&255, int(g)&255, int(b)&255)

            if params['box'] > 0:
                box(draw, x=int(pix/2+x1*pix), y=int(pix/2+y1*pix), r=pix/2, fill=fill, outline=None)
            else:
                draw.point((x, y), fill=fill)

    # https://pillow.readthedocs.io/en/5.1.x/reference/ImageFilter.html
    if params['filter'] == True:
        im = im.filter(ImageFilter.FIND_EDGES)
        im = im.filter(ImageFilter.Kernel(size=(3, 3), kernel=[1,1,1,1,1,1,1,1,1], scale=None, offset=0))
        im = im.filter(ImageFilter.Kernel(size=(3, 3), kernel=[1,1,1,1,1,1,1,1,1], scale=None, offset=0))
        im = im.filter(ImageFilter.Kernel(size=(3, 3), kernel=[1,1,1,1,1,1,1,1,1], scale=None, offset=0))
    im.save(fn)
    show_benchmark(start_time)

def rgbzx(params, fn):
    start_time = dt.now()
    w, h = init_common(params)
    c = math.pi/180
    print('rgbzx...', fn)
    im = Image.new('RGB', (w, h), (0,0,0))
    draw = ImageDraw.Draw(im)

    # ForEveryPixel
    c = -1
    z = int(192/16) # == 12
    for y in range(h):
        if y%z == 0:
            c += 1
        fill1 = ZXCX[c%16]
        fill2 = ZXCX[(c+1)%16]
        fill3 = ZXCX[0]
        l1 = y % z
        for x in range(w):
            if l1 < 6:
                draw.point((x, y), fill=fill1)
            else:
                if ((y & 1 == 0) and (x & 1 == 1)) or ((y & 1 == 1) and (x & 1 == 0)):
                    draw.point((x, y), fill=fill1)
                else:
                    draw.point((x, y), fill=fill2)

    im.save(fn)
    show_benchmark(start_time)

# ---

def rgb_2021_1(params, fn):
    return 0

def rgb_2021_2(params, fn):
    return 0

def rgb_2021_3(params, fn):
    return 0

def rgb_2021_4(params, fn):
    return 0

# ---

def mazy20(draw, params):
    w, h = init_common(params)
    m = params['mode']
    c = math.pi/180
    d = 2 # pixel
    #d = 8 # pixel
    xs = int(w/d/2)
    ys = int(h/d/2)

    for y in range(int(h/d)):
        for x in range(int(w/d)):

            if False:
                vr = 32+128+128*math.sin(x*c)*math.cos(y*c)
                vg = 32+128+128*math.cos(4*x*c)*math.cos(y*c)
                vb = 32+128+64*(math.cos(3*x*c)+math.sin(2*y*c))
                if m == '1':
                    cx = (int(vr), int(vr), int(vr))
                if m == '2':
                    cx = (int(vg), int(vg), int(vg))
                #if m == '3':
                cx = (int(vb), int(vb), int(vb))

            """
            a = 0
            b = 0
#            if m == '1':
#                b = 0
#            if m == '2':
#                b = 10
#            if m == '3':
#                b = 100
            vr = (x+a)*1*math.sin((x+b)*c*2)+y*1*math.cos(y*c*2)
            a = 10
            b = 50
            vg = (x+a)*1*math.sin((x+b)*c*2)+y*1*math.cos(y*c*2)
            b = 20
            b = 100
            vb = (x+a)*1*math.sin((x+b)*c*2)+y*1*math.cos(y*c*2)
            vr = int(vr) % 255
            vg = int(vg) % 255
            vb = int(vb) % 255
            cx = (int(vr), int(vg), int(vb))

            hue = int(vr) % 255
            saturation = 244
            vb = 2000*math.exp(-x/50)
            luminance = int(vb) % 255
            #luminance = 192 # int(vb * 0.7)
            cx = 'hsl(%d, %d%%, %d%%)' % (hue, saturation, luminance)
            """

            if True:
                # ?
                vr = 2000*math.exp(-x/100)
                vg = 2000*math.exp(-y/100)
                hue = int(vr) % 255
                luminance = int(vg) % 255
                cx = 'hsl(%d, %d%%, %d%%)' % (hue, 244, luminance)

            if False:
                # black hole in red bg
                v = (1*math.sqrt((x-xs)*(x-xs)+(y-ys)*(y-ys)))
                cx = (int(abs(v)), int(0), int(0))

            if False:
                # black stripes on red (cool)
                v = (1*math.sqrt((x-xs)*(x-xs)+(y-ys)*(y-ys))) * (math.sin(3.5*c*x)*math.cos(c*x)+math.sin(4*c*y)*math.cos(4*c*x))
                cx = (int(abs(v)), int(0), int(0))

            if False:
                # RGB interpolations - lame but maybe sth?
                vr = (20/6*math.sqrt((x-xs)*(x-xs)+(y-ys)*(y-ys)))
                vg = (20/6*math.sqrt((x-xs*0.9)*(x-xs*0.9)+(y-ys)*(y-ys)))
                vb = (20/6*math.sqrt((x-xs)*(x-xs)+(y-ys*0.9)*(y-ys*0.9)))
                cx = (int(vr)%255, int(vg)%255, int(vb)%255)

            if False:
                # lame?
                vr = 64*(math.cos(2*x*c)+math.sin(2*y*c))
                vg = 64*(math.cos(3*y*c)+math.sin(3*x*c))
                vb = 64*(math.cos(3*x*c)+math.sin(2*y*c))
                def sca(x):
                    if x < 0:
                        if x < 32:
                            return 0
                        else:
                            return 64
                    if x > 32:
                        return 192
                    else:
                        return 128
                vr1 = sca(vr)
                vg1 = sca(vg)
                vb1 = sca(vb)
                cx = (vr1, vg1, vb1)

            if False:
                # lame?
                f0 = 1 + math.cos(x*c*2)
                f1 = 1 + math.cos(y*c*4)
                f0 = int(f0*255)
                f1 = int(5+f1*25)
                cx = 'hsl(%d, %d%%, %d%%)' % (f0, 80+5, f1)

            if False:
                # ?
                #v = (8*math.sqrt((x-xs)*(x-xs)+(y-ys)*(y-ys))) / 4 # opt w/o /4
                v0 = math.sqrt((x-xs)*(x-xs)+(y-ys)*(y-ys))
                v = 3 + math.cos(x*c*1) + math.sin(y*c*1) - math.sin(v0*c*1) # to ok
                v = v * 254
                f0 = int(v) % 255
                #v = (2*math.sqrt((x-xs)*(x-xs)+(y-ys)*(y-ys)))
                #f1 = int(v*100) % 100
                #f1 = random.randint(20, 80) #ok1
                f1 = random.randint(45, 70)
                cx = 'hsl(%d, %d%%, %d%%)' % (f0, 80, f1)
            
            xy = [(x*d, y*d), (x*d+d, y*d+d)]
            draw.rectangle(xy, fill=cx, outline=None)
    # ... todo: fin
    return 0

# ---

start_time = dt.now()
root = '!output-rgb'
if not os.path.exists(root):
    os.makedirs(root)
odir = root+'\\'

w, h = 256, 192
params1 = {'w': w, 'h': h}
rgbzx(params1, odir+'rgbzx-%dx%d-01-001.png' % (w, h))
#exit()    #tmp

w, h = 512, 512
params1 = {'w': w, 'h': h, 'Background': (0, 0, 0), 'mode': 1, 'box': 0, 'filter': False}
rgbxxx(params1, odir+'rgbxxx-%dx%d-01-001.png' % (w, h))
w, h = 2048, 2048
params1 = {'w': w, 'h': h, 'Background': (0, 0, 0), 'mode': 1, 'box': 0, 'filter': False}
rgbxxx(params1, odir+'rgbxxx-%dx%d-01-001.png' % (w, h))

w, h = get_canvas('1024')

params1 = {'w': w, 'h': h, 'Background': (0, 0, 0), 'mode': 0, 'box': 0, 'filter': False}
rgbxxx(params1, odir+'rgbxxx-%dx%d-00-001.png' % (w, h))
params1 = {'w': w, 'h': h, 'Background': (0, 0, 0), 'mode': 1, 'box': 0, 'filter': False}
rgbxxx(params1, odir+'rgbxxx-%dx%d-01-001.png' % (w, h))
params1 = {'w': w, 'h': h, 'Background': (0, 0, 0), 'mode': 2, 'box': 0, 'filter': False}
rgbxxx(params1, odir+'rgbxxx-%dx%d-02-001.png' % (w, h))
params1 = {'w': w, 'h': h, 'Background': (0, 0, 0), 'mode': 3, 'box': 0, 'filter': False}
rgbxxx(params1, odir+'rgbxxx-%dx%d-03-001.png' % (w, h))
params1 = {'w': w, 'h': h, 'Background': (0, 0, 0), 'mode': 4, 'box': 0, 'filter': False}
rgbxxx(params1, odir+'rgbxxx-%dx%d-04-001.png' % (w, h))
#exit()    #tmp

w, h = get_canvas('800')

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

