#! /usr/bin/env python
# -*- coding: utf-8 -*-

# drawings Lissajous in Python
# (c)2018 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz
# https://pillow.readthedocs.io/en/3.1.x/reference/ImageDraw.html
# cre: 20180503
# upd; 20181020

# TODO:
# - ?


from PIL import Image, ImageDraw, ImageFilter
import random, math, string, os, sys
from drawtools import *



def lissajous(draw, params):
    c = math.pi/180
    FF1 = params['FF1']
    FF2 = params['FF2']
    Time = 0
    if FF2 > 0:
        Freq = FF1/FF2
    else:
        Freq = 0
    Fi = params['FFi'] # *math.pi
    sx = params['w']/2
    sy = params['h']/2
    if sx > sy:
        ampli = sy*params['Scale']
    else:
        ampli = sx*params['Scale']

    for i in range(params['Steps']):
        x = int(sx+ampli*math.sin(c*Time))
        y = int(sy+ampli*math.sin(c*(Time*Freq+Fi)))
        if i == 0:
            points = ((x, y), (x, y))
        else:
            points = (points[1], (x, y))
        draw.line(points, fill=params['LineColor'], width=params['LineWidth'])
        Time = Time + params['dT']

def lissajous_loop(draw, params):
    for i in range(10):
        lissajous(draw, params)
        params['FFi'] = params['FFi'] + 2

