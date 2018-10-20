#! /usr/bin/env python
# -*- coding: utf-8 -*-

# paint algorithms (artificial artist), v1.0, Python version
# (c)2018 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz
# new smears (nowe mazy) #5
# cre: 20180805
# upd: 20180807, 08
# upd: 20180928, 29
# upd: 20181019, 20

# see:
# https://pillow.readthedocs.io/en/3.1.x/reference/ImageDraw.html
# http://pillow.readthedocs.io/en/5.1.x/reference/ImageFilter.html

# TODO:
# - ?


from PIL import Image, ImageDraw, ImageFilter
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

# ---

def do_mazy5(cnt, w, h, odir):
    params1 = {'name': 'SMEARS#5', 'call': mazy5, 'w': w, 'h': h, 'Background': (0, 0, 0), 'colors': colors_b, 'outline': None}
    params2 = {'name': 'SMEARS#5', 'call': mazy5, 'w': w, 'h': h, 'Background': (0, 0, 0), 'colors': colors_y, 'outline': None}
    params3 = {'name': 'SMEARS#5', 'call': mazy5, 'w': w, 'h': h, 'Background': (0, 0, 0), 'colors': colors_p, 'outline': (0, 0, 0)}
    params4 = {'name': 'SMEARS#5', 'call': mazy5, 'w': w, 'h': h, 'Background': (0, 0, 0), 'colors': colors_bw, 'outline': None}
    for n in range(cnt):
        art_painter(params1, odir+'mazy5-%dx%d-01-%03d.png' % (w, h, n+1))
        art_painter(params2, odir+'mazy5-%dx%d-02-%03d.png' % (w, h, n+1))
        art_painter(params3, odir+'mazy5-%dx%d-03-%03d.png' % (w, h, n+1))
        art_painter(params4, odir+'mazy5-%dx%d-04-%03d.png' % (w, h, n+1))
        
# ---

cnt = 3
w, h = get_canvas('A3')
odir = '!!!mazy-out\\'
do_mazy5(cnt, w, h, odir)
#tmp CGI
#params1 = {'name': 'SMEARS#5', 'call': mazy5, 'w': w, 'h': h, 'Background': (0, 0, 0), 'colors': colors_b, 'outline': None}
#art_painter(params1, '', output_mode='cgi')
