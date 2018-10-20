#! /usr/bin/env python
# -*- coding: utf-8 -*-

# paint algorithms (artificial artist), v1.0, Python version
# (c)2017-2018 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz
# #1 okrutne czerwone mazy
# #2 circles
# #3 triangles
# #4 poly
# cre: 20180430
# upd: 20180501, 02, 03
# upd: 20181020

# see:
# https://pillow.readthedocs.io/en/3.1.x/reference/ImageDraw.html
# http://pillow.readthedocs.io/en/5.1.x/reference/ImageFilter.html

# TODO:
# - ?


from PIL import Image, ImageDraw, ImageFilter
import random, math, string, os, sys
from bezier import make_bezier
from datetime import datetime as dt
from drawtools import *


def mazy1(params, fn):
    start_time = dt.now()
    w = params['w']
    h = params['h']
    print('mazy1...', fn)
    random.seed()
    im = Image.new('RGB', (w, h), params['bg'])
    draw = ImageDraw.Draw(im)
    ts = [t/100.0 for t in range(101)]
    v = params['v']

    for n in range(params['n']):
        po = [(random.randint(0, w), random.randint(0, h)),
              (random.randint(0, w), random.randint(0, h)),
              (random.randint(0, w), random.randint(0, h)),
              (random.randint(0, w), random.randint(0, h))]
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

        if params['prefill'] == True:
            bezier = make_bezier(po)
            points = bezier(ts)
            draw.polygon(points, fill=color, outline=None)

        for m in range(params['m']):
            if params['keep'] == True:
                po0 = po[0]
                po3 = po[3]
            po[:] = [(xy[0]+random.randint(0, v)-random.randint(0, v), xy[1]+random.randint(0, v)-random.randint(0, v)) for xy in po]
            if params['keep'] == True:
                po[0] = po0
                po[3] = po3
            if params['mode'] == 'red':
                color = (r ^ random.randint(0, 48), 0, 0)
            if params['mode'] == 'color':
                color = (r ^ random.randint(0, 48), g ^ random.randint(0, 48), b ^ random.randint(0, 48))
            if params['mode'] == 'black':
                rr = random.randint(0, 48)
                color = (rr, rr, rr)
            bezier = make_bezier(po)
            points = bezier(ts)
            draw.line(points, fill=color, width=params['pw'])
    if params['blur'] == True:
        im = im.filter(ImageFilter.BLUR)
        im = im.filter(ImageFilter.BLUR)
        im = im.filter(ImageFilter.SHARPEN)
        im = im.filter(ImageFilter.SHARPEN)
    im.save(fn)
    show_benchmark(start_time)


def mazy2(params, fn):
    start_time = dt.now()
    w = params['w']
    h = params['h']
    print('mazy2...', fn)
    random.seed()
    im = Image.new('RGB', (w, h), params['bg'])
    draw = ImageDraw.Draw(im)
    ts = [t/100.0 for t in range(101)]
    v = params['v']

    for n in range(params['n']):
        po = [(random.randint(0, w), random.randint(0, h)),
              (random.randint(0, w), random.randint(0, h))]
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

        circle(draw, po[0][0], po[0][1], random.randint(200, 800), fill=color, outline=None)

        r0 = random.randint(100, 300)
        for m in range(params['m']):
            po[:] = [(xy[0]+random.randint(0, v)-random.randint(0, v), xy[1]+random.randint(0, v)-random.randint(0, v)) for xy in po]
            if params['mode'] == 'red':
                color = (255*(m&1), 0, 0)
            if params['mode'] == 'color':
                color = (random.randint(64, 256), random.randint(64, 256), b ^ random.randint(8, 128))
            if params['mode'] == 'black':
                if m&1 == 0:
                    rr = 0
                else:
                    rr = 255
                color = (rr, rr, rr)
            circle(draw, po[0][0], po[0][1], r0-m*10, fill=color, outline=None)
    if params['blur'] == True:
        im = im.filter(ImageFilter.BLUR)
        im = im.filter(ImageFilter.BLUR)
        im = im.filter(ImageFilter.SHARPEN)
        im = im.filter(ImageFilter.SHARPEN)
    im.save(fn)
    show_benchmark(start_time)

def mazy3(params, fn):
    start_time = dt.now()
    w = params['w']
    h = params['h']
    print('mazy3...', fn)
    random.seed()
    im = Image.new('RGB', (w, h), params['bg'])
    draw = ImageDraw.Draw(im)

    pold = [(random.randint(-w, w*2), random.randint(-h, h*2)),
         (random.randint(-w, w*2), random.randint(-h, h*2)),
         (random.randint(-w, w*2), random.randint(-h, h*2))]

    m = 1000
    for n in range(params['n']):
        w0 = random.randint(0, w)
        h0 = random.randint(0, h)
        po = [(w0+random.randint(0, 300), h0+random.randint(0, 300)),
              (w0+random.randint(0, 300), h0+random.randint(0, 300)),
              (w0+random.randint(0, 300), h0+random.randint(0, 300))]
        cycle = n % 2
        if cycle == 0:
            po[0] = pold[0]
            po[1] = pold[1]
        if cycle == 1:
            po[1] = pold[1]
            po[2] = pold[2]
        if cycle == 2:
            po[2] = pold[2]
            po[0] = pold[0]
        pold = po

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

        triangle(draw, po, fill=color, outline=None)

    if params['blur'] == True:
        im = im.filter(ImageFilter.BLUR)
        im = im.filter(ImageFilter.BLUR)
        im = im.filter(ImageFilter.SHARPEN)
        im = im.filter(ImageFilter.SHARPEN)
    im.save(fn)
    show_benchmark(start_time)

def mazy4(params, fn):
    start_time = dt.now()
    w = params['w']
    h = params['h']
    print('mazy4...', fn)
    random.seed()
    im = Image.new('RGB', (w, h), params['bg'])
    draw = ImageDraw.Draw(im)

    for n in range(params['n']):
        if params['mode'] == 'center':
            w0 = w/2
            h0 = h/2
        else:
            w0 = random.randint(0, w)
            h0 = random.randint(0, h)
        sx = int(w/2.05)
        sy = int(h/2.05)
        po = [(w0+random.randint(-sx, sx), h0+random.randint(-sy, sy)),
              (w0+random.randint(-sx, sx), h0+random.randint(-sy, sy)),
              (w0+random.randint(-sx, sx), h0+random.randint(-sy, sy)),
              (w0+random.randint(-sx, sx), h0+random.randint(-sy, sy)),
              (w0+random.randint(-sx, sx), h0+random.randint(-sy, sy)),
              (w0+random.randint(-sx, sx), h0+random.randint(-sy, sy)),
              (w0+random.randint(-sx, sx), h0+random.randint(-sy, sy)),
              (w0+random.randint(-sx, sx), h0+random.randint(-sy, sy)),
              (w0+random.randint(-sx, sx), h0+random.randint(-sy, sy)),
              (w0+random.randint(-sx, sx), h0+random.randint(-sy, sy)),
              (w0+random.randint(-sx, sx), h0+random.randint(-sy, sy)),
              (w0+random.randint(-sx, sx), h0+random.randint(-sy, sy)),
              (w0+random.randint(-sx, sx), h0+random.randint(-sy, sy)),
              (w0+random.randint(-sx, sx), h0+random.randint(-sy, sy)),
              (w0+random.randint(-sx, sx), h0+random.randint(-sy, sy)),
              (w0+random.randint(-sx, sx), h0+random.randint(-sy, sy)),
              (w0+random.randint(-sx, sx), h0+random.randint(-sy, sy)),
              (w0+random.randint(-sx, sx), h0+random.randint(-sy, sy)),
              (w0+random.randint(-sx, sx), h0+random.randint(-sy, sy)),
              (w0+random.randint(-sx, sx), h0+random.randint(-sy, sy))
              ]

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

        draw.polygon(po, fill=color, outline=None)

    im.save(fn)
    show_benchmark(start_time)

# ---

def do_mazy1(cnt, w, h, odir):

    params1 = {
        'w': w, 'h': h, 'bg': (255, 255, 255),
        'pw': 5+3,
        'v': 50-0-20-10,
        'n': 20*5,
        'm': 100-50-10,
        'prefill': True,
        'blur': True,
        'r0': 64,
        'g0': 64,
        'b0': 64,
        'r1': 256,
        'g1': 256,
        'b1': 256,
        'mode': 'black',
        'keep': False,
    }

    params2 = {
        'w': w, 'h': h, 'bg': (255, 255, 255),
        'pw': 5+3,
        'v': 50+25,
        'n': 20*5,
        'm': 100-50-10,
        'prefill': False,
        'blur': True,
        'r0': 0,
        'g0': 0,
        'b0': 0,
        'r1': 256,
        'g1': 0,
        'b1': 0,
        'mode': 'red',
        'keep': False,
    }

    params3 = {
        'w': w, 'h': h, 'bg': (255, 255, 255),
        'pw': 5+3,
        'v': 50-0-20,
        'n': 20*5,
        'm': 100-50-10,
        'prefill': True,
        'blur': False,
        'r0': 64,
        'g0': 64,
        'b0': 0,
        'r1': 256,
        'g1': 256,
        'b1': 32,
        'mode': 'red',
        'keep': False,
    }

    params4 = {
        'w': w, 'h': h, 'bg': (255, 255, 255),
        'pw': 5+3,
        'v': 50-0-20,
        'n': 20*5,
        'm': 100-50-10,
        'prefill': True,
        'blur': False,
        'r0': 0,
        'g0': 64,
        'b0': 0,
        'r1': 32,
        'g1': 256,
        'b1': 32,
        'mode': 'red',
        'keep': False,
    }

    params5 = {
        'w': w, 'h': h, 'bg': (255, 255, 0),
        'pw': 5,
        'v': 200,
        'n': 50,
        'm': 25,
        'prefill': False,
        'blur': False,
        'r0': 0,
        'g0': 0,
        'b0': 0,
        'r1': 256,
        'g1': 256,
        'b1': 256,
        'mode': 'red',
        'keep': True,
    }

    params6 = {
        'w': w, 'h': h, 'bg': (255, 255, 0),
        'pw': 5,
        'v': 120,
        'n': 48,
        'm': 12,
        'prefill': True,
        'blur': False,
        'r0': 16,
        'g0': 64,
        'b0': 128,
        'r1': 128,
        'g1': 256,
        'b1': 256,
        'mode': 'red',
        'keep': True,
    }

    for n in range(cnt):
        mazy1(params1, odir+'mazy1-%dx%d-01-%03d.png' % (w, h, n+1))
        mazy1(params2, odir+'mazy1-%dx%d-02-%03d.png' % (w, h, n+1))
        mazy1(params3, odir+'mazy1-%dx%d-03-%03d.png' % (w, h, n+1))
        mazy1(params4, odir+'mazy1-%dx%d-04-%03d.png' % (w, h, n+1))
        mazy1(params5, odir+'mazy1-%dx%d-05-%03d.png' % (w, h, n+1))
        mazy1(params6, odir+'mazy1-%dx%d-06-%03d.png' % (w, h, n+1))

def do_mazy2(cnt, w, h, odir):

    params1 = {
        'w': w, 'h': h, 'bg': (255, 255, 255),
        'v': 50-0-20-10,
        'n': 20*4,
        'm': 40,
        'blur': True,
        'r0': 64,
        'g0': 64,
        'b0': 64,
        'r1': 256,
        'g1': 256,
        'b1': 256,
        'mode': 'black',
    }

    params2 = {
        'w': w, 'h': h, 'bg': (255, 255, 255),
        'v': 50+25,
        'n': 20*5,
        'm': 100-50-10,
        'blur': True,
        'r0': 0,
        'g0': 0,
        'b0': 0,
        'r1': 256,
        'g1': 0,
        'b1': 0,
        'mode': 'red',
    }

    params3 = {
        'w': w, 'h': h, 'bg': (255, 255, 255),
        'v': 30,
        'n': 20*5,
        'm': 100-50-10,
        'blur': False,
        'r0': 64,
        'g0': 64,
        'b0': 0,
        'r1': 256,
        'g1': 256,
        'b1': 32,
        'mode': 'red',
    }

    params4 = {
        'w': w, 'h': h, 'bg': (255, 255, 255),
        'v': 30,
        'n': 80,
        'm': 50,
        'blur': False,
        'r0': 0,
        'g0': 48,
        'b0': 0,
        'r1': 2,
        'g1': 256,
        'b1': 48,
        'mode': 'red',
    }

    params5 = {
        'w': w, 'h': h, 'bg': (255, 255, 0),
        'v': 50,
        'n': 30,
        'm': 25,
        'blur': True,
        'r0': 32,
        'g0': 64,
        'b0': 64,
        'r1': 64,
        'g1': 256,
        'b1': 256,
        'mode': 'color',
    }

    params6 = {
        'w': w, 'h': h, 'bg': (0, 0, 0),
        'v': 22,
        'n': 24,
        'm': 40,
        'blur': False,
        'r0': 32,
        'g0': 0,
        'b0': 0,
        'r1': 256,
        'g1': 0,
        'b1': 0,
        'mode': 'black',
    }

    for n in range(cnt):
	    mazy2(params1, odir+'mazy2-%dx%d-01-%03d.png' % (w, h, n+1))
	    mazy2(params2, odir+'mazy2-%dx%d-02-%03d.png' % (w, h, n+1))
	    mazy2(params3, odir+'mazy2-%dx%d-03-%03d.png' % (w, h, n+1))
	    mazy2(params4, odir+'mazy2-%dx%d-04-%03d.png' % (w, h, n+1))
	    mazy2(params5, odir+'mazy2-%dx%d-05-%03d.png' % (w, h, n+1))
	    mazy2(params6, odir+'mazy2-%dx%d-06-%03d.png' % (w, h, n+1))

def do_mazy3(cnt, w, h, odir):

    params1 = {
        'w': w, 'h': h, 'bg': (255, 255, 255),
        'n': 20,
        'm': 0,
        'blur': False,
        'r0': 16,
        'g0': 64,
        'b0': 64,
        'r1': 256,
        'g1': 256,
        'b1': 256,
        'mode': '',
    }

    params2 = {
        'w': w, 'h': h, 'bg': (255, 255, 0),
        'n': 10,
        'm': 0,
        'blur': False,
        'r0': 0,
        'g0': 0,
        'b0': 0,
        'r1': 256,
        'g1': 0,
        'b1': 0,
        'mode': '',
    }

    params3 = {
        'w': w, 'h': h, 'bg': (255, 255, 0),
        'n': 30,
        'm': 0,
        'blur': False,
        'r0': 64,
        'g0': 64,
        'b0': 0,
        'r1': 256,
        'g1': 256,
        'b1': 32,
        'mode': '',
    }

    params4 = {
        'w': w, 'h': h, 'bg': (255, 255, 0),
        'n': 20,
        'm': 0,
        'blur': False,
        'r0': 0,
        'g0': 48,
        'b0': 0,
        'r1': 2,
        'g1': 256,
        'b1': 48,
        'mode': '',
    }

    params5 = {
        'w': w, 'h': h, 'bg': (255, 255, 0),
        'n': 30,
        'm': 0,
        'blur': False,
        'r0': 32,
        'g0': 64,
        'b0': 64,
        'r1': 64,
        'g1': 256,
        'b1': 256,
        'mode': '',
    }

    params6 = {
        'w': w, 'h': h, 'bg': (0, 0, 0),
        'n': 30,
        'm': 0,
        'blur': False,
        'r0': 32,
        'g0': 0,
        'b0': 0,
        'r1': 256,
        'g1': 0,
        'b1': 0,
        'mode': '',
    }

    for n in range(cnt):
	    mazy3(params1, odir+'mazy3-%dx%d-01-%03d.png' % (w, h, n+1))
	    mazy3(params2, odir+'mazy3-%dx%d-02-%03d.png' % (w, h, n+1))
	    mazy3(params3, odir+'mazy3-%dx%d-03-%03d.png' % (w, h, n+1))
	    mazy3(params4, odir+'mazy3-%dx%d-04-%03d.png' % (w, h, n+1))
	    mazy3(params5, odir+'mazy3-%dx%d-05-%03d.png' % (w, h, n+1))
	    mazy3(params6, odir+'mazy3-%dx%d-06-%03d.png' % (w, h, n+1))

def do_mazy4(cnt, w, h, odir):

    params1 = {
        'w': w, 'h': h, 'bg': (255, 255, 255),
        'n': 5,
        'r0': 16,
        'g0': 64,
        'b0': 64,
        'r1': 256,
        'g1': 256,
        'b1': 256,
        'mode': 'center',
    }

    params2 = {
        'w': w, 'h': h, 'bg': (255, 255, 0),
        'n': 5,
        'r0': 0,
        'g0': 0,
        'b0': 0,
        'r1': 256,
        'g1': 0,
        'b1': 0,
        'mode': 'center',
    }

    params3 = {
        'w': w, 'h': h, 'bg': (255, 255, 0),
        'n': 5,
        'r0': 64,
        'g0': 64,
        'b0': 0,
        'r1': 256,
        'g1': 256,
        'b1': 32,
        'mode': 'center',
    }

    params4 = {
        'w': w, 'h': h, 'bg': (255, 255, 0),
        'n': 5,
        'r0': 0,
        'g0': 48,
        'b0': 0,
        'r1': 2,
        'g1': 256,
        'b1': 48,
        'mode': 'center',
    }

    params5 = {
        'w': w, 'h': h, 'bg': (255, 255, 0),
        'n': 4,
        'r0': 32,
        'g0': 64,
        'b0': 64,
        'r1': 64,
        'g1': 256,
        'b1': 256,
        'mode': 'center',
    }

    params6 = {
        'w': w, 'h': h, 'bg': (0, 0, 0),
        'n': 5,
        'r0': 32,
        'g0': 0,
        'b0': 0,
        'r1': 256,
        'g1': 0,
        'b1': 0,
        'mode': '',
    }

    params7 = {
        'w': w, 'h': h, 'bg': (0, 0, 0),
        'n': 3,
        'r0': 64,
        'g0': 0,
        'b0': 0,
        'r1': 256,
        'g1': 0,
        'b1': 0,
        'mode': 'center',
    }

    for n in range(cnt):
	    mazy4(params1, odir+'mazy4-%dx%d-01-%03d.png' % (w, h, n+1))
	    mazy4(params2, odir+'mazy4-%dx%d-02-%03d.png' % (w, h, n+1))
	    mazy4(params3, odir+'mazy4-%dx%d-03-%03d.png' % (w, h, n+1))
	    mazy4(params4, odir+'mazy4-%dx%d-04-%03d.png' % (w, h, n+1))
	    mazy4(params5, odir+'mazy4-%dx%d-05-%03d.png' % (w, h, n+1))
	    mazy4(params6, odir+'mazy4-%dx%d-06-%03d.png' % (w, h, n+1))
	    mazy4(params7, odir+'mazy4-%dx%d-07-%03d.png' % (w, h, n+1))

# ---

def main():
    start_time = dt.now()
    cnt = 10
    w, h = get_canvas('A3')
    odir = '!!!mazy-out\\'
    do_mazy1(cnt, w, h, odir)
    do_mazy2(cnt, w, h, odir)
    do_mazy3(cnt, w, h, odir)
    do_mazy4(cnt, w, h, odir)
    time_elapsed = dt.now() - start_time
    print('ALL done. elapsed time: {}'.format(time_elapsed))


if __name__ == '__main__':
    main()
