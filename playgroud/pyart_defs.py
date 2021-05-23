#! /usr/bin/env python
# -*- coding: utf-8 -*-

# PyArtForms - Python generative art forms paint algorithms (artificial artist)
# predefined forms
# (c)2018-2021 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz
# cre: 20181020
# upd: 20190105, 06, 13, 18, 21, 22
# upd: 20190311, 30
# upd: 20190414, 15, 17, 18, 21, 22, 24, 26, 27
# upd: 20200507, 10
# upd: 20210106
# upd: 20210515, 16, 22, 23


# TODO:
# - add alpha ver for all
# - ?

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


# --- life

def predef_life(w, h):
    a = [
        {'Background': bg_black, 'Color': (255,255,255), 'f': 'f2a'},
        {'Background': bg_black, 'Color': (255,255,255), 'f': 'f2b'},
        {'Background': bg_black, 'Color': (255,255,255), 'f': 'f2c'},
        {'Background': bg_black, 'Color': (255,255,255), 'f': 'f2d'},
        {'Background': bg_black, 'Color': (255,255,255), 'f': 'f2e'},
        {'Background': bg_black, 'Color': (255,255,255), 'f': 'f2f'},
        {'Background': bg_black, 'Color': (255,255,255), 'f': 'f2g'},
    ]
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
   
# --- waves

def predef_waves1(w, h):
    a = [
        {'Background': bg_white, 'z': 12, 'f0': 1, 'horizontal': False, 'color': 'happy'},
        {'Background': bg_white, 'z': 12, 'f0': 1, 'horizontal': True, 'color': 'happy'},
        {'Background': bg_white, 'z': 12, 'f0': 1, 'horizontal': True, 'color': 'happy', 'addalpha': 50},
        {'Background': (200, 200, 0), 'z': 10, 'f0': 1, 'horizontal': True, 'color': 'rg'},
        {'Background': bg_black, 'z': 10, 'f0': 1, 'horizontal': True, 'color': 'Number3'},
        {'Background': bg_black, 'z': 10, 'f0': 0.5, 'horizontal': True, 'color': 'Number3'},
        {'Background': bg_black, 'z': 10, 'f0': 3.0, 'horizontal': True, 'color': 'Number3'},
        {'Background': bg_black, 'z': 15, 'f0': 3.5, 'horizontal': True, 'color': 'Number3', 'addalpha': 70},
    ]
    return append_dflts(a, 'WAVES#1', waves1, w, h)

def predef_waves2(w, h):
    a = [
        {'Background': bg_black, 'z': 100, 'horizontal': False, 'color': 'rg'},
        {'Background': bg_black, 'z': 100, 'horizontal': True, 'color': 'rg'},
        {'Background': bg_white, 'z': 100, 'horizontal': True, 'color': 'happy'},
        {'Background': bg_white, 'z': 250, 'horizontal': True, 'color': 'happy', 'addalpha': 50},
        {'Background': bg_white, 'z': 250, 'horizontal': True, 'color': 'happy', 'addalpha': 25},
        {'Background': bg_white, 'z': 100, 'horizontal': True, 'color': 'Number3'},
        {'Background': bg_white, 'z': 100, 'horizontal': True, 'color': 'Number3', 'addalpha': 50},
        {'Background': bg_white, 'z': 100, 'horizontal': True, 'color': 'BeachTowels'},
        {'Background': bg_black, 'z': 250, 'horizontal': True, 'color': 'green', 'addalpha': 70},
    ]
    params1a = {'w': w, 'h': h, 'Background': bg_white, 'z': 90, 'horizontal': True, 'color': 'BeachTowels', 'addalpha': 90}
    params2a = {'w': w, 'h': h, 'Background': bg_white, 'z': 90, 'horizontal': False, 'color': 'happy', 'addalpha': 70}
    a2 = [
        {'name': 'WAVES#2', 'call': waves_mux, 'w': w, 'h': h, 'Background': bg_white, 'par1': params1a, 'par2': params2a},
    ]
    a = append_dflts(a, 'WAVES#2', waves2, w, h)
    return np.concatenate((a, a2), axis=0)

def predef_waves3(w, h):
    a = [
        {'name': 'WAVES#3', 'call': waves3, 'w': w, 'h': h, 'Background': bg_black, 'z': 18*3, 'c1': (255,255,255), 'c2': (255,255,0), 'c3': (255,0,0)},
    ]
    return a
        
# --- astro - 2x (cir, box) bluegalaxy ellipticgalaxy spiralgalaxy neutronstar blackhole supernova nebula star

def predef_astro(w, h):
    a = [
        {'call': paint0, 'Background': bg_black, 'ou': (0,0,0), 'box_or_cir': False},
        {'call': paint0, 'Background': bg_black, 'ou': (0,0,0), 'box_or_cir': True},
        {'call': paint1, 'Background': bg_black, 'ou': (0,0,0), 'box_or_cir': False},
        {'call': paint1, 'Background': bg_black, 'ou': (0,0,0), 'box_or_cir': True},
        {'call': paint2, 'Background': bg_black, 'ou': (0,0,0), 'box_or_cir': False},
        {'call': paint2, 'Background': bg_black, 'ou': (0,0,0), 'box_or_cir': True},
        {'call': paint3, 'Background': bg_black, 'ou': (0,0,0), 'box_or_cir': False},
        {'call': paint3, 'Background': bg_black, 'ou': (0,0,0), 'box_or_cir': True},
        {'call': paint4, 'Background': bg_black, 'ou': (0,0,0), 'box_or_cir': False},
        {'call': paint4, 'Background': bg_black, 'ou': (0,0,0), 'box_or_cir': True},
        {'call': paint5, 'Background': bg_black, 'ou': (0,0,0), 'box_or_cir': False},
        {'call': paint5, 'Background': bg_black, 'ou': (0,0,0), 'box_or_cir': True},
        {'call': paint6, 'Background': bg_black, 'ou': (0,0,0), 'box_or_cir': False},
        {'call': paint6, 'Background': bg_black, 'ou': (0,0,0), 'box_or_cir': True},
        {'call': paint7, 'Background': bg_black, 'ou': (0,0,0), 'box_or_cir': False},
        {'call': paint7, 'Background': bg_black, 'ou': (0,0,0), 'box_or_cir': True},
    ]
    a = append_dct_item(a, 'name', 'ASTROART')
    a = append_dct_item(a, 'w', w)
    a = append_dct_item(a, 'h', h)
    return a

# --- mandelbrot

def predef_mandelbrot(w, h):
    a = [
        {'x0': -2.5, 'x1': 1.0, 'y0': -1.0, 'y1': 1.0, 'maxiter': 200, 'negative': False, 'Background': bg_black, 'bw': True},
        {'x0': -2.5, 'x1': 1.0, 'y0': -1.0, 'y1': 1.0, 'maxiter': 20, 'negative': False, 'Background': bg_black, 'bw': True},
    ]
    a = append_dct_item(a, 'name', 'MANDELBROT')
    a = append_dct_item(a, 'w', w)
    a = append_dct_item(a, 'h', h)
    a = append_dct_item(a, 'call', generate_mandelbrot)
    return a

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

    # unfilled
    b = [
        #6 red (fix? mar?)
        {'Background': bg_white, 'penw': 8, 'v': 75, 'n': 100, 'm': 40, 'prefill': False, 'mode': 'red', 'keep': False, 'color': 'red_rnd'},

        # 6 red tests new, ok, use
#        {'Background': bg_white, 'penw': 8, 'v': 25, 'n': 100, 'm': 40, 'prefill': False, 'mode': 'red', 'keep': False, 'color': 'red_rnd', 'mar': int(w/15)},
#        {'Background': bg_white, 'penw': 2, 'v': 120, 'n': 40, 'm': 120, 'prefill': False, 'mode': 'red', 'keep': False, 'color': 'red_rnd', 'mar': int(w/15)},
#        {'Background': bg_white, 'penw': 8, 'v': 120, 'n': 40, 'm': 120, 'prefill': False, 'mode': 'red', 'keep': False, 'color': 'red_rnd', 'mar': int(w/15)},
#        {'Background': bg_white, 'penw': 24, 'v': 120, 'n': 40, 'm': 60, 'prefill': False, 'mode': 'red', 'keep': False, 'color': 'red_rnd', 'mar': int(w/15)},
#        {'Background': bg_white, 'penw': 8, 'v': 20, 'n': 500, 'm': 5, 'prefill': False, 'mode': 'red', 'keep': False, 'color': 'red_rnd', 'mar': int(w/15)},

        #?
        {'Background': bg_white, 'penw': 8, 'v': 75, 'n': 100, 'm': 40, 'prefill': False, 'mode': 'happy', 'keep': False},
        {'Background': bg_white, 'penw': 8, 'v': 75, 'n': 100, 'm': 40, 'prefill': False, 'mode': 'wryb', 'keep': False},
        {'Background': bg_white, 'penw': 8, 'v': 75, 'n': 100, 'm': 40, 'prefill': False, 'mode': 'psych', 'keep': False},
        {'Background': bg_white, 'penw': 8, 'v': 75, 'n': 100, 'm': 40, 'prefill': False, 'mode': 'happy', 'keep': False, 'addblack': True},
        {'Background': bg_white, 'penw': 8, 'v': 75, 'n': 100, 'm': 40, 'prefill': False, 'mode': 'wryb', 'keep': False, 'addblack': True},
        {'Background': bg_white, 'penw': 8, 'v': 75, 'n': 100, 'm': 40, 'prefill': False, 'mode': 'psych', 'keep': False, 'addblack': True},
        {'Background': bg_white, 'penw': 8, 'v': 75, 'n': 100, 'm': 40, 'prefill': False, 'mode': 'BeachTowels', 'keep': False},
        {'Background': bg_white, 'penw': 8, 'v': 75, 'n': 100, 'm': 40, 'prefill': False, 'mode': 'MoonlightBytes6', 'keep': False},
        {'Background': bg_white, 'penw': 8, 'v': 75, 'n': 100, 'm': 40, 'prefill': False, 'mode': 'Number3', 'keep': False},
        {'Background': bg_white, 'penw': 8, 'v': 75, 'n': 100, 'm': 40, 'prefill': False, 'mode': 'RainbowDash', 'keep': False},
        {'Background': bg_white, 'penw': 8, 'v': 75, 'n': 100, 'm': 40, 'prefill': False, 'mode': 'Google', 'keep': False},
        {'Background': bg_white, 'penw': 8, 'v': 75, 'n': 100, 'm': 40, 'prefill': False, 'mode': 'MetroUI', 'keep': False},
        {'Background': bg_white, 'penw': 8, 'v': 75, 'n': 100, 'm': 40, 'prefill': False, 'mode': 'ProgramCat', 'keep': False},

        {'Background': bg_yellow, 'penw': 5, 'v': 200, 'n': 50, 'm': 25, 'prefill': False, 'mode': 'red', 'keep': True, 'color': 'any_rnd', 'mar': int(w/20)},
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
        {'Background': bg_black, 'n': 100, 'm': 40, 'color': 'bw0'},
        {'Background': bg_black, 'n': 100, 'm': 200, 'color': 'bw0'},  # ?
        {'Background': bg_black, 'n': 100, 'm': 40, 'color': 'bwx'},
        {'Background': bg_black, 'n': 100, 'm': 30, 'color': 'happy'},
        {'Background': bg_black, 'n': 100+90, 'm': 30+30, 'color': 'happy', 'addalpha': 80}, # test
        {'Background': bg_black, 'n': 100, 'm': 30, 'color': 'wryb'},
        {'Background': bg_black, 'n': 100, 'm': 30, 'color': 'bgo'},

        {'Background': bg_black, 'n': 100, 'm': 30, 'color': 'BeachTowels'},
        {'Background': bg_black, 'n': 100, 'm': 30, 'color': 'MoonlightBytes6'},
        {'Background': bg_black, 'n': 100, 'm': 30, 'color': 'Number3'},
        {'Background': bg_black, 'n': 100, 'm': 30, 'color': 'RainbowDash'},
        {'Background': bg_black, 'n': 100, 'm': 30, 'color': 'MetroUI'},
        {'Background': bg_black, 'n': 100, 'm': 30, 'color': 'ProgramCat'},
    ]
    return append_dflts(a, 'SMEARS#2', mazy2, w, h)

def predef_mazy3(w, h):
    a = [
        {'Background': bg_white, 'n': 30, 'color': 'happy'},
        {'Background': bg_white, 'n': 30, 'color': 'wryb'},

        {'Background': bg_white, 'n': 80, 'color': 'happy'},
        {'Background': bg_white, 'n': 80, 'color': 'wryb'},
        {'Background': bg_white, 'n': 80, 'color': 'BeachTowels'},
        {'Background': bg_white, 'n': 80, 'color': 'SkinTones'},
        {'Background': bg_white, 'n': 80, 'color': 'Rainbow'},

        {'Background': bg_yellow, 'n': 30, 'color': 'red'},
        {'Background': bg_yellow, 'n': 80, 'color': 'red'},
        {'Background': bg_black, 'n': 30, 'color': 'red'},
        {'Background': bg_black, 'n': 80, 'color': 'red'},
        {'Background': bg_black, 'n': 30, 'color': 'bw'},

        {'Background': bg_orange, 'n': 80, 'color': 'bwx'},

        {'Background': bg_white, 'n': 90, 'color': 'happy', 'addalpha': 50},
        {'Background': bg_white, 'n': 90, 'color': 'wryb', 'addalpha': 50},
        {'Background': bg_white, 'n': 90, 'color': 'BeachTowels', 'addalpha': 50},
        {'Background': bg_white, 'n': 90, 'color': 'SkinTones', 'addalpha': 50},
        {'Background': bg_white, 'n': 90, 'color': 'Rainbow', 'addalpha': 50},

        {'Background': bg_yellow, 'n': 90, 'color': 'red', 'addalpha': 50},
        {'Background': bg_black, 'n': 90, 'color': 'red', 'addalpha': 50},
        {'Background': bg_black, 'n': 90, 'color': 'bw', 'addalpha': 50},

        {'Background': bg_orange, 'n': 80, 'color': 'bwx', 'addalpha': 50},
    ]
    a1 = copy.deepcopy(a)
    a2 = copy.deepcopy(a)
    a3 = copy.deepcopy(a)
    for i in range(len(a)):
        a1[i]['mode'] = 'center'
        a2[i]['mode'] = 'xcenter'
        a3[i]['mode'] = 'rnd'
    a = np.concatenate((a1, a2, a3), axis=0)
    return append_dflts(a, 'SMEARS#3', mazy3, w, h)

def predef_mazy4(w, h):
    a = [
        {'Background': bg_white, 'n': 5, 'mode': 'center', 'color': 'happy'},
        {'Background': bg_white, 'n': 5, 'mode': 'center', 'color': 'wryb'},
        {'Background': bg_white, 'n': 4, 'mode': 'center', 'color': 'bgo'},
        #{'Background': bg_white, 'n': 8, 'mode': 'center', 'color': 'avatar'}, # lame
        #{'Background': bg_white, 'n': 8, 'mode': 'center', 'color': 'psych'}, # lame
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

        {'Background': bg_yellow, 'n': 5, 'mode': 'center', 'color': 'red'},
        {'Background': bg_yellow, 'n': 5, 'mode': 'center', 'color': 'rg'},
        {'Background': bg_yellow, 'n': 5, 'mode': 'center', 'color': 'green'},
        {'Background': bg_yellow, 'n': 4, 'mode': 'center', 'color': 'bg'},
        {'Background': bg_black, 'n': 5, 'mode': '', 'color': 'red'},
        {'Background': (128, 0, 0), 'n': 20, 'mode': '', 'color': 'red'}, # ?
        {'Background': bg_black, 'n': 3, 'mode': 'center', 'color': 'red'},
        {'Background': bg_black, 'n': 8, 'mode': 'center', 'color': 'bw'},

        {'Background': bg_gray, 'n': 11, 'mode': 'center', 'color': 'happy'},
        {'Background': bg_gray, 'n': 11, 'mode': 'center', 'color': 'wryb'},
        {'Background': (96,96,80), 'n': 11, 'mode': 'center', 'color': 'bgo'},
        {'Background': bg_gray, 'n': 11, 'mode': 'center', 'color': 'BeachTowels'},

        {'Background': bg_gray, 'n': 11, 'mode': 'center', 'color': 'happy', 'sc': 2.6},
        {'Background': bg_gray, 'n': 11, 'mode': 'center', 'color': 'wryb', 'sc': 2.6},
        {'Background': (96,96,80), 'n': 11, 'mode': 'center', 'color': 'bgo', 'sc': 2.6},
        {'Background': bg_gray, 'n': 11, 'mode': 'center', 'color': 'BeachTowels', 'sc': 2.6},
        
        {'Background': bg_gray, 'n': 100, 'mode': 'center', 'color': 'wryb', 'addalpha': 80, 'sc': 0.3}, # test
        {'Background': bg_gray, 'n': 100, 'mode': 'center', 'color': 'BeachTowels', 'addalpha': 80, 'sc': 0.3}, # test
        {'Background': bg_gray, 'n': 100, 'mode': 'center', 'color': 'MetroUI', 'addalpha': 80, 'sc': 0.3}, # test

        {'Background': bg_gray, 'n': 100, 'mode': 'center', 'color': 'wryb', 'addalpha': 90, 'sc': 0.15}, # test
        {'Background': bg_gray, 'n': 100, 'mode': 'center', 'color': 'BeachTowels', 'addalpha': 90, 'sc': 0.15}, # test
        {'Background': bg_gray, 'n': 100, 'mode': 'center', 'color': 'MetroUI', 'addalpha': 90, 'sc': 0.15}, # test
    ]
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
    return append_dflts(a, 'SMEARS#5', mazy5, w, h)

def predef_mazy6(w, h):
    a = [
        {'Background': bg_black, 'mode': 'red_const', 'n': 18, 'useblack': True},
        {'Background': bg_black, 'mode': 'blue_const', 'n': 18, 'useblack': True},
        {'Background': bg_black, 'mode': 'blue', 'n': 18, 'useblack': True},
        {'Background': bg_black, 'mode': 'blueMap', 'n': 18, 'useblack': True},
        {'Background': bg_black, 'mode': 'white_const', 'n': 18, 'useblack': True},
        {'Background': bg_black, 'mode': 'rg', 'n': 18, 'useblack': True},
        {'Background': bg_black, 'mode': 'gb', 'n': 18, 'useblack': True},
        {'Background': bg_black, 'mode': 'happy', 'n': 18, 'useblack': True},

        {'Background': bg_black, 'mode': 'happy', 'n': 18+12, 'useblack': False},
        {'Background': bg_black, 'mode': 'bwx', 'n': 18+12, 'useblack': False},
        {'Background': bg_black, 'mode': 'psych', 'n': 18+12, 'useblack': False},
        {'Background': bg_white, 'mode': 'BeachTowels', 'n': 18+12, 'useblack': False},
        {'Background': bg_white, 'mode': 'MoonlightBytes6', 'n': 18+12, 'useblack': False},
        {'Background': bg_white, 'mode': 'RainbowDash', 'n': 18+12, 'useblack': False},
        {'Background': bg_white, 'mode': 'Google', 'n': 18+12, 'useblack': False},
        {'Background': bg_white, 'mode': 'MetroUI', 'n': 18+12, 'useblack': False},
        {'Background': bg_white, 'mode': 'ProgramCat', 'n': 18+12, 'useblack': False},
    ]
    return append_dflts(a, 'SMEARS#6', mazy6, w, h)

def predef_mazy7(w, h):
    bk = (0x84, 0x8B, 0x9B)
    a = [
        {'Background': bk, 'cnt': 500,  'cmode': 'rnd', 'mode': 'const'},
        {'Background': bk, 'cnt': 2000, 'cmode': 'rnd', 'mode': 'const'},

        {'Background': bk, 'cnt': 200,  'cmode': 'std', 'mode': 'decp'},
        {'Background': bk, 'cnt': 100,  'cmode': 'std', 'mode': 'decp'},
        {'Background': bk, 'cnt': 50,   'cmode': 'std', 'mode': 'decp'},
        {'Background': bk, 'cnt': 10,   'cmode': 'std', 'mode': 'decp'},
        {'Background': bk, 'cnt': 200,  'cmode': 'std', 'mode': 'dec'},
        {'Background': bk, 'cnt': 100,  'cmode': 'std', 'mode': 'dec'},
        {'Background': bk, 'cnt': 50,   'cmode': 'std', 'mode': 'dec'},
        {'Background': bk, 'cnt': 10,   'cmode': 'std', 'mode': 'dec'},
        {'Background': bk, 'cnt': 200,  'cmode': 'inv', 'mode': 'dec'},
        {'Background': bk, 'cnt': 100,  'cmode': 'inv', 'mode': 'dec'},
        {'Background': bk, 'cnt': 50,   'cmode': 'inv', 'mode': 'dec'},
        {'Background': bk, 'cnt': 10,   'cmode': 'inv', 'mode': 'dec'},
        {'Background': bk, 'cnt': 200,  'cmode': 'rnd', 'mode': 'dec'},
        {'Background': bk, 'cnt': 100,  'cmode': 'rnd', 'mode': 'dec'},
        {'Background': bk, 'cnt': 50,   'cmode': 'rnd', 'mode': 'dec'},
        {'Background': bk, 'cnt': 10,   'cmode': 'rnd', 'mode': 'dec'},

        {'Background': bk, 'cnt': 200,  'cmode': 'color', 'mode': 'dec'},
        {'Background': bk, 'cnt': 100,  'cmode': 'color', 'mode': 'dec'},
        {'Background': bk, 'cnt': 50,   'cmode': 'color', 'mode': 'dec'},
        {'Background': bk, 'cnt': 10,   'cmode': 'color', 'mode': 'dec'},

        {'Background': bk, 'cnt': 200,  'cmode': 'color', 'mode': 'dec', 'addalpha': 99},
        {'Background': bk, 'cnt': 100,  'cmode': 'color', 'mode': 'dec', 'addalpha': 99},
        {'Background': bk, 'cnt': 50,   'cmode': 'color', 'mode': 'dec', 'addalpha': 99},
        {'Background': bk, 'cnt': 10,   'cmode': 'color', 'mode': 'dec', 'addalpha': 99},

        {'Background': bk, 'cnt': 200,  'cmode': 'wryb', 'mode': 'dec'},
        {'Background': bk, 'cnt': 100,  'cmode': 'wryb', 'mode': 'dec'},
        {'Background': bk, 'cnt': 50,   'cmode': 'wryb', 'mode': 'dec'},
        {'Background': bk, 'cnt': 10,   'cmode': 'wryb', 'mode': 'dec'},

        {'Background': bk, 'cnt': 200,  'cmode': 'wryb', 'mode': 'dec', 'addalpha': 99},
        {'Background': bk, 'cnt': 100,  'cmode': 'wryb', 'mode': 'dec', 'addalpha': 99},
        {'Background': bk, 'cnt': 50,   'cmode': 'wryb', 'mode': 'dec', 'addalpha': 99},
        {'Background': bk, 'cnt': 10,   'cmode': 'wryb', 'mode': 'dec', 'addalpha': 99},

        # new tmp
        {'Background': bk, 'cnt': 200,  'cmode': 'BeachTowels', 'mode': 'dec'},
        {'Background': bk, 'cnt': 100,  'cmode': 'BeachTowels', 'mode': 'dec'},
        {'Background': bk, 'cnt': 50,   'cmode': 'BeachTowels', 'mode': 'dec'},
        {'Background': bk, 'cnt': 10,   'cmode': 'BeachTowels', 'mode': 'dec'},

        {'Background': bk, 'cnt': 200,  'cmode': 'MoonlightBytes6', 'mode': 'dec'},
        {'Background': bk, 'cnt': 100,  'cmode': 'MoonlightBytes6', 'mode': 'dec'},
        {'Background': bk, 'cnt': 50,   'cmode': 'MoonlightBytes6', 'mode': 'dec'},
        {'Background': bk, 'cnt': 10,   'cmode': 'MoonlightBytes6', 'mode': 'dec'},

        # new new 202105
        {'Background': bk, 'cnt': 2000, 'cmode': 'BeachTowels', 'mode': 'const'},
        {'Background': bk, 'cnt': 2000, 'cmode': 'MoonlightBytes6', 'mode': 'const'},
        {'Background': bk, 'cnt': 2000, 'cmode': 'BeachTowels', 'mode': 'const', 'addalpha': 99},
        {'Background': bk, 'cnt': 2000, 'cmode': 'MoonlightBytes6', 'mode': 'const', 'addalpha': 99},
        {'Background': bk, 'cnt': 2000, 'cmode': 'BeachTowels', 'mode': 'const', 'addalpha': 99, 'div': 10},
        {'Background': bk, 'cnt': 2000, 'cmode': 'MoonlightBytes6', 'mode': 'const', 'addalpha': 99, 'div': 10},
        {'Background': bk, 'cnt': 2000, 'cmode': 'BeachTowels', 'mode': 'const', 'addalpha': 99, 'div': 5},
        {'Background': bk, 'cnt': 2000, 'cmode': 'MoonlightBytes6', 'mode': 'const', 'addalpha': 99, 'div': 5},
        {'Background': bk, 'cnt': 50, 'cmode': 'BeachTowels', 'mode': 'const', 'addalpha': 99, 'div': 5},
        {'Background': bk, 'cnt': 50, 'cmode': 'MoonlightBytes6', 'mode': 'const', 'addalpha': 99, 'div': 5},
    ]
    return append_dflts(a, 'SMEARS#7', mazy7, w, h)

def predef_mazy8(w, h):
    a = [
        {'Background': bg_white, 'xcnt': 5, 'ycnt': 5, 'color': 'happy'},
        {'Background': bg_white, 'xcnt': 5, 'ycnt': 10, 'color': 'happy'},
        {'Background': bg_white, 'xcnt': 5, 'ycnt': 3, 'color': 'happy'},
        {'Background': bg_white, 'xcnt': 15, 'ycnt': 5, 'color': 'happy'},
        {'Background': bg_white, 'xcnt': 31, 'ycnt': 20, 'color': 'happy'},
        {'Background': bg_white, 'xcnt': 3, 'ycnt': 20, 'color': 'happy'},

        {'Background': bg_white, 'xcnt': 5, 'ycnt': 5, 'color': 'wryb'},
        {'Background': bg_white, 'xcnt': 5, 'ycnt': 10, 'color': 'wryb'},
        {'Background': bg_white, 'xcnt': 5, 'ycnt': 3, 'color': 'wryb'},
        {'Background': bg_white, 'xcnt': 15, 'ycnt': 5, 'color': 'wryb'},
        {'Background': bg_white, 'xcnt': 31, 'ycnt': 20, 'color': 'wryb'},
        {'Background': bg_white, 'xcnt': 3, 'ycnt': 20, 'color': 'wryb'},

        {'Background': bg_white, 'xcnt': 5, 'ycnt': 5, 'color': 'BeachTowels'},
        {'Background': bg_white, 'xcnt': 5, 'ycnt': 10, 'color': 'BeachTowels'},
        {'Background': bg_white, 'xcnt': 5, 'ycnt': 3, 'color': 'BeachTowels'},
        {'Background': bg_white, 'xcnt': 15, 'ycnt': 5, 'color': 'BeachTowels'},
        {'Background': bg_white, 'xcnt': 31, 'ycnt': 20, 'color': 'BeachTowels'},
        {'Background': bg_white, 'xcnt': 3, 'ycnt': 20, 'color': 'BeachTowels'},

        {'Background': bg_white, 'xcnt': 5, 'ycnt': 5, 'color': 'MoonlightBytes6'},
        {'Background': bg_white, 'xcnt': 5, 'ycnt': 10, 'color': 'MoonlightBytes6'},
        {'Background': bg_white, 'xcnt': 5, 'ycnt': 3, 'color': 'MoonlightBytes6'},
        {'Background': bg_white, 'xcnt': 15, 'ycnt': 5, 'color': 'MoonlightBytes6'},
        {'Background': bg_white, 'xcnt': 31, 'ycnt': 20, 'color': 'MoonlightBytes6'},
        {'Background': bg_white, 'xcnt': 3, 'ycnt': 20, 'color': 'MoonlightBytes6'},

        {'Background': bg_white, 'xcnt': 5, 'ycnt': 5, 'color': 'MetroUI'},
        {'Background': bg_white, 'xcnt': 5, 'ycnt': 10, 'color': 'MetroUI'},
        {'Background': bg_white, 'xcnt': 5, 'ycnt': 3, 'color': 'MetroUI'},
        {'Background': bg_white, 'xcnt': 15, 'ycnt': 5, 'color': 'MetroUI'},
        {'Background': bg_white, 'xcnt': 31, 'ycnt': 20, 'color': 'MetroUI'},
        {'Background': bg_white, 'xcnt': 3, 'ycnt': 20, 'color': 'MetroUI'},

        {'Background': bg_white, 'xcnt': 5, 'ycnt': 5, 'color': 'ProgramCat'},
        {'Background': bg_white, 'xcnt': 5, 'ycnt': 10, 'color': 'ProgramCat'},
        {'Background': bg_white, 'xcnt': 5, 'ycnt': 3, 'color': 'ProgramCat'},
        {'Background': bg_white, 'xcnt': 15, 'ycnt': 5, 'color': 'ProgramCat'},
        {'Background': bg_white, 'xcnt': 31, 'ycnt': 20, 'color': 'ProgramCat'},
        {'Background': bg_white, 'xcnt': 3, 'ycnt': 20, 'color': 'ProgramCat'},
    ]
    return append_dflts(a, 'SMEARS#8', mazy8, w, h)

def predef_mazy9(w, h):
    v = float(h)/8
    v2 = float(h)/2
    v3 = float(h)/32
    a = [
        {'n': 16, 'Background': bg_black, 'color': 'happy', 'v': 0, 'rndc': True},
        {'n': 20, 'Background': bg_black, 'color': 'happy', 'v': 0, 'rndc': True},
        {'n': 60, 'Background': bg_black, 'color': 'happy', 'v': 0, 'rndc': True},
        {'n': 128, 'Background': bg_black, 'color': 'happy', 'v': 0, 'rndc': True},
        {'n': 16, 'Background': bg_black, 'color': 'psych', 'v': 0, 'rndc': True},
        {'n': 20, 'Background': bg_black, 'color': 'psych', 'v': 0, 'rndc': True},
        {'n': 60, 'Background': bg_black, 'color': 'psych', 'v': 0, 'rndc': True},
        {'n': 128, 'Background': bg_black, 'color': 'psych', 'v': 0, 'rndc': True},

        {'n': 16, 'Background': bg_black, 'color': 'happy', 'v': 0},
        {'n': 20, 'Background': bg_black, 'color': 'happy', 'v': 0},
        {'n': 64, 'Background': bg_black, 'color': 'happy', 'v': 0},
        {'n': 128, 'Background': bg_black, 'color': 'happy', 'v': 0},
        {'n': 16, 'Background': bg_black, 'color': 'psych', 'v': 0},
        {'n': 20, 'Background': bg_black, 'color': 'psych', 'v': 0},
        {'n': 64, 'Background': bg_black, 'color': 'psych', 'v': 0},
        {'n': 128, 'Background': bg_black, 'color': 'psych', 'v': 0},
           
        {'n': 16, 'Background': bg_black, 'color': 'red', 'v': 0},
        {'n': 64, 'Background': bg_black, 'color': 'red', 'v': 0},
        {'n': 128, 'Background': bg_black, 'color': 'red', 'v': 0},
        {'n': 16, 'Background': bg_black, 'color': 'rg', 'v': 0},
        {'n': 64, 'Background': bg_black, 'color': 'rg', 'v': 0},
        {'n': 128, 'Background': bg_black, 'color': 'rg', 'v': 0},
        {'n': 16, 'Background': bg_black, 'color': 'bw', 'v': 0},
        {'n': 64, 'Background': bg_black, 'color': 'bw', 'v': 0},
        {'n': 128, 'Background': bg_black, 'color': 'bw', 'v': 0},

        {'n': 20, 'Background': bg_black, 'color': 'happy', 'v': v, 'rndc': True},
        {'n': 60, 'Background': bg_black, 'color': 'happy', 'v': v, 'rndc': True},
        {'n': 120, 'Background': bg_black, 'color': 'happy', 'v': v, 'rndc': True},
        {'n': 20, 'Background': bg_black, 'color': 'psych', 'v': v, 'rndc': True},
        {'n': 60, 'Background': bg_black, 'color': 'psych', 'v': v, 'rndc': True},
        {'n': 120, 'Background': bg_black, 'color': 'psych', 'v': v, 'rndc': True},

        {'n': 20, 'Background': bg_black, 'color': 'happy', 'v': v},
        {'n': 60, 'Background': bg_black, 'color': 'happy', 'v': v},
        {'n': 120, 'Background': bg_black, 'color': 'happy', 'v': v},
        {'n': 20, 'Background': bg_black, 'color': 'psych', 'v': v},
        {'n': 60, 'Background': bg_black, 'color': 'psych', 'v': v},
        {'n': 120, 'Background': bg_black, 'color': 'psych', 'v': v},

        {'n': 20, 'Background': bg_black, 'color': 'red', 'v': v},
        {'n': 60, 'Background': bg_black, 'color': 'red', 'v': v},
        {'n': 120, 'Background': bg_black, 'color': 'red', 'v': v},
        {'n': 20, 'Background': bg_black, 'color': 'rg', 'v': v},
        {'n': 60, 'Background': bg_black, 'color': 'rg', 'v': v},
        {'n': 120, 'Background': bg_black, 'color': 'rg', 'v': v},
        {'n': 20, 'Background': bg_black, 'color': 'bw', 'v': v},
        {'n': 60, 'Background': bg_black, 'color': 'bw', 'v': v},
        {'n': 120, 'Background': bg_black, 'color': 'bw', 'v': v},

        {'n': 20, 'Background': bg_black, 'color': 'happy', 'v': v2, 'rndc': True},
        {'n': 60, 'Background': bg_black, 'color': 'happy', 'v': v2, 'rndc': True},
        {'n': 120, 'Background': bg_black, 'color': 'happy', 'v': v2, 'rndc': True},
        {'n': 20, 'Background': bg_black, 'color': 'psych', 'v': v2, 'rndc': True},
        {'n': 60, 'Background': bg_black, 'color': 'psych', 'v': v2, 'rndc': True},
        {'n': 120, 'Background': bg_black, 'color': 'psych', 'v': v2, 'rndc': True},
        {'n': 20, 'Background': bg_black, 'color': 'BeachTowels', 'v': v2, 'rndc': True},
        {'n': 60, 'Background': bg_black, 'color': 'BeachTowels', 'v': v2, 'rndc': True},
        {'n': 120, 'Background': bg_black, 'color': 'BeachTowels', 'v': v2, 'rndc': True},

        {'n': 20, 'Background': bg_black, 'color': 'happy', 'v': v3, 'rndc': True},
        {'n': 60, 'Background': bg_black, 'color': 'happy', 'v': v3, 'rndc': True},
        {'n': 120, 'Background': bg_black, 'color': 'happy', 'v': v3, 'rndc': True},
        {'n': 20, 'Background': bg_black, 'color': 'psych', 'v': v3, 'rndc': True},
        {'n': 60, 'Background': bg_black, 'color': 'psych', 'v': v3, 'rndc': True},
        {'n': 120, 'Background': bg_black, 'color': 'psych', 'v': v3, 'rndc': True},
        {'n': 20, 'Background': bg_black, 'color': 'BeachTowels', 'v': v3, 'rndc': True},
        {'n': 60, 'Background': bg_black, 'color': 'BeachTowels', 'v': v3, 'rndc': True},
        {'n': 120, 'Background': bg_black, 'color': 'BeachTowels', 'v': v3, 'rndc': True},

        # todo: other like that too
        {'n': 360, 'Background': bg_black, 'color': 'BeachTowels', 'v': v, 'rndc': True},
        {'n': 360, 'Background': bg_black, 'color': 'BeachTowels', 'v': v2, 'rndc': True},
        {'n': 360, 'Background': bg_black, 'color': 'BeachTowels', 'v': v3, 'rndc': True},
    ]
    return append_dflts(a, 'SMEARS#9', mazy9, w, h)

def predef_mazy10(w, h):
    bk = (0x84, 0x8B, 0x9B)
    a = [
            # new test n=3 also ok
            #{'Background': bk, 'n': 1, 'penw': 2, 'color': 'blue_const', 'mode': 'fill', 'complexity': 1000, 'open': False, 'addalpha': 90},
            #{'Background': bk, 'n': 3, 'penw': 2, 'color': 'blue_const', 'mode': 'fill', 'complexity': 1000, 'open': False, 'addalpha': 90},

            #{'Background': bk, 'n': 15, 'penw': 32, 'color': 'happy', 'mode': 'line', 'complexity': 70+130, 'open': False},

            {'Background': bk, 'n': 30, 'penw': 8, 'color': 'happy', 'mode': 'line', 'complexity': 70, 'open': False},
            {'Background': bk, 'n': 40, 'penw': 8, 'color': 'rg', 'mode': 'line', 'complexity': 70, 'open': False},
            {'Background': bk, 'n': 40, 'penw': 8, 'color': 'red', 'mode': 'line', 'complexity': 70, 'open': False},
            {'Background': bk, 'n': 40, 'penw': 8, 'color': 'wryb', 'mode': 'line', 'complexity': 70, 'open': False},

            {'Background': bk, 'n': 30, 'penw': 8, 'color': 'happy', 'mode': 'line', 'complexity': 70, 'open': True},
            {'Background': bk, 'n': 40, 'penw': 8, 'color': 'rg', 'mode': 'line', 'complexity': 70, 'open': True},
            {'Background': bk, 'n': 40, 'penw': 8, 'color': 'red', 'mode': 'line', 'complexity': 70, 'open': True},
            {'Background': bk, 'n': 40, 'penw': 8, 'color': 'wryb', 'mode': 'line', 'complexity': 70, 'open': True},

            {'Background': bk, 'n': 30, 'penw': 8, 'color': 'happy', 'mode': 'line', 'complexity': 70, 'open': True, 'addalpha': 90},
            {'Background': bk, 'n': 40, 'penw': 8, 'color': 'rg', 'mode': 'line', 'complexity': 70, 'open': True, 'addalpha': 90},
            {'Background': bk, 'n': 40, 'penw': 8, 'color': 'red', 'mode': 'line', 'complexity': 70, 'open': True, 'addalpha': 90},
            {'Background': bk, 'n': 40, 'penw': 8, 'color': 'wryb', 'mode': 'line', 'complexity': 70, 'open': True, 'addalpha': 90},

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
        {'Background': bg_black, 'n': 8, 'color': 'happy'},
        {'Background': bg_black, 'n': 16, 'color': 'happy'},
        {'Background': bg_black, 'n': 64, 'color': 'happy'},
        {'Background': bg_black, 'n': 8, 'color': 'BeachTowels'},
        {'Background': bg_black, 'n': 16, 'color': 'BeachTowels'},
        {'Background': bg_black, 'n': 64, 'color': 'BeachTowels'},
        {'Background': bg_black, 'n': 8, 'color': 'MoonlightBytes6'},
        {'Background': bg_black, 'n': 16, 'color': 'MoonlightBytes6'},
        {'Background': bg_black, 'n': 64, 'color': 'MoonlightBytes6'},
        {'Background': bg_black, 'n': 8, 'color': 'Rainbow'},
        {'Background': bg_black, 'n': 16, 'color': 'Rainbow'},
        {'Background': bg_black, 'n': 64, 'color': 'Rainbow'},
        {'Background': bg_black, 'n': 8, 'color': 'MetroUI'},
        {'Background': bg_black, 'n': 16, 'color': 'MetroUI'},
        {'Background': bg_black, 'n': 64, 'color': 'MetroUI'},
        {'Background': bg_black, 'n': 8, 'color': 'ProgramCat'},
        {'Background': bg_black, 'n': 16, 'color': 'ProgramCat'},
        {'Background': bg_black, 'n': 64, 'color': 'ProgramCat'},
        {'Background': bg_black, 'n': 8, 'color': 'wryb'},
        {'Background': bg_black, 'n': 16, 'color': 'wryb'},
        {'Background': bg_black, 'n': 64, 'color': 'wryb'},
        {'Background': bg_black, 'n': 8, 'color': 'yorb'},
        {'Background': bg_black, 'n': 16, 'color': 'yorb'},
        {'Background': bg_black, 'n': 64, 'color': 'yorb'},
    ]
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
        {'Background': bg_white, 'n': 6, 'color': bg_black},
        {'Background': bg_white, 'n': 12, 'color': bg_black},
        {'Background': bg_white, 'n': 24, 'color': bg_black},
        {'Background': bg_white, 'n': 36, 'color': bg_black},
        {'Background': bg_white, 'n': 48, 'color': bg_black},
    ]
    a1 = copy.deepcopy(a)
    a2 = copy.deepcopy(a)
    a3 = copy.deepcopy(a)
    a4 = copy.deepcopy(a)
    for i in range(len(a)):
        a1[i]['m'] = 4
        a2[i]['m'] = 8
        a3[i]['m'] = 32
        a4[i]['m'] = 100
    a = np.concatenate((a1, a2, a3, a4), axis=0)
    a_ = [{'Background': bg_white, 'n': 24, 'm': 32, 'color': bg_black, 'div': 5}] # 'special' case (test)
    a = np.concatenate((a, a_), axis=0)
    return append_dflts(a, 'SMEARS#14', mazy14, w, h)

def predef_mazy15(w, h):
    a = [
        {'Background': bg_white, 'n': 8, 'color': bg_black, 'style': 'circle'},
        {'Background': bg_white, 'n': 16, 'color': bg_black, 'style': 'circle'},
        {'Background': bg_white, 'n': 32, 'color': bg_black, 'style': 'circle'},
        {'Background': bg_white, 'n': 64, 'color': bg_black, 'style': 'circle'},
        {'Background': bg_white, 'n': 128, 'color': bg_black, 'style': 'circle'},
        # note: 'style': 'rect' - somehow not so cool
    ]
    a1 = copy.deepcopy(a)
    a2 = copy.deepcopy(a)
    a3 = copy.deepcopy(a)
    a7 = copy.deepcopy(a)
    a8 = copy.deepcopy(a)
    a9 = copy.deepcopy(a)
    a10 = copy.deepcopy(a)
    a11 = copy.deepcopy(a)
    a12 = copy.deepcopy(a)
    a13 = copy.deepcopy(a)
    a14 = copy.deepcopy(a)
    for i in range(len(a)):
        # a1 - a3 const offsets, a1 cool for n=16
        a1[i]['xs1'] = int(-w/10)
        a1[i]['ys1'] = int(-w/100)
        a1[i]['xs2'] = int(w/10)
        a1[i]['ys2'] = int(w/100)

        a2[i]['xs1'] = int(-w/50)
        a2[i]['ys1'] = int(-w/100)
        a2[i]['xs2'] = int(w/50)
        a2[i]['ys2'] = int(w/100)

        a3[i]['xs1'] = int(-w/20)
        a3[i]['ys1'] = int(w/20)
        a3[i]['xs2'] = int(w/20)
        a3[i]['ys2'] = int(-w/20)

        # linear - tested x for c2 only
        a7[i]['mode'] = 'linear'
        a7[i]['xs2v'] = int(w/25)
        a7[i]['ys2v'] = 0
        a8[i]['mode'] = 'linear'
        a8[i]['xs2v'] = int(w/50)
        a8[i]['ys2v'] = 0
        a9[i]['mode'] = 'linear'
        a9[i]['xs2v'] = int(w/100)
        a9[i]['ys2v'] = 0
        a10[i]['mode'] = 'linear'
        a10[i]['xs2v'] = int(w/200)
        a10[i]['ys2v'] = 0

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
    a = np.concatenate((a1, a2, a3, a7, a8, a9, a10, a11, a12, a13, a14), axis=0)
    return append_dflts(a, 'SMEARS#15', mazy15, w, h)

def predef_mazy16(w, h):
    a = [
        {'Background': bg_white, 'n': 24, 'color': bg_black, 'rcoef': 1.0, 'acoef': 1.0, 'rscale': 1.0},
        {'Background': bg_white, 'n': 48, 'color': bg_black, 'rcoef': 1.0, 'acoef': 1.0, 'rscale': 1.0},
        {'Background': bg_white, 'n': 96, 'color': bg_black, 'rcoef': 1.0, 'acoef': 1.0, 'rscale': 1.0},
        {'Background': bg_white, 'n': 256, 'color': bg_black, 'rcoef': 1.0, 'acoef': 1.0, 'rscale': 1.0},
    ]
    a1 = copy.deepcopy(a)
    a2 = copy.deepcopy(a)
    for i in range(len(a)):
        a1[i]['rcoef'] = 1.5
        a2[i]['rcoef'] = 3.0
    a = np.concatenate((a1, a2), axis=0)
    a1 = copy.deepcopy(a)
    a2 = copy.deepcopy(a)
    a3 = copy.deepcopy(a)
    for i in range(len(a)):
        a1[i]['acoef'] = 1.0 #note: dflt
        a2[i]['acoef'] = 7.0
        a3[i]['acoef'] = 19.0
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
    return append_dflts(a, 'SMEARS#16', mazy16, w, h)

def predef_mazy17(w, h):
    a = [
        {'Background': bg_white, 'n': 90, 'v': int(w/30), 'color': 'happy'},
        {'Background': bg_white, 'n': 90, 'v': int(w/30), 'color': 'happy', 'addalpha': 60},
        {'Background': bg_white, 'n': 90, 'v': int(w/30), 'color': 'happy', 'addalpha': 30},
        {'Background': bg_white, 'n': 90, 'v': int(w/30), 'color': 'BeachTowels'},
        {'Background': bg_white, 'n': 90, 'v': int(w/30), 'color': 'BeachTowels', 'addalpha': 90},
        {'Background': bg_white, 'n': 150, 'v': int(w/200), 'color': 'BeachTowels'},
        {'Background': bg_white, 'n': 150, 'v': int(w/200), 'color': 'BeachTowels', 'addalpha': 50},
        {'Background': bg_black, 'n': 90, 'v': int(w/30), 'color': 'bw'},
        {'Background': bg_black, 'n': 90, 'v': int(w/30), 'color': 'wryb'},
        {'Background': bg_black, 'n': 90, 'v': int(w/30), 'color': 'Number3'},
    ]
    return append_dflts(a, 'SMEARS#17', mazy17, w, h)

def predef_mazy18(w, h):
    a = [
        {'Background': bg_white, 'n': 40, 'm': 120, 'v': 50},
        {'Background': bg_white, 'n': 60, 'm': 16, 'v': 80},
        {'Background': bg_white, 'n': 90, 'm': 30, 'v': 20},
        {'Background': bg_white, 'n': 90, 'm': 400, 'v': 100},
        {'Background': bg_white, 'n': 120, 'm': 40, 'v': 20},
        {'Background': bg_white, 'n': 160, 'm': 40, 'v': 20, 'r0v': 250},
    ]
    a1 = copy.deepcopy(a)
    a2 = copy.deepcopy(a)
    a3 = copy.deepcopy(a)
    for i in range(len(a)):
        a1[i]['color'] = 'happy'
        a2[i]['color'] = 'yorb'
        a3[i]['color'] = 'BeachTowels'
    a = np.concatenate((a1, a2, a3), axis=0)
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
    a = [
        {'Background': bg_black, 'n': 1, 'mode': '1'},
        {'Background': bg_black, 'n': 1, 'mode': '2'},
    ]
    return append_dflts(a, 'SMEARS#20', mazy20, w, h)

#def predef_mazy21(w, h):
#def predef_mazy22(w, h):
#def predef_mazy23(w, h):
#def predef_mazy24(w, h):
#def predef_mazy25(w, h):

def enum_defs():
    suma = 0
    for k, v in predefs.items():    #note: py3
        cnt = len(v(0, 0))
        suma += cnt
        print(k, ':', cnt)
    # todo: sort it
    print('total:', suma)

# all predefs
predefs = {'mazy01': predef_mazy1, 'mazy02': predef_mazy2, 'mazy03': predef_mazy3, 'mazy04': predef_mazy4,
           'mazy05': predef_mazy5, 'mazy06': predef_mazy6, 'mazy07': predef_mazy7, 'mazy08': predef_mazy8,
           'mazy09': predef_mazy9, 'mazy10': predef_mazy10, 'mazy11': predef_mazy11, 'mazy12': predef_mazy12,
           'mazy13': predef_mazy13, 'mazy14': predef_mazy14, 'mazy15': predef_mazy15, 'mazy16': predef_mazy16,
           'mazy17': predef_mazy17, 'mazy18': predef_mazy18, 'mazy19': predef_mazy19, 'mazy20': predef_mazy20,
           'life': predef_life, 'lissajous': predef_lissajous, 'astro': predef_astro, 'mandelbrot': predef_mandelbrot,
           'waves01': predef_waves1,'waves02': predef_waves2, 'waves03': predef_waves3, 
           }

# all names
predef_names = [
        'mazy01', 'mazy02', 'mazy03', 'mazy04',  'mazy05', 'mazy06', 'mazy07', 'mazy08',
        'mazy09', 'mazy10', 'mazy11', 'mazy12', 'mazy13', 'mazy14', 'mazy15', 'mazy16',
        'mazy17', 'mazy18', 'mazy19', 'mazy20',
        'astro', 'life', 'lissajous', 'mandelbrot', 'waves01', 'waves02', 'waves03'
        ]

# EOF
