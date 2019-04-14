#! /usr/bin/env python
# -*- coding: utf-8 -*-

# paint algorithms (artificial artist) in Python - demo
# (c)2018-2019 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz
# cre: 20181020
# upd: 20190105, 06, 13, 18, 19, 22
# upd: 20190302, 03, 30
# upd: 20190414

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

def do_mazy(cnt, w, h, odir, name):
    if name == 'mazy01':
        p = predef_mazy1(w, h)
    if name == 'mazy02':
        p = predef_mazy2(w, h)
    if name == 'mazy03':
        p = predef_mazy3(w, h)
    if name == 'mazy04':
        p = predef_mazy4(w, h)
    if name == 'mazy05':
        p = predef_mazy5(w, h)
    if name == 'mazy06':
        p = predef_mazy6(w, h)
    if name == 'mazy07':
        p = predef_mazy7(w, h)
    if name == 'mazy08':
        p = predef_mazy8(w, h)
    if name == 'mazy09':
        p = predef_mazy9(w, h)
    if name == 'mazy10':
        p = predef_mazy10(w, h)
    if name == 'mazy11':
        p = predef_mazy11(w, h)
    if name == 'mazy12':
        p = predef_mazy12(w, h)
    if name == 'mazy13':
        p = predef_mazy13(w, h)
    if name == 'mazy14':
        p = predef_mazy14(w, h)
    if name == 'mazy15':
        p = predef_mazy15(w, h)
    if name == 'mazy16':
        p = predef_mazy16(w, h)

    for n in range(cnt):
        tx = dt.now().strftime('%Y%m%d%H%M%S')
        for i in range(len(p)):
            art_painter(p[i], odir+'%s-%dx%d-%02d-%03d-%s.png' % (name, w, h, i+1, n+1, tx))

# --- go

#w, h = get_canvas('A0')
#w, h = get_canvas('A1') # for self use this
#w, h = get_canvas('A2')
w, h = get_canvas('A3') # for demo use this, not too big, not too small
#w, h = get_canvas('A4')
#w, h = get_canvas('A5')
#w, h = get_canvas('A6')

cnt = 3 # note: it takes some time
do_mazy(cnt, w, h, odir, 'mazy01')
do_mazy(cnt, w, h, odir, 'mazy02')
do_mazy(cnt, w, h, odir, 'mazy03')
do_mazy(cnt, w, h, odir, 'mazy04') # also a bit lame, only red ok, add blue
do_mazy(cnt, w, h, odir, 'mazy05')
do_mazy(cnt, w, h, odir, 'mazy06')
do_mazy(cnt, w, h, odir, 'mazy07')
do_mazy(cnt, w, h, odir, 'mazy08')
do_mazy(cnt, w, h, odir, 'mazy09')
do_mazy(cnt, w, h, odir, 'mazy10')
do_mazy(cnt, w, h, odir, 'mazy11')
do_mazy(cnt, w, h, odir, 'mazy12')
do_mazy(cnt, w, h, odir, 'mazy13')
do_mazy(cnt, w, h, odir, 'mazy14')
do_mazy(cnt, w, h, odir, 'mazy15')
do_mazy(cnt, w, h, odir, 'mazy16')

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

