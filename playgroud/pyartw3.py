#! /usr/bin/env python
# -*- coding: utf-8 -*-

# paint algorithms (artificial artist) in Python - WWW CGI demo
# (c)2018-2019 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz
# https://pillow.readthedocs.io/en/3.1.x/reference/ImageDraw.html
# cre: 20181019
# upd; 20181020, 21
# upd; 20190118, 19
# upd; 20190329, 30
# upd; 20190414, 17, 21, 26

# TODO:
# - ?

import cgi
from drawtools import *
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
if what in predefs:
    pr = predefs[what]
    p = pr(w, h)
if n >= len(p):
    n = len(p)-1
p[n]['alpha'] = True #test
art_painter(p[n], '', 'cgi')
