#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 20190330

# repixelize

# IDEA
#- src pixels as big filled circles
# == Image.getpixel(xy)


import random, math, string, os, sys
from PIL import Image, ImageDraw, ImageFont, ImageOps
from drawtools import *
from color_defs import *

# TODO:
# - xy scale sync issue
# - rnd dots not always circle
# - rnd dot size
# - pixel groupping

def repix(params):
    w = params['w']
    h = params['h']
    src = params['src']
    src = src.resize((src.width/2, src.height/2), resample=PIL.Image.BICUBIC, box=None) # opt
    img = params['img']
    #coef = params['coef'] # dot radius coefficient %
    srcw = src.width
    srch = src.height
    random.seed()
    d = ImageDraw.Draw(img)
    dx = int(w/srcw)
    dy = int(h/srch)
    for x in range(srcw):
        for y in range(srch):
            xy = (x, y)
            c = src.getpixel(xy)
            coef = random.randint(30, 130) / 100 # test
            circle(d, x*dx, y*dy, int(dy/2*coef), fill=c, outline=None)

def do_repix(infile, outfile):
    #w, h = get_canvas('A4')
    w, h = get_canvas('A3')
    #w, h = get_canvas('A2')
    #w, h = get_canvas('A1')
    src = Image.open(infile)
    img = Image.new('RGB', (w, h), color = (255, 255, 255))
    #params = {'w': w, 'h': h, 'src': src, 'img': img, 'coef': 0.85}
    params = {'w': w, 'h': h, 'src': src, 'img': img, 'coef': 0.5}
    repix(params)
    img.save(outfile)
    
# --- go

do_repix('repixel-in\\00base1x-gdc.png', 'repixel01-x.png')
do_repix('repixel-in\\gdc-zx-20181109-3a-x1-x.png', 'repixel02-x.png')
do_repix('repixel-in\\grow22c1v3-1.png', 'repixel03-x.png')
do_repix('repixel-in\\fromopenshot1zzz2-x.png', 'repixel04-x.png')
do_repix('repixel-in\\PIC_2548-cp-min.JPG', 'repixel05-x.png')
do_repix('repixel-in\\test1.png', 'repixel06-x.png')
