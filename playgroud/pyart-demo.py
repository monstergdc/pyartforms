#! /usr/bin/env python
# -*- coding: utf-8 -*-

# paint algorithms (artificial artist) in Python - demo
# (c)2018-2019 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz
# cre: 20181020
# upd: 20190105, 06, 13, 18, 19

# TODO:
# - nice argparse (also per module?)
# - anims: anims | grow (also img) | zxoids-anim (also img maybe?)
# - smears5post
# - asciiart | city-lame | faces (fin) | brush
# - Fibbonaci x PI - ksztalt size z fibb. kolor z pi | spirals
# - more


# NOTE: output can be png, gif, jpg - dep. on file ext

import os
from datetime import datetime as dt

from drawtools import get_canvas, art_painter
from life1 import life
from lissajous import lissajous, lissajous_loop
from waves import *
from astroart import *
from mandelbrot import generate_mandelbrot
from smears import *
from pyart_defs import *


start_time = dt.now()
root = '!output'
if not os.path.exists(root):
    os.makedirs(root)
odir = root+'\\'

# --- life

def do_life(cnt, w, h, odir):
    p = predef_life(w, h)
    #cnt?
    for i in range(len(p)):
        art_painter(p[i], odir+'life-%dx%d-%03d.png' % (w, h, i+1))

# --- lissajous

def do_lissajous(cnt, w, h, odir):
    p = predef_lissajous(w, h)
    #cnt?
    for i in range(len(p)):
        art_painter(p[i], odir+'lissajous-%dx%d-%03d.png' % (w, h, i+1))
   
# --- waves

def do_waves(cnt, w, h, odir):
    p = predef_waves(w, h)
    for n in range(cnt):
        for i in range(len(p)):
            art_painter(p[i], odir+'waves-%dx%d-%02d-%03d.png' % (w, h, i+1, n))
        
# --- astro

def do_astro(cnt, w, h, odir):
    p = predef_astro(w, h)
    #cnt?
    # 2x (cir, box) bluegalaxy ellipticgalaxy spiralgalaxy neutronstar blackhole supernova nebula star
    for i in range(len(p)):
        art_painter(p[i], odir+'astro-%dx%d-%03d.png' % (w, h, i+1))

# --- mandelbrot

def do_mandelbrot(cnt, w, h, odir):
    p = predef_mandelbrot(w, h)
    #cnt?
    for i in range(len(p)):
        art_painter(p[i], odir+'mandelbrot-%03d.png' % (i+1), bw=True)

# --- smears

def do_mazy3(cnt, w, h, odir):
    p = predef_mazy3(w, h)
    for n in range(cnt):
        ts = dt.now().strftime('%Y%m%d%H%M%S')
        for i in range(len(p)):
            for mode in ['std', 'center', 'xcenter', 'rnd']:
                p[i]['mode'] = mode
                art_painter(p[i], odir+'mazy3-%dx%d-%02d-%03d-%s-%s.png' % (w, h, i+1, n+1, mode, ts))

def do_mazy(cnt, w, h, odir, name):
    if name == 'mazy1':
        p = predef_mazy1(w, h)
    if name == 'mazy2':
        p = predef_mazy2(w, h)
    #if name == 'mazy3':
        #?
    if name == 'mazy4':
        p = predef_mazy4(w, h)
    if name == 'mazy5':
        p = predef_mazy5(w, h)
    if name == 'mazy6':
        p = predef_mazy6(w, h)
    if name == 'mazy7':
        p = predef_mazy7(w, h)
    if name == 'mazy8':
        p = predef_mazy8(w, h)

    for n in range(cnt):
        tx = dt.now().strftime('%Y%m%d%H%M%S')
        for i in range(len(p)):
            art_painter(p[i], odir+'%s-%dx%d-%02d-%03d-%s.png' % (name, w, h, i+1, n+1, tx))

# --- go

#w, h = get_canvas('A1')
#w, h = get_canvas('A2')
w, h = get_canvas('A3')
#w, h = get_canvas('A4')

cnt = 4 # *6 each #1..#3 + *7 for #4 = (4)*6*3+(4)*7 = 100 images, it takes some time, easy over 10 minutes
do_mazy(cnt, w, h, odir, 'mazy1') # fix: does not scale well
do_mazy(cnt, w, h, odir, 'mazy2') # fix: does not scale down well
do_mazy3(cnt, w, h, odir) # lame, need fix
do_mazy(cnt, w, h, odir, 'mazy4') # also a bit lame, only red ok, add blue
cnt=3
do_mazy(cnt, w, h, odir, 'mazy5')
do_mazy(cnt, w, h, odir, 'mazy6')
do_mazy(cnt, w, h, odir, 'mazy7')
do_mazy(cnt, w, h, odir, 'mazy8')
cnt = 3
do_waves(cnt, w, h, odir) # fix: does not scale down well

w, h = get_canvas('800')
do_life(0, w, h, odir)

w, h = get_canvas('A4') # fix: does not scale down well (line width)
do_lissajous(0, w, h, odir)

w, h = get_canvas('A3')
do_astro(0, w, h, odir)

do_mandelbrot(0, 700, 400, odir)
    
time_elapsed = dt.now() - start_time
print('ALL done. elapsed time: {}'.format(time_elapsed))

