#! /usr/bin/env python
# -*- coding: utf-8 -*-

# paint algorithms (artificial artist) in Python - demo
# (c)2018-2019 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz
# cre: 20181020
# upd: 20190105, 06, 13, 18, 19, 22
# upd: 20190302, 03, 30
# upd: 20190414, 17, 18, 21

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


def do_mazy(cnt, w, h, odir, name):
    if name in predefs:
        pr = predefs[name]
        p = pr(w, h)
    #else: ?

    for n in range(cnt):
        tx = dt.now().strftime('%Y%m%d%H%M%S')
        for i in range(len(p)):
            p[i]['alpha'] = True #test
            art_painter(p[i], odir+'%s-%dx%d-%02d-%03d-%s.png' % (name, w, h, i+1, n+1, tx))

# --- go

#w, h = get_canvas('A0')
#w, h = get_canvas('A1') # for self use this
#w, h = get_canvas('A2')
w, h = get_canvas('A3') # for demo use this, not too big, not too small
#w, h = get_canvas('A4')
#w, h = get_canvas('A5')
#w, h = get_canvas('A6')
#w, h = get_canvas('A7')

cnt = 3 # note: it takes some time
do_mazy(cnt, w, h, odir, 'mazy01')
do_mazy(cnt, w, h, odir, 'mazy02')
do_mazy(cnt, w, h, odir, 'mazy03')
do_mazy(cnt, w, h, odir, 'mazy04') # a bit lame, only red ok, add blue
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
cnt = 1 # note: 15 and 16 alredy produce a lot
do_mazy(cnt, w, h, odir, 'mazy15')
do_mazy(cnt, w, h, odir, 'mazy16')
cnt = 1 # note: astro only once
do_mazy(cnt, w, h, odir, 'astro')
cnt = 3
do_mazy(cnt, w, h, odir, 'waves') # fix: does not scale down well
cnt = 1
w, h = get_canvas('800')
do_mazy(cnt, w, h, odir, 'life')
cnt = 1
w, h = get_canvas('A4') # fix: does not scale down well (line width)
do_mazy(cnt, w, h, odir, 'lissajous')
do_mazy(cnt, 700, 400, odir, 'mandelbrot')
    
time_elapsed = dt.now() - start_time
print('ALL done. elapsed time: {}'.format(time_elapsed))

