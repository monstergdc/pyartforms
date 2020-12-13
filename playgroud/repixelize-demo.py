#! /usr/bin/env python
# -*- coding: utf-8 -*-

# PyArtForms - Repixelize algorithm (artificial artist), v1.0, Python version - DEMO
# (c)2018-2020 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz
# cre: 20201208, 10, 11, 12, 13


import os, sys
from repixelize import *



def demo_looper(params, files, modes):
    ps = ""
    if 'postfix' in params:
        ps = "-"+str(params['postfix'])
    for fn in files:
        params['infile'] = indir+fn
        for mo in modes:
            params['mode'] = mo
            params['outfile'] = odir+fn+'-repixel-'+mo+ps+'.png'
            start_time1 = dt.now()
            repix(params)
            time_elapsed1 = dt.now() - start_time1
            print('elapsed time per one: {}'.format(time_elapsed1))

# ---

# poly test - nn * flux
def demo_poly_test():
    params = {'w': w, 'h': h, 'bk': (0, 0, 0), 'coef': 0.9, 'scale': 1.0, 'rnd': True, 'rmin': 78, 'rmax': 98}
    for nn in [3, 64]:
        for flux in [0, 5, 40, 100]:
            params['nn'] = nn
            params['flux'] = flux
            params['postfix'] = 'nn' + str(nn) + 'flux' + str(flux)
            demo_looper(params, files=['zz-zx-0011-1-cir.png'], modes=['poly'])

# brush test - nn * bs (100*100 interesting/unexpected)
def demo_brush_test():
    params = {'w': w, 'h': h, 'bk': (0, 0, 0), 'coef': 0.9, 'scale': 1.0, 'rnd': True, 'rmin': 78, 'rmax': 98}
    for nn in [5, 60, 100]:
        for bs in [5, 15, 40, 100]:
            params['nn'] = nn
            params['bs'] = bs
            params['postfix'] = 'nn' + str(nn) + 'bs' + str(bs)
            demo_looper(params, files=['zz-zx-0011-1-cir.png'], modes=['brush'])

# lines test - tr * lw * nn
def demo_lines_test():
    params = {'w': w, 'h': h, 'bk': (0, 0, 0), 'coef': 0.9, 'scale': 1.0, 'rnd': True, 'rmin': 78, 'rmax': 98}
    for tr in [60, 80]:
        for lw in [2, 6]:
            for nn in [4, 25, 60]:
                params['treshold'] = tr
                params['maxlinewidth'] = lw
                params['nn'] = nn
                params['postfix'] = 'tr' + str(tr) + 'lw' + str(lw) + 'nn' + str(nn)
                demo_looper(params, files=['zz-zx-0011-1-cir.png'], modes=['lines'])

# rect and circle test
def demo_rect_and_circle_test():
    params = {'w': w, 'h': h, 'bk': (0, 0, 0), 'coef': 0.9, 'scale': 1.0, 'rmin': 78, 'rmax': 180}
    for r in [False, True]:
        params['rnd'] = r
        params['postfix'] = 'rnd' + str(r)
        demo_looper(params, files=['zz-zx-0011-1-cir.png'], modes=['rect', 'circle'])
    
# demo for private zx files
def demo_private_zx():
        f = 'zx\\'
        files = [f+'BARBAR.png', f+'CABAL.png', f+'Cobra.png', f+'JETPAC.png', f+'MNTYMOLE.png', f+'NOD_YSOD.png', f+'ROBOCOP1.png', f+'skatecrz.png', f+'STORM.png', f+'URIDIUM.png']
        params = {'w': w, 'h': h, 'bk': (0, 0, 0), 'coef': 0.9, 'scale': 1.0, 'rnd': True, 'rmin': 78, 'rmax': 98}
        # todo: test/use new params
        demo_looper(params, files, modes=['brush', 'poly'])

# demo for private files
def demo_private():
    # todo: test/use new params
    params = {'w': w, 'h': h, 'bk': (0, 0, 0), 'coef': 0.9, 'scale': 1.0, 'rnd': True, 'rmin': 78, 'rmax': 98}
    files = ['dragon07e.jpg', 'dragon08x.jpg', 'firemaster.jpg', 'greendevil.jpg', 'robo.jpg', 'zjawa.jpg']
    demo_looper(params, files, modes=['brush', 'lines', 'poly'])

    demo_looper(params, files=['xor1.png', 'AlanW1.png'], modes=['brush', 'lines', 'poly', 'rect', 'circle'])
    demo_looper(params, files=['zz-2014-2020.png'], modes=['rect', 'circle'])

    params = {'w': w, 'h': h, 'bk': (255, 255, 255), 'coef': 0.8, 'scale': 0.5, 'rnd': True, 'rmin': 50, 'rmax': 250}
    demo_looper(params, files=['PIC_2548-cp-min.JPG'], modes=['poly', 'rect', 'lines', 'circle', 'brush'])

    params = {'w': w, 'h': h, 'bk': (255, 255, 255), 'coef': 0.95, 'scale': 0.05, 'rnd': True, 'rmin': 90, 'rmax': 140}
    demo_looper(params, files=['Zuza-orig.jpg', 'Zuza-popr1.jpg', 'Zuza-popr2.jpg'], modes=['poly', 'lines', 'circle', 'brush'])

    params = {'w': w, 'h': h, 'bk': (0, 0, 0), 'coef': 0.9, 'scale': 0.1, 'rnd': True, 'rmin': 15, 'rmax': 180}
    demo_looper(params, files=['rgbxxx-1024-test.png'], modes=['lines'])

# ---

start_time = dt.now()
root = '!output-repixel-test'
odir = root+'/'
indir = 'repixel-in/'
if not os.path.exists(root):
    os.makedirs(root)

w, h = get_canvas('A4') # test4
#w, h = get_canvas('A3') # test3
#w, h = get_canvas('A2') # test2
#w, h = get_canvas('A1') # final
#w, h = get_canvas('800') # for web examples

# select here which demos to run
demo_poly_test()
demo_brush_test()
demo_lines_test()
demo_rect_and_circle_test()
#demo_private_zx()
#demo_private()

time_elapsed = dt.now() - start_time
print('ALL done. elapsed time: {}'.format(time_elapsed))

