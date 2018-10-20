#! /usr/bin/env python
# -*- coding: utf-8 -*-

# paint algorithms (artificial artist) in Python - demo
# (c)2018 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz
# https://pillow.readthedocs.io/en/3.1.x/reference/ImageDraw.html
# cre: 20181019
# upd; 20181020

# TODO:
# - ?

import cgi
from drawtools import get_canvas, art_painter, get_cgi_par
from life1 import life
from lissajous import lissajous, lissajous_loop
from waves import *
from astroart import *


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

#if what == "astro":
    # ?

#if what == "?":
    # ?

#if what == "?":
    # ?
