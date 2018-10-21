#! /usr/bin/env python
# -*- coding: utf-8 -*-

# paint algorithms (artificial artist) in Python - demo
# (c)2018 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz
# https://pillow.readthedocs.io/en/3.1.x/reference/ImageDraw.html
# cre: 20181019
# upd; 20181020, 21

# TODO:
# - ?

import cgi
from drawtools import get_canvas, art_painter, get_cgi_par
from life1 import life
from lissajous import lissajous, lissajous_loop
from waves import *
from astroart import *
from mandelbrot import generate_mandelbrot
from smears import *


form = cgi.FieldStorage()
if "what" in form:
    what = form["what"].value
else:
    what = ""



w, h = get_canvas('640')

if what == "life":
    params1 = {'name': 'LIFE', 'call': life, 'w': w, 'h': h, 'Background': (0, 0, 0), 'Color': (255,255,255), 'f': 'f2a'}
    params1 = get_cgi_par(default=params1)
    art_painter(params1, '', output_mode='cgi')

if what == "lissajous":
    params2 = {'name': 'LISSAJOUS', 'call': lissajous_loop, 'w': w, 'h': h, 'Background': (0, 0, 0), 'LineColor': (50,255,50), 'LineWidth': 4, 'FF1': 3.0, 'FF2': 4.0, 'FFi': 0, 'dT': 1, 'Steps': 2000, 'Scale': 0.9}
    params2 = get_cgi_par(default=params2)
    art_painter(params2, '', output_mode='cgi')

if what == "waves":
    w, h = get_canvas('A3')
    params1b = {
        'name': 'WAVES#3', 'call': waves3, 'w': w, 'h': h, 'Background': (0, 0, 0),       
        'z': 18,
        'gradient': 64,
        'c1': (255,255,255),
        'c2': (255,255,0),
        'c3': (255,0,0),
    }
    art_painter(params1b, '', output_mode='cgi')

if what == "astro":
    w, h = get_canvas('A3') # note: does not scalle well with canvas size, so far optimised only for A3
    #w, h = get_canvas('1024')
    params = {'name': 'ASTROART', 'call': paint0, 'w': w, 'h': h, 'Background': (0, 0, 0), 'ou': (0,0,0), 'box_or_cir': False, 'n': 0}
    params = get_cgi_par(default=params)
    if params['n'] < 0 or params['n'] > 7:
        params['n'] = 0
    if params['n'] == 0:
        params['call'] = paint0
    if params['n'] == 1:
        params['call'] = paint1
    if params['n'] == 2:
        params['call'] = paint2
    if params['n'] == 3:
        params['call'] = paint3
    if params['n'] == 4:
        params['call'] = paint4
    if params['n'] == 5:
        params['call'] = paint5
    if params['n'] == 6:
        params['call'] = paint6
    if params['n'] == 7:
        params['call'] = paint7
    art_painter(params, '', output_mode='cgi')

if what == "mandelbrot":
    params1 = {'name': 'MANDELBROT', 'call': generate_mandelbrot, 'x0': -2.5, 'x1': 1.0, 'y0': -1.0, 'y1': 1.0, 'maxiter': 80, 'w': 700, 'h': 400, 'negative': False}
    art_painter(params1, '', output_mode='cgi', bw=True)

#if what == "smears":
    # ?

#if what == "?":
    # ?
