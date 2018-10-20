#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Mandelbrot fractal example (z'=z^2+c), v1.0, Python
# (c)2017, 2018 Noniewicz.com, Jakub Noniewicz aka MoNsTeR/GDC
# cre: 20180505
# upd: 20181019, 20

from PIL import Image, ImageDraw
import math
from drawtools import *


def generate_mandelbrot(draw, params):
    x0 = params['x0']
    x1 = params['x1']
    y0 = params['y0']
    y1 = params['y1']
    maxiter = params['maxiter']
    w = params['w']
    h = params['h']
    negative = params['negative']

    xs0 = abs(x1-x0)/w
    ys0 = abs(y1-y0)/h
    for y in range(h):
        for x in range(w):
            z = complex(0, 0)
            c = complex(x0+xs0*x, y0+ys0*y)
            i = 0
            noesc = True
            while (noesc == True) and (i < maxiter):
                z = z * z + c
                m = math.sqrt(z.real*z.real + z.imag*z.imag)
                if m >= 2:
                    ii = i
                    noesc = False
                i += 1
            if noesc == True:
                ii = maxiter
            pv = 1.0 - float(ii) / float(maxiter)
            if negative == True:
                pix = 255-round(pv*255)
            else:
                pix = round(pv*255)
            draw.point((x, y), fill=int(pix))

def generate_mandelbrot_(draw, x0, x1, y0, y1, maxiter, w, h, negative):
    params['x0'] = x0
    params['x1'] = x1
    params['y0'] = y0
    params['y1'] = y1
    params['maxiter'] = maxiter
    params['w'] = w
    params['h'] = h
    params['negative'] = negative
    generate_mandelbrot(draw, params)

