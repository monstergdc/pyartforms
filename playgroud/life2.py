#! /usr/bin/env python
# -*- coding: utf-8 -*-

# drawing life (2d) in Python
# (c)2018 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz
# cre: 20181021
# upd; 201810??

# TODO:
# - resize proper
# - cleanup like the rest
# - ?

import cv2
from PIL import Image, ImageDraw, ImageFilter
import random, math, string, os, sys
from drawtools import *


def f2a(a, x, y, w, h):
    z = 0
    suma = 0
    if y == 0 or x == 0:
        suma = 1
    if y > 1+1 and y < h-1-1:
        if x > 1+1 and x < w-1-1:
            suma = a[y-1][x-1] + a[y-1][x] + a[y-1][x+1]
            + a[y][x-1] + a[y][x] + a[y][x+1]
            + a[y+1][x-1] + a[y][x+1] + a[y+1][x+1]
    if suma == 0:
        z = 0
        if random.randint(0, 100) >= 95:
            z = 1
    if suma == 1:
        z = a[y][x]
        if random.randint(0, 100) >= 93:
            z = 0
    if suma == 2:
        z = a[y][x]
    if suma == 3:
        z = a[y][x]
    if suma == 4:
        z = a[y][x]
    if suma == 5:
        z = a[y][x]
    if suma == 6:
        z = a[y][x]
    if suma == 7:
        z = a[y][x]
    if suma == 8:
        if random.randint(0, 100) >= 95:
            z = a[y][x] ^ 1
        else:
            z = a[y][x]
    if suma == 9:
        if random.randint(0, 100) >= 95:
            z = a[y][x] ^ 1
        else:
            z = a[y][x]
    return z

def f2b(a, x, y, w, h):
    z = 0
    suma = 0
    if y > 1+1 and y < h-1-1:
        if x > 1+1 and x < w-1-1:
            suma = a[y-1][x-1] + a[y-1][x] + a[y-1][x+1]
            + a[y][x-1] + a[y][x] + a[y][x+1]
            + a[y+1][x-1] + a[y][x+1] + a[y+1][x+1]
    if suma == 0:
        z = 0
        if random.randint(0, 100) >= 97:
            z = 1
    if suma == 1:
        z = a[y][x]
        if random.randint(0, 100) >= 70:
            z = 0
    if suma == 2:
        z = a[y][x]
    if suma == 3:
        z = a[y][x]
    if suma == 4:
        z = a[y][x]
    if suma == 5:
        z = a[y][x]
    if suma == 6:
        z = a[y][x]
    if suma == 7:
        z = a[y][x]
    if suma == 8:
        z = a[y][x] ^ 1
    if suma == 9:
        z = 0
    return z

def norm_a(a):
    h, w = np.shape(a) # y,x
    for y in range(h):
        for x in range(w):
            if a[y][x] > 40:
                a[y][x] = 1
            else:
                a[y][x] = 0
    return a

def life2d(draw, params):
    a = params['a']
    h, w = np.shape(a) # y,x
    random.seed()

    if params['f'] == 'f2a':
        myfun = f2a
    if params['f'] == 'f2b':
        myfun = f2b

    for i in range(params['iter']):
        b = a
        for y in range(h):
            for x in range(w):
                b[y][x] = myfun(a, x, y, w, h)
        a = b

    for y in range(h):
        for x in range(w):
            if a[y][x] == 1:
                fill = (255, 255, 255)
            else:
                fill = (0, 0, 0)
            draw.point((x, y), fill=fill)
    return a

def art_painter2(params, png_file):
    start_time = dt.now()
    print('drawing %s... %s' % (params['name'], png_file))
    if params['reuse'] == False:
        a = im2arr(params['src'])
        a = norm_a(a)
        params['a'] = a
    h, w = np.shape(params['a']) # y,x
    print('shape:', np.shape(params['a']))
    im = Image.new('RGB', (params['w'], params['h']), (0, 0, 0))
    draw = ImageDraw.Draw(im)
    f = params['call']
    a = f(draw, params)
    im = im.resize((320, 240), resample=0, box=None)
    im.save(png_file, dpi=(300,300), pnginfo=append_myself())
    show_benchmark(start_time)
    return a


def life2_static():
    odir = ''
    params1 = {'name': 'LIFE2', 'call': life2d, 'w': 180, 'h': 150, 'src': 'test-src2-life2.png', 'f': 'f2a', 'iter': 1, 'reuse': False}
    art_painter2(params1, odir+'zz-life2d-001-f2a.png')
    params1 = {'name': 'LIFE2', 'call': life2d, 'w': 180, 'h': 150, 'src': 'test-src2-life2.png', 'f': 'f2a', 'iter': 2, 'reuse': False}
    art_painter2(params1, odir+'zz-life2d-002-f2a.png')
    params1 = {'name': 'LIFE2', 'call': life2d, 'w': 180, 'h': 150, 'src': 'test-src2-life2.png', 'f': 'f2a', 'iter': 3, 'reuse': False}
    art_painter2(params1, odir+'zz-life2d-003-f2a.png')
    params1 = {'name': 'LIFE2', 'call': life2d, 'w': 180, 'h': 150, 'src': 'test-src2-life2.png', 'f': 'f2a', 'iter': 4, 'reuse': False}
    art_painter2(params1, odir+'zz-life2d-004-f2a.png')

# ---

# img

#life2_static()

# vid

video_name = 'life-video.avi'
image_tmp = 'life-tmp.png'   #tmp img file
#fcc = -1
#fcc = cv2.VideoWriter_fourcc(*"XVID")
fcc = cv2.VideoWriter_fourcc(*"MJPG")

#src = 'test-src2-life2.png'
src = 'test-src3-life2.png'

canvas = (320, 240)
video = cv2.VideoWriter(video_name, fcc, 25, canvas)
params1 = {'name': 'LIFE2', 'call': life2d, 'w': 320, 'h': 200, 'src': src, 'f': 'f2a', 'iter': 1, 'reuse': True}
params1['a'] = norm_a(im2arr(params1['src']))

im = Image.open(params1['src'])
im = im.resize(canvas, resample=0, box=None)
im.save(image_tmp, dpi=(300,300))
ima = cv2.imread(image_tmp)
for f in range(10):
    video.write(ima)

for n in range(40):
    print('frame', n)
    params1['a'] = art_painter2(params1, image_tmp)
    ima = cv2.imread(image_tmp)
    for f in range(5):
        video.write(ima)
cv2.destroyAllWindows()
video.release()
