#! /usr/bin/env python
# -*- coding: utf-8 -*-

# PyArtForms - Repixelize algorithm (artificial artist), v1.0, Python version - DEMO
# (c)2018-2020 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz
# cre: 20201208, 10, 11


import os, sys
from repixelize import *


start_time = dt.now()
root = '!output-repixel-test'
if not os.path.exists(root):
    os.makedirs(root)
odir = root+'\\'
indir = 'repixel-in\\'

w, h = get_canvas('A4') # test4
#w, h = get_canvas('A3') # test3
#w, h = get_canvas('A2') # test2
#w, h = get_canvas('A1') # final

# ---

def demo_looper(params, files, modes):
    for fn in files:
        params['infile'] = indir+fn
        for mo in modes:
            params['mode'] = mo
            if 'postfix' in params:
                ps = "-"+str(params['postfix'])
            else:
                ps = ""
            params['outfile'] = odir+fn+'-repixel-'+mo+ps+'.png'
            start_time1 = dt.now()
            repix(params)
            time_elapsed1 = dt.now() - start_time1
            print('elapsed time: {}'.format(time_elapsed1))

# ---

params = {'w': w, 'h': h, 'bk': (0, 0, 0), 'coef': 0.9, 'scale': 1.0, 'rnd': True, 'rmin': 78, 'rmax': 98}
demo_looper(params, files=['test-src2.jpg'], modes=['brush', 'lines', 'poly', 'rect', 'circle'])
params = {'w': w, 'h': h, 'bk': (0, 0, 0), 'coef': 0.9, 'scale': 1.0, 'rnd': False, 'rmin': 78, 'rmax': 98, 'postfix': 'nornd'}
demo_looper(params, files=['test-src2.jpg'], modes=['brush', 'lines', 'poly', 'rect', 'circle'])
quit()

params = {'w': w, 'h': h, 'bk': (0, 0, 0), 'coef': 0.9, 'scale': 1.0, 'rnd': True, 'rmin': 78, 'rmax': 98}

#note: ~time@A4: lines=1:30 brush=1:00, poly=0:30

f = 'zx\\'
files = [f+'BARBAR.png', f+'CABAL.png', f+'Cobra.png', f+'JETPAC.png', f+'MNTYMOLE.png', f+'NOD_YSOD.png', f+'ROBOCOP1.png', f+'skatecrz.png', f+'STORM.png', f+'URIDIUM.png']
demo_looper(params, files, modes=['brush', 'lines', 'poly'])

files = ['dragon07e.jpg', 'dragon08x.jpg', 'firemaster.jpg', 'greendevil.jpg', 'robo.jpg', 'zjawa.jpg']
demo_looper(params, files, modes=['brush', 'lines', 'poly'])

demo_looper(params, files=['head.png', 'xor1.png', 'AlanW1.png'], modes=['brush', 'lines', 'poly', 'rect', 'circle'])
demo_looper(params, files=['zz-2014-2020.png'], modes=['rect', 'poly'])

params = {'w': w, 'h': h, 'bk': (255, 255, 255), 'coef': 0.8, 'scale': 0.5, 'rnd': True, 'rmin': 50, 'rmax': 250}
demo_looper(params, files=['fromopenshot1zzz2-x.png', 'PIC_2548-cp-min.JPG'], modes=['poly', 'rect', 'lines', 'circle', 'brush'])

params = {'w': w, 'h': h, 'bk': (255, 255, 255), 'coef': 0.95, 'scale': 0.05, 'rnd': True, 'rmin': 90, 'rmax': 140}
demo_looper(params, files=['Zuza-orig.jpg', 'Zuza-popr1.jpg', 'Zuza-popr2.jpg'], modes=['poly', 'lines', 'circle', 'brush'])

params = {'w': w, 'h': h, 'bk': (0, 0, 0), 'coef': 0.9, 'scale': 0.1, 'rnd': True, 'rmin': 15, 'rmax': 180}
demo_looper(params, files=['rgbxxx-1024-test.png'], modes=['lines'])

time_elapsed = dt.now() - start_time
print('ALL done. elapsed time: {}'.format(time_elapsed))

