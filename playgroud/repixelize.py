#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Repixelize algorithm (artificial artist), v1.0, Python version
# (c)2018-2019 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz
# cre: 20190330
# upd: 20190401, 02, 03, 15, 22

# repixelize
# IDEA: src pixels as big filled circles/boxes/rnd-shapes, possible rnd size variation, src img rescale
# TODO: xy scale sync issue, proper params, ext call


import random, math, string, os, sys
from PIL import Image, ImageDraw, ImageFont, ImageOps
from drawtools import *
from color_defs import *


def repix(params):
    c = math.pi/180
    w = params['w']
    h = params['h']
    src = Image.open(params['infile'])
    outfile = params['outfile']
    scale = params['scale']
    if scale != 1.0:
        src = src.resize((int(src.width*scale), int(src.height*scale)), resample=Image.BICUBIC, box=None) # opt
    if 'bk' in params:
        bk = params['bk']
    else:
        bk = (0,0,0)
    img = Image.new('RGB', (w, h), color = bk)
    coef = params['coef'] # dot radius coefficient %
    srcw = src.width
    srch = src.height
    random.seed()
    print('repix', params['infile'], outfile)
    d = ImageDraw.Draw(img)
    dx = int(w/srcw)
    dy = int(h/srch)
    for x in range(srcw):
        for y in range(srch):
            xy = (x, y)
            cin = src.getpixel(xy)
            if params['rnd'] == True:
                coef = random.randint(params['rmin'], params['rmax']) / 100
            if params['mode'] == 'rect':
                rect(d, x*dx, y*dy, int(dx/2*coef), int(dy/2*coef), fill=cin, outline=None)
            if params['mode'] == 'circle':
                circle(d, x*dx, y*dy, int(dy/2*coef), fill=cin, outline=None)
            if params['mode'] == 'poly':
                po = []
                r = int(dy/2*coef)
                #nn = 12 # par
                nn = 64 # par
                #nn = params['nn']
                for i in range(nn):
                    #rfx = random.randint(-10, 10) # par
                    #rfy = random.randint(-10, 10) # par
                    rfx = random.randint(-40, 40) # par
                    rfy = random.randint(-40, 40) # par
                    a = c*i/nn*360
                    x1 = int(x*dx+(r+rfx)*math.cos(a))
                    y1 = int(y*dy+(r+rfy)*math.sin(a))
                    po.append((x1, y1))
                d.polygon(po, fill=cin, outline=None)
            if params['mode'] == 'mix-rc':
                if random.randint(0, 100) > 50:
                    rect(d, x*dx, y*dy, int(dx/2*coef), int(dy/2*coef), fill=cin, outline=None)
                else:
                    circle(d, x*dx, y*dy, int(dy/2*coef), fill=cin, outline=None)
            if params['mode'] == 'mix-rcp':
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
    img.save(outfile)

    
# --- go

start_time = dt.now()
root = '!output-repixel'
if not os.path.exists(root):
    os.makedirs(root)
odir = root+'\\'
indir = 'repixel-in\\'

#w, h = get_canvas('A3')
#w, h = get_canvas('A2')
w, h = get_canvas('A1')

params = {'w': w, 'h': h, 'infile': '', 'outfile': '', 'bk': (255, 255, 255), 'coef': 0.8, 'scale': 0.5, 'rnd': True, 'mode': 'poly', 'rmin': 50, 'rmax': 250}
# note: high rmax may be cool, eg 500

params['infile'] = indir+'grow22c1v3-1.png'
params['outfile'] = odir+'repixel03-x.png'
repix(params)
params['infile'] = indir+'fromopenshot1zzz2-x.png'
params['outfile'] = odir+'repixel04-x.png'
repix(params)
params['infile'] = indir+'PIC_2548-cp-min.JPG'
params['outfile'] = odir+'repixel05-x.png'
repix(params)
params['infile'] = indir+'grych2.png'
params['outfile'] = odir+'repixel08-x.png'
repix(params)
params['infile'] = indir+'grych3.png'
params['outfile'] = odir+'repixel09-x.png'
repix(params)

params = {'w': w, 'h': h, 'infile': indir+'Zuza-orig.jpg', 'outfile': odir+'repixel10-x-Zuza1.png', 'bk': (255, 255, 255), 'coef': 0.95, 'scale': 0.05, 'rnd': True, 'mode': 'poly', 'rmin': 90, 'rmax': 140}
repix(params)
# seems best:
params = {'w': w, 'h': h, 'infile': indir+'Zuza-popr1.jpg', 'outfile': odir+'repixel10-x-Zuza2.png', 'bk': (255, 255, 255), 'coef': 0.95, 'scale': 0.05, 'rnd': True, 'mode': 'poly', 'rmin': 90, 'rmax': 140}
repix(params)
params = {'w': w, 'h': h, 'infile': indir+'Zuza-popr2.jpg', 'outfile': odir+'repixel10-x-Zuza3.png', 'bk': (255, 255, 255), 'coef': 0.95, 'scale': 0.05, 'rnd': True, 'mode': 'poly', 'rmin': 90, 'rmax': 140}
repix(params)

params = {'w': w, 'h': h, 'infile': '', 'outfile': '', 'bk': (0, 0, 0), 'coef': 0.9, 'scale': 0.1, 'rnd': True, 'mode': 'rect', 'rmin': 5, 'rmax': 110}

params['infile'] = indir+'enter.png'
params['outfile'] = odir+'repixel10-x-enter.png'
repix(params)

params['infile'] = indir+'rgbxxx-1024-test.png'
params['outfile'] = odir+'repixel11-rgbxxx-1024-test.png'
repix(params)

time_elapsed = dt.now() - start_time
print('ALL done. elapsed time: {}'.format(time_elapsed))

