#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 20190330

# repixelize

# IDEA: src pixels as big filled circles/boxes, possible rnd size variation, src img rescale


import random, math, string, os, sys
from PIL import Image, ImageDraw, ImageFont, ImageOps
from drawtools import *
from color_defs import *

# TODO: xy scale sync issue

def repix(params):
    c = math.pi/180
    w = params['w']
    h = params['h']
    src = Image.open(params['infile'])
    scale = params['scale']
    if scale != 1.0:
        src = src.resize((int(src.width*scale), int(src.height*scale)), resample=Image.BICUBIC, box=None) # opt
    img = Image.new('RGB', (w, h), color = (255, 255, 255))
    coef = params['coef'] # dot radius coefficient %
    srcw = src.width
    srch = src.height
    random.seed()
    d = ImageDraw.Draw(img)
    dx = int(w/srcw)
    dy = int(h/srch)
    for x in range(srcw):
        for y in range(srch):
            xy = (x, y)
            cin = src.getpixel(xy)
            if params['rnd'] == True:
                coef = random.randint(params['rmin'], params['rmax']) / 100
            if params['mode'] == 0:
                rect(d, x*dx, y*dy, int(dx/2*coef), int(dy/2*coef), fill=cin, outline=None)
            if params['mode'] == 1:
                circle(d, x*dx, y*dy, int(dy/2*coef), fill=cin, outline=None)
            if params['mode'] == 2:
                po = []
                r = int(dy/2*coef)
                for i in range(12):
                    rfx = random.randint(-10, 10)
                    rfy = random.randint(-10, 10)
                    a = c*i/12*360
                    x1 = int(x*dx+(r+rfx)*math.cos(a))
                    y1 = int(y*dy+(r+rfy)*math.sin(a))
                    po.append((x1, y1))
                d.polygon(po, fill=cin, outline=None)
            if params['mode'] == 3:
                if random.randint(0, 100) > 50:
                    rect(d, x*dx, y*dy, int(dx/2*coef), int(dy/2*coef), fill=cin, outline=None)
                else:
                    circle(d, x*dx, y*dy, int(dy/2*coef), fill=cin, outline=None)
            if params['mode'] == 4:
                if random.randint(0, 100) > 50:
                    rect(d, x*dx, y*dy, int(dx/2*coef), int(dy/2*coef), fill=cin, outline=None)
                else:
                    if random.randint(0, 100) > 50:
                        circle(d, x*dx, y*dy, int(dy/2*coef), fill=cin, outline=None)
                    else:
                        po = []
                        r = int(dy/2*coef)
                        for i in range(12):
                            rfx = random.randint(-10, 10)
                            rfy = random.randint(-10, 10)
                            a = c*i/12*360
                            x1 = int(x*dx+(r+rfx)*math.cos(a))
                            y1 = int(y*dy+(r+rfy)*math.sin(a))
                            po.append((x1, y1))
                        d.polygon(po, fill=cin, outline=None)


    return img

def do_repix(infile, outfile):
    #w, h = get_canvas('A4')
    w, h = get_canvas('A3')
    #w, h = get_canvas('A2')
    #w, h = get_canvas('A1')
    params = {'w': w, 'h': h, 'infile': infile, 'coef': 0.8, 'scale': 0.5, 'rnd': True, 'mode': 2, 'rmin': 50, 'rmax': 500} # high rmax may be cool, eg 500
    img = repix(params)
    img.save(outfile)
    
# --- go

do_repix('repixel-in\\00base1x-gdc.png', 'repixel01-x.png')
do_repix('repixel-in\\gdc-zx-20181109-3a-x1-x.png', 'repixel02-x.png')
do_repix('repixel-in\\grow22c1v3-1.png', 'repixel03-x.png')
do_repix('repixel-in\\fromopenshot1zzz2-x.png', 'repixel04-x.png')
do_repix('repixel-in\\PIC_2548-cp-min.JPG', 'repixel05-x.png')
do_repix('repixel-in\\test1.png', 'repixel06-x.png')
do_repix('repixel-in\\grych.png', 'repixel07-x.png')
do_repix('repixel-in\\grych2.png', 'repixel08-x.png')
