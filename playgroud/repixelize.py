#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Repixelize algorithm (artificial artist), v1.0, Python version
# IDEA: src pixels as big filled circles/boxes/rnd-shapes, possible rnd size variation, src img rescale
# (c)2018-2019 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz
# cre: 20190330
# upd: 20190401, 02, 03, 15, 22, 23

# note: input must be 24-bit RGB

# TODO: xy scale sync issue | proper params | ext call


import random, math, string, os, sys
from PIL import Image, ImageDraw, ImageFont, ImageOps
from drawtools import *
from color_defs import *


def repix(params):
    # todo: exp more par
    # todo: rect-like poly with sharp edge - rectpoly_ ?
    def rect_():
        rect(d, int(x*dx), int(y*dy), int(dx*coef), int(dy*coef), fill=cin, outline=None)
    def circle_():
        circle(d, int(x*dx), int(y*dy), int(dy/2*coef), fill=cin, outline=None)
    def poly_():
        po = []
        r = int(dy/2*coef)
        #nn = 12 # par [mix rcp]
        nn = 64 # par
        for i in range(nn):
            #rfx = random.randint(-10, 10) # par [mix rcp]
            #rfy = random.randint(-10, 10) # par [mix rcp]
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
        for b in range(25+random.randint(0, 55)): # par
            bs = random.randint(1, 6) # par2
            addx1 = 0
            addy1 = 0
            addx2 = 0
            addy2 = 0
            ex = 4 # par
            if random.randint(0, 100) >= 80:
                addx1 = -dx * random.randint(1, ex)
            if random.randint(0, 100) >= 80:
                addx2 = dx * random.randint(1, ex)
            horizontal = False
            if 'horizontal' in params:
                if params['horizontal'] == True:
                    horizontal = True
            if not horizontal:
                if random.randint(0, 100) > 80:
                    addy1 = -dy * random.randint(1, ex)
                if random.randint(0, 100) >= 80:
                    addy2 = dy * random.randint(1, ex)
            points = [x*dx+addx1+random.randint(0+1, int(dx)-1), y*dy+addy1+random.randint(0+1, int(dy)-1), x*dx+addx2+random.randint(0+1, int(dx)-1), y*dy+addy2+random.randint(0+1, int(dy)-1)]
            d.line(points, fill=cin, width=bs)

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
    if 'nn' in params:
        nn = params['nn']
    else:
        nn = 0
    img = Image.new('RGB', (w, h), color = bk)
    coef = params['coef'] # dot radius coefficient %
    srcw = src.width
    srch = src.height
    random.seed()
    print('repix', params['mode'], params['infile'], outfile)
    d = ImageDraw.Draw(img)
    dx = w/srcw
    dy = h/srch
    for x in range(srcw):
        for y in range(srch):
            xy = (x, y)
            cin = src.getpixel(xy)
            if 'rnd' in params:
                if params['rnd'] == True:
                    coef = float(random.randint(params['rmin'], params['rmax'])) / 100.0
            mix_sel_1 = random.randint(0, 100) > 50
            mix_sel_2 = random.randint(0, 100) > 50
            if params['mode'] == 'rect' or params['mode'] == 'mix-rc' and mix_sel_1 or params['mode'] == 'mix-rcp' and mix_sel_1:
                rect_()
            if params['mode'] == 'circle' or params['mode'] == 'mix-rc' and not mix_sel_1 or params['mode'] == 'mix-rcp' and not mix_sel_1 and mix_sel_2:
                circle_()
            if params['mode'] == 'poly' or params['mode'] == 'mix-rcp' and not mix_sel_1 and not mix_sel_2:
                poly_()
            if params['mode'] == 'brush':
                brush_()
            if params['mode'] == 'lines':
                lines_()
    img.save(outfile)

    
# --- go

start_time = dt.now()
root = '!output-repixel'
if not os.path.exists(root):
    os.makedirs(root)
odir = root+'\\'
indir = 'repixel-in\\'

w, h = get_canvas('A2') # test
#w, h = get_canvas('A1') # final


params = {'w': w, 'h': h, 'bk': (0, 0, 0), 'coef': 0.9, 'scale': 1.0, 'rnd': True, 'rmin': 78, 'rmax': 98}
params['infile'] = indir+'mntr1.png'
#params['infile'] = indir+'head.png'

params['mode'] = 'rect'
params['outfile'] = odir+'repixel-rect.png'
repix(params)
params['mode'] = 'circle'
params['outfile'] = odir+'repixel-circle.png'
repix(params)
params['mode'] = 'brush'
params['outfile'] = odir+'repixel-brush.png'
repix(params)
params['mode'] = 'lines'
params['outfile'] = odir+'repixel-lines.png'
repix(params)
params['mode'] = 'poly'
params['outfile'] = odir+'repixel-poly.png'
repix(params)
params['mode'] = 'mix-rc'
params['outfile'] = odir+'repixel-mixrc.png'
repix(params)
params['mode'] = 'mix-rcp'
params['outfile'] = odir+'repixel-mixrcp.png'
repix(params)

quit()

params = {'w': w, 'h': h, 'bk': (255, 255, 255), 'coef': 0.8, 'scale': 0.5, 'rnd': True, 'mode': 'poly', 'rmin': 50, 'rmax': 250}
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

params = {'w': w, 'h': h, 'bk': (0, 0, 0), 'coef': 0.9, 'scale': 0.1, 'rnd': True, 'mode': 'rect', 'rmin': 15, 'rmax': 180}

params['infile'] = indir+'enter.png'
params['outfile'] = odir+'repixel10-x-enter.png'
repix(params)

params['infile'] = indir+'rgbxxx-1024-test.png'
params['outfile'] = odir+'repixel11-rgbxxx-1024-test.png'
repix(params)

time_elapsed = dt.now() - start_time
print('ALL done. elapsed time: {}'.format(time_elapsed))

