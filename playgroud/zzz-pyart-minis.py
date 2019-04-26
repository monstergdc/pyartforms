#! /usr/bin/env python
# -*- coding: utf-8 -*-

# paint algorithms (artificial artist) in Python - demo
# (c)2018-2019 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz
# cre: 20181020
# upd: 20190105, 06, 13, 18, 19, 22
# upd: 20190302, 03, 30
# upd: 20190414, 17, 21, 22, 24, 26

# miniatures renderer


import os
from datetime import datetime as dt
from drawtools import *
from pyart_defs import *


start_time = dt.now()
root = 'minis' #linux
if not os.path.exists(root):
    os.makedirs(root)
odir = root+'/' #linux


def do_mazy(cnt, w, h, odir, name):
    if name in predefs:
        pr = predefs[name]
        p = pr(w, h)
    #else: ?

    for n in range(cnt):
        for i in range(len(p)):
            p[i]['alpha'] = True #test
            art_painter(p[i], odir+'%s-%dx%d-%02d.png' % (p[i]['name'], w, h, i+1))

# --- go

w, h = get_canvas('256')
cnt = 1
predef_names1 = predef_names
#predef_names1 = ['mazy11']
for m in predef_names1:
    do_mazy(cnt, w, h, odir, m)
    
time_elapsed = dt.now() - start_time
print('ALL done. elapsed time: {}'.format(time_elapsed))

