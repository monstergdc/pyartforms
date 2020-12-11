#! /usr/bin/env python
# -*- coding: utf-8 -*-

# PyArtForms - Repixelize algorithm (artificial artist), v1.0, Python version
# IDEA: src pixels as big filled circles/boxes/rnd-shapes, possible rnd size variation, src img rescale
# (c)2018-2020 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz
# tested with Python 3.5.2
# cre: 20190330
# upd: 20190401, 02, 03, 15, 22, 23
# upd: 20200724, 25, 30
# upd: 20201208, 10, 11

# note: input must be 24-bit RGB

# TODO: xy scale sync issue | more params


import random, math, os, sys
from PIL import Image, ImageDraw, ImageFont, ImageOps
from drawtools import *


def repix(params):
    """
    'Repixelize' - remake small image into big one, change each pixel to bigger predefined multipixel form
    """
    def rect_():
        rect(d, int(x*dx), int(y*dy), int(dx*coef), int(dy*coef), fill=cin, outline=None)
    def circle_():
        circle(d, int(x*dx), int(y*dy), int(dy/2*coef), fill=cin, outline=None)
    def poly_():
        po = []
        r = int(dy/2*coef)
        nn = 64 # par
        for i in range(nn):
            rfx = random.randint(-40, 40) # par
            rfy = random.randint(-40, 40) # par
            a = c*i/nn*360
            x1 = int(x*dx+(r+rfx)*math.cos(a))
            y1 = int(y*dy+(r+rfy)*math.sin(a))
            po.append((x1, y1))
        d.polygon(po, fill=cin, outline=None)
    def brush_():
        for b in range(30+random.randint(0, 60)): # par
            bs = 2+random.randint(0, 15) # par
            if random.randint(0, 100) > 90: # par, opt - exceed dest rect
                ofsx = random.randint(int(-dx), int(dx*2))
                ofsy = random.randint(int(-dy), int(dy*2))
            else:
                ofsx = random.randint(0+1, int(dx)-1)
                ofsy = random.randint(0+1, int(dy)-1)
            rect(d, int(x*dx+ofsx), int(y*dy+ofsy), int(bs), int(bs), fill=cin, outline=None)
    def lines_():
        for b in range(random.randint(25, 25+55)): # par
            bs = random.randint(1, 6) # par
            addx1 = 0
            addy1 = 0
            addx2 = 0
            addy2 = 0
            ex = 4 # par
            if random.randint(0, 100) >= 80: #par?
                addx1 = -dx * random.randint(1, ex)
            if random.randint(0, 100) >= 80: #par?
                addx2 = dx * random.randint(1, ex)
            horizontal = False
            if 'horizontal' in params:
                if params['horizontal'] == True:
                    horizontal = True
            if not horizontal:
                if random.randint(0, 100) > 80: #par?
                    addy1 = -dy * random.randint(1, ex)
                if random.randint(0, 100) >= 80: #par?
                    addy2 = dy * random.randint(1, ex)
            points = [x*dx+addx1+random.randint(0+1, int(dx)-1), y*dy+addy1+random.randint(0+1, int(dy)-1), x*dx+addx2+random.randint(0+1, int(dx)-1), y*dy+addy2+random.randint(0+1, int(dy)-1)]
            d.line(points, fill=cin, width=bs)

    c = math.pi/180
    w = params['w']
    h = params['h']
    try:
        src = Image.open(params['infile'])
    except:
        print("Error opening file:", params['infile'])
        return
    outfile = params['outfile']
    if 'scale' in params:
        scale = params['scale']
        if scale != 1.0:
            src = src.resize((int(src.width*scale), int(src.height*scale)), resample=Image.BICUBIC, box=None)
    if 'bk' in params:
        bk = params['bk']
    else:
        bk = (0,0,0)
    if 'nn' in params:
        nn = params['nn']
    else:
        nn = 0
    img = Image.new('RGB', (w, h), color = bk)
    coef = params['coef'] # note: dot radius coefficient %
    srcw = src.width
    srch = src.height
    random.seed()
    print('repix', params['mode'], params['infile'], '->', outfile)
    d = ImageDraw.Draw(img)
    dx = w/srcw
    dy = h/srch
    for x in range(srcw):
        for y in range(srch):
            cin = src.getpixel((x, y))
            if 'rnd' in params:
                if params['rnd'] == True:
                    coef = float(random.randint(params['rmin'], params['rmax'])) / 100.0
            if params['mode'] == 'rect':
                rect_()
            if params['mode'] == 'circle':
                circle_()
            if params['mode'] == 'poly':
                poly_()
            if params['mode'] == 'brush':
                brush_()
            if params['mode'] == 'lines':
                lines_()
    img.save(outfile)

# EOF
