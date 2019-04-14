#! /usr/bin/env python
# -*- coding: utf-8 -*-

# paint algorithms (artificial artist) in Python - WWW CGI demo
# (c)2018-2019 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz
# https://pillow.readthedocs.io/en/3.1.x/reference/ImageDraw.html
# cre: 20181019
# upd; 20181020, 21
# upd; 20190118, 19
# upd; 20190329, 30
# upd; 20190414

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
from pyart_defs import *


form = cgi.FieldStorage()
if "what" in form:
    what = form["what"].value
else:
    what = ""
if "canvas" in form:
    ca = form["canvas"].value
    canvas = get_canvas(ca)
else:
    canvas = get_canvas('800')
if "n" in form:
    n = int(form["n"].value)-1
    if n < 0:
        n = 0
else:
    n = 0

w, h = canvas
bw = False

if what == "smears1":
    p = predef_mazy1(w, h)
if what == "smears2":
    p = predef_mazy2(w, h)
if what == "smears3":
    p = predef_mazy3(w, h)
if what == "smears4":
    p = predef_mazy4(w, h)
if what == "smears5":
    p = predef_mazy5(w, h)
if what == "smears6":
    p = predef_mazy6(w, h)
if what == "smears7":
    p = predef_mazy7(w, h)
if what == "smears8":
    p = predef_mazy8(w, h)
if what == "smears9":
    p = predef_mazy9(w, h)
if what == "smears10":
    p = predef_mazy10(w, h)
if what == "smears11":
    p = predef_mazy11(w, h)
if what == "smears12":
    p = predef_mazy12(w, h)
if what == "smears13":
    p = predef_mazy13(w, h)
if what == "smears14":
    p = predef_mazy14(w, h)
if what == "smears15":
    p = predef_mazy15(w, h)
if what == "smears16":
    p = predef_mazy16(w, h)
if what == "life":
    p = predef_life(w, h)
if what == "lissajous":
    p = predef_lissajous(w, h)
if what == "astro":
    p = predef_astro(w, h)
if what == "waves":
    p = predef_waves(w, h)
if what == "mandelbrot":
    p = predef_mandelbrot(w, h)
    bw = True
if n >= len(p):
    n = len(p)-1
art_painter(p[n], '', 'cgi', bw)
