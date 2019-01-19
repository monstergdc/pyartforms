#! /usr/bin/env python
# -*- coding: utf-8 -*-

# paint algorithms (artificial artist) in Python - demo
# (c)2018-2019 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz
# cre: 20181020
# upd: 20190105, 06, 13, 18

# predefined forms

from drawtools import get_canvas, art_painter
from life1 import life
from lissajous import lissajous, lissajous_loop
from waves import *
from astroart import *
from mandelbrot import generate_mandelbrot
from smears import *
from pyart_defs import *


# --- life

def predef_life(w, h):
    return [
        {'name': 'LIFE', 'call': life, 'w': w, 'h': h, 'Background': (0, 0, 0), 'Color': (255,255,255), 'f': 'f2a'},
        {'name': 'LIFE', 'call': life, 'w': w, 'h': h, 'Background': (0, 0, 0), 'Color': (255,255,255), 'f': 'f2b'},
        {'name': 'LIFE', 'call': life, 'w': w, 'h': h, 'Background': (0, 0, 0), 'Color': (255,255,255), 'f': 'f2c'},
        {'name': 'LIFE', 'call': life, 'w': w, 'h': h, 'Background': (0, 0, 0), 'Color': (255,255,255), 'f': 'f2d'},
        {'name': 'LIFE', 'call': life, 'w': w, 'h': h, 'Background': (0, 0, 0), 'Color': (255,255,255), 'f': 'f2e'},
        {'name': 'LIFE', 'call': life, 'w': w, 'h': h, 'Background': (0, 0, 0), 'Color': (255,255,255), 'f': 'f2f'},
        {'name': 'LIFE', 'call': life, 'w': w, 'h': h, 'Background': (0, 0, 0), 'Color': (255,255,255), 'f': 'f2g'}
    ]

# --- lissajous

def predef_lissajous(w, h):
    bg = (0, 0, 0)
    return [
        {'w': w, 'h': h, 'name': 'LISSAJOUS', 'call': lissajous_loop, 'Background': bg, 'LineColor': (255,255,255), 'LineWidth': 10,
        'FF1': 19.0, 'FF2': 31.0, 'FFi': 0, 'dT': 1, 'Steps': 2000, 'Scale': 0.9},
        {'w': w, 'h': h, 'name': 'LISSAJOUS', 'call': lissajous_loop, 'Background': bg, 'LineColor': (50,255,50), 'LineWidth': 10,
        'FF1': 3.0, 'FF2': 4.0, 'FFi': 0, 'dT': 1, 'Steps': 2000, 'Scale': 0.9},
        {'w': w, 'h': h, 'name': 'LISSAJOUS', 'call': lissajous_loop, 'Background': bg, 'LineColor': (50,255,50), 'LineWidth': 10,
        'FF1': 2.0, 'FF2': 3.0, 'FFi': 0, 'dT': 1, 'Steps': 2000, 'Scale': 0.9}
    ]
   
# --- waves

def predef_waves(w, h):
    return [
        {'name': 'WAVES#1', 'call': waves1, 'w': w, 'h': h, 'Background': (224, 244, 0),
        'z': 14, 'f0': 1, 'horizontal': False,
        'gradient': 256,
        'c1': (0,0,255),
        'c2': (0,255,255),
        'c3': (255,255,255),
        },
        {'name': 'WAVES#1', 'call': waves1, 'w': w, 'h': h, 'Background': (224, 244, 0),
        'z': 12, 'f0': 1, 'horizontal': True,
        'gradient': 256,
        'c1': (0,0,0),
        'c2': (0,255,0),
        'c3': (255,255,0),
        },
        {'name': 'WAVES#1', 'call': waves1, 'w': w, 'h': h, 'Background': (0, 0, 0),
        'z': 9, 'f0': 1, 'horizontal': False,
        'gradient': 24,
        'c1': (0,0,0),
        'c2': (255,0,0),
        'c3': (255,255,0),
        },
        {'name': 'WAVES#1', 'call': waves1, 'w': w, 'h': h, 'Background': (0, 0, 0),
        'z': 4, 'f0': 0.33, 'horizontal': True,
        'gradient': 256,
        'c1': (255,0,0),
        'c2': (0,255,0),
        'c3': (0,0,255),
        },
        {'name': 'WAVES#1', 'call': waves1, 'w': w, 'h': h, 'Background': (0, 0, 0),
        'z': 4, 'f0': 3.0, 'horizontal': True,
        'gradient': 256,
        'c1': (255,0,0),
        'c2': (0,255,0),
        'c3': (0,0,255),
        },
        {'name': 'WAVES#2', 'call': waves2, 'w': w, 'h': h, 'Background': (0, 0, 0),
        'z': 96, 'f0': 1, 'horizontal': False,
        'gradient': 256,
        'c1': (255,0,0),
        'c2': (255,255,0),
        'c3': (255,255,255),
        },
        {'name': 'WAVES#2', 'call': waves2, 'w': w, 'h': h, 'Background': (0, 0, 0),
        'z': 48, 'f0': 1, 'horizontal': True,
        'gradient': 256,
        'c1': (0,128,0),
        'c2': (0,255,0),
        'c3': (0,0,255),
        },
        {'name': 'WAVES#3', 'call': waves3, 'w': w, 'h': h, 'Background': (0, 0, 0),
        'z': 18, 'gradient': 64,
        'c1': (255,255,255),
        'c2': (255,255,0),
        'c3': (255,0,0),
        }
#        {'name': 'WAVES#2#MUX', 'call': waves_mux, 'w': w, 'h': h, 'Background': (0, 0, 0),
#        'par1': params1a, 'par2': params2a,
#        }
    ]
        
# --- astro

def predef_astro(w, h):
    return [
        {'name': 'ASTROART', 'call': paint0, 'w': w, 'h': h, 'Background': (0, 0, 0), 'ou': (0,0,0), 'box_or_cir': False},
        {'name': 'ASTROART', 'call': paint0, 'w': w, 'h': h, 'Background': (0, 0, 0), 'ou': (0,0,0), 'box_or_cir': True},
        {'name': 'ASTROART', 'call': paint1, 'w': w, 'h': h, 'Background': (0, 0, 0), 'ou': (0,0,0), 'box_or_cir': False},
        {'name': 'ASTROART', 'call': paint1, 'w': w, 'h': h, 'Background': (0, 0, 0), 'ou': (0,0,0), 'box_or_cir': True},
        {'name': 'ASTROART', 'call': paint2, 'w': w, 'h': h, 'Background': (0, 0, 0), 'ou': (0,0,0), 'box_or_cir': False},
        {'name': 'ASTROART', 'call': paint2, 'w': w, 'h': h, 'Background': (0, 0, 0), 'ou': (0,0,0), 'box_or_cir': True},
        {'name': 'ASTROART', 'call': paint3, 'w': w, 'h': h, 'Background': (0, 0, 0), 'ou': (0,0,0), 'box_or_cir': False},
        {'name': 'ASTROART', 'call': paint3, 'w': w, 'h': h, 'Background': (0, 0, 0), 'ou': (0,0,0), 'box_or_cir': True},
        {'name': 'ASTROART', 'call': paint4, 'w': w, 'h': h, 'Background': (0, 0, 0), 'ou': (0,0,0), 'box_or_cir': False},
        {'name': 'ASTROART', 'call': paint4, 'w': w, 'h': h, 'Background': (0, 0, 0), 'ou': (0,0,0), 'box_or_cir': True},
        {'name': 'ASTROART', 'call': paint5, 'w': w, 'h': h, 'Background': (0, 0, 0), 'ou': (0,0,0), 'box_or_cir': False},
        {'name': 'ASTROART', 'call': paint5, 'w': w, 'h': h, 'Background': (0, 0, 0), 'ou': (0,0,0), 'box_or_cir': True},
        {'name': 'ASTROART', 'call': paint6, 'w': w, 'h': h, 'Background': (0, 0, 0), 'ou': (0,0,0), 'box_or_cir': False},
        {'name': 'ASTROART', 'call': paint6, 'w': w, 'h': h, 'Background': (0, 0, 0), 'ou': (0,0,0), 'box_or_cir': True},
        {'name': 'ASTROART', 'call': paint7, 'w': w, 'h': h, 'Background': (0, 0, 0), 'ou': (0,0,0), 'box_or_cir': False},
        {'name': 'ASTROART', 'call': paint7, 'w': w, 'h': h, 'Background': (0, 0, 0), 'ou': (0,0,0), 'box_or_cir': True}
    ]

# --- mandelbrot

def predef_mandelbrot(w, h):
    return [
        {'name': 'MANDELBROT', 'call': generate_mandelbrot, 'x0': -2.5, 'x1': 1.0, 'y0': -1.0, 'y1': 1.0, 'maxiter': 200, 'w': w, 'h': h, 'negative': False},
        {'name': 'MANDELBROT', 'call': generate_mandelbrot, 'x0': -2.5, 'x1': 1.0, 'y0': -1.0, 'y1': 1.0, 'maxiter': 20, 'w': w, 'h': h, 'negative': False}
    ]

# --- smears

def predef_mazy1(w, h):
    bg_white = (255, 255, 255)
    bg_yellow = (255, 255, 0)
    return [
        {'name': 'SMEARS#1', 'call': mazy1, 'w': w, 'h': h, 'Background': bg_white,
        'penw': 8, 'v': 20, 'n': 100, 'm': 40, 'prefill': True, 'blur': True, 'mode': 'black', 'keep': False,
        'r0': 64, 'g0': 64, 'b0': 64,
        'r1': 256, 'g1': 256, 'b1': 256},
        {'name': 'SMEARS#1', 'call': mazy1, 'w': w, 'h': h, 'Background': bg_white,
        'penw': 8, 'v': 20, 'n': 100, 'm': 40, 'prefill': True, 'blur': True, 'mode': 'black', 'keep': False, 'color': 'happy',
        'r0': 64, 'g0': 64, 'b0': 64,
        'r1': 256, 'g1': 256, 'b1': 256},
        {'name': 'SMEARS#1', 'call': mazy1, 'w': w, 'h': h, 'Background': bg_white,
        'penw': 8, 'v': 20, 'n': 100, 'm': 40, 'prefill': True, 'blur': True, 'mode': 'black', 'keep': False, 'color': 'rg',
        'r0': 64, 'g0': 64, 'b0': 64,
        'r1': 256, 'g1': 256, 'b1': 256},
        {'name': 'SMEARS#1', 'call': mazy1, 'w': w, 'h': h, 'Background': bg_white,
        'penw': 8, 'v': 20, 'n': 100, 'm': 40, 'prefill': True, 'blur': True, 'mode': 'black', 'keep': False, 'color': 'psych',
        'r0': 64, 'g0': 64, 'b0': 64,
        'r1': 256, 'g1': 256, 'b1': 256},
        {'name': 'SMEARS#1', 'call': mazy1, 'w': w, 'h': h, 'Background': bg_white,
        'penw': 8, 'v': 75, 'n': 100, 'm': 40, 'prefill': False, 'blur': True, 'mode': 'red', 'keep': False,
        'r0': 0, 'g0': 0, 'b0': 0,
        'r1': 256, 'g1': 0, 'b1': 0},
        {'name': 'SMEARS#1', 'call': mazy1, 'w': w, 'h': h, 'Background': bg_white,
        'penw': 8, 'v': 75, 'n': 100, 'm': 40, 'prefill': False, 'blur': True, 'mode': 'happy', 'keep': False,
        'r0': 0, 'g0': 0, 'b0': 0,
        'r1': 256, 'g1': 0, 'b1': 0},
        {'name': 'SMEARS#1', 'call': mazy1, 'w': w, 'h': h, 'Background': bg_white,
        'penw': 8, 'v': 75, 'n': 100, 'm': 40, 'prefill': False, 'blur': True, 'mode': 'psych', 'keep': False,
        'r0': 0, 'g0': 0, 'b0': 0,
        'r1': 256, 'g1': 0, 'b1': 0},
        {'name': 'SMEARS#1', 'call': mazy1, 'w': w, 'h': h, 'Background': bg_white,
        'penw': 8, 'v': 30, 'n': 100, 'm': 40, 'prefill': True, 'blur': False, 'mode': 'red', 'keep': False,
        'r0': 64, 'g0': 64, 'b0': 0,
        'r1': 256, 'g1': 256, 'b1': 32},
        {'name': 'SMEARS#1', 'call': mazy1, 'w': w, 'h': h, 'Background': bg_white,
        'penw': 8, 'v': 30, 'n': 100, 'm': 40, 'prefill': True, 'blur': False, 'mode': 'red', 'keep': False,
        'r0': 0, 'g0': 64, 'b0': 0,
        'r1': 32, 'g1': 256, 'b1': 32},
        {'name': 'SMEARS#1', 'call': mazy1, 'w': w, 'h': h, 'Background': bg_yellow,
        'penw': 5, 'v': 200, 'n': 50, 'm': 25, 'prefill': False, 'blur': False, 'mode': 'red', 'keep': True,
        'r0': 0, 'g0': 0, 'b0': 0,
        'r1': 256, 'g1': 256, 'b1': 256},
        {'name': 'SMEARS#1', 'call': mazy1, 'w': w, 'h': h, 'Background': bg_yellow,
        'penw': 5, 'v': 120, 'n': 48, 'm': 12, 'prefill': True, 'blur': False, 'mode': 'red', 'keep': True,
        'r0': 16, 'g0': 64, 'b0': 128,
        'r1': 128, 'g1': 256, 'b1': 256}
    ]

def predef_mazy2(w, h):
    return [
        {'name': 'SMEARS#2', 'call': mazy2, 'w': w, 'h': h, 'Background': (0, 0, 0), 'v': 20, 'n': 100, 'm': 40, 'blur': True,
        'c0': (64, 64, 64), 'c1': (255, 255, 255), 'mode': 'black'},
        {'name': 'SMEARS#2', 'call': mazy2, 'w': w, 'h': h, 'Background': (0, 0, 0), 'v': 90, 'n': 90, 'm': 50, 'blur': True,
        'c0': (0, 0, 0), 'c1': (255, 0, 0), 'mode': 'red'},
        {'name': 'SMEARS#2', 'call': mazy2, 'w': w, 'h': h, 'Background': (0, 0, 0), 'v': 50, 'n': 50, 'm': 25, 'blur': True,
        'c0': (32, 64, 64), 'c1': (64, 255, 255), 'mode': 'color'},
        {'name': 'SMEARS#2', 'call': mazy2, 'w': w, 'h': h, 'Background': (0, 0, 0), 'v': 22, 'n': 40, 'm': 35, 'blur': False,
        'c0': (32, 0, 0), 'c1': (255, 0, 0), 'mode': 'black'},
        {'name': 'SMEARS#2', 'call': mazy2, 'w': w, 'h': h, 'Background': (0, 0, 0), 'v': 22, 'n': 40, 'm': 35, 'blur': True,
        'c0': (32, 0, 0), 'c1': (255, 0, 0), 'mode': 'black'}
    ]

def predef_mazy3(w, h):
    bg_yellow = (255, 255, 0)
    return [
        {'name': 'SMEARS#3', 'call': mazy3, 'w': w, 'h': h, 'Background': (255, 255, 255), 'n': 20, 'color': 'happy'},
        {'name': 'SMEARS#3', 'call': mazy3, 'w': w, 'h': h, 'Background': bg_yellow, 'n': 25+5, 'color': 'red'},
        {'name': 'SMEARS#3', 'call': mazy3, 'w': w, 'h': h, 'Background': (255, 255, 255), 'n': 30, 'color': 'rg'},
        {'name': 'SMEARS#3', 'call': mazy3, 'w': w, 'h': h, 'Background': bg_yellow, 'n': 20, 'color': 'green'},
        {'name': 'SMEARS#3', 'call': mazy3, 'w': w, 'h': h, 'Background': bg_yellow, 'n': 30+20, 'color': 'bg'},
        {'name': 'SMEARS#3', 'call': mazy3, 'w': w, 'h': h, 'Background': (0, 0, 0), 'n': 20, 'color': 'red'},
        {'name': 'SMEARS#3', 'call': mazy3, 'w': w, 'h': h, 'Background': (0, 0, 0), 'n': 20, 'color': 'bw'},
    ]

def predef_mazy4(w, h):
    return [
        {'name': 'SMEARS#4', 'call': mazy4, 'w': w, 'h': h, 'Background': (255, 255, 255), 'n': 5, 'mode': 'center', 'color': 'happy'},
        {'name': 'SMEARS#4', 'call': mazy4, 'w': w, 'h': h, 'Background': (255, 255, 0), 'n': 5, 'mode': 'center', 'color': 'red'},
        {'name': 'SMEARS#4', 'call': mazy4, 'w': w, 'h': h, 'Background': (255, 255, 0), 'n': 5, 'mode': 'center', 'color': 'rg'},
        {'name': 'SMEARS#4', 'call': mazy4, 'w': w, 'h': h, 'Background': (255, 255, 0), 'n': 5, 'mode': 'center', 'color': 'green'},
        {'name': 'SMEARS#4', 'call': mazy4, 'w': w, 'h': h, 'Background': (255, 255, 0), 'n': 4, 'mode': 'center', 'color': 'bg'},
        {'name': 'SMEARS#4', 'call': mazy4, 'w': w, 'h': h, 'Background': (0, 0, 0), 'n': 5, 'mode': '', 'color': 'red'},
        {'name': 'SMEARS#4', 'call': mazy4, 'w': w, 'h': h, 'Background': (0, 0, 0), 'n': 3, 'mode': 'center', 'color': 'red'},
        {'name': 'SMEARS#4', 'call': mazy4, 'w': w, 'h': h, 'Background': (0, 0, 0), 'n': 8, 'mode': 'center', 'color': 'bw'},
        {'name': 'SMEARS#4', 'call': mazy4, 'w': w, 'h': h, 'Background': (192, 192, 192), 'n': 11, 'mode': 'center', 'color': 'happy'}
    ]

def predef_mazy5(w, h):
    bk = (0, 0, 0)
    return [
        {'name': 'SMEARS#5', 'call': mazy5, 'w': w, 'h': h, 'Background': bk, 'colors': colors_b, 'outline': None},
        {'name': 'SMEARS#5', 'call': mazy5, 'w': w, 'h': h, 'Background': bk, 'colors': colors_y, 'outline': None},
        {'name': 'SMEARS#5', 'call': mazy5, 'w': w, 'h': h, 'Background': bk, 'colors': colors_p, 'outline': (0, 0, 0)},
        {'name': 'SMEARS#5', 'call': mazy5, 'w': w, 'h': h, 'Background': bk, 'colors': colors_bw, 'outline': None},
        {'name': 'SMEARS#5', 'call': mazy5, 'w': w, 'h': h, 'Background': bk, 'colors': colors_happy, 'outline': None}
    ]

def predef_mazy6(w, h):
    bk = (0, 0, 0)
    return [
        {'name': 'SMEARS#6', 'call': mazy6, 'w': w, 'h': h, 'Background': bk, 'mode': 'red', 'cnt': 18},
        {'name': 'SMEARS#6', 'call': mazy6, 'w': w, 'h': h, 'Background': bk, 'mode': 'blue', 'cnt': 18},
        {'name': 'SMEARS#6', 'call': mazy6, 'w': w, 'h': h, 'Background': bk, 'mode': 'black', 'cnt': 18},
        {'name': 'SMEARS#6', 'call': mazy6, 'w': w, 'h': h, 'Background': bk, 'mode': 'rg', 'cnt': 18},
        {'name': 'SMEARS#6', 'call': mazy6, 'w': w, 'h': h, 'Background': bk, 'mode': 'gb', 'cnt': 18}
    ]

def predef_mazy7(w, h):
    bk = (0x84, 0x8B, 0x9B)
    return [
        {'name': 'SMEARS#7', 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 500,  'cmode': 'rnd', 'mode': 'const'},
        {'name': 'SMEARS#7', 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 2000, 'cmode': 'rnd', 'mode': 'const'},
        {'name': 'SMEARS#7', 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 200,  'cmode': 'std', 'mode': 'decp'},
        {'name': 'SMEARS#7', 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 100,  'cmode': 'std', 'mode': 'decp'},
        {'name': 'SMEARS#7', 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 50,   'cmode': 'std', 'mode': 'decp'},
        {'name': 'SMEARS#7', 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 10,   'cmode': 'std', 'mode': 'decp'},
        {'name': 'SMEARS#7', 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 200,  'cmode': 'std', 'mode': 'dec'},
        {'name': 'SMEARS#7', 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 100,  'cmode': 'std', 'mode': 'dec'},
        {'name': 'SMEARS#7', 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 50,   'cmode': 'std', 'mode': 'dec'},
        {'name': 'SMEARS#7', 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 10,   'cmode': 'std', 'mode': 'dec'},
        {'name': 'SMEARS#7', 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 200,  'cmode': 'inv', 'mode': 'dec'},
        {'name': 'SMEARS#7', 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 100,  'cmode': 'inv', 'mode': 'dec'},
        {'name': 'SMEARS#7', 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 50,   'cmode': 'inv', 'mode': 'dec'},
        {'name': 'SMEARS#7', 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 10,   'cmode': 'inv', 'mode': 'dec'},
        {'name': 'SMEARS#7', 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 200,  'cmode': 'rnd', 'mode': 'dec'},
        {'name': 'SMEARS#7', 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 100,  'cmode': 'rnd', 'mode': 'dec'},
        {'name': 'SMEARS#7', 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 50,   'cmode': 'rnd', 'mode': 'dec'},
        {'name': 'SMEARS#7', 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 10,   'cmode': 'rnd', 'mode': 'dec'},
        {'name': 'SMEARS#7', 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 200,  'cmode': 'color', 'mode': 'dec'},
        {'name': 'SMEARS#7', 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 100,  'cmode': 'color', 'mode': 'dec'},
        {'name': 'SMEARS#7', 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 50,   'cmode': 'color', 'mode': 'dec'},
        {'name': 'SMEARS#7', 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 10,   'cmode': 'color', 'mode': 'dec'}
    ]

def predef_mazy8(w, h):
    bk = (255, 255, 255)
    return [
        {'name': 'SMEARS#8', 'call': mazy8, 'w': w, 'h': h, 'Background': bk, 'mode': '', 'xcnt': 5, 'ycnt': 5},
        {'name': 'SMEARS#8', 'call': mazy8, 'w': w, 'h': h, 'Background': bk, 'mode': '', 'xcnt': 5, 'ycnt': 10},
        {'name': 'SMEARS#8', 'call': mazy8, 'w': w, 'h': h, 'Background': bk, 'mode': '', 'xcnt': 5, 'ycnt': 3}
    ]

def predef_mazy9(w, h):
        v = float(h)/8
        p = [
            {'name': 'SMEARS#9', 'call': mazy9, 'w': w, 'h': h, 'n': 20, 'Background': (0,0,0), 'color': 'happy', 'v': 0, 'rndc': True},
            {'name': 'SMEARS#9', 'call': mazy9, 'w': w, 'h': h, 'n': 60, 'Background': (0,0,0), 'color': 'happy', 'v': 0, 'rndc': True},
            {'name': 'SMEARS#9', 'call': mazy9, 'w': w, 'h': h, 'n': 120, 'Background': (0,0,0), 'color': 'happy', 'v': 0, 'rndc': True},
            {'name': 'SMEARS#9', 'call': mazy9, 'w': w, 'h': h, 'n': 20, 'Background': (0,0,0), 'color': 'psych', 'v': 0, 'rndc': True},
            {'name': 'SMEARS#9', 'call': mazy9, 'w': w, 'h': h, 'n': 60, 'Background': (0,0,0), 'color': 'psych', 'v': 0, 'rndc': True},
            {'name': 'SMEARS#9', 'call': mazy9, 'w': w, 'h': h, 'n': 120, 'Background': (0,0,0), 'color': 'psych', 'v': 0, 'rndc': True},

            {'name': 'SMEARS#9', 'call': mazy9, 'w': w, 'h': h, 'n': 20, 'Background': (0,0,0), 'color': 'happy', 'v': 0},
            {'name': 'SMEARS#9', 'call': mazy9, 'w': w, 'h': h, 'n': 60, 'Background': (0,0,0), 'color': 'happy', 'v': 0},
            {'name': 'SMEARS#9', 'call': mazy9, 'w': w, 'h': h, 'n': 120, 'Background': (0,0,0), 'color': 'happy', 'v': 0},
            {'name': 'SMEARS#9', 'call': mazy9, 'w': w, 'h': h, 'n': 20, 'Background': (0,0,0), 'color': 'psych', 'v': 0},
            {'name': 'SMEARS#9', 'call': mazy9, 'w': w, 'h': h, 'n': 60, 'Background': (0,0,0), 'color': 'psych', 'v': 0},
            {'name': 'SMEARS#9', 'call': mazy9, 'w': w, 'h': h, 'n': 120, 'Background': (0,0,0), 'color': 'psych', 'v': 0},
           
            {'name': 'SMEARS#9', 'call': mazy9, 'w': w, 'h': h, 'n': 20, 'Background': (0,0,0), 'color': 'red', 'v': 0},
            {'name': 'SMEARS#9', 'call': mazy9, 'w': w, 'h': h, 'n': 60, 'Background': (0,0,0), 'color': 'red', 'v': 0},
            {'name': 'SMEARS#9', 'call': mazy9, 'w': w, 'h': h, 'n': 120, 'Background': (0,0,0), 'color': 'red', 'v': 0},
            {'name': 'SMEARS#9', 'call': mazy9, 'w': w, 'h': h, 'n': 20, 'Background': (0,0,0), 'color': 'rg', 'v': 0},
            {'name': 'SMEARS#9', 'call': mazy9, 'w': w, 'h': h, 'n': 60, 'Background': (0,0,0), 'color': 'rg', 'v': 0},
            {'name': 'SMEARS#9', 'call': mazy9, 'w': w, 'h': h, 'n': 120, 'Background': (0,0,0), 'color': 'rg', 'v': 0},
            {'name': 'SMEARS#9', 'call': mazy9, 'w': w, 'h': h, 'n': 20, 'Background': (0,0,0), 'color': 'bw', 'v': 0},
            {'name': 'SMEARS#9', 'call': mazy9, 'w': w, 'h': h, 'n': 60, 'Background': (0,0,0), 'color': 'bw', 'v': 0},
            {'name': 'SMEARS#9', 'call': mazy9, 'w': w, 'h': h, 'n': 120, 'Background': (0,0,0), 'color': 'bw', 'v': 0},

            {'name': 'SMEARS#9', 'call': mazy9, 'w': w, 'h': h, 'n': 20, 'Background': (0,0,0), 'color': 'happy', 'v': v, 'rndc': True},
            {'name': 'SMEARS#9', 'call': mazy9, 'w': w, 'h': h, 'n': 60, 'Background': (0,0,0), 'color': 'happy', 'v': v, 'rndc': True},
            {'name': 'SMEARS#9', 'call': mazy9, 'w': w, 'h': h, 'n': 120, 'Background': (0,0,0), 'color': 'happy', 'v': v, 'rndc': True},
            {'name': 'SMEARS#9', 'call': mazy9, 'w': w, 'h': h, 'n': 20, 'Background': (0,0,0), 'color': 'psych', 'v': v, 'rndc': True},
            {'name': 'SMEARS#9', 'call': mazy9, 'w': w, 'h': h, 'n': 60, 'Background': (0,0,0), 'color': 'psych', 'v': v, 'rndc': True},
            {'name': 'SMEARS#9', 'call': mazy9, 'w': w, 'h': h, 'n': 120, 'Background': (0,0,0), 'color': 'psych', 'v': v, 'rndc': True},

            {'name': 'SMEARS#9', 'call': mazy9, 'w': w, 'h': h, 'n': 20, 'Background': (0,0,0), 'color': 'happy', 'v': v},
            {'name': 'SMEARS#9', 'call': mazy9, 'w': w, 'h': h, 'n': 60, 'Background': (0,0,0), 'color': 'happy', 'v': v},
            {'name': 'SMEARS#9', 'call': mazy9, 'w': w, 'h': h, 'n': 120, 'Background': (0,0,0), 'color': 'happy', 'v': v},
            {'name': 'SMEARS#9', 'call': mazy9, 'w': w, 'h': h, 'n': 20, 'Background': (0,0,0), 'color': 'psych', 'v': v},
            {'name': 'SMEARS#9', 'call': mazy9, 'w': w, 'h': h, 'n': 60, 'Background': (0,0,0), 'color': 'psych', 'v': v},
            {'name': 'SMEARS#9', 'call': mazy9, 'w': w, 'h': h, 'n': 120, 'Background': (0,0,0), 'color': 'psych', 'v': v},

            {'name': 'SMEARS#9', 'call': mazy9, 'w': w, 'h': h, 'n': 20, 'Background': (0,0,0), 'color': 'red', 'v': v},
            {'name': 'SMEARS#9', 'call': mazy9, 'w': w, 'h': h, 'n': 60, 'Background': (0,0,0), 'color': 'red', 'v': v},
            {'name': 'SMEARS#9', 'call': mazy9, 'w': w, 'h': h, 'n': 120, 'Background': (0,0,0), 'color': 'red', 'v': v},
            {'name': 'SMEARS#9', 'call': mazy9, 'w': w, 'h': h, 'n': 20, 'Background': (0,0,0), 'color': 'rg', 'v': v},
            {'name': 'SMEARS#9', 'call': mazy9, 'w': w, 'h': h, 'n': 60, 'Background': (0,0,0), 'color': 'rg', 'v': v},
            {'name': 'SMEARS#9', 'call': mazy9, 'w': w, 'h': h, 'n': 120, 'Background': (0,0,0), 'color': 'rg', 'v': v},
            {'name': 'SMEARS#9', 'call': mazy9, 'w': w, 'h': h, 'n': 20, 'Background': (0,0,0), 'color': 'bw', 'v': v},
            {'name': 'SMEARS#9', 'call': mazy9, 'w': w, 'h': h, 'n': 60, 'Background': (0,0,0), 'color': 'bw', 'v': v},
            {'name': 'SMEARS#9', 'call': mazy9, 'w': w, 'h': h, 'n': 120, 'Background': (0,0,0), 'color': 'bw', 'v': v},
        ]


# EOF
