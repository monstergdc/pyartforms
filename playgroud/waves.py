#! /usr/bin/env python
# -*- coding: utf-8 -*-

# paint algorithms (artificial artist), v1.0, Python version
# #1 waves
# (c)2018-2021 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz
# cre: 20180505
# upd: 20181020
# upd: 20190118
# upd: 20190421, 22
# upd: 20210612

# TODO:
# - ?


from PIL import Image, ImageDraw
import random, math, string, os, sys
from bezier import make_bezier
from drawtools import *
from color_defs import *


def waves2(draw, params):
    if 'par1' in params and 'par2' in params:
        waves2(draw, params['par1'])
        waves2(draw, params['par2'])
        return

    # todo: uproscic kod (czemu 2x?) | exp par
    w = params['w']
    h = params['h']
    cnt = params['n']
    random.seed()
    c = math.pi/180

    sc = 3.0  #par was 4
    if params['horizontal'] == True:
        rn = w
        dx = h/float(cnt)*sc
    else:
        rn = h
        dx = w/float(cnt)*sc

    for z in range(cnt):
        ndx = random.randint(0, cnt)
        color = new_colorer(params['color'], ndx, cnt)
        if 'addalpha' in params:
            color = add_alpha(color, params['addalpha'])
        aofs1 = random.randint(0, 360)
        aofs2 = random.randint(0, 360)
        aofs3 = random.randint(0, 360)
        aofs4 = random.randint(0, 360)
        fofs1 = random.randint(0, 100)/100.0*1 # par
        fofs2 = random.randint(0, 100)/100.0*1 # par
        fofs3 = random.randint(0, 100)/100.0*2 # par
        fofs4 = random.randint(0, 100)/100.0*2 # par
        mofs1 = float(z*dx)
        am1 = 1.0 # par
        am2 = 1.0 # par
        am3 = 3.0 # par was 2
        am4 = 3.0 # par was 2

        y = 0
        points1 = []
        points2 = []
        points1a = []
        points2a = []
        for n in range(rn):
            nsc = float(n)/float(rn)*360*10 # par 10
            x_in =  int(mofs1 + dx * (1 + (am1*math.sin(c*(nsc*fofs1+aofs1))+am3*math.sin(c*(nsc*fofs3+aofs3)))))
            x_out = int(mofs1 + dx * (1 + (am2*math.sin(c*(nsc*fofs2+aofs2))+am4*math.sin(c*(nsc*fofs4+aofs4)))))
            if params['horizontal'] == True:
                points1.extend((y, x_in))
                points2.extend((y, x_out))
            else:
                points1.extend((x_in, y))
                points2.extend((x_out, y))
            y += 1
        lw = random.randint(1, int(w/30)) #par, opt big->small?

        points1a[:] = [xy for xy in points1]
        points2a[:] = [xy for xy in points2]
        for a in range(int(len(points1a)/2)):
            ndx = int(len(points1a)/2)-1-a
            if params['horizontal'] == True:
                points1.extend((points1a[ndx*2], lw+points1a[ndx*2+1]))
            else:
                points1.extend((lw+points1a[ndx*2], points1a[ndx*2+1]))
        for a in range(int(len(points2a)/2)):
            ndx = int(len(points2a)/2)-1-a
            if params['horizontal'] == True:
                points2.extend((points2a[ndx*2], lw+points2a[ndx*2+1]))
            else:
                points2.extend((lw+points2a[ndx*2], points2a[ndx*2+1]))
        draw.polygon(points1, fill=color, outline=color)
        draw.polygon(points2, fill=color, outline=color)

