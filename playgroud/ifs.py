#! /usr/bin/env python
# -*- coding: utf-8 -*-

# paint algorithms (artificial artist) - IFS, v1.0, Python version
# based on my old Pascal/Delphi code from 1996-1999 and 2006
# (c)2019-2021 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz
# cre: 20190428
# upd: 20210612

# TODO:
# - ?

from PIL import Image, ImageDraw
import random, math, os, sys
from datetime import datetime as dt
from drawtools import *
from color_defs import *


def ifs(params, fn):
    def ret(xy, t):
        return [t['a']*xy[0] + t['b']*xy[1] + t['e'], t['c']*xy[0] + t['d']*xy[1] + t['f']]

    def ptest(p, data1, data2):
        return (p > data1) and (p <= data2)

    start_time = dt.now()
    random.seed()
    w = params['w']
    h = params['h']
    cnt = params['n']
    tran = params['tran']
    xy = (random.randint(0, 99), random.randint(0, 99))
    im = Image.new('RGB', (w, h), params['Background'])
    draw = ImageDraw.Draw(im)
    sc = params['sc']
    y0 = params['y0']
    x0 = w/2

    for iter1 in range(cnt):
        p = random.random()
        pp = 0
        sel = len(tran)
        for i in range(sel):
            if ptest(p, pp, pp+tran[i]['p']):
                sel = i
            pp = pp + tran[i]['p']
        xy = ret(xy, tran[sel])
        x = int(x0+sc*xy[0])
        y = int(y0+sc*xy[1])
        if iter1%250000 == 0:
            print(iter1, '/', cnt, int(iter1/cnt*100), '%')
        # if ?
        color = (0,0,0)
        #color = colors_happy[1+sel%7] # tmp avoid white
        draw.point((x, y), fill=color)

    im.save(fn)
    show_benchmark(start_time)

# ---

start_time = dt.now()
#w, h = get_canvas('1024')
w, h = get_canvas('A6')
odir = '!output-test\\'

# classic fern
t1 = {'a':  0.85, 'b':  0.04, 'c': -0.04, 'd': 0.85, 'e': 0, 'f': 1.6,  'p': 0.85}
t2 = {'a': -0.15, 'b':  0.28, 'c':  0.26, 'd': 0.24, 'e': 0, 'f': 0.44, 'p': 0.07}
t3 = {'a':  0.2,  'b': -0.26, 'c':  0.23, 'd': 0.22, 'e': 0, 'f': 1.6,  'p': 0.07}
t4 = {'a':  0.0,  'b':  0.0,  'c':  0.0,  'd': 0.16, 'e': 0, 'f': 0.0,  'p': 0.01}
tran_fern = [t1, t2, t3, t4]

# Sierpinski?
t1 = {'a':  0.5, 'b': 0.0, 'c': 0.0, 'd': 0.5, 'e': 150, 'f': 0.0, 'p': 0.33}
t2 = {'a':  0.5, 'b': 0.0, 'c': 0.0, 'd': 0.5, 'e':   0, 'f': 0.0, 'p': 0.33}
t3 = {'a':  0.5, 'b': 0.0, 'c': 0.0, 'd': 0.5, 'e':  75, 'f': 150, 'p': 0.34}
tran_sier = [t1, t2, t3]

# http://paulbourke.net/fractals/ifs/

# some leaf
t1 = {'a': 0.14, 'b':  0.01, 'c':  0.00, 'd': 0.51, 'e': -0.08, 'f': -1.31, 'p': 0.25}
t2 = {'a': 0.43, 'b':  0.52, 'c': -0.45, 'd': 0.50, 'e':  1.49, 'f': -0.75, 'p': 0.25}
t3 = {'a': 0.45, 'b': -0.49, 'c':  0.47, 'd': 0.47, 'e': -1.62, 'f': -0.74, 'p': 0.25}
t4 = {'a': 0.49, 'b':  0.00, 'c':  0.00, 'd': 0.51, 'e':  0.02, 'f':  1.62, 'p': 0.25}
tran_leaf = [t1, t2, t3, t4]

# tree ?
t1 = {'a':  0.05, 'b':  0.00, 'c':  0.00, 'd':  0.40, 'e': -0.06, 'f': -0.47, 'p': 1/7}
t2 = {'a': -0.05, 'b':  0.00, 'c':  0.00, 'd': -0.40, 'e': -0.06, 'f': -0.47, 'p': 1/7}
t3 = {'a':  0.03, 'b': -0.14, 'c':  0.00, 'd':  0.26, 'e': -0.16, 'f': -0.01, 'p': 1/7}
t4 = {'a': -0.03, 'b':  0.14, 'c':  0.00, 'd': -0.26, 'e': -0.16, 'f': -0.01, 'p': 1/7}
t5 = {'a':  0.56, 'b':  0.44, 'c': -0.37, 'd':  0.51, 'e':  0.30, 'f':  0.15, 'p': 1/7}
t6 = {'a':  0.19, 'b':  0.07, 'c': -0.10, 'd':  0.15, 'e': -0.20, 'f':  0.28, 'p': 1/7}
t7 = {'a': -0.33, 'b': -0.34, 'c': -0.33, 'd':  0.34, 'e': -0.54, 'f':  0.39, 'p': 1/7}
tran_tree = [t1, t2, t3, t4, t5, t6, t7]

# for 1024
n = 150000*30
y0 = h/2-300
sc = 70.0

# ?
n = 150000*30
y0 = h/2-100
sc = 70.0*3

# A5 need a lot of iterations for big image
#n = 150000*200
#y0 = h/2-2000
#sc = 70.0*5

params1 = {'w': w, 'h': h, 'Background': (255, 255, 255), 'n': n, 'y0': y0, 'sc': sc, 'tran': tran_fern}
params2 = {'w': w, 'h': h, 'Background': (255, 255, 255), 'n': n, 'y0': y0, 'sc': sc, 'tran': tran_leaf}
params3 = {'w': w, 'h': h, 'Background': (255, 255, 255), 'n': n, 'y0': y0, 'sc': sc, 'tran': tran_tree}

ifs(params1, odir+'ifs-%dx%d-01-001.png' % (w, h))
ifs(params2, odir+'ifs-%dx%d-02-001.png' % (w, h))
ifs(params3, odir+'ifs-%dx%d-03-001.png' % (w, h))

time_elapsed = dt.now() - start_time
print('ALL done. elapsed time: {}'.format(time_elapsed))

