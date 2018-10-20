#! /usr/bin/env python
# -*- coding: utf-8 -*-

# paint algorithms (artificial artist), v1.0, Python version
# (c)2018 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz
# #5 nowe mazy
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
from datetime import datetime as dt
from drawtools import *

#zielony
#fioletowy
#pomarancz
#rozowo-fioletowy
#niebieski
#ciemny zolty
#rolty
#rozowy

# old?
colors_old = [(0x8A, 0xD3, 0x8C),
          (0x96, 0x78, 0xD6),
          (0xE9, 0x8B, 0x7B),
          (0xD0, 0x76, 0xD0),
          (0x8C, 0xA8, 0xD0),
          (0xED, 0xA0, 0x7C),
          (0xD5, 0xCB, 0x7D),
          (0xE0, 0x79, 0x9C),
          ]

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
          (0x00, 0x00, 0xA),
          (0x00, 0x00, 0xC0),
          (0x00, 0x00, 0xE0),
          (0x00, 0x00, 0xFF),
          ]


def mazy5(params, png_file='smears5.png', output_mode='save'):
    start_time = dt.now()
    w = params['w']
    h = params['h']
    colors = params['colors']
    print('mazy5...', png_file)
    random.seed()
    im = Image.new('RGB', (w, h), params['bg'])
    draw = ImageDraw.Draw(im)
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
            draw.polygon(points, fill=colors[m%8], outline=None)
            #draw.polygon(points, fill=colors[m%8], outline=(0,0,0)) # opt outlined

    if output_mode == 'save':
        im.save(png_file)
        show_benchmark(start_time)
    else:
        im2cgi(im)

# ---

def do_mazy5(cnt, w, h, odir):
    params1 = {'w': w, 'h': h, 'bg': (0, 0, 0), 'colors': colors_b}
    params2 = {'w': w, 'h': h, 'bg': (0, 0, 0), 'colors': colors_p}
    params3 = {'w': w, 'h': h, 'bg': (0, 0, 0), 'colors': colors_bw}
    for n in range(cnt):
        mazy5(params1, odir+'mazy5-%dx%d-01-%03d.png' % (w, h, n+1))
        mazy5(params2, odir+'mazy5-%dx%d-02-%03d.png' % (w, h, n+1))
        mazy5(params3, odir+'mazy5-%dx%d-03-%03d.png' % (w, h, n+1))
        
# ---

def main():
    start_time = dt.now()
    cnt = 4
    w, h = get_canvas('A3')
    odir = '!!!mazy-out\\'
    do_mazy5(cnt, w, h, odir)
    #tmp CGI
    #do_mazy5(1, w, h, '', output_mode='cgi')
    time_elapsed = dt.now() - start_time
    print('ALL done. elapsed time: {}'.format(time_elapsed))


if __name__ == '__main__':
    main()
