#! /usr/bin/env python
# -*- coding: utf-8 -*-

# paint algorithms (artificial artist) in Python - demo
# (c)2018-2025 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz
# cre: 20181020
# upd: 20190105, 12, 13, 18, 19
# upd: 20190311, 30
# upd: 20190414, 21, 22, 24, 26
# upd: 20190606
# upd: 20200507, 10
# upd: 20210106, 20
# upd: 20210612
# upd: 20240224, 25
# upd: 20240512
# upd: 20240723
# upd: 20250205

# TODO:
# - ?


import os
from datetime import datetime as dt
from drawtools import get_canvas, art_painter
from pyart_defs import *
#import tracemalloc


#tracemalloc.start()
start_time = dt.now()
root = '!output-test'
if not os.path.exists(root):
    os.makedirs(root)
odir = root+'\\'



def do_mazy(cnt, w, h, odir, name):
    if name in predefs:
        pr = predefs[name]
        p = pr(w, h)
    else:
        print('name [%s] not in predefs?' % name)
        return
        # more?

#    snapshot1 = tracemalloc.take_snapshot()
    for n in range(cnt):
        tx = dt.now().strftime('%Y%m%d%H%M%S')
        for i in range(len(p)):
            p[i]['alpha'] = True #test
            art_painter(p[i], odir+'%s-%dx%d-%02d-%03d-%s.png' % (p[i]['name'], w, h, i+1, n+1, tx))
#    snapshot2 = tracemalloc.take_snapshot()
#    top_stats = snapshot2.compare_to(snapshot1, 'lineno')
#    print("[ Top 5 differences (in1) ]")
#    for stat in top_stats[:5]:
#        print(stat)
#    print("[ Top 5 lineno (in1) ]")
#    top_stats = snapshot2.statistics('lineno')
#    for stat in top_stats[:5]:
#        print(stat)
#    print("[ Top 5 traceback (in1) ]")
#    top_stats = snapshot2.statistics('traceback')
#    for stat in top_stats[:5]:
#        print(stat)

# --- 

#w, h = get_canvas('4A0') # can't even open locally
#w, h = get_canvas('2A0') # ?
#w, h = get_canvas('A0') # this?
#w, h = get_canvas('A1') # fin - this or A0
w, h = get_canvas('A2')
#w, h = get_canvas('A3')
#w, h = get_canvas('A4') # test - this

##w, h = get_canvas('A5') # test - also this 4 speed
#w, h = get_canvas('A6') # small - this
##w, h = get_canvas('A7')
#w, h = get_canvas('1024')

cnt = 1
#cnt = 2
#cnt = 3
#cnt = 4
#cnt = 5

enum_defs()

predef_names1 = predef_names

predef_names1 = [
        'mazy01', 'mazy02', 'mazy03', 'mazy04',  'mazy05', 'mazy06', 'mazy07', 'mazy08',
        'mazy09', 'mazy10', 'mazy11', 'mazy12', 'mazy13', 'mazy14', 'mazy15', 'mazy16',
        'mazy17', 'mazy18', 'mazy19', 'mazy20', 'mazy21', 'mazy22', 'mazy23', 'mazy24',
        'mazy25', 'mazy26', 'mazy27'
        ]
predef_names1 = ['mazy27']
predef_names1 = ['mazy12', 'mazy13', 'mazy14', 'mazy15', 'mazy16', 'mazy19', 'mazy20', 'mazy21', 'mazy23', 'mazy24']
predef_names1 = ['mazy31', 'mazy32']
predef_names1 = ['mazy31']
#predef_names1 = ['mazy32']
predef_names1 = ['mazy33']
#predef_names1 = ['mazy06']


for m in predef_names1:
    do_mazy(cnt, w, h, odir, m)

#do_mazy(cnt, w, h, odir, 'astro')
#do_mazy(cnt, w, h, odir, 'life')
#do_mazy(cnt, w, h, odir, 'lissajous')
#do_mazy(cnt, 700, 400, odir, 'mandelbrot')

time_elapsed = dt.now() - start_time
print('ALL done. elapsed time: {}'.format(time_elapsed))

#snapshot = tracemalloc.take_snapshot()
#top_stats = snapshot.statistics('lineno')
#print("[ Top ALL 20 ]")
#for stat in top_stats[:20]:
#    print(stat)
#top_stats = snapshot.statistics('traceback')
#for stat in top_stats[:20]:
#    print(stat)
