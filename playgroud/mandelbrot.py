#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Mandelbrot fractal example (z'=z^2+c), v1.0, Python
# (c)2017, 2018 Noniewicz.com, Jakub Noniewicz aka MoNsTeR/GDC
# cre: 20180505
# upd: 20181019, 20

from PIL import Image, ImageDraw
import math
from datetime import datetime as dt
from drawtools import *


def generate_mandelbrot(x0, x1, y0, y1, maxiter, w, h, negative, png_file='mandel.png', output_mode='save'):
    start_time = dt.now()
    print('generating mandel...', w, h, 'iter', maxiter)
    im = Image.new('L', (w, h), (0))
    draw = ImageDraw.Draw(im)
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
    if output_mode == 'save':
        im.save(png_file, dpi=(300,300))
        show_benchmark(start_time)
    else:
        im2cgi(im)

# ---

#tmp CGI
#generate_mandelbrot(-2.5, 1.0, -1.0, 1.0, 70, 600, 400, False, '')

generate_mandelbrot(-2.5, 1.0, -1.0, 1.0, 200, 700, 400, False, 'mandel-001.png')
generate_mandelbrot(-2.5, 1.0, -1.0, 1.0, 20, 700, 400, False, 'mandel-002.png')
