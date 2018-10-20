#! /usr/bin/env python
# -*- coding: utf-8 -*-

# paint algorithms (artificial artist), v1.0, Python version
# #1 waves
# (c)2018 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz
# cre: 20180505
# upd: 20181020

# see:
# https://pillow.readthedocs.io/en/3.1.x/reference/ImageDraw.html

# TODO:
# - ?


from PIL import Image, ImageDraw
import random, math, string, os, sys
from bezier import make_bezier
from datetime import datetime as dt
from drawtools import *


def waves1(draw, params):
    w = params['w']
    h = params['h']
    random.seed()
    c = math.pi/180

    if params['horizontal'] == True:
        rn = params['w']
        dx = params['h']/(params['z']*2+4)
    else:
        rn = params['h']
        dx = params['w']/(params['z']*2+4)

    gr = params['gradient']
    for z in range(params['z']):
        ndx = random.randint(0, gr)
        color = gradient(params['c1'], params['c2'], params['c3'], ndx, gr-1)
        aofs1 = random.randint(0, 360)
        aofs2 = random.randint(0, 360)
        aofs3 = random.randint(0, 360)
        aofs4 = random.randint(0, 360)
        fx = 100
        fd = 100*params['f0']
        fofs1 = random.randint(0, fx)/fd
        fofs2 = random.randint(0, fx)/fd
        fofs3 = random.randint(0, fx)/fd*2
        fofs4 = random.randint(0, fx)/fd*2
        mofs1 = (z+2)*dx

        y = 0
        for n in range(rn):
            x_in =  mofs1 + dx * (1 + (math.sin(c*(n*fofs1+aofs1))+2*math.sin(c*(n*fofs3+aofs3)))/3)
            x_out = mofs1 + dx * (1 + (math.sin(c*(n*fofs2+aofs2))+2*math.sin(c*(n*fofs4+aofs4)))/3)
            if params['horizontal'] == True:
                xy = [(y, x_in), (y, h - x_out)]
            else:
                xy = [(x_in, y), (w - x_out, y)]
            draw.rectangle(xy, fill=color, outline=None)
            y += 1

def waves2(draw, params):
    w = params['w']
    h = params['h']
    random.seed()
    c = math.pi/180

    if params['horizontal'] == True:
        rn = w
        dx = h/params['z']*4
    else:
        rn = h
        dx = w/params['z']*4

    gr = params['gradient']
    for z in range(params['z']):
        ndx = random.randint(0, gr)
        color = gradient(params['c1'], params['c2'], params['c3'], ndx, gr-1)
        aofs1 = random.randint(0, 360)
        aofs2 = random.randint(0, 360)
        aofs3 = random.randint(0, 360)
        aofs4 = random.randint(0, 360)
        fx = 100
        fd = 100*params['f0']
        fofs1 = random.randint(0, fx)/fd
        fofs2 = random.randint(0, fx)/fd
        fofs3 = random.randint(0, fx)/fd*2
        fofs4 = random.randint(0, fx)/fd*2
        mofs1 = z*dx

        y = 0
        points1 = []
        points2 = []
        for n in range(rn):
            x_in =  mofs1 + dx * (1 + (math.sin(c*(n*fofs1+aofs1))+2*math.sin(c*(n*fofs3+aofs3)))/3)
            x_out = mofs1 + dx * (1 + (math.sin(c*(n*fofs2+aofs2))+2*math.sin(c*(n*fofs4+aofs4)))/3)
            if params['horizontal'] == True:
                points1.extend((y, x_in))
                points2.extend((y, x_out))
            else:
                points1.extend((x_in, y))
                points2.extend((x_out, y))
            y += 1
        draw.line(points1, fill=color, width=random.randint(2, 8))
        draw.line(points2, fill=color, width=random.randint(2, 8))

def waves3(draw, params):
    w = params['w']
    h = params['h']
    random.seed()
    c = math.pi/180

    gr = params['gradient']
    for z in range(params['z']):
        ndx = gr*z/params['z']
        color = gradient(params['c1'], params['c2'], params['c3'], ndx, gr-1)
        a = z/params['z']
        dx = h/2 * (1-a)
        if z == 0:
            da = 0
        else:
            da = random.randint(0, 180)
        points = []
        for n in range(w):
            y =  h/2 + dx * math.sin(c*(n*a+da))
            points.extend((n, y))
        draw.line(points, fill=color, width=8)

def waves_mux(draw, params):
    waves2(draw, params['par1'])
    waves2(draw, params['par2'])

# ---

def do_waves(cnt, w, h, odir):
    params1 = {
        'w': w, 'h': h, 'Background': (224, 244, 0),
        'name': 'WAVES#1', 'call': waves1, 
        'z': 14,
        'f0': 1,
        'horizontal': False,
        'gradient': 256,
        'c1': (0,0,255),
        'c2': (0,255,255),
        'c3': (255,255,255),
    }
    params2 = {
        'w': w, 'h': h, 'Background': (224, 244, 0),
        'name': 'WAVES#1', 'call': waves1, 
        'z': 12,
        'f0': 1,
        'horizontal': True,
        'gradient': 256,
        'c1': (0,0,0),
        'c2': (0,255,0),
        'c3': (255,255,0),
    }
    params3 = {
        'w': w, 'h': h, 'Background': (0, 0, 0),
        'name': 'WAVES#1', 'call': waves1, 
        'z': 9,
        'f0': 1,
        'horizontal': False,
        'gradient': 24,
        'c1': (0,0,0),
        'c2': (255,0,0),
        'c3': (255,255,0),
    }
    params4 = {
        'w': w, 'h': h, 'Background': (0, 0, 0),
        'name': 'WAVES#1', 'call': waves1, 
        'z': 4,
        'f0': 0.33,
        'horizontal': True,
        'gradient': 256,
        'c1': (255,0,0),
        'c2': (0,255,0),
        'c3': (0,0,255),
    }
    params5 = {
        'w': w, 'h': h, 'Background': (0, 0, 0),
        'name': 'WAVES#1', 'call': waves1, 
        'z': 4,
        'f0': 3.0,
        'horizontal': True,
        'gradient': 256,
        'c1': (255,0,0),
        'c2': (0,255,0),
        'c3': (0,0,255),
    }

    params1a = {
        'w': w, 'h': h, 'Background': (0, 0, 0),
        'name': 'WAVES#2', 'call': waves2, 
        'z': 96,
        'f0': 1,
        'horizontal': False,
        'gradient': 256,
        'c1': (255,0,0),
        'c2': (255,255,0),
        'c3': (255,255,255),
    }
    params2a = {
        'w': w, 'h': h, 'Background': (0, 0, 0),
        'name': 'WAVES#2', 'call': waves2, 
        'z': 48,
        'f0': 1,
        'horizontal': True,
        'gradient': 256,
        'c1': (0,128,0),
        'c2': (0,255,0),
        'c3': (0,0,255),
    }

    params1b = {
        'w': w, 'h': h, 'Background': (0, 0, 0),
        'name': 'WAVES#3', 'call': waves3, 
        'z': 18,
        'gradient': 64,
        'c1': (255,255,255),
        'c2': (255,255,0),
        'c3': (255,0,0),
    }

    paramsX = {
        'w': w, 'h': h, 'Background': (0, 0, 0),
        'name': 'WAVES#2#MUX', 'call': waves_mux, 
        'par1': params1a,
        'par2': params2a,
    }

    for n in range(cnt):
        art_painter(params1, odir+'waves1-%dx%d-01-%03d.png' % (w, h, n+1))
        art_painter(params2, odir+'waves1-%dx%d-02-%03d.png' % (w, h, n+1))
        art_painter(params3, odir+'waves1-%dx%d-03-%03d.png' % (w, h, n+1))
        art_painter(params4, odir+'waves1-%dx%d-04-%03d.png' % (w, h, n+1))
        art_painter(params5, odir+'waves1-%dx%d-05-%03d.png' % (w, h, n+1))
        art_painter(params1a, odir+'waves2-%dx%d-01-%03d.png' % (w, h, n+1))
        art_painter(params2a, odir+'waves2-%dx%d-02-%03d.png' % (w, h, n+1))
        art_painter(params1b, odir+'waves3-%dx%d-01-%03d.png' % (w, h, n+1))
        art_painter(paramsX, odir+'waves_mux-%dx%d-01-%03d.png' % (w, h, n+1))
        
# ---

def main():
    start_time = dt.now()
    cnt = 3
    w, h = get_canvas('A3')
    do_waves(cnt, w, h, '')
    time_elapsed = dt.now() - start_time
    print('ALL done. elapsed time: {}'.format(time_elapsed))


if __name__ == '__main__':
    main()
