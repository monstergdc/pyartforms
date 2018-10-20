#! /usr/bin/env python
# -*- coding: utf-8 -*-

# paint algorithms (artificial artist) in Python, v1.0
# (c)2017-2018 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz
# #1 okrutne czerwone mazy
# #2 circles
# #3 triangles
# #4 poly
# #5 new smears
# cre: 20180430
# upd: 20180501, 02, 03
# cre: 20180805, 07, 08
# upd: 20180928, 29
# upd: 20181019, 20

# see:
# https://pillow.readthedocs.io/en/3.1.x/reference/ImageDraw.html
# http://pillow.readthedocs.io/en/5.1.x/reference/ImageFilter.html

# TODO:
# - ?


from PIL import Image, ImageDraw
import random, math, string, os, sys
from bezier import make_bezier
from drawtools import *


# bw x2
colors_bw = [(0xff, 0xff, 0xff),
          (0xc0, 0xc0, 0xc0),
          (0xff, 0xff, 0xff),
          (0xc0, 0xc0, 0xc0),
          (0xff, 0xff, 0xff),
          (0xc0, 0xc0, 0xc0),
          (0xff, 0xff, 0xff),
          (0xc0, 0xc0, 0xc0),
          ]

# pastel psychedelic
colors_p = [(0x78, 0xE6, 0x7B),   #78E67B
          (0x8F, 0x60, 0xEE),   #8F60EE
          (0xFE, 0x7B, 0x65),   #FF7B65
          (0xE7, 0x5F, 0xE5),   #E75FE5
          (0x7B, 0xA4, 0xE0),   #7BA4E0
          (0xFF, 0x9C, 0x6B),   #FF9C6B
          (0xEB, 0xDD, 0x67),   #EBDD67
          (0xFA, 0x60, 0x93),   #FA6093
          ]

# magic blue
colors_b = [(0x00, 0x00, 0x20),
          (0x00, 0x00, 0x40),
          (0x00, 0x00, 0x60),
          (0x00, 0x00, 0x80),
          (0x00, 0x00, 0xA0),
          (0x00, 0x00, 0xC0),
          (0x00, 0x00, 0xE0),
          (0x00, 0x00, 0xFF),
          ]

# just yellow
colors_y = [(0x20, 0x20, 0x00),
          (0x40, 0x40, 0x00),
          (0x60, 0x60, 0x00),
          (0x80, 0x80, 0x00),
          (0xA0, 0xA0, 0x00),
          (0xC0, 0xC0, 0x00),
          (0xE0, 0xE0, 0x00),
          (0xFF, 0xFF, 0x00),
          ]

# ---

def mazy1(draw, params):
    w = params['w']
    h = params['h']
    random.seed()
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

def mazy2(draw, params):
    w = params['w']
    h = params['h']
    random.seed()
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

def mazy3(draw, params):
    w = params['w']
    h = params['h']
    random.seed()

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

def mazy4(draw, params):
    w = params['w']
    h = params['h']
    random.seed()

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

def mazy5(draw, params):
    w = params['w']
    h = params['h']
    colors = params['colors']
    random.seed()
    ts = [t/100.0 for t in range(101)]
    c = math.pi/180

    dg = h*0.037 # thickness
    r0 = h/2*0.93 # base radius
    rOut = h*0.76 # outer circle radous
    for i in range(int(8+1)):
        #a = params['a']
        #rv = params['rv']
        a = random.randint(6, 24)
        rv = random.randint(20, 350)
        if i == 0:
            x0 = w/2
            y0 = h/2
        else:
            x0 = w/2 + rOut * math.cos(c*(i-1)*360/8)
            y0 = h/2 + rOut * math.sin(c*(i-1)*360/8)
        for m in range(16):
            points = []
            for n in range(int(3600)):
                angle = c*n/10
                r = r0 - m*dg + rv * math.sin(angle*a)
                x = x0 + r * math.cos(angle)
                y = y0 + r * math.sin(angle)
                points.extend((x, y))
            draw.polygon(points, fill=colors[m%8], outline=params['outline'])

