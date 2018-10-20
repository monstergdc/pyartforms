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
from drawtools import get_canvas, circle, box, triangle, gradient, gradient2, im2cgi, show_benchmark



# blue galaxy
def paint0(draw, ou, box_or_cir):
    for r in range(36):
        for n in range(8):
            color = (0, 32+n*24, 32+n*40)
            da = 360/8*c
            x = canvas[0]/2+(60+r*60)*math.cos(n*da+r*36*c)
            y = canvas[1]/2+(60+r*60)*math.sin(n*da+r*36*c)
            z = 110-r*1.3
            if box_or_cir == False:
                circle(draw, x, y, z, fill=color, outline=ou)
            else:
                box(draw, x, y, z, fill=color, outline=ou)

# elliptic galaxy
def paint1(draw, ou, box_or_cir):
    for r in range(48):
        for n in range(24):
            if random.randint(0, 100) > 80:
                cx = (random.randint(192, 255), 0, 0)
            else:
                rg1 = random.randint(192, 255)
                cx = (rg1, rg1, 0)
            da = 360/24*c
            x = canvas[0]/2+(64+r*50)*math.cos(n*da+r*36*c)
            y = canvas[1]/2+(64+r*50)*math.sin(n*da+r*36*c)
            z = 72-1.8*r
            if box_or_cir == False:
                circle(draw, x, y, z, fill=(cx), outline=ou)
            else:
                box(draw, x, y, z, fill=(cx), outline=ou)

# spiral galaxy
def paint2(draw, ou, box_or_cir):
    for r in range(48):
        for n in range(18):
            cx = gradient((255,255,224), (255,255,0), (255,0,0), r, 48)
            da = 360/12*c
            x = canvas[0]/2+(64+r*50)*math.cos(n*da+r*36*1.1*c)
            y = canvas[1]/2+(64+r*50)*math.sin(n*da+r*36*c)
            z = 80-1.65*r
            if box_or_cir == False:
                circle(draw, x, y, z, fill=(cx), outline=ou)
            else:
                box(draw, x, y, z, fill=(cx), outline=ou)

# neutron star
def paint3(draw, ou, box_or_cir):
    for r in range(50):
        for n in range(12):
            if n&1 == 0:
                cx = (255,255,255)
            else:
                cx = (0,192,255)
            da = 360/8*c
            x = canvas[0]/2+8*(5+r*6)*math.cos(n*da+r*72*c)
            y = canvas[1]/2+8*(5+r*6)*math.sin(n*da+r*72*c)
            z = 120-1.6*r
            if box_or_cir == False:
                circle(draw, x, y, z, fill=(cx), outline=ou)
            else:
                box(draw, x, y, z, fill=(cx), outline=ou)

# black hole
def paint4(draw, ou, box_or_cir):
    for r in range(32):
        for n in range(16):
            nn = n%8
            cx = gradient2((255,255,255), (255,224,0), r, 32)
            da = 360/16*c
            x = canvas[0]/2+8*(6+r*12)*math.cos(n*da+r*72*c)
            y = canvas[1]/2+8*(6+r*12)*math.sin(n*da+r*72*c)
            z = 25+1.65*r*r
            if box_or_cir == False:
                circle(draw, x, y, z, fill=(cx), outline=ou)
            else:
                box(draw, x, y, z, fill=(cx), outline=ou)

# supernova
def paint5(draw, ou, box_or_cir):
    for r in range(48):
        for n in range(8):
            cx = gradient((255,255,0), (0,128,255), (255,255,255), n*r, 48*8)
            da = 360/8*c
            x = canvas[0]/2+8*(8+r*8)*math.cos(n*da+r*72*c)
            y = canvas[1]/2+8*(8+r*8)*math.sin(n*da+r*72*c)
            z = 24+80*(1+math.sin(r*16*c))
            if box_or_cir == False:
                circle(draw, x, y, z, fill=(cx), outline=ou)
            else:
                box(draw, x, y, z, fill=(cx), outline=ou)

# nebula
def paint6(draw, ou, box_or_cir):
    for r in range(2048):
        for n in range(24):
            cx = (random.randint(32, 256), 32+r*12, 32+n*32)
            da = 360/24*c
            x = canvas[0]/2+random.randint(0, int(canvas[0]/4))-random.randint(0, int(canvas[0]/4))+8*(4+r*16)*math.cos(n*da+r*72*c)
            y = canvas[1]/2+random.randint(0, int(canvas[1]/4))-random.randint(0, int(canvas[1]/4))+8*(4+r*16)*math.sin(n*da+r*72*c)
            z = random.randint(8, 100)
            if box_or_cir == False:
                circle(draw, x, y, z, fill=(cx), outline=ou)
            else:
                box(draw, x, y, z, fill=(cx), outline=ou)

# star
def paint7(draw, ou, box_or_cir):
    for r in range(40):
        for n in range(8):
            color = gradient((255,255,255), (255,255,0), (255,0,0), r, 40)
            da = 360/8*c
            x = canvas[0]/2+(60+r*60)*math.cos(n*da+r*36*c)
            y = canvas[1]/2+(60+r*60)*math.sin(n*da+r*36*c)
            z = 110-r*1.3
            if box_or_cir == False:
                circle(draw, x, y, z, fill=color, outline=ou)
            else:
                box(draw, x, y, z, fill=color, outline=ou)

# ---

def call_painter(n, box_or_cir, png_file, output_mode = 'save'):
    start_time = dt.now()
    print('drawing...', png_file)
    im = Image.new('RGB', canvas, (0, 0, 0))
    draw = ImageDraw.Draw(im)
    random.seed()
    ou = (0, 0, 0)
    if n == 0:
        paint0(draw, ou, box_or_cir)
    if n == 1:
        paint1(draw, ou, box_or_cir)
    if n == 2:
        paint2(draw, ou, box_or_cir)
    if n == 3:
        paint3(draw, ou, box_or_cir)
    if n == 4:
        paint4(draw, ou, box_or_cir)
    if n == 5:
        paint5(draw, ou, box_or_cir)
    if n == 6:
        paint6(draw, ou, box_or_cir)
    if n == 7:
        paint7(draw, ou, box_or_cir)

    if output_mode == 'save':
        im.save(png_file, dpi=(300,300))
        show_benchmark(start_time)
    else:
        im2cgi(im)

# ---

canvas = get_canvas('A3')
#canvas = get_canvas('640')
# note: does not scalle well with canvas size, so far optimised only for A3
c = math.pi/180

#tmp CGI
#p = cgiart.get_cgi_par()
#n = 0 # 0..7
#n = int(p["f"])
#call_painter(n, False, '')


call_painter(0, False, 'zz-01-bluegalaxy-cir.png')
call_painter(0, True, 'zz-01-bluegalaxy-box.png')

call_painter(1, False, 'zz-02-ellipticgalaxy-cir.png')
call_painter(1, True, 'zz-02-ellipticgalaxy-box.png')

call_painter(2, False, 'zz-03-spiralgalaxy-cir.png')
call_painter(2, True, 'zz-03-spiralgalaxy-box.png')

call_painter(3, False, 'zz-04-neutronstar-cir.png')
call_painter(3, True, 'zz-04-neutronstar-box.png')

call_painter(4, False, 'zz-05-blackhole-cir.png')
call_painter(4, True, 'zz-05-blackhole-box.png')

call_painter(5, False, 'zz-06-supernova-cir.png')
call_painter(5, True, 'zz-06-supernova-box.png')

call_painter(6, False, 'zz-07-nebula-cir.png')
call_painter(6, True, 'zz-07-nebula-box.png')

call_painter(7, False, 'zz-08-star-cir.png')
call_painter(7, True, 'zz-08-star-box.png')
