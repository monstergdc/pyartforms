#! /usr/bin/env python
# -*- coding: utf-8 -*-

# paint algorithms (artificial artist) in Python - demo
# (c)2018-2019 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz
# cre: 20181020
# upd: 20190105, 12, 13, 18, 19
# upd: 20190311, 30
# upd: 20190414, 21

# TODO:
# - nice argparse (also per module?)
# - anims: anims | grow (also img) | zxoids-anim (also img maybe?)
# - smears5post
# - asciiart | city-lame | faces (fin) | brush


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
#import tracemalloc


#tracemalloc.start()
start_time = dt.now()
root = '!output-test'
if not os.path.exists(root):
    os.makedirs(root)
odir = root+'\\'


def do_mazy(cnt, w, h, odir, name):
    if name in predefs:
        pr = predefs[name]
        p = pr(w, h)
    #else: ?

#    snapshot1 = tracemalloc.take_snapshot()
    for n in range(cnt):
        tx = dt.now().strftime('%Y%m%d%H%M%S')
        for i in range(len(p)):
            p[i]['alpha'] = True #test
            art_painter(p[i], odir+'%s-%dx%d-%02d-%03d-%s.png' % (p[i]['name'], w, h, i+1, n+1, tx))
#    snapshot2 = tracemalloc.take_snapshot()
#    top_stats = snapshot2.compare_to(snapshot1, 'lineno')
#    print("[ Top 5 differences (in1) ]")
#    for stat in top_stats[:5]:
#        print(stat)
#    print("[ Top 5 lineno (in1) ]")
#    top_stats = snapshot2.statistics('lineno')
#    for stat in top_stats[:5]:
#        print(stat)
#    print("[ Top 5 traceback (in1) ]")
#    top_stats = snapshot2.statistics('traceback')
#    for stat in top_stats[:5]:
#        print(stat)

# --- 

#w, h = get_canvas('A0')
#w, h = get_canvas('A1') # fin - ten
#w, h = get_canvas('A2')
#w, h = get_canvas('A3')
#w, h = get_canvas('A4') # test - ten
#w, h = get_canvas('A5')
w, h = get_canvas('A6') # small - ten
#w, h = get_canvas('A7')
#w, h = get_canvas('1024')

cnt = 1
#cnt = 2
#cnt = 3
#cnt = 4

enum_defs()
    
#do_mazy(cnt, w, h, odir, 'mazy01')
#do_mazy(cnt, w, h, odir, 'mazy02')
#do_mazy(cnt, w, h, odir, 'mazy03')
#do_mazy(cnt, w, h, odir, 'mazy04')
#do_mazy(cnt, w, h, odir, 'mazy05')
#do_mazy(cnt, w, h, odir, 'mazy06')
#do_mazy(cnt, w, h, odir, 'mazy07')
#do_mazy(cnt, w, h, odir, 'mazy08')
#do_mazy(cnt, w, h, odir, 'mazy09')
#do_mazy(cnt, w, h, odir, 'mazy10')
#do_mazy(cnt, w, h, odir, 'mazy11')
#do_mazy(cnt, w, h, odir, 'mazy12')
#do_mazy(cnt, w, h, odir, 'mazy13')
#do_mazy(cnt, w, h, odir, 'mazy14')
#do_mazy(cnt, w, h, odir, 'mazy15')
#do_mazy(cnt, w, h, odir, 'mazy16')
do_mazy(cnt, w, h, odir, 'waves')
#do_mazy(cnt, w, h, odir, 'astro')
    
time_elapsed = dt.now() - start_time
print('ALL done. elapsed time: {}'.format(time_elapsed))

#snapshot = tracemalloc.take_snapshot()
#top_stats = snapshot.statistics('lineno')
#print("[ Top ALL 20 ]")
#for stat in top_stats[:20]:
#    print(stat)
#top_stats = snapshot.statistics('traceback')
#for stat in top_stats[:20]:
#    print(stat)
