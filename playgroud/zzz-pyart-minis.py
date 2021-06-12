#! /usr/bin/env python
# -*- coding: utf-8 -*-

# paint algorithms (artificial artist) in Python - demo
# (c)2018-2021 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz
# miniatures renderer
# cre: 20181020
# upd: 20190105, 06, 13, 18, 19, 22
# upd: 20190302, 03, 30
# upd: 20190414, 17, 21, 22, 24, 26
# upd: 20210612


import os
from datetime import datetime as dt
from drawtools import *
from pyart_defs import *


def do_mazy(cnt, w, h, odir, name):
    if name in predefs:
        pr = predefs[name]
        p = pr(w, h)
    else:
        print('no "%s" in predefs!' % name)
        return
    for n in range(cnt):
        for i in range(len(p)):
            p[i]['alpha'] = True #test, old, remove of fix proper
            art_painter(p[i], odir+'%s-%dx%d-%02d.png' % (p[i]['name'], w, h, i+1))

def build_minis():
    start_time = dt.now()
    root = 'minis' #linux
    if not os.path.exists(root):
        os.makedirs(root)
    odir = root+'/' #linux
    w, h = get_canvas('256')
    predef_names1 = predef_names
    nn = 0
    for m in predef_names1:
        nn += len(m)
    print('base len:', len(predef_names1))
    for m in predef_names1:
        do_mazy(1, w, h, odir, m)
       
    time_elapsed = dt.now() - start_time
    print('ALL done. elapsed time: {}'.format(time_elapsed))

# --- go

build_minis()

