#! /usr/bin/env python
# -*- coding: utf-8 -*-

# paint algorithms (artificial artist) in Python - demo
# (c)2018-2019 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz
# cre: 20181020
# upd: 20190105, 06, 13, 18, 21, 22
# upd: 20190311, 30
# upd: 20190414

# predefined forms

# TODO:
# - add alpha ver for: 1 / 2 ~60 ?
# - opt off blur for lowres #1
# -

import copy
from drawtools import get_canvas, art_painter
from life1 import life
from lissajous import lissajous, lissajous_loop
from waves import *
from astroart import *
from mandelbrot import generate_mandelbrot
from smears import *
from pyart_defs import *
from color_defs import *


bg_black = (0, 0, 0)
bg_gray = (192, 192, 192)
bg_white = (255, 255, 255)
bg_yellow = (255, 255, 0)
bg_orange = (255, 128, 0)


# --- life

def predef_life(w, h):
    return [
        {'name': 'LIFE', 'call': life, 'w': w, 'h': h, 'Background': bg_black, 'Color': (255,255,255), 'f': 'f2a'},
        {'name': 'LIFE', 'call': life, 'w': w, 'h': h, 'Background': bg_black, 'Color': (255,255,255), 'f': 'f2b'},
        {'name': 'LIFE', 'call': life, 'w': w, 'h': h, 'Background': bg_black, 'Color': (255,255,255), 'f': 'f2c'},
        {'name': 'LIFE', 'call': life, 'w': w, 'h': h, 'Background': bg_black, 'Color': (255,255,255), 'f': 'f2d'},
        {'name': 'LIFE', 'call': life, 'w': w, 'h': h, 'Background': bg_black, 'Color': (255,255,255), 'f': 'f2e'},
        {'name': 'LIFE', 'call': life, 'w': w, 'h': h, 'Background': bg_black, 'Color': (255,255,255), 'f': 'f2f'},
        {'name': 'LIFE', 'call': life, 'w': w, 'h': h, 'Background': bg_black, 'Color': (255,255,255), 'f': 'f2g'}
    ]

# --- lissajous

def predef_lissajous(w, h):
    return [
        {'w': w, 'h': h, 'name': 'LISSAJOUS', 'call': lissajous_loop, 'Background': bg_black, 'LineColor': (255,255,255), 'LineWidth': 10,
        'FF1': 19.0, 'FF2': 31.0, 'FFi': 0, 'dT': 1, 'Steps': 2000, 'Scale': 0.9},
        {'w': w, 'h': h, 'name': 'LISSAJOUS', 'call': lissajous_loop, 'Background': bg_black, 'LineColor': (50,255,50), 'LineWidth': 10,
        'FF1': 3.0, 'FF2': 4.0, 'FFi': 0, 'dT': 1, 'Steps': 2000, 'Scale': 0.9},
        {'w': w, 'h': h, 'name': 'LISSAJOUS', 'call': lissajous_loop, 'Background': bg_black, 'LineColor': (50,255,50), 'LineWidth': 10,
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
        {'name': 'WAVES#1', 'call': waves1, 'w': w, 'h': h, 'Background': bg_black,
        'z': 9, 'f0': 1, 'horizontal': False,
        'gradient': 24,
        'c1': (0,0,0),
        'c2': (255,0,0),
        'c3': (255,255,0),
        },
        {'name': 'WAVES#1', 'call': waves1, 'w': w, 'h': h, 'Background': bg_black,
        'z': 4, 'f0': 0.33, 'horizontal': True,
        'gradient': 256,
        'c1': (255,0,0),
        'c2': (0,255,0),
        'c3': (0,0,255),
        },
        {'name': 'WAVES#1', 'call': waves1, 'w': w, 'h': h, 'Background': bg_black,
        'z': 4, 'f0': 3.0, 'horizontal': True,
        'gradient': 256,
        'c1': (255,0,0),
        'c2': (0,255,0),
        'c3': (0,0,255),
        },
        {'name': 'WAVES#2', 'call': waves2, 'w': w, 'h': h, 'Background': bg_black,
        'z': 96, 'f0': 1, 'horizontal': False,
        'gradient': 256,
        'c1': (255,0,0),
        'c2': (255,255,0),
        'c3': (255,255,255),
        },
        {'name': 'WAVES#2', 'call': waves2, 'w': w, 'h': h, 'Background': bg_black,
        'z': 48, 'f0': 1, 'horizontal': True,
        'gradient': 256,
        'c1': (0,128,0),
        'c2': (0,255,0),
        'c3': (0,0,255),
        },
        {'name': 'WAVES#3', 'call': waves3, 'w': w, 'h': h, 'Background': bg_black,
        'z': 18, 'gradient': 64,
        'c1': (255,255,255),
        'c2': (255,255,0),
        'c3': (255,0,0),
        }
#        {'name': 'WAVES#2#MUX', 'call': waves_mux, 'w': w, 'h': h, 'Background': bg_black,
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

# note: use this for aplha (but call must handle alpha value too): 'alpha': True

def predef_mazy1(w, h):
    n = 'SMEARS#1'
    return [
        {'name': n, 'call': mazy1, 'w': w, 'h': h, 'Background': bg_white,
        'penw': 8, 'v': 20, 'n': 100, 'm': 40, 'prefill': True, 'blur': True, 'mode': 'black', 'keep': False,
        'r0': 64, 'g0': 64, 'b0': 64,
        'r1': 256, 'g1': 256, 'b1': 256},

#        {'name': n, 'call': mazy1, 'w': w, 'h': h, 'Background': bg_white,
#        'penw': 8, 'v': 20, 'n': 100, 'm': 40, 'prefill': True, 'blur': True, 'mode': 'black', 'keep': False,
#        'r0': 64, 'g0': 64, 'b0': 64,
#        'r1': 256, 'g1': 256, 'b1': 256, 'alpha': True},

        {'name': n, 'call': mazy1, 'w': w, 'h': h, 'Background': bg_white,
        'penw': 8, 'v': 20, 'n': 100, 'm': 40, 'prefill': True, 'blur': True, 'mode': 'black', 'keep': False, 'color': 'happy',
        'r0': 64, 'g0': 64, 'b0': 64,
        'r1': 256, 'g1': 256, 'b1': 256},

        {'name': n, 'call': mazy1, 'w': w, 'h': h, 'Background': bg_white,
        'penw': 8, 'v': 20, 'n': 100, 'm': 40, 'prefill': True, 'blur': True, 'mode': 'black', 'keep': False, 'color': 'wryb',
        'r0': 64, 'g0': 64, 'b0': 64,
        'r1': 256, 'g1': 256, 'b1': 256},

#        {'name': n, 'call': mazy1, 'w': w, 'h': h, 'Background': bg_white,
#        'penw': 8, 'v': 20, 'n': 100, 'm': 40, 'prefill': True, 'blur': True, 'mode': 'black', 'keep': False, 'color': 'happy',
#        'r0': 64, 'g0': 64, 'b0': 64,
#        'r1': 256, 'g1': 256, 'b1': 256, 'alpha': True},

#addalpha=60
        
        {'name': n, 'call': mazy1, 'w': w, 'h': h, 'Background': bg_white,
        'penw': 8, 'v': 20, 'n': 100, 'm': 40, 'prefill': True, 'blur': True, 'mode': 'black', 'keep': False, 'color': 'rg',
        'r0': 64, 'g0': 64, 'b0': 64,
        'r1': 256, 'g1': 256, 'b1': 256},
        {'name': n, 'call': mazy1, 'w': w, 'h': h, 'Background': bg_white,
        'penw': 8, 'v': 20, 'n': 100, 'm': 40, 'prefill': True, 'blur': True, 'mode': 'black', 'keep': False, 'color': 'psych',
        'r0': 64, 'g0': 64, 'b0': 64,
        'r1': 256, 'g1': 256, 'b1': 256},
        {'name': n, 'call': mazy1, 'w': w, 'h': h, 'Background': bg_white,
        'penw': 8, 'v': 75, 'n': 100, 'm': 40, 'prefill': False, 'blur': True, 'mode': 'red', 'keep': False,
        'r0': 0, 'g0': 0, 'b0': 0,
        'r1': 256, 'g1': 0, 'b1': 0},
        {'name': n, 'call': mazy1, 'w': w, 'h': h, 'Background': bg_white,
        'penw': 8, 'v': 75, 'n': 100, 'm': 40, 'prefill': False, 'blur': True, 'mode': 'happy', 'keep': False,
        'r0': 0, 'g0': 0, 'b0': 0,
        'r1': 256, 'g1': 0, 'b1': 0},
        {'name': n, 'call': mazy1, 'w': w, 'h': h, 'Background': bg_white,
        'penw': 8, 'v': 75, 'n': 100, 'm': 40, 'prefill': False, 'blur': True, 'mode': 'wryb', 'keep': False,
        'r0': 0, 'g0': 0, 'b0': 0,
        'r1': 256, 'g1': 0, 'b1': 0},
        {'name': n, 'call': mazy1, 'w': w, 'h': h, 'Background': bg_white,
        'penw': 8, 'v': 75, 'n': 100, 'm': 40, 'prefill': False, 'blur': True, 'mode': 'psych', 'keep': False,
        'r0': 0, 'g0': 0, 'b0': 0,
        'r1': 256, 'g1': 0, 'b1': 0},
        {'name': n, 'call': mazy1, 'w': w, 'h': h, 'Background': bg_white,
        'penw': 8, 'v': 30, 'n': 100, 'm': 40, 'prefill': True, 'blur': False, 'mode': 'red', 'keep': False,
        'r0': 64, 'g0': 64, 'b0': 0,
        'r1': 256, 'g1': 256, 'b1': 32},
        {'name': n, 'call': mazy1, 'w': w, 'h': h, 'Background': bg_white,
        'penw': 8, 'v': 30, 'n': 100, 'm': 40, 'prefill': True, 'blur': False, 'mode': 'red', 'keep': False,
        'r0': 0, 'g0': 64, 'b0': 0,
        'r1': 32, 'g1': 256, 'b1': 32},
        {'name': n, 'call': mazy1, 'w': w, 'h': h, 'Background': bg_yellow,
        'penw': 5, 'v': 200, 'n': 50, 'm': 25, 'prefill': False, 'blur': False, 'mode': 'red', 'keep': True,
        'r0': 0, 'g0': 0, 'b0': 0,
        'r1': 256, 'g1': 256, 'b1': 256},
        {'name': n, 'call': mazy1, 'w': w, 'h': h, 'Background': bg_yellow,
        'penw': 5, 'v': 120, 'n': 48, 'm': 12, 'prefill': True, 'blur': False, 'mode': 'red', 'keep': True,
        'r0': 16, 'g0': 64, 'b0': 128,
        'r1': 128, 'g1': 256, 'b1': 256}
    ]

def predef_mazy2(w, h):
    n = 'SMEARS#2'
    return [
        {'name': n, 'call': mazy2, 'w': w, 'h': h, 'Background': bg_black, 'n': 100, 'm': 40, 'color': 'bw0'},
        {'name': n, 'call': mazy2, 'w': w, 'h': h, 'Background': bg_black, 'n': 10, 'm': 300, 'color': 'bw0'},  # ?
        {'name': n, 'call': mazy2, 'w': w, 'h': h, 'Background': bg_black, 'n': 100, 'm': 40, 'color': 'bwx'},
        {'name': n, 'call': mazy2, 'w': w, 'h': h, 'Background': bg_black, 'n': 100, 'm': 40, 'color': 'bw'},
        {'name': n, 'call': mazy2, 'w': w, 'h': h, 'Background': bg_black, 'n': 100, 'm': 90, 'color': 'red'},
        {'name': n, 'call': mazy2, 'w': w, 'h': h, 'Background': bg_black, 'n': 100, 'm': 30, 'color': 'happy'},
        {'name': n, 'call': mazy2, 'w': w, 'h': h, 'Background': bg_black, 'n': 100, 'm': 30, 'color': 'wryb'},
        {'name': n, 'call': mazy2, 'w': w, 'h': h, 'Background': bg_black, 'n': 100, 'm': 30, 'color': 'psych'},
        {'name': n, 'call': mazy2, 'w': w, 'h': h, 'Background': bg_black, 'n': 100, 'm': 30, 'color': 'bgo'},
    ]

def predef_mazy3(w, h):
    n = 'SMEARS#3'
    a = [
        {'name': n, 'call': mazy3, 'w': w, 'h': h, 'Background': bg_white, 'n': 20, 'color': 'happy'},
        {'name': n, 'call': mazy3, 'w': w, 'h': h, 'Background': bg_white, 'n': 20, 'color': 'wryb'},

        {'name': n, 'call': mazy3, 'w': w, 'h': h, 'Background': bg_white, 'n': 80, 'color': 'happy'},
        {'name': n, 'call': mazy3, 'w': w, 'h': h, 'Background': bg_white, 'n': 80, 'color': 'wryb'},

        {'name': n, 'call': mazy3, 'w': w, 'h': h, 'Background': bg_yellow, 'n': 30, 'color': 'red'},
        {'name': n, 'call': mazy3, 'w': w, 'h': h, 'Background': bg_yellow, 'n': 80, 'color': 'red'},
        {'name': n, 'call': mazy3, 'w': w, 'h': h, 'Background': bg_black, 'n': 30, 'color': 'red'},
        {'name': n, 'call': mazy3, 'w': w, 'h': h, 'Background': bg_black, 'n': 80, 'color': 'red'},
        {'name': n, 'call': mazy3, 'w': w, 'h': h, 'Background': bg_black, 'n': 20, 'color': 'bw'},
        {'name': n, 'call': mazy3, 'w': w, 'h': h, 'Background': bg_white, 'n': 30, 'color': 'rg'},

        {'name': n, 'call': mazy3, 'w': w, 'h': h, 'Background': bg_orange, 'n': 80, 'color': 'bwx'},

        {'name': n, 'call': mazy3, 'w': w, 'h': h, 'Background': bg_white, 'n': 90, 'color': 'happy', 'addalpha': 50},
        {'name': n, 'call': mazy3, 'w': w, 'h': h, 'Background': bg_white, 'n': 90, 'color': 'wryb', 'addalpha': 50},

        {'name': n, 'call': mazy3, 'w': w, 'h': h, 'Background': bg_yellow, 'n': 90, 'color': 'red', 'addalpha': 50},
        {'name': n, 'call': mazy3, 'w': w, 'h': h, 'Background': bg_black, 'n': 90, 'color': 'red', 'addalpha': 50},
        {'name': n, 'call': mazy3, 'w': w, 'h': h, 'Background': bg_black, 'n': 90, 'color': 'bw', 'addalpha': 50},
        {'name': n, 'call': mazy3, 'w': w, 'h': h, 'Background': bg_white, 'n': 90, 'color': 'rg', 'addalpha': 50},

        {'name': n, 'call': mazy3, 'w': w, 'h': h, 'Background': bg_orange, 'n': 80, 'color': 'bwx', 'addalpha': 50},
    ]
    a1 = copy.deepcopy(a)
    a2 = copy.deepcopy(a)
    a3 = copy.deepcopy(a)
    for i in range(len(a)):
        a1[i]['mode'] = 'center'
        #a1[i]['name'] = n+'-center'
        a2[i]['mode'] = 'xcenter'
        #a2[i]['name'] = n+'-xcenter'
        a3[i]['mode'] = 'rnd'
        #a3[i]['name'] = n+'-rnd'
    return np.concatenate((a1, a2, a3), axis=0)

def predef_mazy4(w, h):
    n = 'SMEARS#4'
    return [
        {'name': n, 'call': mazy4, 'w': w, 'h': h, 'Background': bg_white, 'n': 5, 'mode': 'center', 'color': 'happy'},
        {'name': n, 'call': mazy4, 'w': w, 'h': h, 'Background': bg_white, 'n': 5, 'mode': 'center', 'color': 'wryb'},
        {'name': n, 'call': mazy4, 'w': w, 'h': h, 'Background': bg_white, 'n': 4, 'mode': 'center', 'color': 'bgo'},
        {'name': n, 'call': mazy4, 'w': w, 'h': h, 'Background': bg_white, 'n': 8, 'mode': 'center', 'color': 'avatar'},
        {'name': n, 'call': mazy4, 'w': w, 'h': h, 'Background': bg_white, 'n': 8, 'mode': 'center', 'color': 'psych'},

        {'name': n, 'call': mazy4, 'w': w, 'h': h, 'Background': bg_white, 'n': 5, 'mode': 'center', 'color': 'happy', 'addalpha': 90},
        {'name': n, 'call': mazy4, 'w': w, 'h': h, 'Background': bg_white, 'n': 5, 'mode': 'center', 'color': 'wryb', 'addalpha': 90},
        {'name': n, 'call': mazy4, 'w': w, 'h': h, 'Background': bg_white, 'n': 4, 'mode': 'center', 'color': 'bgo', 'addalpha': 90},
        {'name': n, 'call': mazy4, 'w': w, 'h': h, 'Background': bg_white, 'n': 8, 'mode': 'center', 'color': 'avatar', 'addalpha': 90},
        {'name': n, 'call': mazy4, 'w': w, 'h': h, 'Background': bg_white, 'n': 8, 'mode': 'center', 'color': 'psych', 'addalpha': 90},

        {'name': n, 'call': mazy4, 'w': w, 'h': h, 'Background': bg_white, 'n': 20, 'mode': '', 'color': 'happy', 'addalpha': 50},
        {'name': n, 'call': mazy4, 'w': w, 'h': h, 'Background': bg_white, 'n': 20, 'mode': '', 'color': 'wryb', 'addalpha': 50},
        {'name': n, 'call': mazy4, 'w': w, 'h': h, 'Background': bg_white, 'n': 20, 'mode': '', 'color': 'bgo', 'addalpha': 50},
        {'name': n, 'call': mazy4, 'w': w, 'h': h, 'Background': bg_white, 'n': 20, 'mode': '', 'color': 'avatar', 'addalpha': 50},
        {'name': n, 'call': mazy4, 'w': w, 'h': h, 'Background': bg_white, 'n': 20, 'mode': '', 'color': 'psych', 'addalpha': 50},

        {'name': n, 'call': mazy4, 'w': w, 'h': h, 'Background': bg_yellow, 'n': 5, 'mode': 'center', 'color': 'red'},
        {'name': n, 'call': mazy4, 'w': w, 'h': h, 'Background': bg_yellow, 'n': 5, 'mode': 'center', 'color': 'rg'},
        {'name': n, 'call': mazy4, 'w': w, 'h': h, 'Background': bg_yellow, 'n': 5, 'mode': 'center', 'color': 'green'},
        {'name': n, 'call': mazy4, 'w': w, 'h': h, 'Background': bg_yellow, 'n': 4, 'mode': 'center', 'color': 'bg'},
        {'name': n, 'call': mazy4, 'w': w, 'h': h, 'Background': bg_black, 'n': 5, 'mode': '', 'color': 'red'},
        {'name': n, 'call': mazy4, 'w': w, 'h': h, 'Background': (128, 0, 0), 'n': 20, 'mode': '', 'color': 'red'}, # ?
        {'name': n, 'call': mazy4, 'w': w, 'h': h, 'Background': bg_black, 'n': 3, 'mode': 'center', 'color': 'red'},
        {'name': n, 'call': mazy4, 'w': w, 'h': h, 'Background': bg_black, 'n': 8, 'mode': 'center', 'color': 'bw'},
        {'name': n, 'call': mazy4, 'w': w, 'h': h, 'Background': bg_gray, 'n': 11, 'mode': 'center', 'color': 'happy'},
        {'name': n, 'call': mazy4, 'w': w, 'h': h, 'Background': bg_gray, 'n': 11, 'mode': 'center', 'color': 'wryb'},
        {'name': n, 'call': mazy4, 'w': w, 'h': h, 'Background': bg_black, 'n': 11, 'mode': 'center', 'color': 'psych'},
    ]

def predef_mazy5(w, h):
    n = 'SMEARS#5'
    return [
        {'name': n, 'call': mazy5, 'w': w, 'h': h, 'Background': bg_black, 'colors': colors_b, 'outline': None},
        {'name': n, 'call': mazy5, 'w': w, 'h': h, 'Background': bg_black, 'colors': colors_y, 'outline': None},
        {'name': n, 'call': mazy5, 'w': w, 'h': h, 'Background': bg_black, 'colors': colors_p, 'outline': (0, 0, 0)},
        {'name': n, 'call': mazy5, 'w': w, 'h': h, 'Background': bg_black, 'colors': colors_bw0, 'outline': None},
        {'name': n, 'call': mazy5, 'w': w, 'h': h, 'Background': bg_black, 'colors': colors_bwx, 'outline': None},
        {'name': n, 'call': mazy5, 'w': w, 'h': h, 'Background': bg_black, 'colors': colors_happy, 'outline': None},
    ]

def predef_mazy6(w, h):
    n = 'SMEARS#6'
    return [
        {'name': n, 'call': mazy6, 'w': w, 'h': h, 'Background': bg_black, 'mode': 'red', 'cnt': 18, 'useblack': True},
        {'name': n, 'call': mazy6, 'w': w, 'h': h, 'Background': bg_black, 'mode': 'blue', 'cnt': 18, 'useblack': True},
        {'name': n, 'call': mazy6, 'w': w, 'h': h, 'Background': bg_black, 'mode': 'black', 'cnt': 18, 'useblack': True},
        {'name': n, 'call': mazy6, 'w': w, 'h': h, 'Background': bg_black, 'mode': 'rg', 'cnt': 18, 'useblack': True},
        {'name': n, 'call': mazy6, 'w': w, 'h': h, 'Background': bg_black, 'mode': 'gb', 'cnt': 18, 'useblack': True},

        {'name': n, 'call': mazy6, 'w': w, 'h': h, 'Background': bg_black, 'mode': 'happy', 'cnt': 18, 'useblack': True},
        {'name': n, 'call': mazy6, 'w': w, 'h': h, 'Background': bg_black, 'mode': 'happy', 'cnt': 18+12, 'useblack': False},
        {'name': n, 'call': mazy6, 'w': w, 'h': h, 'Background': bg_black, 'mode': 'bwx', 'cnt': 18+12, 'useblack': False},
        {'name': n, 'call': mazy6, 'w': w, 'h': h, 'Background': bg_black, 'mode': 'psych', 'cnt': 18+12, 'useblack': False},
    ]

def predef_mazy7(w, h):
    n = 'SMEARS#7'
    bk = (0x84, 0x8B, 0x9B)
    return [
        {'name': n, 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 500,  'cmode': 'rnd', 'mode': 'const'},
        {'name': n, 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 2000, 'cmode': 'rnd', 'mode': 'const'},
        {'name': n, 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 200,  'cmode': 'std', 'mode': 'decp'},
        {'name': n, 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 100,  'cmode': 'std', 'mode': 'decp'},
        {'name': n, 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 50,   'cmode': 'std', 'mode': 'decp'},
        {'name': n, 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 10,   'cmode': 'std', 'mode': 'decp'},
        {'name': n, 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 200,  'cmode': 'std', 'mode': 'dec'},
        {'name': n, 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 100,  'cmode': 'std', 'mode': 'dec'},
        {'name': n, 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 50,   'cmode': 'std', 'mode': 'dec'},
        {'name': n, 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 10,   'cmode': 'std', 'mode': 'dec'},
        {'name': n, 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 200,  'cmode': 'inv', 'mode': 'dec'},
        {'name': n, 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 100,  'cmode': 'inv', 'mode': 'dec'},
        {'name': n, 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 50,   'cmode': 'inv', 'mode': 'dec'},
        {'name': n, 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 10,   'cmode': 'inv', 'mode': 'dec'},
        {'name': n, 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 200,  'cmode': 'rnd', 'mode': 'dec'},
        {'name': n, 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 100,  'cmode': 'rnd', 'mode': 'dec'},
        {'name': n, 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 50,   'cmode': 'rnd', 'mode': 'dec'},
        {'name': n, 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 10,   'cmode': 'rnd', 'mode': 'dec'},

        {'name': n, 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 200,  'cmode': 'color', 'mode': 'dec'},
        {'name': n, 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 100,  'cmode': 'color', 'mode': 'dec'},
        {'name': n, 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 50,   'cmode': 'color', 'mode': 'dec'},
        {'name': n, 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 10,   'cmode': 'color', 'mode': 'dec'},

        {'name': n, 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 200,  'cmode': 'color', 'mode': 'dec', 'addalpha': 99},
        {'name': n, 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 100,  'cmode': 'color', 'mode': 'dec', 'addalpha': 99},
        {'name': n, 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 50,   'cmode': 'color', 'mode': 'dec', 'addalpha': 99},
        {'name': n, 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 10,   'cmode': 'color', 'mode': 'dec', 'addalpha': 99},

        {'name': n, 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 200,  'cmode': 'wryb', 'mode': 'dec'},
        {'name': n, 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 100,  'cmode': 'wryb', 'mode': 'dec'},
        {'name': n, 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 50,   'cmode': 'wryb', 'mode': 'dec'},
        {'name': n, 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 10,   'cmode': 'wryb', 'mode': 'dec'},

        {'name': n, 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 200,  'cmode': 'wryb', 'mode': 'dec', 'addalpha': 99},
        {'name': n, 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 100,  'cmode': 'wryb', 'mode': 'dec', 'addalpha': 99},
        {'name': n, 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 50,   'cmode': 'wryb', 'mode': 'dec', 'addalpha': 99},
        {'name': n, 'call': mazy7, 'w': w, 'h': h, 'Background': bk, 'cnt': 10,   'cmode': 'wryb', 'mode': 'dec', 'addalpha': 99},
    ]

def predef_mazy8(w, h):
    n = 'SMEARS#8'
    return [
        {'name': n, 'call': mazy8, 'w': w, 'h': h, 'Background': bg_white, 'mode': '', 'xcnt': 5, 'ycnt': 5},
        {'name': n, 'call': mazy8, 'w': w, 'h': h, 'Background': bg_white, 'mode': '', 'xcnt': 5, 'ycnt': 10},
        {'name': n, 'call': mazy8, 'w': w, 'h': h, 'Background': bg_white, 'mode': '', 'xcnt': 5, 'ycnt': 3},
        {'name': n, 'call': mazy8, 'w': w, 'h': h, 'Background': bg_white, 'mode': '', 'xcnt': 15, 'ycnt': 5}
    ]

def predef_mazy9(w, h):
    n = 'SMEARS#9'
    v = float(h)/8
    v2 = float(h)/2
    v3 = float(h)/32
    return [
        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 16, 'Background': bg_black, 'color': 'happy', 'v': 0, 'rndc': True},
        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 20, 'Background': bg_black, 'color': 'happy', 'v': 0, 'rndc': True},
        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 60, 'Background': bg_black, 'color': 'happy', 'v': 0, 'rndc': True},
        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 128, 'Background': bg_black, 'color': 'happy', 'v': 0, 'rndc': True},
        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 16, 'Background': bg_black, 'color': 'psych', 'v': 0, 'rndc': True},
        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 20, 'Background': bg_black, 'color': 'psych', 'v': 0, 'rndc': True},
        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 60, 'Background': bg_black, 'color': 'psych', 'v': 0, 'rndc': True},
        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 128, 'Background': bg_black, 'color': 'psych', 'v': 0, 'rndc': True},

        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 16, 'Background': bg_black, 'color': 'happy', 'v': 0},
        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 20, 'Background': bg_black, 'color': 'happy', 'v': 0},
        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 64, 'Background': bg_black, 'color': 'happy', 'v': 0},
        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 128, 'Background': bg_black, 'color': 'happy', 'v': 0},
        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 16, 'Background': bg_black, 'color': 'psych', 'v': 0},
        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 20, 'Background': bg_black, 'color': 'psych', 'v': 0},
        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 64, 'Background': bg_black, 'color': 'psych', 'v': 0},
        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 128, 'Background': bg_black, 'color': 'psych', 'v': 0},
           
        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 16, 'Background': bg_black, 'color': 'red', 'v': 0},
        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 64, 'Background': bg_black, 'color': 'red', 'v': 0},
        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 128, 'Background': bg_black, 'color': 'red', 'v': 0},
        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 16, 'Background': bg_black, 'color': 'rg', 'v': 0},
        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 64, 'Background': bg_black, 'color': 'rg', 'v': 0},
        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 128, 'Background': bg_black, 'color': 'rg', 'v': 0},
        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 16, 'Background': bg_black, 'color': 'bw', 'v': 0},
        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 64, 'Background': bg_black, 'color': 'bw', 'v': 0},
        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 128, 'Background': bg_black, 'color': 'bw', 'v': 0},

        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 20, 'Background': bg_black, 'color': 'happy', 'v': v, 'rndc': True},
        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 60, 'Background': bg_black, 'color': 'happy', 'v': v, 'rndc': True},
        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 120, 'Background': bg_black, 'color': 'happy', 'v': v, 'rndc': True},
        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 20, 'Background': bg_black, 'color': 'psych', 'v': v, 'rndc': True},
        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 60, 'Background': bg_black, 'color': 'psych', 'v': v, 'rndc': True},
        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 120, 'Background': bg_black, 'color': 'psych', 'v': v, 'rndc': True},

        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 20, 'Background': bg_black, 'color': 'happy', 'v': v},
        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 60, 'Background': bg_black, 'color': 'happy', 'v': v},
        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 120, 'Background': bg_black, 'color': 'happy', 'v': v},
        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 20, 'Background': bg_black, 'color': 'psych', 'v': v},
        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 60, 'Background': bg_black, 'color': 'psych', 'v': v},
        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 120, 'Background': bg_black, 'color': 'psych', 'v': v},

        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 20, 'Background': bg_black, 'color': 'red', 'v': v},
        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 60, 'Background': bg_black, 'color': 'red', 'v': v},
        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 120, 'Background': bg_black, 'color': 'red', 'v': v},
        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 20, 'Background': bg_black, 'color': 'rg', 'v': v},
        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 60, 'Background': bg_black, 'color': 'rg', 'v': v},
        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 120, 'Background': bg_black, 'color': 'rg', 'v': v},
        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 20, 'Background': bg_black, 'color': 'bw', 'v': v},
        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 60, 'Background': bg_black, 'color': 'bw', 'v': v},
        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 120, 'Background': bg_black, 'color': 'bw', 'v': v},

        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 20, 'Background': bg_black, 'color': 'happy', 'v': v2, 'rndc': True},
        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 60, 'Background': bg_black, 'color': 'happy', 'v': v2, 'rndc': True},
        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 120, 'Background': bg_black, 'color': 'happy', 'v': v2, 'rndc': True},
        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 20, 'Background': bg_black, 'color': 'psych', 'v': v2, 'rndc': True},
        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 60, 'Background': bg_black, 'color': 'psych', 'v': v2, 'rndc': True},
        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 120, 'Background': bg_black, 'color': 'psych', 'v': v2, 'rndc': True},

        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 20, 'Background': bg_black, 'color': 'happy', 'v': v3, 'rndc': True},
        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 60, 'Background': bg_black, 'color': 'happy', 'v': v3, 'rndc': True},
        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 120, 'Background': bg_black, 'color': 'happy', 'v': v3, 'rndc': True},
        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 20, 'Background': bg_black, 'color': 'psych', 'v': v3, 'rndc': True},
        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 60, 'Background': bg_black, 'color': 'psych', 'v': v3, 'rndc': True},
        {'name': n, 'call': mazy9, 'w': w, 'h': h, 'n': 120, 'Background': bg_black, 'color': 'psych', 'v': v3, 'rndc': True},
    ]

def predef_mazy10(w, h):
    n = 'SMEARS#10'
    bk = (0x84, 0x8B, 0x9B)
    return [
            {'name': n, 'call': mazy10, 'w': w, 'h': h, 'Background': bk, 'n': 30, 'penw': 8, 'color': 'happy', 'mode': 'line', 'complexity': 70, 'open': False},
            {'name': n, 'call': mazy10, 'w': w, 'h': h, 'Background': bk, 'n': 40, 'penw': 8, 'color': 'rg', 'mode': 'line', 'complexity': 70, 'open': False},
            {'name': n, 'call': mazy10, 'w': w, 'h': h, 'Background': bk, 'n': 40, 'penw': 8, 'color': 'red', 'mode': 'line', 'complexity': 70, 'open': False},
            {'name': n, 'call': mazy10, 'w': w, 'h': h, 'Background': bk, 'n': 40, 'penw': 8, 'color': 'wryb', 'mode': 'line', 'complexity': 70, 'open': False},

            {'name': n, 'call': mazy10, 'w': w, 'h': h, 'Background': bk, 'n': 30, 'penw': 8, 'color': 'happy', 'mode': 'line', 'complexity': 70, 'open': True},
            {'name': n, 'call': mazy10, 'w': w, 'h': h, 'Background': bk, 'n': 40, 'penw': 8, 'color': 'rg', 'mode': 'line', 'complexity': 70, 'open': True},
            {'name': n, 'call': mazy10, 'w': w, 'h': h, 'Background': bk, 'n': 40, 'penw': 8, 'color': 'red', 'mode': 'line', 'complexity': 70, 'open': True},
            {'name': n, 'call': mazy10, 'w': w, 'h': h, 'Background': bk, 'n': 40, 'penw': 8, 'color': 'wryb', 'mode': 'line', 'complexity': 70, 'open': True},

            {'name': n, 'call': mazy10, 'w': w, 'h': h, 'Background': bk, 'n': 30, 'penw': 8, 'color': 'happy', 'mode': 'line', 'complexity': 70, 'open': True, 'addalpha': 90},
            {'name': n, 'call': mazy10, 'w': w, 'h': h, 'Background': bk, 'n': 40, 'penw': 8, 'color': 'rg', 'mode': 'line', 'complexity': 70, 'open': True, 'addalpha': 90},
            {'name': n, 'call': mazy10, 'w': w, 'h': h, 'Background': bk, 'n': 40, 'penw': 8, 'color': 'red', 'mode': 'line', 'complexity': 70, 'open': True, 'addalpha': 90},
            {'name': n, 'call': mazy10, 'w': w, 'h': h, 'Background': bk, 'n': 40, 'penw': 8, 'color': 'wryb', 'mode': 'line', 'complexity': 70, 'open': True, 'addalpha': 90},
# TODO: more wryb
            {'name': n, 'call': mazy10, 'w': w, 'h': h, 'Background': bg_white, 'n': 6, 'penw': 1, 'color': 'happy', 'mode': 'fill', 'complexity': 40, 'open': False},
            {'name': n, 'call': mazy10, 'w': w, 'h': h, 'Background': bg_white, 'n': 6, 'penw': 1, 'color': 'happy', 'mode': 'fill', 'complexity': 40, 'open': True},

            {'name': n, 'call': mazy10, 'w': w, 'h': h, 'Background': bg_white, 'n': 6, 'penw': 1, 'color': 'happy', 'mode': 'fill', 'complexity': 40, 'open': False, 'addalpha': 80},
            {'name': n, 'call': mazy10, 'w': w, 'h': h, 'Background': bg_white, 'n': 6, 'penw': 1, 'color': 'happy', 'mode': 'fill', 'complexity': 40, 'open': True, 'addalpha': 80},

            {'name': n, 'call': mazy10, 'w': w, 'h': h, 'Background': bg_white, 'n': 24, 'penw': 1, 'color': 'happy', 'mode': 'fill', 'complexity': 40, 'open': False},
            {'name': n, 'call': mazy10, 'w': w, 'h': h, 'Background': bg_white, 'n': 24, 'penw': 1, 'color': 'happy', 'mode': 'fill', 'complexity': 40, 'open': True},

            {'name': n, 'call': mazy10, 'w': w, 'h': h, 'Background': bg_white, 'n': 24, 'penw': 1, 'color': 'happy', 'mode': 'fill', 'complexity': 40, 'open': False, 'addalpha': 80},
            {'name': n, 'call': mazy10, 'w': w, 'h': h, 'Background': bg_white, 'n': 24, 'penw': 1, 'color': 'happy', 'mode': 'fill', 'complexity': 40, 'open': True, 'addalpha': 80},
    ]

def predef_mazy11(w, h):
    n = 'SMEARS#11'
    return [
        {'name': n, 'call': mazy11, 'w': w, 'h': h, 'Background': bg_black, 'n': 8},
        {'name': n, 'call': mazy11, 'w': w, 'h': h, 'Background': bg_black, 'n': 16},
        {'name': n, 'call': mazy11, 'w': w, 'h': h, 'Background': bg_black, 'n': 64}
    ]

def predef_mazy12(w, h):
    n = 'SMEARS#12'
    return [
        {'name': n, 'call': mazy12, 'w': w, 'h': h, 'Background': bg_white, 'n': 24, 'color': None, 'o': 'box', 'v': False},
        {'name': n, 'call': mazy12, 'w': w, 'h': h, 'Background': bg_white, 'n': 48, 'color': None, 'o': 'box', 'v': False},
        {'name': n, 'call': mazy12, 'w': w, 'h': h, 'Background': bg_white, 'n': 96, 'color': None, 'o': 'box', 'v': False},
        {'name': n, 'call': mazy12, 'w': w, 'h': h, 'Background': bg_white, 'n': 24, 'color': None, 'o': 'cir', 'v': False},
        {'name': n, 'call': mazy12, 'w': w, 'h': h, 'Background': bg_white, 'n': 48, 'color': None, 'o': 'cir', 'v': False},
        {'name': n, 'call': mazy12, 'w': w, 'h': h, 'Background': bg_white, 'n': 96, 'color': None, 'o': 'cir', 'v': False},

        {'name': n, 'call': mazy12, 'w': w, 'h': h, 'Background': bg_white, 'n': 48, 'color': 'happy', 'o': 'box', 'v': False},
        {'name': n, 'call': mazy12, 'w': w, 'h': h, 'Background': bg_white, 'n': 48, 'color': 'happy', 'o': 'cir', 'v': False},

        {'name': n, 'call': mazy12, 'w': w, 'h': h, 'Background': bg_white, 'n': 24, 'color': None, 'o': 'box', 'v': True},
        {'name': n, 'call': mazy12, 'w': w, 'h': h, 'Background': bg_white, 'n': 48, 'color': None, 'o': 'box', 'v': True},
        {'name': n, 'call': mazy12, 'w': w, 'h': h, 'Background': bg_white, 'n': 96, 'color': None, 'o': 'box', 'v': True},
        {'name': n, 'call': mazy12, 'w': w, 'h': h, 'Background': bg_white, 'n': 24, 'color': None, 'o': 'cir', 'v': True},
        {'name': n, 'call': mazy12, 'w': w, 'h': h, 'Background': bg_white, 'n': 48, 'color': None, 'o': 'cir', 'v': True},
        {'name': n, 'call': mazy12, 'w': w, 'h': h, 'Background': bg_white, 'n': 96, 'color': None, 'o': 'cir', 'v': True},

        {'name': n, 'call': mazy12, 'w': w, 'h': h, 'Background': bg_white, 'n': 48, 'color': 'happy', 'o': 'box', 'v': True},
        {'name': n, 'call': mazy12, 'w': w, 'h': h, 'Background': bg_white, 'n': 48, 'color': 'happy', 'o': 'cir', 'v': True},
    ]

def predef_mazy13(w, h):
    n = 'SMEARS#13'
    return [
        {'name': n, 'call': mazy13, 'w': w, 'h': h, 'Background': bg_black, 'n': 64, 'color': (255, 255, 255)},
        {'name': n, 'call': mazy13, 'w': w, 'h': h, 'Background': bg_black, 'n': 128, 'color': (255, 255, 255)},
        {'name': n, 'call': mazy13, 'w': w, 'h': h, 'Background': bg_white, 'n': 64, 'color': (224, 0, 0)},
        {'name': n, 'call': mazy13, 'w': w, 'h': h, 'Background': bg_white, 'n': 128, 'color': (224, 0, 0)},
    ]

def predef_mazy14(w, h):
    n = 'SMEARS#14'
    return [
        {'name': n, 'call': mazy14, 'w': w, 'h': h, 'Background': bg_white, 'n': 12, 'color': bg_black},
        {'name': n, 'call': mazy14, 'w': w, 'h': h, 'Background': bg_white, 'n': 24, 'color': bg_black},
        {'name': n, 'call': mazy14, 'w': w, 'h': h, 'Background': bg_white, 'n': 36, 'color': bg_black},
        {'name': n, 'call': mazy14, 'w': w, 'h': h, 'Background': bg_white, 'n': 48, 'color': bg_black},
    ]

def predef_mazy15(w, h):
    n = 'SMEARS#15'
    a = [# note: color seems lame ... but try with other tran yet
        {'name': n, 'call': mazy15, 'w': w, 'h': h, 'Background': bg_white, 'n': 16, 'color': bg_black, 'style': 'circle', 'tran': 'difference'},
        {'name': n, 'call': mazy15, 'w': w, 'h': h, 'Background': bg_white, 'n': 32, 'color': bg_black, 'style': 'circle', 'tran': 'difference'},
        {'name': n, 'call': mazy15, 'w': w, 'h': h, 'Background': bg_white, 'n': 64, 'color': bg_black, 'style': 'circle', 'tran': 'difference'},
        {'name': n, 'call': mazy15, 'w': w, 'h': h, 'Background': bg_white, 'n': 128, 'color': bg_black, 'style': 'circle', 'tran': 'difference'},

        {'name': n, 'call': mazy15, 'w': w, 'h': h, 'Background': bg_white, 'n': 16, 'color': bg_black, 'style': 'rect', 'tran': 'difference'},
        {'name': n, 'call': mazy15, 'w': w, 'h': h, 'Background': bg_white, 'n': 32, 'color': bg_black, 'style': 'rect', 'tran': 'difference'},
        {'name': n, 'call': mazy15, 'w': w, 'h': h, 'Background': bg_white, 'n': 64, 'color': bg_black, 'style': 'rect', 'tran': 'difference'},
        {'name': n, 'call': mazy15, 'w': w, 'h': h, 'Background': bg_white, 'n': 128, 'color': bg_black, 'style': 'rect', 'tran': 'difference'},
    ]
    a1 = copy.deepcopy(a)
    a2 = copy.deepcopy(a)
    a3 = copy.deepcopy(a)
    a4 = copy.deepcopy(a)
    a5 = copy.deepcopy(a)
    a6 = copy.deepcopy(a)
    a7 = copy.deepcopy(a)
    a8 = copy.deepcopy(a)
    a9 = copy.deepcopy(a)
    a10 = copy.deepcopy(a)
    a11 = copy.deepcopy(a)
    a12 = copy.deepcopy(a)
    a13 = copy.deepcopy(a)
    a14 = copy.deepcopy(a)
    for i in range(len(a)):
        a1[i]['xs2'] = int(w/5) # cool for n=16
        a1[i]['ys2'] = int(w/100)
        a2[i]['xs2'] = int(w/50)
        a2[i]['ys2'] = int(w/100)
        a3[i]['xs2'] = int(w/100)
        a3[i]['ys2'] = int(w/100)
        a4[i]['mode'] = 'rnd'
        a4[i]['xs2v'] = int(w/5)
        a4[i]['ys2v'] = int(w/5)
        a5[i]['mode'] = 'rnd'
        a5[i]['xs2v'] = 20
        a5[i]['ys2v'] = 20
        a6[i]['mode'] = 'rnd'
        a6[i]['xs2v'] = int(w/50)
        a6[i]['ys2v'] = int(w/50)
        a7[i]['mode'] = 'linear'
        a7[i]['xs2v'] = int(w/5)
        a7[i]['ys2v'] = 1
        a8[i]['mode'] = 'linear'
        a8[i]['xs2v'] = int(w/5)
        a8[i]['ys2v'] = int(w/5)
        a9[i]['mode'] = 'linear'
        a9[i]['xs2v'] = int(w/25)
        a9[i]['ys2v'] = 1
        a10[i]['mode'] = 'linear'
        a10[i]['xs2v'] = int(w/50)
        a10[i]['ys2v'] = 1
        a11[i]['mode'] = 'circle'
        a11[i]['xs2v'] = int(w/50)
        a11[i]['ys2v'] = int(w/50)
        a12[i]['mode'] = 'circle'
        a12[i]['xs2v'] = int(w/25)
        a12[i]['ys2v'] = int(w/25)
        a13[i]['mode'] = 'circle'
        a13[i]['xs2v'] = int(w/10)
        a13[i]['ys2v'] = int(w/10)
        a14[i]['mode'] = 'circle'
        a14[i]['xs2v'] = int(w/5)
        a14[i]['ys2v'] = int(w/5)
    a = np.concatenate((a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14), axis=0)
    a1 = copy.deepcopy(a)
    a2 = copy.deepcopy(a)
    a3 = copy.deepcopy(a)
    for i in range(len(a)):
        #note: unused now: 'darker' 'lighter' 'multiply'
        a1[i]['tran'] = 'difference' #note: dflt
        a2[i]['tran'] = 'blend'
        a3[i]['tran'] = 'subtract'
    return np.concatenate((a1, a2, a3), axis=0)

def predef_mazy16(w, h):
    n = 'SMEARS#16'
    a = [
        {'name': n, 'call': mazy16, 'w': w, 'h': h, 'Background': bg_white, 'n': 12, 'color': bg_black, 'rcoef': 1.0, 'acoef': 1.0, 'rscale': 1.0},
        {'name': n, 'call': mazy16, 'w': w, 'h': h, 'Background': bg_white, 'n': 24, 'color': bg_black, 'rcoef': 1.0, 'acoef': 1.0, 'rscale': 1.0},
        {'name': n, 'call': mazy16, 'w': w, 'h': h, 'Background': bg_white, 'n': 48, 'color': bg_black, 'rcoef': 1.0, 'acoef': 1.0, 'rscale': 1.0},
        {'name': n, 'call': mazy16, 'w': w, 'h': h, 'Background': bg_white, 'n': 96, 'color': bg_black, 'rcoef': 1.0, 'acoef': 1.0, 'rscale': 1.0},
    ]
    a1 = copy.deepcopy(a)
    a2 = copy.deepcopy(a)
    a3 = copy.deepcopy(a)
    for i in range(len(a)):
        a1[i]['rcoef'] = 1.0 #note: dflt
        a2[i]['rcoef'] = 1.1
        a3[i]['rcoef'] = 1.5
    a = np.concatenate((a1, a2, a3), axis=0)
    a1 = copy.deepcopy(a)
    a2 = copy.deepcopy(a)
    a3 = copy.deepcopy(a)
    for i in range(len(a)):
        a1[i]['acoef'] = 1.0 #note: dflt
        a2[i]['acoef'] = 1.5
        a3[i]['acoef'] = 2.0
    a = np.concatenate((a1, a2, a3), axis=0)
    a1 = copy.deepcopy(a)
    a2 = copy.deepcopy(a)
    a3 = copy.deepcopy(a)
    a4 = copy.deepcopy(a)
    for i in range(len(a)):
        a1[i]['rscale'] = 1.0 #note: dflt
        a2[i]['rscale'] = 0.33
        a3[i]['rscale'] = 1.5
        a4[i]['rscale'] = 2.0
    a = np.concatenate((a1, a2, a3, a4), axis=0)
    return a

#def predef_mazy17(w, h):
#def predef_mazy18(w, h):
#def predef_mazy19(w, h):
#def predef_mazy20(w, h):


def enum_defs():
    print('1:', len(predef_mazy1(0, 0)))
    print('2:', len(predef_mazy2(0, 0)))
    print('3:', len(predef_mazy3(0, 0)))
    print('4:', len(predef_mazy4(0, 0)))
    print('5:', len(predef_mazy5(0, 0)))
    print('6:', len(predef_mazy6(0, 0)))
    print('7:', len(predef_mazy7(0, 0)))
    print('8:', len(predef_mazy8(0, 0)))
    print('9:', len(predef_mazy9(0, 0)))
    print('10:', len(predef_mazy10(0, 0)))
    print('11:', len(predef_mazy11(0, 0)))
    print('12:', len(predef_mazy12(0, 0)))
    print('13:', len(predef_mazy13(0, 0)))
    print('14:', len(predef_mazy14(0, 0)))
    print('15:', len(predef_mazy15(0, 0)))
    print('16:', len(predef_mazy16(0, 0)))
    #print('17:', len(predef_mazy17(0, 0)))
    #print('18:', len(predef_mazy18(0, 0)))
    #print('19:', len(predef_mazy19(0, 0)))
    #print('20:', len(predef_mazy20(0, 0)))

# EOF
