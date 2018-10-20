#! /usr/bin/env python
# -*- coding: utf-8 -*-

# paint algorithms (artificial artist) in Python - demo
# (c)2018 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz
# cre: 20181020
# upd: 201810??

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


start_time = dt.now()
root = '!output'
if not os.path.exists(root):
    os.makedirs(root)
odir = root+'\\'

# --- life

w, h = get_canvas('800')

params1 = {'name': 'LIFE', 'call': life, 'w': w, 'h': h, 'Background': (0, 0, 0), 'Color': (255,255,255), 'f': 'f2a'}

params1['f'] = 'f2a'

s = '-%dx%d' % (w, h)

art_painter(params1, odir+'life'+s+'-001.jpg') #diff fmt check
art_painter(params1, odir+'life'+s+'-001.gif') #diff fmt check
art_painter(params1, odir+'life'+s+'-001.png')
art_painter(params1, odir+'life'+s+'-001a.png')
params1['f'] = 'f2b'
art_painter(params1, odir+'life'+s+'-002a.png')
art_painter(params1, odir+'life'+s+'-002b.png')
params1['f'] = 'f2c'
art_painter(params1, odir+'life'+s+'-003a.png')
art_painter(params1, odir+'life'+s+'-003b.png')
params1['f'] = 'f2d'
art_painter(params1, odir+'life'+s+'-004a.png')
art_painter(params1, odir+'life'+s+'-004b.png')
params1['f'] = 'f2e'
art_painter(params1, odir+'life'+s+'-005a.png')
art_painter(params1, odir+'life'+s+'-005b.png')
params1['f'] = 'f2f'
art_painter(params1, odir+'life'+s+'-006a.png')
art_painter(params1, odir+'life'+s+'-006b.png')
params1['f'] = 'f2g'
art_painter(params1, odir+'life'+s+'-007a.png')
art_painter(params1, odir+'life'+s+'-007b.png')

# --- lissajous

w, h = get_canvas('A4')

params1 = {
    'w': w, 'h': h, 'name': 'LISSAJOUS', 'call': lissajous_loop, 'Background': (0, 0, 0),
    'LineColor': (255,255,255), 'LineWidth': 10,
    'FF1': 19.0,
    'FF2': 31.0,
    'FFi': 0,
    'dT': 1,
    'Steps': 2000,
    'Scale': 0.9,
}
params2 = {
    'w': w, 'h': h, 'name': 'LISSAJOUS', 'call': lissajous_loop, 'Background': (0, 0, 0),
    'LineColor': (50,255,50), 'LineWidth': 10,
    'FF1': 3.0,
    'FF2': 4.0,
    'FFi': 0,
    'dT': 1,
    'Steps': 2000,
    'Scale': 0.9,
}
params3 = {
    'w': w, 'h': h, 'name': 'LISSAJOUS', 'call': lissajous_loop, 'Background': (0, 0, 0),
    'LineColor': (50,255,50), 'LineWidth': 10,
    'FF1': 2.0,
    'FF2': 3.0,
    'FFi': 0,
    'dT': 1,
    'Steps': 2000,
    'Scale': 0.9,
}

art_painter(params1, odir+'lissajous-%dx%d-001.png' % (w, h))
art_painter(params2, odir+'lissajous-%dx%d-002.png' % (w, h))
art_painter(params3, odir+'lissajous-%dx%d-003.png' % (w, h))

# --- ?

def do_waves(cnt, w, h, odir):
    params1 = {
        'w': w, 'h': h, 'Background': (224, 244, 0),
        'name': 'WAVES#1', 'call': waves1, 
        'z': 14,
        'f0': 1,
        'horizontal': False,
        'gradient': 256,
        'c1': (0,0,255),
        'c2': (0,255,255),
        'c3': (255,255,255),
    }
    params2 = {
        'w': w, 'h': h, 'Background': (224, 244, 0),
        'name': 'WAVES#1', 'call': waves1, 
        'z': 12,
        'f0': 1,
        'horizontal': True,
        'gradient': 256,
        'c1': (0,0,0),
        'c2': (0,255,0),
        'c3': (255,255,0),
    }
    params3 = {
        'w': w, 'h': h, 'Background': (0, 0, 0),
        'name': 'WAVES#1', 'call': waves1, 
        'z': 9,
        'f0': 1,
        'horizontal': False,
        'gradient': 24,
        'c1': (0,0,0),
        'c2': (255,0,0),
        'c3': (255,255,0),
    }
    params4 = {
        'w': w, 'h': h, 'Background': (0, 0, 0),
        'name': 'WAVES#1', 'call': waves1, 
        'z': 4,
        'f0': 0.33,
        'horizontal': True,
        'gradient': 256,
        'c1': (255,0,0),
        'c2': (0,255,0),
        'c3': (0,0,255),
    }
    params5 = {
        'w': w, 'h': h, 'Background': (0, 0, 0),
        'name': 'WAVES#1', 'call': waves1, 
        'z': 4,
        'f0': 3.0,
        'horizontal': True,
        'gradient': 256,
        'c1': (255,0,0),
        'c2': (0,255,0),
        'c3': (0,0,255),
    }

    params1a = {
        'w': w, 'h': h, 'Background': (0, 0, 0),
        'name': 'WAVES#2', 'call': waves2, 
        'z': 96,
        'f0': 1,
        'horizontal': False,
        'gradient': 256,
        'c1': (255,0,0),
        'c2': (255,255,0),
        'c3': (255,255,255),
    }
    params2a = {
        'w': w, 'h': h, 'Background': (0, 0, 0),
        'name': 'WAVES#2', 'call': waves2, 
        'z': 48,
        'f0': 1,
        'horizontal': True,
        'gradient': 256,
        'c1': (0,128,0),
        'c2': (0,255,0),
        'c3': (0,0,255),
    }

    params1b = {
        'w': w, 'h': h, 'Background': (0, 0, 0),
        'name': 'WAVES#3', 'call': waves3, 
        'z': 18,
        'gradient': 64,
        'c1': (255,255,255),
        'c2': (255,255,0),
        'c3': (255,0,0),
    }

    paramsX = {
        'w': w, 'h': h, 'Background': (0, 0, 0),
        'name': 'WAVES#2#MUX', 'call': waves_mux, 
        'par1': params1a,
        'par2': params2a,
    }

    for n in range(cnt):
        art_painter(params1, odir+'waves1-%dx%d-01-%03d.png' % (w, h, n+1))
        art_painter(params2, odir+'waves1-%dx%d-02-%03d.png' % (w, h, n+1))
        art_painter(params3, odir+'waves1-%dx%d-03-%03d.png' % (w, h, n+1))
        art_painter(params4, odir+'waves1-%dx%d-04-%03d.png' % (w, h, n+1))
        art_painter(params5, odir+'waves1-%dx%d-05-%03d.png' % (w, h, n+1))
        art_painter(params1a, odir+'waves2-%dx%d-01-%03d.png' % (w, h, n+1))
        art_painter(params2a, odir+'waves2-%dx%d-02-%03d.png' % (w, h, n+1))
        art_painter(params1b, odir+'waves3-%dx%d-01-%03d.png' % (w, h, n+1))
        art_painter(paramsX, odir+'waves_mux-%dx%d-01-%03d.png' % (w, h, n+1))
        
w, h = get_canvas('A3')
do_waves(3, w, h, odir)

# --- astro

w, h = get_canvas('A3') # note: does not scalle well with canvas size, so far optimised only for A3

params0f = {'name': 'ASTROART', 'call': paint0, 'w': w, 'h': h, 'Background': (0, 0, 0), 'ou': (0,0,0), 'box_or_cir': False}
params0t = {'name': 'ASTROART', 'call': paint0, 'w': w, 'h': h, 'Background': (0, 0, 0), 'ou': (0,0,0), 'box_or_cir': True}
params1f = {'name': 'ASTROART', 'call': paint1, 'w': w, 'h': h, 'Background': (0, 0, 0), 'ou': (0,0,0), 'box_or_cir': False}
params1t = {'name': 'ASTROART', 'call': paint1, 'w': w, 'h': h, 'Background': (0, 0, 0), 'ou': (0,0,0), 'box_or_cir': True}
params2f = {'name': 'ASTROART', 'call': paint2, 'w': w, 'h': h, 'Background': (0, 0, 0), 'ou': (0,0,0), 'box_or_cir': False}
params2t = {'name': 'ASTROART', 'call': paint2, 'w': w, 'h': h, 'Background': (0, 0, 0), 'ou': (0,0,0), 'box_or_cir': True}
params3f = {'name': 'ASTROART', 'call': paint3, 'w': w, 'h': h, 'Background': (0, 0, 0), 'ou': (0,0,0), 'box_or_cir': False}
params3t = {'name': 'ASTROART', 'call': paint3, 'w': w, 'h': h, 'Background': (0, 0, 0), 'ou': (0,0,0), 'box_or_cir': True}
params4f = {'name': 'ASTROART', 'call': paint4, 'w': w, 'h': h, 'Background': (0, 0, 0), 'ou': (0,0,0), 'box_or_cir': False}
params4t = {'name': 'ASTROART', 'call': paint4, 'w': w, 'h': h, 'Background': (0, 0, 0), 'ou': (0,0,0), 'box_or_cir': True}
params5f = {'name': 'ASTROART', 'call': paint5, 'w': w, 'h': h, 'Background': (0, 0, 0), 'ou': (0,0,0), 'box_or_cir': False}
params5t = {'name': 'ASTROART', 'call': paint5, 'w': w, 'h': h, 'Background': (0, 0, 0), 'ou': (0,0,0), 'box_or_cir': True}
params6f = {'name': 'ASTROART', 'call': paint6, 'w': w, 'h': h, 'Background': (0, 0, 0), 'ou': (0,0,0), 'box_or_cir': False}
params6t = {'name': 'ASTROART', 'call': paint6, 'w': w, 'h': h, 'Background': (0, 0, 0), 'ou': (0,0,0), 'box_or_cir': True}
params7f = {'name': 'ASTROART', 'call': paint7, 'w': w, 'h': h, 'Background': (0, 0, 0), 'ou': (0,0,0), 'box_or_cir': False}
params7t = {'name': 'ASTROART', 'call': paint7, 'w': w, 'h': h, 'Background': (0, 0, 0), 'ou': (0,0,0), 'box_or_cir': True}

art_painter(params0f, odir+'astro-01-bluegalaxy-cir.png')
art_painter(params0t, odir+'astro-01-bluegalaxy-box.png')

art_painter(params1f, odir+'astro-02-ellipticgalaxy-cir.png')
art_painter(params1t, odir+'astro-02-ellipticgalaxy-box.png')

art_painter(params2f, odir+'astro-03-spiralgalaxy-cir.png')
art_painter(params2t, odir+'astro-03-spiralgalaxy-box.png')

art_painter(params3f, odir+'astro-04-neutronstar-cir.png')
art_painter(params3t, odir+'astro-04-neutronstar-box.png')

art_painter(params4f, odir+'astro-05-blackhole-cir.png')
art_painter(params4t, odir+'astro-05-blackhole-box.png')

art_painter(params5f, odir+'astro-06-supernova-cir.png')
art_painter(params5t, odir+'astro-06-supernova-box.png')

art_painter(params6f, odir+'astro-07-nebula-cir.png')
art_painter(params6t, odir+'astro-07-nebula-box.png')

art_painter(params7f, odir+'astro-08-star-cir.png')
art_painter(params7t, odir+'astro-08-star-box.png')

# --- mandelbrot

params1 = {'name': 'MANDELBROT', 'call': generate_mandelbrot, 'x0': -2.5, 'x1': 1.0, 'y0': -1.0, 'y1': 1.0, 'maxiter': 200, 'w': 700, 'h': 400, 'negative': False}
params2 = {'name': 'MANDELBROT', 'call': generate_mandelbrot, 'x0': -2.5, 'x1': 1.0, 'y0': -1.0, 'y1': 1.0, 'maxiter': 20, 'w': 700, 'h': 400, 'negative': False}
art_painter(params1, odir+'mandelbrot-001.png', bw=True)
art_painter(params2, odir+'mandelbrot-002.png', bw=True)

# --- smears 1-5

def do_mazy1(cnt, w, h, odir):

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

    for n in range(cnt):
        art_painter(params1, odir+'mazy1-%dx%d-01-%03d.png' % (w, h, n+1))
        art_painter(params2, odir+'mazy1-%dx%d-02-%03d.png' % (w, h, n+1))
        art_painter(params3, odir+'mazy1-%dx%d-03-%03d.png' % (w, h, n+1))
        art_painter(params4, odir+'mazy1-%dx%d-04-%03d.png' % (w, h, n+1))
        art_painter(params5, odir+'mazy1-%dx%d-05-%03d.png' % (w, h, n+1))
        art_painter(params6, odir+'mazy1-%dx%d-06-%03d.png' % (w, h, n+1))

def do_mazy2(cnt, w, h, odir):

    params1 = {
        'name': 'SMEARS#2', 'call': mazy2, 'w': w, 'h': h, 'Background': (255, 255, 255),
        'v': 50-0-20-10,
        'n': 20*4,
        'm': 40,
        'blur': True,
        'r0': 64,
        'g0': 64,
        'b0': 64,
        'r1': 256,
        'g1': 256,
        'b1': 256,
        'mode': 'black',
    }

    params2 = {
        'name': 'SMEARS#2', 'call': mazy2, 'w': w, 'h': h, 'Background': (255, 255, 255),
        'v': 50+25,
        'n': 20*5,
        'm': 100-50-10,
        'blur': True,
        'r0': 0,
        'g0': 0,
        'b0': 0,
        'r1': 256,
        'g1': 0,
        'b1': 0,
        'mode': 'red',
    }

    params3 = {
        'name': 'SMEARS#2', 'call': mazy2, 'w': w, 'h': h, 'Background': (255, 255, 255),
        'v': 30,
        'n': 20*5,
        'm': 100-50-10,
        'blur': False,
        'r0': 64,
        'g0': 64,
        'b0': 0,
        'r1': 256,
        'g1': 256,
        'b1': 32,
        'mode': 'red',
    }

    params4 = {
        'name': 'SMEARS#2', 'call': mazy2, 'w': w, 'h': h, 'Background': (255, 255, 255),
        'v': 30,
        'n': 80,
        'm': 50,
        'blur': False,
        'r0': 0,
        'g0': 48,
        'b0': 0,
        'r1': 2,
        'g1': 256,
        'b1': 48,
        'mode': 'red',
    }

    params5 = {
        'name': 'SMEARS#2', 'call': mazy2, 'w': w, 'h': h, 'Background': (255, 255, 0),
        'v': 50,
        'n': 30,
        'm': 25,
        'blur': True,
        'r0': 32,
        'g0': 64,
        'b0': 64,
        'r1': 64,
        'g1': 256,
        'b1': 256,
        'mode': 'color',
    }

    params6 = {
        'name': 'SMEARS#2', 'call': mazy2, 'w': w, 'h': h, 'Background': (0, 0, 0),
        'v': 22,
        'n': 24,
        'm': 40,
        'blur': False,
        'r0': 32,
        'g0': 0,
        'b0': 0,
        'r1': 256,
        'g1': 0,
        'b1': 0,
        'mode': 'black',
    }

    for n in range(cnt):
        art_painter(params1, odir+'mazy2-%dx%d-01-%03d.png' % (w, h, n+1))
        art_painter(params2, odir+'mazy2-%dx%d-02-%03d.png' % (w, h, n+1))
        art_painter(params3, odir+'mazy2-%dx%d-03-%03d.png' % (w, h, n+1))
        art_painter(params4, odir+'mazy2-%dx%d-04-%03d.png' % (w, h, n+1))
        art_painter(params5, odir+'mazy2-%dx%d-05-%03d.png' % (w, h, n+1))
        art_painter(params6, odir+'mazy2-%dx%d-06-%03d.png' % (w, h, n+1))

def do_mazy3(cnt, w, h, odir):

    params1 = {
        'name': 'SMEARS#3', 'call': mazy3, 'w': w, 'h': h, 'Background': (255, 255, 255),
        'n': 20,
        'm': 0,
        'blur': False,
        'r0': 16,
        'g0': 64,
        'b0': 64,
        'r1': 256,
        'g1': 256,
        'b1': 256,
        'mode': '',
    }

    params2 = {
        'name': 'SMEARS#3', 'call': mazy3, 'w': w, 'h': h, 'Background': (255, 255, 0),
        'n': 10,
        'm': 0,
        'blur': False,
        'r0': 0,
        'g0': 0,
        'b0': 0,
        'r1': 256,
        'g1': 0,
        'b1': 0,
        'mode': '',
    }

    params3 = {
        'name': 'SMEARS#3', 'call': mazy3, 'w': w, 'h': h, 'Background': (255, 255, 0),
        'n': 30,
        'm': 0,
        'blur': False,
        'r0': 64,
        'g0': 64,
        'b0': 0,
        'r1': 256,
        'g1': 256,
        'b1': 32,
        'mode': '',
    }

    params4 = {
        'name': 'SMEARS#3', 'call': mazy3, 'w': w, 'h': h, 'Background': (255, 255, 0),
        'n': 20,
        'm': 0,
        'blur': False,
        'r0': 0,
        'g0': 48,
        'b0': 0,
        'r1': 2,
        'g1': 256,
        'b1': 48,
        'mode': '',
    }

    params5 = {
        'name': 'SMEARS#3', 'call': mazy3, 'w': w, 'h': h, 'Background': (255, 255, 0),
        'n': 30,
        'm': 0,
        'blur': False,
        'r0': 32,
        'g0': 64,
        'b0': 64,
        'r1': 64,
        'g1': 256,
        'b1': 256,
        'mode': '',
    }

    params6 = {
        'name': 'SMEARS#3', 'call': mazy3, 'w': w, 'h': h, 'Background': (0, 0, 0),
        'n': 30,
        'm': 0,
        'blur': False,
        'r0': 32,
        'g0': 0,
        'b0': 0,
        'r1': 256,
        'g1': 0,
        'b1': 0,
        'mode': '',
    }

    for n in range(cnt):
        art_painter(params1, odir+'mazy3-%dx%d-01-%03d.png' % (w, h, n+1))
        art_painter(params2, odir+'mazy3-%dx%d-02-%03d.png' % (w, h, n+1))
        art_painter(params3, odir+'mazy3-%dx%d-03-%03d.png' % (w, h, n+1))
        art_painter(params4, odir+'mazy3-%dx%d-04-%03d.png' % (w, h, n+1))
        art_painter(params5, odir+'mazy3-%dx%d-05-%03d.png' % (w, h, n+1))
        art_painter(params6, odir+'mazy3-%dx%d-06-%03d.png' % (w, h, n+1))

def do_mazy4(cnt, w, h, odir):

    params1 = {
        'name': 'SMEARS#4', 'call': mazy4, 'w': w, 'h': h, 'Background': (255, 255, 255),
        'n': 5,
        'r0': 16,
        'g0': 64,
        'b0': 64,
        'r1': 256,
        'g1': 256,
        'b1': 256,
        'mode': 'center',
    }

    params2 = {
        'name': 'SMEARS#4', 'call': mazy4, 'w': w, 'h': h, 'Background': (255, 255, 0),
        'n': 5,
        'r0': 0,
        'g0': 0,
        'b0': 0,
        'r1': 256,
        'g1': 0,
        'b1': 0,
        'mode': 'center',
    }

    params3 = {
        'name': 'SMEARS#4', 'call': mazy4, 'w': w, 'h': h, 'Background': (255, 255, 0),
        'n': 5,
        'r0': 64,
        'g0': 64,
        'b0': 0,
        'r1': 256,
        'g1': 256,
        'b1': 32,
        'mode': 'center',
    }

    params4 = {
        'name': 'SMEARS#4', 'call': mazy4, 'w': w, 'h': h, 'Background': (255, 255, 0),
        'n': 5,
        'r0': 0,
        'g0': 48,
        'b0': 0,
        'r1': 2,
        'g1': 256,
        'b1': 48,
        'mode': 'center',
    }

    params5 = {
        'name': 'SMEARS#4', 'call': mazy4, 'w': w, 'h': h, 'Background': (255, 255, 0),
        'n': 4,
        'r0': 32,
        'g0': 64,
        'b0': 64,
        'r1': 64,
        'g1': 256,
        'b1': 256,
        'mode': 'center',
    }

    params6 = {
        'name': 'SMEARS#4', 'call': mazy4, 'w': w, 'h': h, 'Background': (0, 0, 0),
        'n': 5,
        'r0': 32,
        'g0': 0,
        'b0': 0,
        'r1': 256,
        'g1': 0,
        'b1': 0,
        'mode': '',
    }

    params7 = {
        'name': 'SMEARS#4', 'call': mazy4, 'w': w, 'h': h, 'Background': (0, 0, 0),
        'n': 3,
        'r0': 64,
        'g0': 0,
        'b0': 0,
        'r1': 256,
        'g1': 0,
        'b1': 0,
        'mode': 'center',
    }

    for n in range(cnt):
        art_painter(params1, odir+'mazy4-%dx%d-01-%03d.png' % (w, h, n+1))
        art_painter(params2, odir+'mazy4-%dx%d-02-%03d.png' % (w, h, n+1))
        art_painter(params3, odir+'mazy4-%dx%d-03-%03d.png' % (w, h, n+1))
        art_painter(params4, odir+'mazy4-%dx%d-04-%03d.png' % (w, h, n+1))
        art_painter(params5, odir+'mazy4-%dx%d-05-%03d.png' % (w, h, n+1))
        art_painter(params6, odir+'mazy4-%dx%d-06-%03d.png' % (w, h, n+1))
        art_painter(params7, odir+'mazy4-%dx%d-07-%03d.png' % (w, h, n+1))

def do_mazy5(cnt, w, h, odir):
    params1 = {'name': 'SMEARS#5', 'call': mazy5, 'w': w, 'h': h, 'Background': (0, 0, 0), 'colors': colors_b, 'outline': None}
    params2 = {'name': 'SMEARS#5', 'call': mazy5, 'w': w, 'h': h, 'Background': (0, 0, 0), 'colors': colors_y, 'outline': None}
    params3 = {'name': 'SMEARS#5', 'call': mazy5, 'w': w, 'h': h, 'Background': (0, 0, 0), 'colors': colors_p, 'outline': (0, 0, 0)}
    params4 = {'name': 'SMEARS#5', 'call': mazy5, 'w': w, 'h': h, 'Background': (0, 0, 0), 'colors': colors_bw, 'outline': None}
    for n in range(cnt):
        art_painter(params1, odir+'mazy5-%dx%d-01-%03d.png' % (w, h, n+1))
        art_painter(params2, odir+'mazy5-%dx%d-02-%03d.png' % (w, h, n+1))
        art_painter(params3, odir+'mazy5-%dx%d-03-%03d.png' % (w, h, n+1))
        art_painter(params4, odir+'mazy5-%dx%d-04-%03d.png' % (w, h, n+1))

w, h = get_canvas('A3')
cnt = 4 # *6 each #1..#3 + *7 for #4 = (4)*6*3+(4)*7 = 100 images, it takes some time, easy over 10 minutes
do_mazy1(cnt, w, h, odir)
do_mazy2(cnt, w, h, odir)
do_mazy3(cnt, w, h, odir)
do_mazy4(cnt, w, h, odir)
cnt = 3 # *4 each = 12
do_mazy5(cnt, w, h, odir)

# --- ?

# --- ?

time_elapsed = dt.now() - start_time
print('ALL done. elapsed time: {}'.format(time_elapsed))

