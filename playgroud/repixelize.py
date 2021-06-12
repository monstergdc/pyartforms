#! /usr/bin/env python
# -*- coding: utf-8 -*-

# PyArtForms - Repixelize algorithm (artificial artist), v1.0, Python version
# IDEA: src pixels as big filled circles/boxes/rnd-shapes, possible rnd size variation, src img rescale
# (c)2018-2021 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz
# tested with Python 3.5.2
# cre: 20190330
# upd: 20190401, 02, 03, 15, 22, 23
# upd: 20200724, 25, 30
# upd: 20201208, 10, 11, 12, 13
# upd: 20210507, 08

# note: input must be 24-bit RGB

# TODO: aspect ratio src->dst issue (opt add border to preserve ratio?)


import random, math
from PIL import Image, ImageDraw, ImageFont, ImageOps
from drawtools import *


def repix(params):
    """
    'Repixelize' - remake small image into big one, change each pixel to bigger predefined but variable multipixel form
    """
    def rect_():
        rect(d, int(x*dx), int(y*dy), int(dx*coef), int(dy*coef), fill=cin, outline=None)
    def circle_():
        circle(d, int(x*dx), int(y*dy), int(dy/2*coef), fill=cin, outline=None)
    def poly_():
        po = []
        r = int(dy/2*coef)
        if 'nn' in params:  # 'nn' - count of poly sides, bigger == smoother, default 64
            nn = int(params['nn'])
            if nn < 3:
                nn = 3
        else:
            nn = 64
        if 'flux' in params:  # 'flux' - random poly points variation (absoulte values), 0 == no variation, default 40
            flux = int(params['flux'])
        else:
            flux = 40
        for i in range(nn):
            rfx = random.randint(-flux, flux)
            rfy = random.randint(-flux, flux)
            a = c*i/nn*360
            x1 = int(x*dx+(r+rfx)*math.cos(a))
            y1 = int(y*dy+(r+rfy)*math.sin(a))
            po.append((x1, y1))
        d.polygon(po, fill=cin, outline=None)
    def brush_():
        if 'bs' in params: # 'bs' - brush rect block size variation, default 15
            bs0 = int(params['bs'])
            if bs0 < 0:
                bs0 = 0
        else:
            bs0 = 15
        if 'nn' in params:  # 'nn' - max extra count of rects, default 60
            nn = int(params['nn'])
            if nn < 0:
                nn = 0
        else:
            nn = 60
        for b in range(30+random.randint(0, nn)):
            bs = 2+random.randint(0, bs0)
            if random.randint(0, 100) > 90: # sometimes exceed dest rect
                ofsx = random.randint(int(-dx), int(dx*2))
                ofsy = random.randint(int(-dy), int(dy*2))
            else:
                ofsx = random.randint(0+1, int(dx)-1)
                ofsy = random.randint(0+1, int(dy)-1)
            rect(d, int(x*dx+ofsx), int(y*dy+ofsy), int(bs), int(bs), fill=cin, outline=None) #note: with outline migth be interesting too
    def lines_():
        horizontal = False
        if 'horizontal' in params: # 'horizontal' - opt only horizontal lines
            horizontal = params['horizontal']
        maxlinewidth = 2
        if 'maxlinewidth' in params: # 'maxlinewidth' - max line width, default 2
            maxlinewidth = int(params['maxlinewidth'])
        treshold = 80
        if 'treshold' in params: # 'treshold' - probability treshold for line rnd extension beyond current 'pixel' area, default 80
            treshold = int(params['treshold'])
        nn = 4
        if 'nn' in params:  # 'nn' - line iteration count per 'pixel' (big slows down), default 4
            nn = int(params['nn'])
        ex = 4
        for b in range(nn):
            addx1 = 0
            addy1 = 0
            addx2 = 0
            addy2 = 0
            if random.randint(0, 100) >= treshold:
                addx1 = -dx * random.randint(1, ex)
            if random.randint(0, 100) >= treshold:
                addx2 = dx * random.randint(1, ex)
            if not horizontal:
                if random.randint(0, 100) >= treshold:
                    addy1 = -dy * random.randint(1, ex)
                if random.randint(0, 100) >= treshold:
                    addy2 = dy * random.randint(1, ex)
            points = [x*dx+addx1+random.randint(0+1, int(dx)-1), y*dy+addy1+random.randint(0+1, int(dy)-1),
                      x*dx+addx2+random.randint(0+1, int(dx)-1), y*dy+addy2+random.randint(0+1, int(dy)-1)]
            bs = random.randint(1, maxlinewidth)
            d.line(points, fill=cin, width=bs)
    def image_():
        if cin[0] <= 2 and cin[1] <= 2 and cin[2] <= 2: # bk, with some margin
            return
        rgb = int((cin[0] + cin[1] + cin[2]) / 3) / (256/(bxn*byn)) # by lightness?
        xb = int(rgb % bxn)
        yb = int(rgb / byn)
        if xb >= bxn or yb >= byn:
            print('WTF?', xb, yb, bxn, byn, 'rgb', rgb)
        # https://stackoverflow.com/questions/43111029/how-to-find-the-average-colour-of-an-image-in-python-with-opencv
        position = (int(x*dx), int(y*dy)) # todo: proper! chk
        bimc_rot = bimg[yb][xb].rotate(random.randint(-30, 30)) # todo: rot proper?
        img.paste(bimc_rot, position, bimc_rot)

    if not 'mode' in params:
        print("Mode not given")
        return
    if not 'infile' in params:
        print("Source image (inflie) not given")
        return
    try:
        src = Image.open(params['infile'])
    except:
        print("Error opening source image:", params['infile'])
        return
    if not 'w' in params:
        print("Destination width not given")
        return
    if not 'h' in params:
        print("Destination height not given")
        return
    w = int(params['w'])
    h = int(params['h'])
    if h <= 0:
        print("Destination height must be > 0")
        return
    if w <= 0:
        print("Destination width must be > 0")
        return
    if 'scale' in params:
        scale = params['scale']
        if scale != 1.0:
            src = src.resize((int(src.width*scale), int(src.height*scale)), resample=Image.BICUBIC, box=None)
    if 'bk' in params:
        bk = params['bk']
    else:
        bk = (0,0,0)
    if 'coef' in params: # dot radius coefficient % (1.0 = 100%), default 0.9
        coef = params['coef']
    else:
        coef = 0.9
    outfile = ''
    if 'outfile' in params:
        outfile = params['outfile']
    img = Image.new('RGB', (w, h), color = bk)
    srcw = src.width
    srch = src.height
    c = math.pi/180
    random.seed()
    print('repix', params['mode'], params['infile'], '->', outfile, '- resize:', (srcw, srch), '->', (w, h))
    d = ImageDraw.Draw(img)
    dx = w/srcw
    dy = h/srch # todo: opt fix for aspect ratio here?

    if params['mode'] == 'image':
        imc = Image.open(params['brush'])
        bxn = params['bxn']
        byn = params['byn']
        bw = int(imc.size[0] / bxn)
        bh = int(imc.size[1] / byn)
        cut2 = 12 #frame cut - or more in test case - remove blank brush margin
        scale_coeff = 1.5 # slightly bigger
        print('imc.size:', imc.size, 'b:xcnt/ycnt:', bxn, byn, 'b:width/height:', bw, bh)
        bimg = [[None for x in range(bxn)] for y in range(byn)]
        for x in range(bxn):
            for y in range(byn):
                x0 = x * bw
                y0 = y * bh
                box = (x0+cut2, y0+cut2, x0+bw-1-cut2, y0+bh-1-cut2)
                bimg[y][x] = imc.crop(box)
                scalex = dx/bimg[y][x].width*scale_coeff
                scaley = dy/bimg[y][x].height*scale_coeff
                bimg[y][x] = bimg[y][x].resize((int(bimg[y][x].width*scalex), int(bimg[y][x].height*scaley)), resample=Image.BICUBIC, box=None)

    for x in range(srcw):
        #print(x, srcw)
        for y in range(srch):
            cin = src.getpixel((x, y))
            if 'rnd' in params: # random coef variation in range rmin..rmax
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
            if params['mode'] == 'image':
                image_()

    if outfile != '':
        img.save(outfile)
    return img

# EOF
