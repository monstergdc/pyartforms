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

if what == "smears1":
    w, h = get_canvas('A3')

    params1 = {
        'name': 'SMEARS#1', 'call': mazy1, 'w': w, 'h': h, 'Background': (255, 255, 255),
        'pw': 5+3,
        'v': 50-0-20-10,
        'n': 20*5,
        'm': 100-50-10,
        'prefill': True,
        'blur': True,
        'r0': 64,
        'g0': 64,
        'b0': 64,
        'r1': 256,
        'g1': 256,
        'b1': 256,
        'mode': 'black',
        'keep': False,
    }

    params2 = {
        'name': 'SMEARS#1', 'call': mazy1, 'w': w, 'h': h, 'Background': (255, 255, 255),
        'pw': 5+3,
        'v': 50+25,
        'n': 20*5,
        'm': 100-50-10,
        'prefill': False,
        'blur': True,
        'r0': 0,
        'g0': 0,
        'b0': 0,
        'r1': 256,
        'g1': 0,
        'b1': 0,
        'mode': 'red',
        'keep': False,
    }

    params3 = {
        'name': 'SMEARS#1', 'call': mazy1, 'w': w, 'h': h, 'Background': (255, 255, 255),
        'pw': 5+3,
        'v': 50-0-20,
        'n': 20*5,
        'm': 100-50-10,
        'prefill': True,
        'blur': False,
        'r0': 64,
        'g0': 64,
        'b0': 0,
        'r1': 256,
        'g1': 256,
        'b1': 32,
        'mode': 'red',
        'keep': False,
    }

    params4 = {
        'name': 'SMEARS#1', 'call': mazy1, 'w': w, 'h': h, 'Background': (255, 255, 255),
        'pw': 5+3,
        'v': 50-0-20,
        'n': 20*5,
        'm': 100-50-10,
        'prefill': True,
        'blur': False,
        'r0': 0,
        'g0': 64,
        'b0': 0,
        'r1': 32,
        'g1': 256,
        'b1': 32,
        'mode': 'red',
        'keep': False,
    }

    params5 = {
        'name': 'SMEARS#1', 'call': mazy1, 'w': w, 'h': h, 'Background': (255, 255, 0),
        'pw': 5,
        'v': 200,
        'n': 50,
        'm': 25,
        'prefill': False,
        'blur': False,
        'r0': 0,
        'g0': 0,
        'b0': 0,
        'r1': 256,
        'g1': 256,
        'b1': 256,
        'mode': 'red',
        'keep': True,
    }

    params6 = {
        'name': 'SMEARS#1', 'call': mazy1, 'w': w, 'h': h, 'Background': (255, 255, 0),
        'pw': 5,
        'v': 120,
        'n': 48,
        'm': 12,
        'prefill': True,
        'blur': False,
        'r0': 16,
        'g0': 64,
        'b0': 128,
        'r1': 128,
        'g1': 256,
        'b1': 256,
        'mode': 'red',
        'keep': True,
    }

    p0 = get_cgi_par(default=None)
    params = params1
    if p0['n'] == 1:
        params = params1
    if p0['n'] == 2:
        params = params2
    if p0['n'] == 3:
        params = params3
    if p0['n'] == 4:
        params = params4
    if p0['n'] == 5:
        params = params5
    if p0['n'] == 6:
        params = params6
    art_painter(params, '', output_mode='cgi')

if what == "smears4":
    w, h = get_canvas('A3')
    p0 = get_cgi_par(default=None)
    params2 = {
        'name': 'SMEARS#4', 'call': mazy4, 'w': w, 'h': h, 'Background': (255, 255, 0),
        'n': 5,
        'r0': 0, 'g0': 0, 'b0': 0,
        'r1': 256, 'g1': 0, 'b1': 0,
        'mode': 'center',
    }
    params4 = {
        'name': 'SMEARS#4', 'call': mazy4, 'w': w, 'h': h, 'Background': (255, 255, 0),
        'n': 5,
        'r0': 0, 'g0': 48, 'b0': 0,
        'r1': 2, 'g1': 256, 'b1': 48,
        'mode': 'center',
    }
    params5 = {
        'name': 'SMEARS#4', 'call': mazy4, 'w': w, 'h': h, 'Background': (255, 255, 0),
        'n': 4,
        'r0': 32, 'g0': 64, 'b0': 64,
        'r1': 64, 'g1': 256, 'b1': 256,
        'mode': 'center',
    }
    params6 = {
        'name': 'SMEARS#4', 'call': mazy4, 'w': w, 'h': h, 'Background': (0, 0, 0),
        'n': 5,
        'r0': 32, 'g0': 0, 'b0': 0,
        'r1': 256, 'g1': 0, 'b1': 0,
        'mode': '',
    }
    params = params2
    if p0['n'] == 1:
        params = params4
    if p0['n'] == 2:
        params = params5
    if p0['n'] == 3:
        params = params6
    art_painter(params, '', output_mode='cgi')

if what == "smears5":
    w, h = get_canvas('A3')
    #params = {'name': 'SMEARS#5', 'call': mazy5, 'w': w, 'h': h, 'Background': (0, 0, 0), 'colors': colors_b, 'outline': None}
    #params = {'name': 'SMEARS#5', 'call': mazy5, 'w': w, 'h': h, 'Background': (0, 0, 0), 'colors': colors_y, 'outline': None}
    params = {'name': 'SMEARS#5', 'call': mazy5, 'w': w, 'h': h, 'Background': (0, 0, 0), 'colors': colors_p, 'outline': (0, 0, 0)}
    #params = {'name': 'SMEARS#5', 'call': mazy5, 'w': w, 'h': h, 'Background': (0, 0, 0), 'colors': colors_bw, 'outline': None}
    art_painter(params, '', output_mode='cgi')

#if what == "?":
    # ?
