#! /usr/bin/env python
# -*- coding: utf-8 -*-

# drawings (astro objects) in Python
# (c)2018 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz
# https://pillow.readthedocs.io/en/3.1.x/reference/ImageDraw.html
# cre: 20180405
# upd; 20180406, 07
# upd; 20180502, 03
# upd: 20181020

# TODO:
# - misc
# - big bang, more


from PIL import Image, ImageDraw, ImageFilter
import random, math, string, os, sys
from datetime import datetime as dt
from drawtools import *


def draw_tool(draw, params, color, x, y, z):
    box_or_cir = params['box_or_cir']
    ou = params['ou']
    if box_or_cir == False:
        circle(draw, x, y, z, fill=color, outline=ou)
    else:
        box(draw, x, y, z, fill=color, outline=ou)

# blue galaxy
def paint0(draw, params):
    w = params['w']
    h = params['h']
    for r in range(36):
        for n in range(8):
            color = (0, 32+n*24, 32+n*40)
            da = 360/8*c
            x = w/2+(60+r*60)*math.cos(n*da+r*36*c)
            y = h/2+(60+r*60)*math.sin(n*da+r*36*c)
            z = 110-r*1.3
            draw_tool(draw, params, color, x, y, z)

# elliptic galaxy
def paint1(draw, params):
    w = params['w']
    h = params['h']
    random.seed()
    for r in range(48):
        for n in range(24):
            if random.randint(0, 100) > 80:
                color = (random.randint(192, 255), 0, 0)
            else:
                rg1 = random.randint(192, 255)
                color = (rg1, rg1, 0)
            da = 360/24*c
            x = w/2+(64+r*50)*math.cos(n*da+r*36*c)
            y = h/2+(64+r*50)*math.sin(n*da+r*36*c)
            z = 72-1.8*r
            draw_tool(draw, params, color, x, y, z)

# spiral galaxy
def paint2(draw, params):
    w = params['w']
    h = params['h']
    for r in range(48):
        for n in range(18):
            color = gradient((255,255,224), (255,255,0), (255,0,0), r, 48)
            da = 360/12*c
            x = w/2+(64+r*50)*math.cos(n*da+r*36*1.1*c)
            y = h/2+(64+r*50)*math.sin(n*da+r*36*c)
            z = 80-1.65*r
            draw_tool(draw, params, color, x, y, z)

# neutron star
def paint3(draw, params):
    w = params['w']
    h = params['h']
    for r in range(50):
        for n in range(12):
            if n&1 == 0:
                color = (255,255,255)
            else:
                color = (0,192,255)
            da = 360/8*c
            x = w/2+8*(5+r*6)*math.cos(n*da+r*72*c)
            y = h/2+8*(5+r*6)*math.sin(n*da+r*72*c)
            z = 120-1.6*r
            draw_tool(draw, params, color, x, y, z)

# black hole
def paint4(draw, params):
    w = params['w']
    h = params['h']
    for r in range(32):
        for n in range(16):
            nn = n%8
            color = gradient2((255,255,255), (255,224,0), r, 32)
            da = 360/16*c
            x = w/2+8*(6+r*12)*math.cos(n*da+r*72*c)
            y = h/2+8*(6+r*12)*math.sin(n*da+r*72*c)
            z = 25+1.65*r*r
            draw_tool(draw, params, color, x, y, z)

# supernova
def paint5(draw, params):
    w = params['w']
    h = params['h']
    for r in range(48):
        for n in range(8):
            color = gradient((255,255,0), (0,128,255), (255,255,255), n*r, 48*8)
            da = 360/8*c
            x = w/2+8*(8+r*8)*math.cos(n*da+r*72*c)
            y = h/2+8*(8+r*8)*math.sin(n*da+r*72*c)
            z = 24+80*(1+math.sin(r*16*c))
            draw_tool(draw, params, color, x, y, z)

# nebula
def paint6(draw, params):
    w = params['w']
    h = params['h']
    random.seed()
    for r in range(2048):
        for n in range(24):
            color = (random.randint(32, 256), 32+r*12, 32+n*32)
            da = 360/24*c
            x = w/2+random.randint(0, int(w/4))-random.randint(0, int(w/4))+8*(4+r*16)*math.cos(n*da+r*72*c)
            y = h/2+random.randint(0, int(h/4))-random.randint(0, int(h/4))+8*(4+r*16)*math.sin(n*da+r*72*c)
            z = random.randint(8, 100)
            draw_tool(draw, params, color, x, y, z)

# star
def paint7(draw, params):
    w = params['w']
    h = params['h']
    for r in range(40):
        for n in range(8):
            color = gradient((255,255,255), (255,255,0), (255,0,0), r, 40)
            da = 360/8*c
            x = w/2+(60+r*60)*math.cos(n*da+r*36*c)
            y = h/2+(60+r*60)*math.sin(n*da+r*36*c)
            z = 110-r*1.3
            draw_tool(draw, params, color, x, y, z)

# ---

c = math.pi/180
w, h = get_canvas('A3') # note: does not scalle well with canvas size, so far optimised only for A3

params0f = {'name': 'ASTROART', 'call': paint0, 'w': w, 'h': h, 'Background': (0, 0, 0), 'ou': (0,0,0), 'box_or_cir': False}
params0t = {'name': 'ASTROART', 'call': paint0, 'w': w, 'h': h, 'Background': (0, 0, 0), 'ou': (0,0,0), 'box_or_cir': True}
params1f = {'name': 'ASTROART', 'call': paint1, 'w': w, 'h': h, 'Background': (0, 0, 0), 'ou': (0,0,0), 'box_or_cir': False}
params1t = {'name': 'ASTROART', 'call': paint1, 'w': w, 'h': h, 'Background': (0, 0, 0), 'ou': (0,0,0), 'box_or_cir': True}
params2f = {'name': 'ASTROART', 'call': paint2, 'w': w, 'h': h, 'Background': (0, 0, 0), 'ou': (0,0,0), 'box_or_cir': False}
params2t = {'name': 'ASTROART', 'call': paint2, 'w': w, 'h': h, 'Background': (0, 0, 0), 'ou': (0,0,0), 'box_or_cir': True}
params3f = {'name': 'ASTROART', 'call': paint3, 'w': w, 'h': h, 'Background': (0, 0, 0), 'ou': (0,0,0), 'box_or_cir': False}
params3t = {'name': 'ASTROART', 'call': paint3, 'w': w, 'h': h, 'Background': (0, 0, 0), 'ou': (0,0,0), 'box_or_cir': True}
params4f = {'name': 'ASTROART', 'call': paint4, 'w': w, 'h': h, 'Background': (0, 0, 0), 'ou': (0,0,0), 'box_or_cir': False}
params4t = {'name': 'ASTROART', 'call': paint4, 'w': w, 'h': h, 'Background': (0, 0, 0), 'ou': (0,0,0), 'box_or_cir': True}
params5f = {'name': 'ASTROART', 'call': paint5, 'w': w, 'h': h, 'Background': (0, 0, 0), 'ou': (0,0,0), 'box_or_cir': False}
params5t = {'name': 'ASTROART', 'call': paint5, 'w': w, 'h': h, 'Background': (0, 0, 0), 'ou': (0,0,0), 'box_or_cir': True}
params6f = {'name': 'ASTROART', 'call': paint6, 'w': w, 'h': h, 'Background': (0, 0, 0), 'ou': (0,0,0), 'box_or_cir': False}
params6t = {'name': 'ASTROART', 'call': paint6, 'w': w, 'h': h, 'Background': (0, 0, 0), 'ou': (0,0,0), 'box_or_cir': True}
params7f = {'name': 'ASTROART', 'call': paint7, 'w': w, 'h': h, 'Background': (0, 0, 0), 'ou': (0,0,0), 'box_or_cir': False}
params7t = {'name': 'ASTROART', 'call': paint7, 'w': w, 'h': h, 'Background': (0, 0, 0), 'ou': (0,0,0), 'box_or_cir': True}

#tmp CGI
#p = cgiart.get_cgi_par()
#n = 0 # 0..7
#n = int(p["f"])
#art_painter(...?


art_painter(params0f, 'zz-01-bluegalaxy-cir.png')
art_painter(params0t, 'zz-01-bluegalaxy-box.png')

art_painter(params1f, 'zz-02-ellipticgalaxy-cir.png')
art_painter(params1t, 'zz-02-ellipticgalaxy-box.png')

art_painter(params2f, 'zz-03-spiralgalaxy-cir.png')
art_painter(params2t, 'zz-03-spiralgalaxy-box.png')

art_painter(params3f, 'zz-04-neutronstar-cir.png')
art_painter(params3t, 'zz-04-neutronstar-box.png')

art_painter(params4f, 'zz-05-blackhole-cir.png')
art_painter(params4t, 'zz-05-blackhole-box.png')

art_painter(params5f, 'zz-06-supernova-cir.png')
art_painter(params5t, 'zz-06-supernova-box.png')

art_painter(params5f, 'zz-07-nebula-cir.png')
art_painter(params6t, 'zz-07-nebula-box.png')

art_painter(params7f, 'zz-08-star-cir.png')
art_painter(params7t, 'zz-08-star-box.png')
