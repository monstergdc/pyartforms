#! /usr/bin/env python
# -*- coding: utf-8 -*-

# PyArtForms - Python generative art forms paint algorithms (artificial artist), v1.0
# (c)2017-2024 Noniewicz.com, Jakub Noniewicz aka MoNsTeR/GDC
# predefined forms
"""
cre: 20181020
upd: 20190105, 06, 13, 18, 21, 22
upd: 20190311, 30
upd: 20190414, 15, 17, 18, 21, 22, 24, 26, 27
upd: 20200507, 10
upd: 20210106
upd: 20210515, 16, 22, 23, 24, 26, 27
upd: 20210606, 07, 10, 11, 12, 13, 18, 19, 20
upd: 20240224, 25
upd: 20240304
upd: 20240512
"""

# TODO:
# - add alpha ver for all
# - cleanup/compact

import copy
from collections import OrderedDict
from drawtools import get_canvas, art_painter
from life1 import life
from lissajous import lissajous, lissajous_loop
from astroart import *
from mandelbrot import generate_mandelbrot
from smears import *
from pyart_defs import *
from color_defs import *


# --- common color defs

bg_black = (0, 0, 0)
bg_gray = (192, 192, 192)
bg_white = (255, 255, 255)
bg_yellow = (255, 255, 0)
bg_orange = (255, 128, 0)

# --- local tools

def append_dct_item(a, name, value):
    for i in range(len(a)):
        a[i][name] = value
    return a

def append_dflts(a, name, call, w, h):
    a = append_dct_item(a, 'name', name)
    a = append_dct_item(a, 'call', call)
    a = append_dct_item(a, 'w', w)
    a = append_dct_item(a, 'h', h)
    return a

def mux_param(a, name, values):
    b = copy.deepcopy(a)
    a = []
    for p in values:
        a1 = copy.deepcopy(b)
        for i in range(len(a1)):
            a1[i][name] = p
        a = np.concatenate((a, a1), axis=0)
    return a


# --- life

def predef_life(w, h):
    a = [
        {'Background': bg_black, 'Color': bg_white},
    ]
    a = mux_param(a, 'f', ['f2a', 'f2b', 'f2c', 'f2d', 'f2e', 'f2f', 'f2g'])
    return append_dflts(a, 'LIFE', life, w, h)

# --- lissajous

def predef_lissajous(w, h):
    lw = int(w/496)
    if lw < 1:
        lw = 1
    a = [
        {'Background': bg_black, 'LineColor': (255,255,255), 'LineWidth': lw, 'FF1': 19.0, 'FF2': 31.0, 'FFi': 0, 'dT': 1, 'Steps': 2000, 'Scale': 0.9},
        {'Background': bg_black, 'LineColor': (50,255,50), 'LineWidth': lw, 'FF1': 3.0, 'FF2': 4.0, 'FFi': 0, 'dT': 1, 'Steps': 2000, 'Scale': 0.9},
        {'Background': bg_black, 'LineColor': (50,255,50), 'LineWidth': lw, 'FF1': 2.0, 'FF2': 3.0, 'FFi': 0, 'dT': 1, 'Steps': 2000, 'Scale': 0.9},
        {'Background': bg_black, 'LineColor': (50,255,50), 'LineWidth': lw, 'FF1': 2.0, 'FF2': 2.9, 'FFi': 0, 'dT': 0.5, 'Steps': 15000, 'Scale': 0.9},
    ]
    return append_dflts(a, 'LISSAJOUS', lissajous_loop, w, h)

# --- astro - 2x (cir, box) bluegalaxy ellipticgalaxy spiralgalaxy neutronstar blackhole supernova nebula star

def predef_astro(w, h):
    a = [
        {'call': paint0, 'Background': bg_black, 'ou': bg_black, 'box_or_cir': False},
        {'call': paint0, 'Background': bg_black, 'ou': bg_black, 'box_or_cir': True},
        {'call': paint1, 'Background': bg_black, 'ou': bg_black, 'box_or_cir': False},
        {'call': paint1, 'Background': bg_black, 'ou': bg_black, 'box_or_cir': True},
        {'call': paint2, 'Background': bg_black, 'ou': bg_black, 'box_or_cir': False},
        {'call': paint2, 'Background': bg_black, 'ou': bg_black, 'box_or_cir': True},
        {'call': paint3, 'Background': bg_black, 'ou': bg_black, 'box_or_cir': False},
        {'call': paint3, 'Background': bg_black, 'ou': bg_black, 'box_or_cir': True},
        {'call': paint4, 'Background': bg_black, 'ou': bg_black, 'box_or_cir': False},
        {'call': paint4, 'Background': bg_black, 'ou': bg_black, 'box_or_cir': True},
        {'call': paint5, 'Background': bg_black, 'ou': bg_black, 'box_or_cir': False},
        {'call': paint5, 'Background': bg_black, 'ou': bg_black, 'box_or_cir': True},
        {'call': paint6, 'Background': bg_black, 'ou': bg_black, 'box_or_cir': False},
        {'call': paint6, 'Background': bg_black, 'ou': bg_black, 'box_or_cir': True},
        {'call': paint7, 'Background': bg_black, 'ou': bg_black, 'box_or_cir': False},
        {'call': paint7, 'Background': bg_black, 'ou': bg_black, 'box_or_cir': True},
    ]
    a = append_dct_item(a, 'name', 'ASTROART')
    a = append_dct_item(a, 'w', w)
    a = append_dct_item(a, 'h', h)
    return a

# --- mandelbrot

def predef_mandelbrot(w, h):
    a = [
        {'x0': -2.5, 'x1': 1.0, 'y0': -1.0, 'y1': 1.0, 'maxiter': 20, 'negative': False, 'Background': bg_black, 'bw': True},
        {'x0': -2.5, 'x1': 1.0, 'y0': -1.0, 'y1': 1.0, 'maxiter': 200, 'negative': False, 'Background': bg_black, 'bw': True},
    ]
    return append_dflts(a, 'MANDELBROT', generate_mandelbrot, w, h)

# --- smears

def predef_mazy1(w, h):
    # prefilled
    a = [
        {'Background': bg_white, 'penw': 8, 'v': 20, 'n': 100, 'm': 40, 'prefill': True, 'mode': 'black', 'keep': False, 'color': 'any_rnd'},
        {'Background': bg_white, 'penw': 8, 'v': 20, 'n': 100, 'm': 40, 'prefill': True, 'mode': 'black', 'keep': False, 'color': 'happy'},
        {'Background': bg_white, 'penw': 8, 'v': 20, 'n': 100, 'm': 40, 'prefill': True, 'mode': 'black', 'keep': False, 'color': 'wryb'},
        {'Background': bg_white, 'penw': 8, 'v': 20, 'n': 100, 'm': 40, 'prefill': True, 'mode': 'black', 'keep': False, 'color': 'psych'},
        {'Background': bg_white, 'penw': 8, 'v': 20, 'n': 100, 'm': 40, 'prefill': True, 'mode': 'black', 'keep': False, 'color': 'BeachTowels'},
        {'Background': bg_white, 'penw': 8, 'v': 20, 'n': 100, 'm': 40, 'prefill': True, 'mode': 'black', 'keep': False, 'color': 'MoonlightBytes6'},
        {'Background': bg_white, 'penw': 8, 'v': 20, 'n': 100, 'm': 40, 'prefill': True, 'mode': 'black', 'keep': False, 'color': 'Number3'},
        {'Background': bg_white, 'penw': 8, 'v': 20, 'n': 100, 'm': 40, 'prefill': True, 'mode': 'black', 'keep': False, 'color': 'RainbowDash'},
        {'Background': bg_white, 'penw': 8, 'v': 20, 'n': 100, 'm': 40, 'prefill': True, 'mode': 'black', 'keep': False, 'color': 'Google'},
        {'Background': bg_white, 'penw': 8, 'v': 20, 'n': 100, 'm': 40, 'prefill': True, 'mode': 'black', 'keep': False, 'color': 'MetroUI'},
        {'Background': bg_white, 'penw': 8, 'v': 20, 'n': 100, 'm': 40, 'prefill': True, 'mode': 'black', 'keep': False, 'color': 'ProgramCat'},
        {'Background': bg_white, 'penw': 8, 'v': 20, 'n': 100, 'm': 40, 'prefill': True, 'mode': 'black', 'keep': False, 'color': 'rg'},
        {'Background': bg_yellow, 'penw': 5, 'v': 120, 'n': 48, 'm': 12, 'prefill': True, 'mode': 'red', 'keep': True, 'color': 'blue_rnd'},
        {'Background': bg_white, 'penw': 8, 'v': 30, 'n': 100, 'm': 40, 'prefill': True, 'mode': 'red', 'keep': False, 'color': 'green_rnd'},

        {'Background': bg_white, 'penw': 8, 'v': 30, 'n': 100, 'm': 40, 'prefill': True, 'mode': 'black', 'keep': False, 'color': 'colors_ZXC1'},

        # new test, quite ok, use proper
#        {'Background': bg_white, 'penw': 8, 'v': 20, 'n': 300, 'm': 4, 'prefill': True, 'mode': 'black', 'keep': False, 'color': 'happy', 'addalpha': 75, 'mar': int(w/10)},
#        {'Background': bg_white, 'penw': 8, 'v': 20, 'n': 300, 'm': 4, 'prefill': True, 'mode': 'black', 'keep': False, 'color': 'happy', 'addalpha': 75, 'mar': int(-w/2)},
#        {'Background': bg_white, 'penw': 8, 'v': 20, 'n': 50, 'm': 4, 'prefill': True, 'mode': 'black', 'keep': False, 'color': 'happy', 'addalpha': 75},
#        {'Background': bg_white, 'penw': 4, 'v': 20, 'n': 20, 'm': 4, 'prefill': True, 'mode': 'black', 'keep': False, 'color': 'happy', 'addalpha': 75},
#        {'Background': bg_white, 'penw': 4, 'v': 20, 'n': 20, 'm': 4, 'prefill': True, 'mode': 'black', 'keep': False, 'color': 'happy', 'addalpha': 75, 'mar': int(-w/2)},
#        {'Background': bg_white, 'penw': 8, 'v': 20, 'n': 20, 'm': 40, 'prefill': True, 'mode': 'black', 'keep': False, 'color': 'happy', 'addalpha': 75, 'mar': int(-w/2)},
    ]

    # unfilled (aka open)
    b = [
        #6 red (fix? mar?)
        {'Background': bg_white, 'penw': 8, 'v': 75, 'n': 100, 'm': 40, 'prefill': False, 'mode': 'red', 'keep': False, 'color': 'red_rnd'},

        # 6 red tests new, ok, use
        {'Background': bg_white, 'penw': 8, 'v': 25, 'n': 100, 'm': 40, 'prefill': False, 'mode': 'red', 'keep': False, 'color': 'red_rnd', 'mar': int(w/15)},
        {'Background': bg_white, 'penw': 2, 'v': 120, 'n': 40, 'm': 120, 'prefill': False, 'mode': 'red', 'keep': False, 'color': 'red_rnd', 'mar': int(w/15)},
        {'Background': bg_white, 'penw': 8, 'v': 120, 'n': 40, 'm': 120, 'prefill': False, 'mode': 'red', 'keep': False, 'color': 'red_rnd', 'mar': int(w/15)},
        {'Background': bg_white, 'penw': 24, 'v': 120, 'n': 40, 'm': 60, 'prefill': False, 'mode': 'red', 'keep': False, 'color': 'red_rnd', 'mar': int(w/15)},
        {'Background': bg_white, 'penw': 8, 'v': 20, 'n': 500, 'm': 5, 'prefill': False, 'mode': 'red', 'keep': False, 'color': 'red_rnd', 'mar': int(w/15)},

        #?
        {'Background': bg_white, 'penw': 8, 'v': 75, 'n': 100, 'm': 40, 'prefill': False, 'mode': 'happy', 'keep': False},
        {'Background': bg_white, 'penw': 8, 'v': 75, 'n': 100, 'm': 40, 'prefill': False, 'mode': 'wryb', 'keep': False},

        {'Background': bg_white, 'penw': 8, 'v': 75, 'n': 100, 'm': 40, 'prefill': False, 'mode': 'happy', 'keep': False, 'addblack': True},
        {'Background': bg_white, 'penw': 8, 'v': 75, 'n': 100, 'm': 40, 'prefill': False, 'mode': 'wryb', 'keep': False, 'addblack': True},

        {'Background': bg_white, 'penw': 8, 'v': 75, 'n': 100, 'm': 40, 'prefill': False, 'mode': 'BeachTowels', 'keep': False},
        {'Background': bg_white, 'penw': 8, 'v': 75, 'n': 100, 'm': 40, 'prefill': False, 'mode': 'MoonlightBytes6', 'keep': False},
        {'Background': bg_white, 'penw': 8, 'v': 75, 'n': 100, 'm': 40, 'prefill': False, 'mode': 'Number3', 'keep': False},
        {'Background': bg_white, 'penw': 8, 'v': 75, 'n': 100, 'm': 40, 'prefill': False, 'mode': 'RainbowDash', 'keep': False},
        {'Background': bg_white, 'penw': 8, 'v': 75, 'n': 100, 'm': 40, 'prefill': False, 'mode': 'Google', 'keep': False},
        {'Background': bg_white, 'penw': 8, 'v': 75, 'n': 100, 'm': 40, 'prefill': False, 'mode': 'MetroUI', 'keep': False},
        {'Background': bg_white, 'penw': 8, 'v': 75, 'n': 100, 'm': 40, 'prefill': False, 'mode': 'ProgramCat', 'keep': False},
    ]

    # * addalpha
    a1 = copy.deepcopy(a)
    a2 = copy.deepcopy(a)
    a3 = copy.deepcopy(a)
    for i in range(len(a)):
        #a1 - orig, no alpha
        a2[i]['addalpha'] = 75
        a3[i]['addalpha'] = 50
    a = np.concatenate((a1, a2, a3), axis=0)
    # todo: ?
    #a = mux_param(a, 'addalpha', [0, 50, 75]) # todo: 75++ ?

    # * variation
    a1 = copy.deepcopy(a)
    a2 = copy.deepcopy(a)
    a3 = copy.deepcopy(a)
    for i in range(len(a)):
        #a1 - orig, no change
        a2[i]['v'] = 500 # 'v': 500, 'n': 10, 'm': 4, ...
        a2[i]['n'] = 10
        a2[i]['m'] = 4
        a3[i]['v'] = 50 # 'v': 100, 'n': 20, 'm': 4, ...
        a3[i]['n'] = 20
        a3[i]['m'] = 4
    a = np.concatenate((a1, a2, a3), axis=0)

    a = np.concatenate((a, b), axis=0)
    return append_dflts(a, 'SMEARS#1', mazy1, w, h)

def predef_mazy2(w, h):
    a = [
        {'Background': bg_black, 'n': 100},
    ]
    a = mux_param(a, 'color', [ 'bwx', 'red_rnd', 'any_rnd', 'happy', 'wryb', 'Number3', 'BeachTowels', 'ProgramCat', 'BrGrRd'])
    a = mux_param(a, 'm', [12, 30, 180])
    a = mux_param(a, 'sc', [20, 50, 100]) # todo: also 0 ?
    a = mux_param(a, 'addalpha', [0, 120])
    return append_dflts(a, 'SMEARS#2', mazy2, w, h)

def predef_mazy3(w, h):
    a = [
        {'Background': bg_white, 'color': 'happy'},
        {'Background': bg_white, 'color': 'wryb'},
        {'Background': bg_white, 'color': 'BeachTowels'},
        {'Background': bg_white, 'color': 'Number3'},
        {'Background': bg_black, 'color': 'red'},
        {'Background': bg_black, 'color': 'bw'},
        {'Background': bg_black, 'color': 'BrGrRd'},
    ]
    a = mux_param(a, 'n', [90, 12])
    a = mux_param(a, 'mode', ['center', 'xcenter', 'rnd'])
    a = mux_param(a, 'addalpha', [0, 70])

    b = [{'Background': bg_orange, 'color': 'bwx', 'addalpha': 70}]
    b = mux_param(b, 'mode', ['center', 'xcenter', 'rnd'])
    b = mux_param(b, 'n', [90, 12])
    a = np.append(a, b)

    return append_dflts(a, 'SMEARS#3', mazy3, w, h)

def predef_mazy4(w, h):
    a = [
        {'Background': bg_white, 'n': 1, 'mode': 'center', 'color': 'black_const'},
        {'Background': bg_black, 'n': 8, 'mode': 'center', 'color': 'bw'},
        {'Background': bg_black, 'n': 8, 'mode': 'center', 'color': 'bw', 'sc': 0.4, 'addalpha': 90},
        {'Background': bg_black, 'n': 8, 'mode': '', 'color': 'red'},
        {'Background': bg_black, 'n': 5, 'mode': 'center', 'color': 'red'},

        {'Background': bg_white, 'n': 8, 'mode': 'center', 'color': 'happy'},
        {'Background': bg_white, 'n': 8, 'mode': 'center', 'color': 'wryb'},
        {'Background': bg_white, 'n': 8, 'mode': 'center', 'color': 'BeachTowels'},
        {'Background': bg_white, 'n': 8, 'mode': 'center', 'color': 'MetroUI'},

        {'Background': bg_white, 'n': 5, 'mode': 'center', 'color': 'happy', 'addalpha': 90},
        {'Background': bg_white, 'n': 5, 'mode': 'center', 'color': 'wryb', 'addalpha': 90},
        {'Background': bg_white, 'n': 4, 'mode': 'center', 'color': 'bgo', 'addalpha': 90},
        {'Background': bg_white, 'n': 8, 'mode': 'center', 'color': 'avatar', 'addalpha': 90},
        {'Background': bg_white, 'n': 8, 'mode': 'center', 'color': 'psych', 'addalpha': 90},
        {'Background': bg_white, 'n': 8, 'mode': 'center', 'color': 'BeachTowels', 'addalpha': 90},
        {'Background': bg_white, 'n': 8, 'mode': 'center', 'color': 'MetroUI', 'addalpha': 90},

        {'Background': bg_white, 'n': 20, 'mode': '', 'color': 'happy', 'addalpha': 50},
        {'Background': bg_white, 'n': 20, 'mode': '', 'color': 'wryb', 'addalpha': 50},
        {'Background': bg_white, 'n': 20, 'mode': '', 'color': 'bgo', 'addalpha': 50},
        {'Background': bg_white, 'n': 20, 'mode': '', 'color': 'avatar', 'addalpha': 50},
        {'Background': bg_white, 'n': 20, 'mode': '', 'color': 'psych', 'addalpha': 50},
        {'Background': bg_white, 'n': 20, 'mode': '', 'color': 'BeachTowels', 'addalpha': 50},
        {'Background': bg_white, 'n': 20, 'mode': '', 'color': 'MetroUI', 'addalpha': 50},

        {'Background': bg_yellow, 'n': 4, 'mode': 'center', 'color': 'red', 'addalpha': 110}, # +a ok
        {'Background': bg_yellow, 'n': 4, 'mode': 'center', 'color': 'green', 'addalpha': 110}, # +a ok
        
        {'Background': bg_gray, 'n': 10, 'mode': 'center', 'color': 'happy'},
        {'Background': bg_gray, 'n': 10, 'mode': 'center', 'color': 'wryb'},
        {'Background': bg_gray, 'n': 10, 'mode': 'center', 'color': 'BeachTowels'},

        {'Background': bg_gray, 'n': 10, 'mode': 'center', 'color': 'happy', 'sc': 2.5},
        {'Background': bg_gray, 'n': 10, 'mode': 'center', 'color': 'wryb', 'sc': 2.5},
        {'Background': bg_gray, 'n': 10, 'mode': 'center', 'color': 'BeachTowels', 'sc': 2.5},

        {'Background': bg_gray, 'n': 100, 'mode': 'center', 'color': 'happy', 'addalpha': 80, 'sc': 0.3},
        {'Background': bg_gray, 'n': 100, 'mode': 'center', 'color': 'wryb', 'addalpha': 80, 'sc': 0.3},
        {'Background': bg_gray, 'n': 100, 'mode': 'center', 'color': 'BeachTowels', 'addalpha': 80, 'sc': 0.3},
        {'Background': bg_gray, 'n': 100, 'mode': 'center', 'color': 'MetroUI', 'addalpha': 80, 'sc': 0.3},

        {'Background': bg_gray, 'n': 20, 'mode': 'center', 'color': 'happy', 'addalpha': 130, 'sc': 0.3},
        {'Background': bg_gray, 'n': 20, 'mode': 'center', 'color': 'wryb', 'addalpha': 130, 'sc': 0.3},
        {'Background': bg_gray, 'n': 20, 'mode': 'center', 'color': 'BeachTowels', 'addalpha': 130, 'sc': 0.3},
        {'Background': bg_gray, 'n': 20, 'mode': 'center', 'color': 'MetroUI', 'addalpha': 130, 'sc': 0.3},
    ]
    a = mux_param(a, 'pc', [20, 40, 100])
    return append_dflts(a, 'SMEARS#4', mazy4, w, h)

def predef_mazy5(w, h):
    a = [
        {'Background': bg_black, 'colors': colors_b, 'outline': None},
        {'Background': bg_black, 'colors': colors_p, 'outline': None},
        {'Background': bg_black, 'colors': colors_bw0, 'outline': None},
        {'Background': bg_black, 'colors': colors_bwx, 'outline': None},
        {'Background': bg_black, 'colors': colors_happy, 'outline': None},
        {'Background': bg_black, 'colors': colors_BeachTowels, 'outline': None},
        {'Background': bg_black, 'colors': colors_MetroUI, 'outline': None},
        {'Background': bg_black, 'colors': colors_Number3, 'outline': None},
        {'Background': bg_black, 'colors': colors_RainbowDash, 'outline': None},
        {'Background': bg_black, 'colors': colors_ProgramCat, 'outline': None},
        {'Background': bg_black, 'colors': colors_Rainbow, 'outline': None},
        {'Background': bg_black, 'colors': colors_fwd, 'outline': None},
        {'Background': bg_black, 'colors': colors_happy_nw7, 'outline': None},
    ]
    #a = mux_param(a, 'colors', ['happy', 'BeachTowels', 'ProgramCat', 'Number3', 'red', 'bw'])
    return append_dflts(a, 'SMEARS#5', mazy5, w, h)

def predef_mazy6(w, h):
    n = 18
    a = [
        {'Background': bg_black, 'mode': 'red_const', 'n': n, 'useblack': True},
        {'Background': bg_black, 'mode': 'blue_const', 'n': n, 'useblack': True},
        {'Background': bg_black, 'mode': 'blue', 'n': n, 'useblack': True},
        {'Background': bg_black, 'mode': 'blueMap', 'n': n, 'useblack': True},
        {'Background': bg_black, 'mode': 'white_const', 'n': n, 'useblack': True},
        {'Background': bg_black, 'mode': 'rg', 'n': n, 'useblack': True},
        {'Background': bg_white, 'mode': 'gb', 'n': n, 'useblack': True},

        {'Background': bg_black, 'mode': 'bwx', 'n': 18+12, 'useblack': False},
        {'Background': bg_white, 'mode': 'happy', 'n': 18+12, 'useblack': False},
        {'Background': bg_white, 'mode': 'BeachTowels', 'n': 18+12, 'useblack': False},
        {'Background': bg_white, 'mode': 'MoonlightBytes6', 'n': 18+12, 'useblack': False},
        {'Background': bg_white, 'mode': 'ProgramCat', 'n': 18+12, 'useblack': False},
    ]
    return append_dflts(a, 'SMEARS#6', mazy6, w, h)

def predef_mazy7(w, h):
    bk = (0x84, 0x8B, 0x9B)
    a = [
        {'Background': bk, 'n': 500,  'cmode': 'rnd', 'mode': 'const'},
        {'Background': bk, 'n': 2000, 'cmode': 'rnd', 'mode': 'const'},

        {'Background': bk, 'n': 200,  'cmode': 'std', 'mode': 'decp'},
        {'Background': bk, 'n': 100,  'cmode': 'std', 'mode': 'decp'},
        {'Background': bk, 'n': 50,   'cmode': 'std', 'mode': 'decp'},
        {'Background': bk, 'n': 10,   'cmode': 'std', 'mode': 'decp'},
        {'Background': bk, 'n': 200,  'cmode': 'std', 'mode': 'dec'},
        {'Background': bk, 'n': 100,  'cmode': 'std', 'mode': 'dec'},
        {'Background': bk, 'n': 50,   'cmode': 'std', 'mode': 'dec'},
        {'Background': bk, 'n': 10,   'cmode': 'std', 'mode': 'dec'},
        {'Background': bk, 'n': 200,  'cmode': 'inv', 'mode': 'dec'},
        {'Background': bk, 'n': 100,  'cmode': 'inv', 'mode': 'dec'},
        {'Background': bk, 'n': 50,   'cmode': 'inv', 'mode': 'dec'},
        {'Background': bk, 'n': 10,   'cmode': 'inv', 'mode': 'dec'},
        {'Background': bk, 'n': 200,  'cmode': 'rnd', 'mode': 'dec'},
        {'Background': bk, 'n': 100,  'cmode': 'rnd', 'mode': 'dec'},
        {'Background': bk, 'n': 50,   'cmode': 'rnd', 'mode': 'dec'},
        {'Background': bk, 'n': 10,   'cmode': 'rnd', 'mode': 'dec'},

        {'Background': bk, 'n': 200,  'cmode': 'color', 'mode': 'dec'},
        {'Background': bk, 'n': 100,  'cmode': 'color', 'mode': 'dec'},
        {'Background': bk, 'n': 50,   'cmode': 'color', 'mode': 'dec'},
        {'Background': bk, 'n': 10,   'cmode': 'color', 'mode': 'dec'},

        {'Background': bk, 'n': 200,  'cmode': 'color', 'mode': 'dec', 'addalpha': 99},
        {'Background': bk, 'n': 100,  'cmode': 'color', 'mode': 'dec', 'addalpha': 99},
        {'Background': bk, 'n': 50,   'cmode': 'color', 'mode': 'dec', 'addalpha': 99},
        {'Background': bk, 'n': 10,   'cmode': 'color', 'mode': 'dec', 'addalpha': 99},

        {'Background': bk, 'n': 200,  'cmode': 'wryb', 'mode': 'dec'},
        {'Background': bk, 'n': 100,  'cmode': 'wryb', 'mode': 'dec'},
        {'Background': bk, 'n': 50,   'cmode': 'wryb', 'mode': 'dec'},
        {'Background': bk, 'n': 10,   'cmode': 'wryb', 'mode': 'dec'},

        {'Background': bk, 'n': 200,  'cmode': 'wryb', 'mode': 'dec', 'addalpha': 99},
        {'Background': bk, 'n': 100,  'cmode': 'wryb', 'mode': 'dec', 'addalpha': 99},
        {'Background': bk, 'n': 50,   'cmode': 'wryb', 'mode': 'dec', 'addalpha': 99},
        {'Background': bk, 'n': 10,   'cmode': 'wryb', 'mode': 'dec', 'addalpha': 99},

        # new tmp
        {'Background': bk, 'n': 200,  'cmode': 'BeachTowels', 'mode': 'dec'},
        {'Background': bk, 'n': 100,  'cmode': 'BeachTowels', 'mode': 'dec'},
        {'Background': bk, 'n': 50,   'cmode': 'BeachTowels', 'mode': 'dec'},
        {'Background': bk, 'n': 10,   'cmode': 'BeachTowels', 'mode': 'dec'},

        {'Background': bk, 'n': 200,  'cmode': 'MoonlightBytes6', 'mode': 'dec'},
        {'Background': bk, 'n': 100,  'cmode': 'MoonlightBytes6', 'mode': 'dec'},
        {'Background': bk, 'n': 50,   'cmode': 'MoonlightBytes6', 'mode': 'dec'},
        {'Background': bk, 'n': 10,   'cmode': 'MoonlightBytes6', 'mode': 'dec'},

        # new new 202105
        {'Background': bk, 'n': 2000, 'cmode': 'BeachTowels', 'mode': 'const'},
        {'Background': bk, 'n': 2000, 'cmode': 'MoonlightBytes6', 'mode': 'const'},
        {'Background': bk, 'n': 2000, 'cmode': 'BeachTowels', 'mode': 'const', 'addalpha': 99},
        {'Background': bk, 'n': 2000, 'cmode': 'MoonlightBytes6', 'mode': 'const', 'addalpha': 99},
        {'Background': bk, 'n': 2000, 'cmode': 'BeachTowels', 'mode': 'const', 'addalpha': 99, 'div': 10},
        {'Background': bk, 'n': 2000, 'cmode': 'MoonlightBytes6', 'mode': 'const', 'addalpha': 99, 'div': 10},
        {'Background': bk, 'n': 2000, 'cmode': 'BeachTowels', 'mode': 'const', 'addalpha': 99, 'div': 5},
        {'Background': bk, 'n': 2000, 'cmode': 'MoonlightBytes6', 'mode': 'const', 'addalpha': 99, 'div': 5},
        {'Background': bk, 'n': 50, 'cmode': 'BeachTowels', 'mode': 'const', 'addalpha': 99, 'div': 5},
        {'Background': bk, 'n': 50, 'cmode': 'MoonlightBytes6', 'mode': 'const', 'addalpha': 99, 'div': 5},
    ]
    return append_dflts(a, 'SMEARS#7', mazy7, w, h)

def predef_mazy8(w, h):
    a = [
        {'Background': bg_white, 'xcnt': 5, 'ycnt': 5},
        {'Background': bg_white, 'xcnt': 5, 'ycnt': 10},
        {'Background': bg_white, 'xcnt': 5, 'ycnt': 3},
        {'Background': bg_white, 'xcnt': 15, 'ycnt': 5},
        {'Background': bg_white, 'xcnt': 31, 'ycnt': 20},
        {'Background': bg_white, 'xcnt': 3, 'ycnt': 20},
    ]
    a = mux_param(a, 'color', ['happy', 'wryb', 'BeachTowels', 'MoonlightBytes6', 'MetroUI', 'ProgramCat'])
    a1 = copy.deepcopy(a)
    a2 = copy.deepcopy(a)
    for i in range(len(a)):
        a2[i]['flux_p'] = 75
        a2[i]['v'] = 50
    a = np.concatenate((a1, a2), axis=0)
    # todo: add flux alpha | add border | add ou opt
    return append_dflts(a, 'SMEARS#8', mazy8, w, h)

def predef_mazy9(w, h):
    v1 = float(h)/8
    v2 = float(h)/2
    v3 = float(h)/32
    a = [
        {'Background': bg_black},
    ]
    # TODO: reduce count - rndc=False only good if v>0
    a = mux_param(a, 'n', [60, 120, 360])
    a = mux_param(a, 'v', [0, v1, v2, v3])
    a = mux_param(a, 'rndc', [False, True])
    a = mux_param(a, 'color', ['happy', 'BeachTowels', 'ProgramCat', 'Number3', 'red', 'bw', 'BrGrRd'])
    return append_dflts(a, 'SMEARS#9', mazy9, w, h)

def predef_mazy10(w, h):
    bk = (0x84, 0x8B, 0x9B)
    a = [
            # new test n=3 also ok
            #{'Background': bk, 'n': 1, 'penw': 2, 'color': 'blue_const', 'mode': 'fill', 'complexity': 1000, 'open': False, 'addalpha': 90},
            #{'Background': bk, 'n': 3, 'penw': 2, 'color': 'blue_const', 'mode': 'fill', 'complexity': 1000, 'open': False, 'addalpha': 90},

            #{'Background': bk, 'n': 15, 'penw': 32, 'color': 'happy', 'mode': 'line', 'complexity': 70+130, 'open': False},

            {'Background': bk, 'n': 30, 'penw': 8, 'color': 'happy', 'mode': 'line', 'complexity': 70, 'open': False},
            {'Background': bk, 'n': 40, 'penw': 8, 'color': 'rg',    'mode': 'line', 'complexity': 70, 'open': False},
            {'Background': bk, 'n': 40, 'penw': 8, 'color': 'red',   'mode': 'line', 'complexity': 70, 'open': False},
            {'Background': bk, 'n': 40, 'penw': 8, 'color': 'wryb',  'mode': 'line', 'complexity': 70, 'open': False},

            {'Background': bk, 'n': 30, 'penw': 8, 'color': 'happy', 'mode': 'line', 'complexity': 70, 'open': True},
            {'Background': bk, 'n': 40, 'penw': 8, 'color': 'rg',    'mode': 'line', 'complexity': 70, 'open': True},
            {'Background': bk, 'n': 40, 'penw': 8, 'color': 'red',   'mode': 'line', 'complexity': 70, 'open': True},
            {'Background': bk, 'n': 40, 'penw': 8, 'color': 'wryb',  'mode': 'line', 'complexity': 70, 'open': True},

            {'Background': bk, 'n': 30, 'penw': 8, 'color': 'happy', 'mode': 'line', 'complexity': 70, 'open': True, 'addalpha': 90},
            {'Background': bk, 'n': 40, 'penw': 8, 'color': 'rg',    'mode': 'line', 'complexity': 70, 'open': True, 'addalpha': 90},
            {'Background': bk, 'n': 40, 'penw': 8, 'color': 'red',   'mode': 'line', 'complexity': 70, 'open': True, 'addalpha': 90},
            {'Background': bk, 'n': 40, 'penw': 8, 'color': 'wryb',  'mode': 'line', 'complexity': 70, 'open': True, 'addalpha': 90},

# TODO: more wryb
            {'Background': bg_white, 'n': 6, 'penw': 1, 'color': 'happy', 'mode': 'fill', 'complexity': 40, 'open': False},
            {'Background': bg_white, 'n': 6, 'penw': 1, 'color': 'happy', 'mode': 'fill', 'complexity': 40, 'open': True},

            {'Background': bg_white, 'n': 6, 'penw': 1, 'color': 'happy', 'mode': 'fill', 'complexity': 40, 'open': False, 'addalpha': 80},
            {'Background': bg_white, 'n': 6, 'penw': 1, 'color': 'happy', 'mode': 'fill', 'complexity': 40, 'open': True, 'addalpha': 80},

            {'Background': bg_white, 'n': 24, 'penw': 1, 'color': 'happy', 'mode': 'fill', 'complexity': 40, 'open': False},
            {'Background': bg_white, 'n': 24, 'penw': 1, 'color': 'happy', 'mode': 'fill', 'complexity': 40, 'open': True},

            {'Background': bg_white, 'n': 24, 'penw': 1, 'color': 'happy', 'mode': 'fill', 'complexity': 40, 'open': False, 'addalpha': 80},
            {'Background': bg_white, 'n': 24, 'penw': 1, 'color': 'happy', 'mode': 'fill', 'complexity': 40, 'open': True, 'addalpha': 80},
    ]
    return append_dflts(a, 'SMEARS#10', mazy10, w, h)

def predef_mazy11(w, h):
    a = [
        {'Background': bg_black, 'n': 8},
        {'Background': bg_black, 'n': 16},
        {'Background': bg_black, 'n': 64},
        {'Background': bg_black, 'n': 128},
    ]
    a = mux_param(a, 'color', ['happy', 'BeachTowels', 'MoonlightBytes6', 'Rainbow', 'MetroUI', 'ProgramCat', 'wryb', 'yorb', 'BrGrRd'])
    return append_dflts(a, 'SMEARS#11', mazy11, w, h)

def predef_mazy12(w, h):
    a = [
        {'Background': bg_white, 'n': 48-1, 'o': 'box', 'v': False},
        {'Background': bg_white, 'n': 48-1, 'o': 'box', 'v': False, 'rc': 1.3},
        {'Background': bg_white, 'n': 96-1, 'o': 'box', 'v': False},
        {'Background': bg_white, 'n': 96-1, 'o': 'box', 'v': False, 'rc': 1.3},

        {'Background': bg_white, 'n': 48, 'o': 'cir', 'v': False, 'rc': 0.95},
        {'Background': bg_white, 'n': 48-1, 'o': 'cir', 'v': False, 'rc': 0.95},
        {'Background': bg_white, 'n': 96, 'o': 'cir', 'v': False, 'rc': 0.95},
        {'Background': bg_white, 'n': 96-1, 'o': 'cir', 'v': False, 'rc': 0.95},

        {'Background': bg_white, 'n': 48, 'o': 'box', 'v': True, 'rc': 1.1},
        {'Background': bg_white, 'n': 96, 'o': 'box', 'v': True, 'rc': 1.1},

        {'Background': bg_white, 'n': 48, 'o': 'cir', 'v': True, 'rc': 0.7},
        {'Background': bg_white, 'n': 96, 'o': 'cir', 'v': True, 'rc': 0.7},

        {'Background': bg_white, 'n': 48-1, 'o': 'tri', 'rc': 0.5},
        {'Background': bg_white, 'n': 96*3-1, 'o': 'tri', 'rc': 0.5},
        {'Background': bg_white, 'n': 48-1, 'o': 'tri'},
        {'Background': bg_white, 'n': 96*3-1, 'o': 'tri'},
        {'Background': bg_white, 'n': 48-1, 'o': 'tri', 'rc': 1.7},
        {'Background': bg_white, 'n': 96*3-1, 'o': 'tri', 'rc': 1.7},
    ]
    return append_dflts(a, 'SMEARS#12', mazy12, w, h)

def predef_mazy13(w, h):
    a = [
        {'Background': bg_black, 'n': 32, 'color': (255, 255, 255)},
        {'Background': bg_black, 'n': 64, 'color': (255, 255, 255)},
        {'Background': bg_black, 'n': 128, 'color': (255, 255, 255)},
        {'Background': bg_white, 'n': 32, 'color': (224, 0, 0)},
        {'Background': bg_white, 'n': 64, 'color': (224, 0, 0)},
        {'Background': bg_white, 'n': 128, 'color': (224, 0, 0)},
        {'Background': (0,0,255), 'n': 24, 'color': (255, 0, 0)},
        {'Background': (0,0,255), 'n': 64, 'color': (255, 0, 0)},
        {'Background': (0,0,255), 'n': 128, 'color': (255, 0, 0)},
    ]
    return append_dflts(a, 'SMEARS#13', mazy13, w, h)

def predef_mazy14(w, h):
    a = [
        {'Background': bg_white, 'color': bg_black},
    ]
    a = mux_param(a, 'n', [6, 12, 24, 36, 48])
    a = mux_param(a, 'm', [4, 8, 32, 100])
    a_ = [{'Background': bg_white, 'color': bg_black, 'n': 24, 'm': 32, 'div': 5}] # 'special' case (test)
    a = np.concatenate((a, a_), axis=0)
    return append_dflts(a, 'SMEARS#14', mazy14, w, h)

def predef_mazy15(w, h):
    a = [
        # const offsets, a1 cool for n=16
        {'Background': bg_white, 'color': bg_black, 'xs1': int(-w/10), 'ys1': int(-w/100), 'xs2': int(w/10), 'ys2': int(w/100)},
        {'Background': bg_white, 'color': bg_black, 'xs1': int(-w/50), 'ys1': int(-w/100), 'xs2': int(w/50), 'ys2': int(w/100)},
        {'Background': bg_white, 'color': bg_black, 'xs1': int(-w/20), 'ys1': int(w/20),   'xs2': int(w/20), 'ys2': int(-w/20)},
        # linear - tested for c2 only
        {'Background': bg_white, 'color': bg_black, 'xs2v': int(w/25),  'ys2v': 0, 'mode': 'linear'},
        {'Background': bg_white, 'color': bg_black, 'xs2v': int(w/50),  'ys2v': 0, 'mode': 'linear'},
        {'Background': bg_white, 'color': bg_black, 'xs2v': int(w/100), 'ys2v': 0, 'mode': 'linear'},
        {'Background': bg_white, 'color': bg_black, 'xs2v': int(w/200), 'ys2v': 0, 'mode': 'linear'},
        # circle - tested for c2 only
        {'Background': bg_white, 'color': bg_black, 'xs2v': int(w/50),  'ys2v': int(w/50), 'mode': 'circle'},
        {'Background': bg_white, 'color': bg_black, 'xs2v': int(w/25),  'ys2v': int(w/25), 'mode': 'circle'},
        {'Background': bg_white, 'color': bg_black, 'xs2v': int(w/10),  'ys2v': int(w/10), 'mode': 'circle'},
        {'Background': bg_white, 'color': bg_black, 'xs2v': int(w/4),   'ys2v': int(w/4), 'mode': 'circle'},
        #?
        {'Background': bg_white, 'color': bg_black, 'xs1v': int(w/10), 'ys1v': int(w/10), 'xs2v': int(w/3), 'ys2v': int(w/3), 'mode': 'circle'},
    ]
    a = mux_param(a, 'n', [32, 64, 128])
    a = mux_param(a, 'colorer', [None, 'happy', 'wryb', 'ProgramCat'])
    return append_dflts(a, 'SMEARS#15', mazy15, w, h)

def predef_mazy16(w, h):
    a = [
        {'Background': bg_white, 'n': 24, 'color': bg_black, 'rcoef': 1.0, 'acoef': 1.0, 'rscale': 1.0},
        {'Background': bg_white, 'n': 48, 'color': bg_black, 'rcoef': 1.0, 'acoef': 1.0, 'rscale': 1.0},
        {'Background': bg_white, 'n': 96, 'color': bg_black, 'rcoef': 1.0, 'acoef': 1.0, 'rscale': 1.0},
        {'Background': bg_white, 'n': 256, 'color': bg_black, 'rcoef': 1.0, 'acoef': 1.0, 'rscale': 1.0},
    ]
    a = mux_param(a, 'rcoef', [1.5, 3.0])
    a = mux_param(a, 'acoef', [1.0, 7.0, 19.0])
    a = mux_param(a, 'rscale', [0.33, 1.0, 1.5, 2.0])
    return append_dflts(a, 'SMEARS#16', mazy16, w, h)

def predef_mazy17(w, h):
    n = 150
    a = [
        {'Background': bg_white, 'n': n, 'v': 1/30, 'addalpha': 0},
        {'Background': bg_white, 'n': n, 'v': 1/30, 'addalpha': 90},
        {'Background': bg_white, 'n': n, 'v': 1/30, 'addalpha': 60},
        {'Background': bg_white, 'n': n, 'v': 1/200, 'addalpha': 0},
        {'Background': bg_white, 'n': n, 'v': 1/200, 'addalpha': 90},
        {'Background': bg_white, 'n': n, 'v': 1/200, 'addalpha': 60},
        {'Background': bg_white, 'n': n, 'v': 1/4, 'addalpha': 90}, # w/o addalpha lame
        {'Background': bg_white, 'n': n, 'v': 1/4, 'addalpha': 60}, # w/o addalpha lame
    ]
    a = mux_param(a, 'color', ['happy', 'yorb', 'wryb', 'BeachTowels', 'Number3' , 'bw', 'bgo', 'MoonlightBytes6', 'MetroUI', 'ProgramCat'])
    return append_dflts(a, 'SMEARS#17', mazy17, w, h)

def predef_mazy18(w, h):
    a = [
        {'Background': bg_white, 'n': 40, 'm': 120, 'v': 50},
        {'Background': bg_white, 'n': 60, 'm': 16, 'v': 80},
        {'Background': bg_white, 'n': 90, 'm': 30, 'v': 20},
        {'Background': bg_white, 'n': 90, 'm': 120, 'v': 100},
        {'Background': bg_white, 'n': 120, 'm': 40, 'v': 20},
        {'Background': bg_white, 'n': 180, 'm': 40, 'v': 20, 'r0v': 300},

        {'Background': bg_white, 'multi': [
            {'n': 60, 'm': 16, 'v': 80},
            {'n': 90, 'm': 30, 'v': 20},
            {'n': 120, 'm': 40, 'v': 20, 'r0v': 250},
            {'n': 60, 'm': 40, 'v': 20, 'r0v': 500},
         ]}, # new concept - interesting, work it more

        {'Background': bg_white, 'multi': [
            {'n': 30, 'm': 20, 'v': 200},
            {'n': 30, 'm': 20, 'v': 10},
         ]}, # new concept - interesting, work it more
    ]
    a = mux_param(a, 'color', ['happy', 'yorb', 'wryb', 'BeachTowels', 'Number3'])
    return append_dflts(a, 'SMEARS#18', mazy18, w, h)

def predef_mazy19(w, h):
    a = [
        {'Background': bg_black, 'n': 20, 'm': 10, 'mode': 'grid'},
        {'Background': bg_black, 'n': 60, 'm': 10, 'mode': 'grid'},

        {'Background': bg_black, 'n': 8, 'm': 10, 'mode': 'lin'},
        {'Background': bg_black, 'n': 8, 'm': 20, 'mode': 'lin'},
        
        {'Background': bg_black, 'n': 40, 'm': 10, 'mode': 'exp'},
        {'Background': bg_black, 'n': 40, 'm': 40, 'mode': 'exp'},
        {'Background': bg_black, 'n': 80, 'm': 40, 'mode': 'exp'},
        {'Background': bg_black, 'n': 20, 'm': 20, 'mode': 'exp'},

        {'Background': bg_black, 'n': 40, 'm': 40, 'mode': 'sin'},
        {'Background': bg_black, 'n': 80, 'm': 40, 'mode': 'sin'},
        {'Background': bg_black, 'n': 160, 'm': 40, 'mode': 'sin'},

        {'Background': bg_black, 'n': 40, 'm': 40, 'mode': 'sin', 'c_black': (255,0,0), 'c_white': (0,0,255)},
        {'Background': bg_black, 'n': 80, 'm': 40, 'mode': 'sin', 'c_black': (255,0,0), 'c_white': (0,0,255)},
        {'Background': bg_black, 'n': 160, 'm': 40, 'mode': 'sin', 'c_black': (255,0,0), 'c_white': (0,0,255)},
    ]
    return append_dflts(a, 'SMEARS#19', mazy19, w, h)

def predef_mazy20(w, h):
    n = 16 # good for A4
    a = [
        {'Background': bg_black, 'Foreground': bg_white, 'n': n, 'da': 6},
        {'Background': bg_black, 'Foreground': bg_white, 'n': n, 'da': 6, 'invert': True},
        {'Background': bg_white, 'Foreground': bg_black, 'n': n, 'da': 6},

        {'Background': bg_black, 'Foreground': bg_white, 'n': n, 'da': 15},
        {'Background': bg_black, 'Foreground': bg_white, 'n': n, 'da': 15, 'invert': True},
        {'Background': bg_white, 'Foreground': bg_black, 'n': n, 'da': 15},

        {'Background': bg_black, 'Foreground': bg_white, 'n': n, 'da': 30},
        {'Background': bg_black, 'Foreground': bg_white, 'n': n, 'da': 30, 'invert': True},
        {'Background': bg_white, 'Foreground': bg_black, 'n': n, 'da': 30},
        
        {'Background': bg_black, 'Foreground': bg_white, 'n': n, 'da': 45},
        {'Background': bg_black, 'Foreground': bg_white, 'n': n, 'da': 45, 'invert': True},
        {'Background': bg_white, 'Foreground': bg_black, 'n': n, 'da': 45},
    ]
    a = mux_param(a, 'sc', [0.75, 0.5])
    return append_dflts(a, 'SMEARS#20', mazy20, w, h)

def predef_mazy21(w, h):
    n = 9+3
    a = [
        {'Background': bg_black, 'Foreground': bg_white, 'n': n, 'mode': 0},
        {'Background': bg_black, 'Foreground': bg_white, 'n': n, 'mode': 0, 'invert': True},
        {'Background': bg_black, 'Foreground': bg_white, 'n': n, 'mode': 1},
        {'Background': bg_black, 'Foreground': bg_white, 'n': n, 'mode': 1, 'invert': True},
        {'Background': bg_black, 'Foreground': bg_white, 'n': n, 'mode': 2},
        {'Background': bg_black, 'Foreground': bg_white, 'n': n, 'mode': 2, 'invert': True},
        {'Background': bg_black, 'Foreground': bg_white, 'n': n, 'mode': 3},
        {'Background': bg_black, 'Foreground': bg_white, 'n': n, 'mode': 3, 'invert': True},
        {'Background': bg_black, 'Foreground': bg_white, 'n': n, 'mode': 4},
        {'Background': bg_black, 'Foreground': bg_white, 'n': n, 'mode': 4, 'invert': True},
        {'Background': bg_black, 'Foreground': bg_white, 'n': n, 'mode': 5},
        {'Background': bg_black, 'Foreground': bg_white, 'n': n, 'mode': 5, 'invert': True},
        {'Background': bg_black, 'Foreground': bg_white, 'n': n, 'mode': 6},
        {'Background': bg_black, 'Foreground': bg_white, 'n': n, 'mode': 6, 'invert': True},
    ]
    return append_dflts(a, 'SMEARS#21', mazy21, w, h)

def predef_mazy22(w, h):
    a = [
        {'Background': bg_black, 'n': 36*1, 'color': None},
        {'Background': bg_black, 'n': 36*2, 'color': None},
        {'Background': bg_black, 'n': 36*3, 'color': None},
        {'Background': bg_black, 'n': 36*4, 'color': None},
        {'Background': bg_black, 'n': 36*8, 'color': None},
    ]
    # todo: not so excessive count?
    a = mux_param(a, 'da', [90, 89, 85, 80, 45, 12, 5])
    a = mux_param(a, 'a_e', [90, 60, 45, 35, 10, 5])
    a = mux_param(a, 'drc', [0.97, 0.98])
    a = mux_param(a, 'color', ['bw', 'red', 'happy', 'Number3', 'wryb', 'ProgramCat'])

    n = 48
    c = [
        {'Background': bg_black, 'n': n-8, 'color': 'bw', 'rnd': True},
        {'Background': bg_white, 'n': n-8, 'color': 'bw', 'rnd': True},
        {'Background': bg_black, 'n': n-8, 'color': 'red', 'rnd': True},
        {'Background': bg_white, 'n': n+8, 'color': 'happy', 'rnd': True},
        {'Background': bg_white, 'n': n+8, 'color': 'Number3', 'rnd': True},
        {'Background': bg_white, 'n': n+8, 'color': 'wryb', 'rnd': True},
        {'Background': bg_white, 'n': n+8, 'color': 'ProgramCat', 'rnd': True},
    ]

    a = np.concatenate((a, c), axis=0)
    #a = c #test rnd only
    return append_dflts(a, 'SMEARS#22', mazy22, w, h)

def predef_mazy23(w, h):
    mar = 3/100 # 3% margin
    n = 8 # n=8 ok for A4
    #n = 10 # n=10 ok for A0
    a = [
        {'Background': bg_black, 'color1': bg_white, 'color2': bg_black, 'n': 4, 'margin': mar},
        {'Background': bg_black, 'color1': bg_white, 'color2': bg_black, 'n': 5, 'margin': mar},
        {'Background': bg_black, 'color1': bg_white, 'color2': bg_black, 'n': n, 'margin': mar},
        {'Background': bg_white, 'color1': bg_black, 'color2': bg_white, 'n': n, 'margin': mar},
        {'Background': bg_white, 'color1': bg_black, 'color2': (255,0,0), 'n': n, 'margin': mar},
        {'Background': bg_white, 'color1': (0,0,240), 'color2': (255,128,0), 'n': n, 'margin': mar},

        {'Background': bg_white, 'color1': bg_black, 'color2': bg_white, 'colorer': 'wryb', 'colorer_mode': 0, 'n': n, 'margin': mar},
        {'Background': bg_white, 'color1': bg_black, 'color2': bg_white, 'colorer': 'ProgramCat', 'colorer_mode': 0, 'n': n, 'margin': mar},
        {'Background': bg_white, 'color1': bg_black, 'color2': bg_white, 'colorer': 'Number3', 'colorer_mode': 0, 'n': n, 'margin': mar},
        {'Background': bg_white, 'color1': bg_black, 'color2': bg_white, 'colorer': 'bw', 'colorer_mode': 0, 'n': n, 'margin': mar},
        {'Background': bg_white, 'color1': bg_black, 'color2': bg_white, 'colorer': 'red', 'colorer_mode': 0, 'n': n, 'margin': mar},

        {'Background': bg_white, 'color1': bg_black, 'color2': bg_white, 'colorer': 'wryb', 'colorer_mode': 1, 'n': n, 'margin': mar},
        {'Background': bg_white, 'color1': bg_black, 'color2': bg_white, 'colorer': 'ProgramCat', 'colorer_mode': 1, 'n': n, 'margin': mar},
        {'Background': bg_white, 'color1': bg_black, 'color2': bg_white, 'colorer': 'Number3', 'colorer_mode': 1, 'n': n, 'margin': mar},
        {'Background': bg_white, 'color1': bg_black, 'color2': bg_white, 'colorer': 'bw', 'colorer_mode': 1, 'n': n, 'margin': mar},
        {'Background': bg_white, 'color1': bg_black, 'color2': bg_white, 'colorer': 'red', 'colorer_mode': 1, 'n': n, 'margin': mar},
    ]
    return append_dflts(a, 'SMEARS#23', mazy23, w, h)

def predef_mazy24(w, h):
    a = [
        {'Background': bg_black, 'n': 0, 'ou': bg_black},
        {'Background': bg_white, 'n': 0, 'ou': bg_black},
        {'Background': bg_black, 'n': 0, 'ou': bg_black, 'addalpha': 120},
        {'Background': bg_white, 'n': 0, 'ou': bg_black, 'addalpha': 120},
    ]
    # todo: reduce count - some too similar / some lame
    # todo: no bw on white bg - lame anyway
    # todo: op art bw
    # todo: no ou opt (some?)
    a = mux_param(a, 'n', [40, 40+16, 72])
    a = mux_param(a, 'a_base', [0.87, 1.0, 4.0])
    a = mux_param(a, 'an_sc', [0.2, 0.75, 1.0, 2.0, 4.0])
    a = mux_param(a, 'colorer', ['happy', 'wryb', 'Number3', 'ProgramCat', 'bw', 'red'])
    return append_dflts(a, 'SMEARS#24', mazy24, w, h)

def predef_mazy25(w, h):
    a = [
        {'Background': bg_white, 'n': 12, 'f0': 1, 'horizontal': False, 'color': 'happy'},
        {'Background': bg_white, 'n': 12, 'f0': 3, 'horizontal': False, 'color': 'happy'},
        {'Background': bg_white, 'n': 32, 'f0': 1, 'horizontal': False, 'color': 'happy'},

        {'Background': bg_white, 'n': 4, 'f0': 5, 'horizontal': False, 'color': 'wryb'},

        {'Background': bg_white, 'n': 12, 'f0': 1, 'horizontal': True, 'color': 'happy'},
        {'Background': bg_white, 'n': 12, 'f0': 1, 'horizontal': True, 'color': 'happy', 'addalpha': 150},

        {'Background': bg_black, 'n': 10, 'f0': 1, 'horizontal': True, 'color': 'wryb'},

        {'Background': bg_black, 'n': 10, 'f0': 1, 'horizontal': True, 'color': 'Number3'},
        {'Background': bg_black, 'n': 10, 'f0': 0.5, 'horizontal': True, 'color': 'Number3'},

        {'Background': bg_black, 'n': 10, 'f0': 3.0, 'horizontal': True, 'color': 'Number3'},
        {'Background': bg_black, 'n': 15, 'f0': 3.5, 'horizontal': True, 'color': 'Number3', 'addalpha': 70},

        {'Background': bg_white, 'n': 10, 'f0': 3.0, 'horizontal': True, 'color': 'Number3'},
        {'Background': bg_white, 'n': 15, 'f0': 3.5, 'horizontal': True, 'color': 'Number3', 'addalpha': 70},
    ]
    return append_dflts(a, 'SMEARS#25', mazy25, w, h)

def predef_mazy26(w, h):
    params1a = {'w': w, 'h': h, 'Background': bg_white, 'n': 90, 'horizontal': True, 'color': 'BeachTowels', 'addalpha': 90}
    params2a = {'w': w, 'h': h, 'Background': bg_white, 'n': 90, 'horizontal': False, 'color': 'happy', 'addalpha': 70}
    params1b = {'w': w, 'h': h, 'Background': bg_white, 'n': 100, 'horizontal': True, 'color': 'happy', 'addalpha': 100}
    params2b = {'w': w, 'h': h, 'Background': bg_white, 'n': 100, 'horizontal': False, 'color': 'happy', 'addalpha': 100}
    a = [
        {'Background': bg_white, 'n': 100, 'horizontal': True, 'color': 'happy'},
        {'Background': bg_white, 'n': 250, 'horizontal': True, 'color': 'happy', 'addalpha': 50},
        {'Background': bg_white, 'n': 250, 'horizontal': True, 'color': 'happy', 'addalpha': 25},
        {'Background': bg_white, 'n': 100, 'horizontal': True, 'color': 'Number3'},
        {'Background': bg_white, 'n': 100, 'horizontal': True, 'color': 'Number3', 'addalpha': 50},
        {'Background': bg_white, 'n': 100, 'horizontal': True, 'color': 'BeachTowels'},
        {'Background': bg_black, 'n': 250, 'horizontal': True, 'color': 'green', 'addalpha': 70},
        {'Background': bg_white, 'par1': params1a, 'par2': params2a},
        {'Background': bg_white, 'par1': params1b, 'par2': params2b},
    ]
    return append_dflts(a, 'SMEARS#26', mazy26, w, h)

def predef_mazy27(w, h):
    n = 300*3
# TODO:
# rmin = int(h/30)
# rmax = h/4 # h h/2 # h/4
    a = [
        {'Background': bg_white, 'n': n},
        {'Background': bg_white, 'n': n, 'minsides': 6, 'maxsides': 6, 'maxangle': 0},
    ]
    a = mux_param(a, 'rsc', [0.997, 0.99, 0])
    a = mux_param(a, 'addalpha', [0, 140, 90])
    a = mux_param(a, 'colorer', ['happy', 'wryb', 'yorb', 'Number3', 'ProgramCat'])
    return append_dflts(a, 'SMEARS#27', mazy27, w, h)

def predef_mazy28(w, h):
    a = [
        {'Background': bg_white, 'n': 1},
    ]
    return append_dflts(a, 'SMEARS#28', mazy28, w, h)

def predef_mazy29(w, h):
    a = [
        {'Background': bg_black, 'n': 1},
    ]
    return append_dflts(a, 'SMEARS#29', mazy29, w, h)

def predef_mazy30(w, h):
    a = [
        {'Background': bg_white, 'n': 1},
    ]
    return append_dflts(a, 'SMEARS#30', mazy30, w, h)

def predef_mazy31(w, h):
    steps = 20+10 # not too much!
    a = [
        {'Background': bg_white, 'n': 1, 'mode': 0, 'steps': steps},
        {'Background': bg_white, 'n': 1, 'mode': 0, 'steps': 60},
        {'Background': bg_white, 'n': 1, 'mode': 0, 'steps': steps, 'color': 'any_rnd'},
        {'Background': bg_white, 'n': 1, 'mode': 0, 'steps': steps, 'color': 'happy'},
        {'Background': bg_white, 'n': 1, 'mode': 0, 'steps': steps, 'color': 'wryb'},
        {'Background': bg_white, 'n': 1, 'mode': 0, 'steps': steps, 'color': 'psych'},
        {'Background': bg_white, 'n': 1, 'mode': 0, 'steps': steps, 'color': 'MoonlightBytes6'},

        {'Background': bg_white, 'n': 1, 'mode': 1, 'steps': steps},
        {'Background': bg_white, 'n': 1, 'mode': 2, 'steps': steps},

        {'Background': bg_white, 'n': 1, 'mode': 3, 'steps': steps+12},
        {'Background': bg_white, 'n': 1, 'mode': 3, 'steps': steps+70},

        {'Background': bg_white, 'n': 1, 'mode': 3, 'steps': steps+12, 'color': 'any_rnd'},
        {'Background': bg_white, 'n': 1, 'mode': 3, 'steps': steps+12, 'color': 'happy'},
        {'Background': bg_white, 'n': 1, 'mode': 3, 'steps': steps+12, 'color': 'wryb'},
        {'Background': bg_white, 'n': 1, 'mode': 3, 'steps': steps+12, 'color': 'psych'},
        {'Background': bg_white, 'n': 1, 'mode': 3, 'steps': steps+12, 'color': 'MoonlightBytes6'},

        {'Background': bg_white, 'n': 1, 'mode': 4, 'steps': steps+12},
        {'Background': bg_white, 'n': 1, 'mode': 4, 'steps': steps+70},

        {'Background': bg_white, 'n': 1, 'mode': 5, 'steps': steps},
        {'Background': bg_white, 'n': 1, 'mode': 5, 'steps': steps+20},
        {'Background': bg_white, 'n': 1, 'mode': 5, 'steps': steps+220},
        {'Background': bg_white, 'n': 1, 'mode': 5, 'steps': steps+670},

        {'Background': bg_white, 'n': 1, 'mode': 5, 'steps': steps+670, 'color': 'any_rnd'},
        {'Background': bg_white, 'n': 1, 'mode': 5, 'steps': steps+670, 'color': 'happy'},
        {'Background': bg_white, 'n': 1, 'mode': 5, 'steps': steps+670, 'color': 'wryb'},
        {'Background': bg_white, 'n': 1, 'mode': 5, 'steps': steps+670, 'color': 'psych'},
        {'Background': bg_white, 'n': 1, 'mode': 5, 'steps': steps+670, 'color': 'MoonlightBytes6'},

        {'Background': bg_white, 'n': 1, 'mode': 6, 'steps': steps},
        {'Background': bg_white, 'n': 1, 'mode': 7, 'steps': steps},
        {'Background': bg_white, 'n': 1, 'mode': 8, 'steps': steps},
        {'Background': bg_white, 'n': 1, 'mode': 9, 'steps': steps},
        {'Background': bg_white, 'n': 1, 'mode': 10, 'steps': steps},
        {'Background': bg_white, 'n': 1, 'mode': 11, 'steps': steps},
        {'Background': bg_white, 'n': 1, 'mode': 12, 'steps': steps},
        {'Background': bg_white, 'n': 1, 'mode': 13, 'steps': steps},

        {'Background': bg_white, 'n': 1, 'mode': 6, 'steps': steps+20, 'color': 'wryb'},
        {'Background': bg_white, 'n': 1, 'mode': 7, 'steps': steps+20, 'color': 'wryb'},
        {'Background': bg_white, 'n': 1, 'mode': 8, 'steps': steps+30, 'color': 'wryb'},
        {'Background': bg_white, 'n': 1, 'mode': 9, 'steps': steps+20, 'color': 'wryb'},
        {'Background': bg_white, 'n': 1, 'mode': 10, 'steps': steps+30, 'color': 'wryb'},
        {'Background': bg_white, 'n': 1, 'mode': 11, 'steps': steps+20, 'color': 'wryb'},
        {'Background': bg_white, 'n': 1, 'mode': 12, 'steps': steps+30, 'color': 'wryb'},
        {'Background': bg_white, 'n': 1, 'mode': 13, 'steps': steps+20, 'color': 'wryb'},

    ]
    return append_dflts(a, 'SMEARS#31', mazy31, w, h)

def predef_mazy32(w, h):
    a = [
        {'Background': bg_white, 'n': 360},
    ]
    return append_dflts(a, 'SMEARS#32', mazy32, w, h)

def predef_mazy33(w, h):
    a = [
        {'Background': bg_black, 'n': 1},
    ]
    return append_dflts(a, 'SMEARS#33', mazy32, w, h)

def predef_mazy34(w, h):
    a = [
        {'Background': bg_black, 'n': 1},
    ]
    return append_dflts(a, 'SMEARS#34', mazy32, w, h)

# ---

def enum_defs(doprint=True):
    suma = 0
    dout = {}
    for k, v in predefs.items():    #note: py3
        cnt = len(v(0, 0))
        suma += cnt
        dout[k] = cnt
    dout1 = OrderedDict(sorted(dout.items()))
    if doprint:
        for k, v in dout1.items():    #note: py3
            print(k, ':', v)
        print('total:', suma)
    return suma

# all predefs
predefs = {'mazy01': predef_mazy1, 'mazy02': predef_mazy2, 'mazy03': predef_mazy3, 'mazy04': predef_mazy4,
           'mazy05': predef_mazy5, 'mazy06': predef_mazy6, 'mazy07': predef_mazy7, 'mazy08': predef_mazy8,
           'mazy09': predef_mazy9, 'mazy10': predef_mazy10, 'mazy11': predef_mazy11, 'mazy12': predef_mazy12,
           'mazy13': predef_mazy13, 'mazy14': predef_mazy14, 'mazy15': predef_mazy15, 'mazy16': predef_mazy16,
           'mazy17': predef_mazy17, 'mazy18': predef_mazy18, 'mazy19': predef_mazy19, 'mazy20': predef_mazy20,
           'mazy21': predef_mazy21, 'mazy22': predef_mazy22, 'mazy23': predef_mazy23, 'mazy24': predef_mazy24,
           'mazy25': predef_mazy25, 'mazy26': predef_mazy26, 'mazy27': predef_mazy27, 'mazy28': predef_mazy28,
           'mazy29': predef_mazy29, 'mazy30': predef_mazy30, 'mazy31': predef_mazy31, 'mazy32': predef_mazy32,
           'life': predef_life, 'lissajous': predef_lissajous, 'astro': predef_astro, 'mandelbrot': predef_mandelbrot,
           }

# all names
predef_names = [
        'mazy01', 'mazy02', 'mazy03', 'mazy04', 'mazy05', 'mazy06', 'mazy07', 'mazy08',
        'mazy09', 'mazy10', 'mazy11', 'mazy12', 'mazy13', 'mazy14', 'mazy15', 'mazy16',
        'mazy17', 'mazy18', 'mazy19', 'mazy20', 'mazy21', 'mazy22', 'mazy23', 'mazy24',
        'mazy25', 'mazy26', 'mazy27', 'mazy28', 'mazy29', 'mazy30', 'mazy31', 'mazy32',
        'astro', 'life', 'lissajous', 'mandelbrot'
        ]

# EOF
