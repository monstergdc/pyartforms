#! /usr/bin/env python
# -*- coding: utf-8 -*-

# paint algorithms (artificial artist) in Python - demo
# (c)2018-2021 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz
# cre: 20181020
# upd: 20190105, 06, 13, 18, 19, 22
# upd: 20190302, 03, 30
# upd: 20190414, 17, 18, 21, 22, 26
# upd: 20210612, 13

# TODO:
# - nice argparse (also per module?)
# - anims: anims | grow (also img) | zxoids-anim (also img maybe?)
# - asciiart | city-lame | faces (fin) | brush
# - Fibbonaci x PI - ksztalt size z fibb. kolor z pi | spirals
# - more


# NOTE: output can be png, gif, jpg - dep. on file ext

import os
from datetime import datetime as dt
from drawtools import *
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

for m in predef_names:
    if m in ['mazy15', 'mazy16', 'astro', 'lissajous', 'life', 'mandelbrot']
        cnt = 1 # note: only once
    else:
        cnt = 3 # note: it takes some time
    if m in ['life', 'mandelbrot']:
        w, h = get_canvas('800')
    do_mazy(cnt, w, h, odir, m)

time_elapsed = dt.now() - start_time
print('ALL done. elapsed time: {}'.format(time_elapsed))

