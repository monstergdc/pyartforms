#! /usr/bin/env python
# -*- coding: utf-8 -*-

# paint algorithms (artificial artist) in Python - demo
# (c)2018-2019 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz
# cre: 20181020
# upd: 20190105, 06, 13

# TODO:
# - nice argparse (also per module?)
# - anims: anims | grow (also img) | zxoids-anim (also img maybe?)
# - smears5post
# - asciiart | city-lame | faces (fin) | brush

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


start_time = dt.now()
root = '!output'
if not os.path.exists(root):
    os.makedirs(root)
odir = root+'\\'

# --- life

def do_life(cnt, w, h, odir):
    params1 = {'name': 'LIFE', 'call': life, 'w': w, 'h': h, 'Background': (0, 0, 0), 'Color': (255,255,255), 'f': 'f2a'}

    params1['f'] = 'f2a'
    art_painter(params1, odir+'life-%dx%d-001a.png' % (w, h))
    art_painter(params1, odir+'life-%dx%d-001b.png' % (w, h))
    params1['f'] = 'f2b'
    art_painter(params1, odir+'life-%dx%d-002a.png' % (w, h))
    art_painter(params1, odir+'life-%dx%d-002b.png' % (w, h))
    params1['f'] = 'f2c'
    art_painter(params1, odir+'life-%dx%d-003a.png' % (w, h))
    art_painter(params1, odir+'life-%dx%d-003b.png' % (w, h))
    params1['f'] = 'f2d'
    art_painter(params1, odir+'life-%dx%d-004a.png' % (w, h))
    art_painter(params1, odir+'life-%dx%d-004b.png' % (w, h))
    params1['f'] = 'f2e'
    art_painter(params1, odir+'life-%dx%d-005a.png' % (w, h))
    art_painter(params1, odir+'life-%dx%d-005b.png' % (w, h))
    params1['f'] = 'f2f'
    art_painter(params1, odir+'life-%dx%d-006a.png' % (w, h))
    art_painter(params1, odir+'life-%dx%d-006b.png' % (w, h))
    params1['f'] = 'f2g'
    art_painter(params1, odir+'life-%dx%d-007a.png' % (w, h))
    art_painter(params1, odir+'life-%dx%d-007b.png' % (w, h))

# --- lissajous

def do_lissajous(cnt, w, h, odir):
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
   
# --- waves

def do_waves(cnt, w, h, odir):
    params1 = {
        'name': 'WAVES#1', 'call': waves1, 'w': w, 'h': h, 'Background': (224, 244, 0),
        'z': 14,
        'f0': 1,
        'horizontal': False,
        'gradient': 256,
        'c1': (0,0,255),
        'c2': (0,255,255),
        'c3': (255,255,255),
    }
    params2 = {
        'name': 'WAVES#1', 'call': waves1, 'w': w, 'h': h, 'Background': (224, 244, 0),
        'z': 12,
        'f0': 1,
        'horizontal': True,
        'gradient': 256,
        'c1': (0,0,0),
        'c2': (0,255,0),
        'c3': (255,255,0),
    }
    params3 = {
        'name': 'WAVES#1', 'call': waves1, 'w': w, 'h': h, 'Background': (0, 0, 0),
        'z': 9,
        'f0': 1,
        'horizontal': False,
        'gradient': 24,
        'c1': (0,0,0),
        'c2': (255,0,0),
        'c3': (255,255,0),
    }
    params4 = {
        'name': 'WAVES#1', 'call': waves1, 'w': w, 'h': h, 'Background': (0, 0, 0),
        'z': 4,
        'f0': 0.33,
        'horizontal': True,
        'gradient': 256,
        'c1': (255,0,0),
        'c2': (0,255,0),
        'c3': (0,0,255),
    }
    params5 = {
        'name': 'WAVES#1', 'call': waves1, 'w': w, 'h': h, 'Background': (0, 0, 0),
        'z': 4,
        'f0': 3.0,
        'horizontal': True,
        'gradient': 256,
        'c1': (255,0,0),
        'c2': (0,255,0),
        'c3': (0,0,255),
    }

    params1a = {
        'name': 'WAVES#2', 'call': waves2, 'w': w, 'h': h, 'Background': (0, 0, 0),
        'z': 96,
        'f0': 1,
        'horizontal': False,
        'gradient': 256,
        'c1': (255,0,0),
        'c2': (255,255,0),
        'c3': (255,255,255),
    }
    params2a = {
        'name': 'WAVES#2', 'call': waves2, 'w': w, 'h': h, 'Background': (0, 0, 0),
        'z': 48,
        'f0': 1,
        'horizontal': True,
        'gradient': 256,
        'c1': (0,128,0),
        'c2': (0,255,0),
        'c3': (0,0,255),
    }
    params1b = {
        'name': 'WAVES#3', 'call': waves3, 'w': w, 'h': h, 'Background': (0, 0, 0),
        'z': 18,
        'gradient': 64,
        'c1': (255,255,255),
        'c2': (255,255,0),
        'c3': (255,0,0),
    }

    paramsX = {
        'name': 'WAVES#2#MUX', 'call': waves_mux, 'w': w, 'h': h, 'Background': (0, 0, 0),
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
        
# --- astro

def do_astro(cnt, w, h, odir):
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

def do_mandelbrot(cnt, w, h, odir):
    params1 = {'name': 'MANDELBROT', 'call': generate_mandelbrot, 'x0': -2.5, 'x1': 1.0, 'y0': -1.0, 'y1': 1.0, 'maxiter': 200, 'w': w, 'h': h, 'negative': False}
    params2 = {'name': 'MANDELBROT', 'call': generate_mandelbrot, 'x0': -2.5, 'x1': 1.0, 'y0': -1.0, 'y1': 1.0, 'maxiter': 20, 'w': w, 'h': h, 'negative': False}
    art_painter(params1, odir+'mandelbrot-001.png', bw=True)
    art_painter(params2, odir+'mandelbrot-002.png', bw=True)

# --- smears

def do_mazy1(cnt, w, h, odir):
    params1 = {
        'name': 'SMEARS#1', 'call': mazy1, 'w': w, 'h': h, 'Background': (255, 255, 255),
        'pw': 8,
        'v': 50-20-10,
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
        'mode': 'black', 'keep': False,
    }
    params2 = {
        'name': 'SMEARS#1', 'call': mazy1, 'w': w, 'h': h, 'Background': (255, 255, 255),
        'pw': 8,
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
        'mode': 'red', 'keep': False,
    }
    params3 = {
        'name': 'SMEARS#1', 'call': mazy1, 'w': w, 'h': h, 'Background': (255, 255, 255),
        'pw': 8,
        'v': 50-20,
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
        'mode': 'red', 'keep': False,
    }
    params4 = {
        'name': 'SMEARS#1', 'call': mazy1, 'w': w, 'h': h, 'Background': (255, 255, 255),
        'pw': 8,
        'v': 50-20,
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
        'mode': 'red', 'keep': False,
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
        'mode': 'red', 'keep': True,
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
        'mode': 'red', 'keep': True,
    }

    for n in range(cnt):
        ts = dt.now().strftime('%Y%m%d%H%M%S')
        art_painter(params1, odir+'mazy1-%dx%d-01-%03d-%s.png' % (w, h, n+1, ts))
        art_painter(params2, odir+'mazy1-%dx%d-02-%03d-%s.png' % (w, h, n+1, ts))
        art_painter(params3, odir+'mazy1-%dx%d-03-%03d-%s.png' % (w, h, n+1, ts))
        art_painter(params4, odir+'mazy1-%dx%d-04-%03d-%s.png' % (w, h, n+1, ts))
        art_painter(params5, odir+'mazy1-%dx%d-05-%03d-%s.png' % (w, h, n+1, ts))
        art_painter(params6, odir+'mazy1-%dx%d-06-%03d-%s.png' % (w, h, n+1, ts))

def do_mazy2(cnt, w, h, odir):
    params1 = {
        'name': 'SMEARS#2', 'call': mazy2, 'w': w, 'h': h, 'Background': (0, 0, 0),
        'v': 20, 'n': 100, 'm': 40, 'blur': True,
        'c0': (64, 64, 64), 'c1': (255, 255, 255), 'mode': 'black',
    }
    params2 = {
        'name': 'SMEARS#2', 'call': mazy2, 'w': w, 'h': h, 'Background': (0, 0, 0),
        'v': 50+25+(50), 'n': 100, 'm': 60, 'blur': True,
        'c0': (0, 0, 0), 'c1': (255, 0, 0), 'mode': 'red',
    }
    params3 = {
        'name': 'SMEARS#2', 'call': mazy2, 'w': w, 'h': h, 'Background': (0, 0, 0),
        'v': 30, 'n': 100, 'm': 40, 'blur': False,
        'c0': (64, 64, 0), 'c1': (255, 255, 32), 'mode': 'red',
    }
    params4 = {
        'name': 'SMEARS#2', 'call': mazy2, 'w': w, 'h': h, 'Background': (0, 0, 0),
        'v': 30, 'n': 80, 'm': 50, 'blur': False,
        'c0': (0, 64, 0), 'c1': (32, 255, 48), 'mode': 'red',
    }
    params5 = {
        'name': 'SMEARS#2', 'call': mazy2, 'w': w, 'h': h, 'Background': (0, 0, 0),
        'v': 50, 'n': 30, 'm': 25, 'blur': True,
        'c0': (32, 64, 64), 'c1': (64, 255, 255), 'mode': 'color',
    }
    params6 = {
        'name': 'SMEARS#2', 'call': mazy2, 'w': w, 'h': h, 'Background': (0, 0, 0),
        'v': 22, 'n': 30, 'm': 40, 'blur': False,
        'c0': (32, 0, 0), 'c1': (255, 0, 0), 'mode': 'black',
    }
    params7 = {
        'name': 'SMEARS#2', 'call': mazy2, 'w': w, 'h': h, 'Background': (0, 0, 0),
        'v': 22, 'n': 30, 'm': 40, 'blur': True,
        'c0': (32, 0, 0), 'c1': (255, 0, 0), 'mode': 'black',
    }

    for n in range(cnt):
        ts = dt.now().strftime('%Y%m%d%H%M%S')
        art_painter(params1, odir+'mazy2-%dx%d-01-%03d-%s.png' % (w, h, n+1, ts))
        art_painter(params2, odir+'mazy2-%dx%d-02-%03d-%s.png' % (w, h, n+1, ts))
        art_painter(params3, odir+'mazy2-%dx%d-03-%03d-%s.png' % (w, h, n+1, ts))
        art_painter(params4, odir+'mazy2-%dx%d-04-%03d-%s.png' % (w, h, n+1, ts))
        art_painter(params5, odir+'mazy2-%dx%d-05-%03d-%s.png' % (w, h, n+1, ts))
        art_painter(params6, odir+'mazy2-%dx%d-06-%03d-%s.png' % (w, h, n+1, ts))
        art_painter(params7, odir+'mazy2-%dx%d-07-%03d-%s.png' % (w, h, n+1, ts))

def do_mazy3(cnt, w, h, odir):
    params1 = {'name': 'SMEARS#3', 'call': mazy3, 'w': w, 'h': h, 'Background': (255, 255, 255),
        'n': 20, 'blur': False, 'r0': 16, 'g0': 64, 'b0': 64, 'r1': 256, 'g1': 256, 'b1': 256, 'mode': '',
    }
    params2 = {'name': 'SMEARS#3', 'call': mazy3, 'w': w, 'h': h, 'Background': (255, 255, 0),
        'n': 10, 'blur': False, 'r0': 0, 'g0': 0, 'b0': 0, 'r1': 256, 'g1': 0, 'b1': 0, 'mode': '',
    }
    params3 = {'name': 'SMEARS#3', 'call': mazy3, 'w': w, 'h': h, 'Background': (255, 255, 0),
        'n': 30, 'blur': False, 'r0': 64, 'g0': 64, 'b0': 0, 'r1': 256, 'g1': 256, 'b1': 32, 'mode': '',
    }
    params4 = {'name': 'SMEARS#3', 'call': mazy3, 'w': w, 'h': h, 'Background': (255, 255, 0),
        'n': 20, 'blur': False, 'r0': 0, 'g0': 48, 'b0': 0, 'r1': 2, 'g1': 256, 'b1': 48, 'mode': '',
    }
    params5 = {'name': 'SMEARS#3', 'call': mazy3, 'w': w, 'h': h, 'Background': (255, 255, 0),
        'n': 30, 'blur': False, 'r0': 32, 'g0': 64, 'b0': 64, 'r1': 64, 'g1': 256, 'b1': 256, 'mode': '',
    }
    params6 = {'name': 'SMEARS#3', 'call': mazy3, 'w': w, 'h': h, 'Background': (0, 0, 0),
        'n': 30, 'blur': False, 'r0': 32, 'g0': 0, 'b0': 0, 'r1': 256, 'g1': 0, 'b1': 0, 'mode': '',
    }
    for n in range(cnt):
        ts = dt.now().strftime('%Y%m%d%H%M%S')
        art_painter(params1, odir+'mazy3-%dx%d-01-%03d-%s.png' % (w, h, n+1, ts))
        art_painter(params2, odir+'mazy3-%dx%d-02-%03d-%s.png' % (w, h, n+1, ts))
        art_painter(params3, odir+'mazy3-%dx%d-03-%03d-%s.png' % (w, h, n+1, ts))
        art_painter(params4, odir+'mazy3-%dx%d-04-%03d-%s.png' % (w, h, n+1, ts))
        art_painter(params5, odir+'mazy3-%dx%d-05-%03d-%s.png' % (w, h, n+1, ts))
        art_painter(params6, odir+'mazy3-%dx%d-06-%03d-%s.png' % (w, h, n+1, ts))

def do_mazy4(cnt, w, h, odir):
    params1 = {'name': 'SMEARS#4', 'call': mazy4, 'w': w, 'h': h, 'Background': (255, 255, 255), 'n': 5, 'mode': 'center', 'color': 'happy'}
    params2 = {'name': 'SMEARS#4', 'call': mazy4, 'w': w, 'h': h, 'Background': (255, 255, 0), 'n': 5, 'mode': 'center', 'color': 'red'}
    params3 = {'name': 'SMEARS#4', 'call': mazy4, 'w': w, 'h': h, 'Background': (255, 255, 0), 'n': 5, 'mode': 'center', 'color': 'rg'}
    params4 = {'name': 'SMEARS#4', 'call': mazy4, 'w': w, 'h': h, 'Background': (255, 255, 0), 'n': 5, 'mode': 'center', 'color': 'green'}
    params5 = {'name': 'SMEARS#4', 'call': mazy4, 'w': w, 'h': h, 'Background': (255, 255, 0), 'n': 4, 'mode': 'center', 'color': 'bg'}
    params6 = {'name': 'SMEARS#4', 'call': mazy4, 'w': w, 'h': h, 'Background': (0, 0, 0), 'n': 5, 'mode': '', 'color': 'red'}
    params7 = {'name': 'SMEARS#4', 'call': mazy4, 'w': w, 'h': h, 'Background': (0, 0, 0), 'n': 3, 'mode': 'center', 'color': 'red'}
    params8 = {'name': 'SMEARS#4', 'call': mazy4, 'w': w, 'h': h, 'Background': (0, 0, 0), 'n': 8, 'mode': 'center', 'color': 'bw'}
    params9 = {'name': 'SMEARS#4', 'call': mazy4, 'w': w, 'h': h, 'Background': (192, 192, 192), 'n': 11, 'mode': 'center', 'color': 'happy'}
    for n in range(cnt):
        ts = dt.now().strftime('%Y%m%d%H%M%S')
        art_painter(params1, odir+'mazy4-%dx%d-01-%03d-%s.png' % (w, h, n+1, ts))
        art_painter(params2, odir+'mazy4-%dx%d-02-%03d-%s.png' % (w, h, n+1, ts))
        art_painter(params3, odir+'mazy4-%dx%d-03-%03d-%s.png' % (w, h, n+1, ts))
        art_painter(params4, odir+'mazy4-%dx%d-04-%03d-%s.png' % (w, h, n+1, ts))
        art_painter(params5, odir+'mazy4-%dx%d-05-%03d-%s.png' % (w, h, n+1, ts))
        art_painter(params6, odir+'mazy4-%dx%d-06-%03d-%s.png' % (w, h, n+1, ts))
        art_painter(params7, odir+'mazy4-%dx%d-07-%03d-%s.png' % (w, h, n+1, ts))
        art_painter(params8, odir+'mazy4-%dx%d-08-%03d-%s.png' % (w, h, n+1, ts))
        art_painter(params9, odir+'mazy4-%dx%d-09-%03d-%s.png' % (w, h, n+1, ts))

def do_mazy5(cnt, w, h, odir):
    params1 = {'name': 'SMEARS#5', 'call': mazy5, 'w': w, 'h': h, 'Background': (0, 0, 0), 'colors': colors_b, 'outline': None}
    params2 = {'name': 'SMEARS#5', 'call': mazy5, 'w': w, 'h': h, 'Background': (0, 0, 0), 'colors': colors_y, 'outline': None}
    params3 = {'name': 'SMEARS#5', 'call': mazy5, 'w': w, 'h': h, 'Background': (0, 0, 0), 'colors': colors_p, 'outline': (0, 0, 0)}
    params4 = {'name': 'SMEARS#5', 'call': mazy5, 'w': w, 'h': h, 'Background': (0, 0, 0), 'colors': colors_bw, 'outline': None}
    params5 = {'name': 'SMEARS#5', 'call': mazy5, 'w': w, 'h': h, 'Background': (0, 0, 0), 'colors': colors_happy, 'outline': None}
    for n in range(cnt):
        ts = dt.now().strftime('%Y%m%d%H%M%S')
        art_painter(params1, odir+'mazy5-%dx%d-01-%03d-%s.png' % (w, h, n+1, ts))
        art_painter(params2, odir+'mazy5-%dx%d-02-%03d-%s.png' % (w, h, n+1, ts))
        art_painter(params3, odir+'mazy5-%dx%d-03-%03d-%s.png' % (w, h, n+1, ts))
        art_painter(params4, odir+'mazy5-%dx%d-04-%03d-%s.png' % (w, h, n+1, ts))
        art_painter(params5, odir+'mazy5-%dx%d-05-%03d-%s.png' % (w, h, n+1, ts))

def do_mazy6(cnt, w, h, odir):
    params1 = {'name': 'SMEARS#6', 'call': mazy6, 'w': w, 'h': h, 'Background': (0, 0, 0), 'mode': 'red', 'cnt': 18}
    params2 = {'name': 'SMEARS#6', 'call': mazy6, 'w': w, 'h': h, 'Background': (0, 0, 0), 'mode': 'blue', 'cnt': 18}
    params3 = {'name': 'SMEARS#6', 'call': mazy6, 'w': w, 'h': h, 'Background': (0, 0, 0), 'mode': 'black', 'cnt': 18}
    params4 = {'name': 'SMEARS#6', 'call': mazy6, 'w': w, 'h': h, 'Background': (0, 0, 0), 'mode': 'rg', 'cnt': 18}
    params5 = {'name': 'SMEARS#6', 'call': mazy6, 'w': w, 'h': h, 'Background': (0, 0, 0), 'mode': 'gb', 'cnt': 18}
    for n in range(cnt):
        ts = dt.now().strftime('%Y%m%d%H%M%S')
        art_painter(params1, odir+'mazy6-%dx%d-01-%03d-%s.png' % (w, h, n+1, ts))
        art_painter(params2, odir+'mazy6-%dx%d-02-%03d-%s.png' % (w, h, n+1, ts))
        art_painter(params3, odir+'mazy6-%dx%d-03-%03d-%s.png' % (w, h, n+1, ts))
        art_painter(params4, odir+'mazy6-%dx%d-04-%03d-%s.png' % (w, h, n+1, ts))
        art_painter(params5, odir+'mazy6-%dx%d-05-%03d-%s.png' % (w, h, n+1, ts))

def do_mazy7(cnt, w, h, odir):
    bk = (0x84, 0x8B, 0x9B)
    params1a = {'name': 'SMEARS#7', 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 500, 'cmode': 'rnd', 'mode': 'const'}
    params2a = {'name': 'SMEARS#7', 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 2000, 'cmode': 'rnd', 'mode': 'const'}

    params1b = {'name': 'SMEARS#7', 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 200, 'cmode': 'std', 'mode': 'decp'}
    params2b = {'name': 'SMEARS#7', 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 100, 'cmode': 'std', 'mode': 'decp'}
    params3b = {'name': 'SMEARS#7', 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 50, 'cmode': 'std', 'mode': 'decp'}
    params4b = {'name': 'SMEARS#7', 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 10, 'cmode': 'std', 'mode': 'decp'}

    params1c = {'name': 'SMEARS#7', 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 200, 'cmode': 'std', 'mode': 'dec'}
    params2c = {'name': 'SMEARS#7', 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 100, 'cmode': 'std', 'mode': 'dec'}
    params3c = {'name': 'SMEARS#7', 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 50, 'cmode': 'std', 'mode': 'dec'}
    params4c = {'name': 'SMEARS#7', 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 10, 'cmode': 'std', 'mode': 'dec'}

    params1d = {'name': 'SMEARS#7', 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 200, 'cmode': 'inv', 'mode': 'dec'}
    params2d = {'name': 'SMEARS#7', 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 100, 'cmode': 'inv', 'mode': 'dec'}
    params3d = {'name': 'SMEARS#7', 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 50, 'cmode': 'inv', 'mode': 'dec'}
    params4d = {'name': 'SMEARS#7', 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 10, 'cmode': 'inv', 'mode': 'dec'}

    params1e = {'name': 'SMEARS#7', 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 200, 'cmode': 'rnd', 'mode': 'dec'}
    params2e = {'name': 'SMEARS#7', 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 100, 'cmode': 'rnd', 'mode': 'dec'}
    params3e = {'name': 'SMEARS#7', 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 50, 'cmode': 'rnd', 'mode': 'dec'}
    params4e = {'name': 'SMEARS#7', 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 10, 'cmode': 'rnd', 'mode': 'dec'}

    params1f = {'name': 'SMEARS#7', 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 200, 'cmode': 'color', 'mode': 'dec'}
    params2f = {'name': 'SMEARS#7', 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 100, 'cmode': 'color', 'mode': 'dec'}
    params3f = {'name': 'SMEARS#7', 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 50, 'cmode': 'color', 'mode': 'dec'}
    params4f = {'name': 'SMEARS#7', 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 10, 'cmode': 'color', 'mode': 'dec'}

    for n in range(cnt):
        tx = dt.now().strftime('%Y%m%d%H%M%S')

        art_painter(params1a, odir+'mazy7a-%dx%d-01-%03d-%s.png' % (w, h, n+1, tx))
        art_painter(params2a, odir+'mazy7a-%dx%d-02-%03d-%s.png' % (w, h, n+1, tx))

        art_painter(params1b, odir+'mazy7b-%dx%d-01-%03d-%s.png' % (w, h, n+1, tx))
        art_painter(params2b, odir+'mazy7b-%dx%d-02-%03d-%s.png' % (w, h, n+1, tx))
        art_painter(params3b, odir+'mazy7b-%dx%d-03-%03d-%s.png' % (w, h, n+1, tx))
        art_painter(params4b, odir+'mazy7b-%dx%d-04-%03d-%s.png' % (w, h, n+1, tx))

        art_painter(params1c, odir+'mazy7c-%dx%d-01-%03d-%s.png' % (w, h, n+1, tx))
        art_painter(params2c, odir+'mazy7c-%dx%d-02-%03d-%s.png' % (w, h, n+1, tx))
        art_painter(params3c, odir+'mazy7c-%dx%d-03-%03d-%s.png' % (w, h, n+1, tx))
        art_painter(params4c, odir+'mazy7c-%dx%d-04-%03d-%s.png' % (w, h, n+1, tx))

        art_painter(params1d, odir+'mazy7d-%dx%d-01-%03d-%s.png' % (w, h, n+1, tx))
        art_painter(params2d, odir+'mazy7d-%dx%d-02-%03d-%s.png' % (w, h, n+1, tx))
        art_painter(params3d, odir+'mazy7d-%dx%d-03-%03d-%s.png' % (w, h, n+1, tx))
        art_painter(params4d, odir+'mazy7d-%dx%d-04-%03d-%s.png' % (w, h, n+1, tx))

        art_painter(params1e, odir+'mazy7e-%dx%d-01-%03d-%s.png' % (w, h, n+1, tx))
        art_painter(params2e, odir+'mazy7e-%dx%d-02-%03d-%s.png' % (w, h, n+1, tx))
        art_painter(params3e, odir+'mazy7e-%dx%d-03-%03d-%s.png' % (w, h, n+1, tx))
        art_painter(params4e, odir+'mazy7e-%dx%d-04-%03d-%s.png' % (w, h, n+1, tx))

        art_painter(params1f, odir+'mazy7f-%dx%d-01-%03d-%s.png' % (w, h, n+1, tx))
        art_painter(params2f, odir+'mazy7f-%dx%d-02-%03d-%s.png' % (w, h, n+1, tx))
        art_painter(params3f, odir+'mazy7f-%dx%d-03-%03d-%s.png' % (w, h, n+1, tx))
        art_painter(params4f, odir+'mazy7f-%dx%d-04-%03d-%s.png' % (w, h, n+1, tx))

def do_mazy8(cnt, w, h, odir):
    bk = (0xff, 0xff, 0xff)
    params1 = {'name': 'SMEARS#8', 'call': mazy8, 'w': w, 'h': h, 'Background': bk, 'mode': '', 'xcnt': 5, 'ycnt': 5}
    params2 = {'name': 'SMEARS#8', 'call': mazy8, 'w': w, 'h': h, 'Background': bk, 'mode': '', 'xcnt': 5, 'ycnt': 10}
    params3 = {'name': 'SMEARS#8', 'call': mazy8, 'w': w, 'h': h, 'Background': bk, 'mode': '', 'xcnt': 5, 'ycnt': 3}
    for n in range(cnt):
        tx = dt.now().strftime('%Y%m%d%H%M%S')
        art_painter(params1, odir+'mazy8-%dx%d-01-%03d-%s.png' % (w, h, n+1, tx))
        art_painter(params2, odir+'mazy8-%dx%d-02-%03d-%s.png' % (w, h, n+1, tx))
        art_painter(params3, odir+'mazy8-%dx%d-03-%03d-%s.png' % (w, h, n+1, tx))

# --- go

#w, h = get_canvas('A2')
w, h = get_canvas('A3')
cnt = 4 # *6 each #1..#3 + *7 for #4 = (4)*6*3+(4)*7 = 100 images, it takes some time, easy over 10 minutes
do_mazy1(cnt, w, h, odir)
do_mazy2(cnt, w, h, odir)
do_mazy3(cnt, w, h, odir) # lame, need fix
do_mazy4(cnt, w, h, odir) # also a bit lame, only red ok, add blue
cnt = 3 # *4 each = 12
do_mazy5(cnt, w, h, odir)
cnt = 3
do_mazy6(cnt, w, h, odir)
cnt = 3
do_mazy7(cnt, w, h, odir)
cnt = 3
do_mazy8(cnt, w, h, odir)

w, h = get_canvas('800')
do_life(0, w, h, odir)

w, h = get_canvas('A4')
do_lissajous(0, w, h, odir)

w, h = get_canvas('A3') # note: does not scalle well with canvas size, so far optimised only for A3
do_astro(0, w, h, odir)

do_mandelbrot(0, 700, 400, odir)
    
w, h = get_canvas('A3')
cnt = 3
do_waves(cnt, w, h, odir)

time_elapsed = dt.now() - start_time
print('ALL done. elapsed time: {}'.format(time_elapsed))

