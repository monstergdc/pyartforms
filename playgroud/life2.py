#! /usr/bin/env python
# -*- coding: utf-8 -*-

# PyArtForms - Python generative art forms paint algorithms (artificial artist)
# drawing life (2d) in Python, v1.0
# (c)2018-2021 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz
# cre: 20181021
# upd; 20210301
# upd; 20210515

# note: slow, but interesting, do experiment more!

# TODO:
# - resize proper
# - cleanup like the rest
# - fix weird issues
# - ?

import cv2
from PIL import Image, ImageDraw, ImageFilter
import random, math, string, os, sys
from drawtools import *


def f2a(a, x, y, w, h):
    z = 0
    suma = a[y][x]
    if y > 0 and y < h-1-1:
        if x > 0 and x < w-1-1:
            suma = a[y-1][x-1] + a[y-1][x] + a[y-1][x+1]
            + a[y][x-1] + a[y][x] + a[y][x+1]
            + a[y+1][x-1] + a[y+1][x] + a[y+1][x+1]
#    if suma > 9:
#        print(x, y, 'ERR: sum too big:', suma, 'at:', x, y)
    if suma == 0:
#        z = 0
#        if random.randint(0, 1000) >= 999:
#            z = 1
        z = a[y][x]
    if suma == 1:
        z = a[y][x]
    if suma == 2:
        z = a[y][x] ^ 1
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
        z = a[y][x]
    return z

# nice white eater
def f2b(a, x, y, w, h):
    z = 0
    suma = 0
    if y > 1+1 and y < h-1-1:
        if x > 1+1 and x < w-1-1:
            suma = a[y-1][x-1] + a[y-1][x] + a[y-1][x+1]
            + a[y][x-1] + a[y][x] + a[y][x+1]
            + a[y+1][x-1] + a[y][x+1] + a[y+1][x+1] #even with this error :)
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

# this one is quite stable visually
def f2c(a, x, y, w, h):
    z = 0
    suma = a[y][x]
    if y > 0 and y < h-1-1:
        if x > 0 and x < w-1-1:
            suma = a[y-1][x-1] + a[y-1][x] + a[y-1][x+1]
            + a[y][x-1] + a[y][x] + a[y][x+1]
            + a[y+1][x-1] + a[y+1][x] + a[y+1][x+1]
    if suma == 0:
        z = a[y][x]
    if suma == 1:
        z = a[y][x]
    if suma == 2:
        z = 0
    if suma > 2 and suma < 9:
        z = a[y][x]
        if random.randint(0, 100) >= 80:
            z = a[y][x] ^ 1
    if suma == 9:
        z = 0
    return z

def norm_a(a):
    h, w = np.shape(a) # y,x
    for y in range(h):
        for x in range(w):
            if a[y][x] > 32:    # remap 0-255 -> 0-1
                #print('DEBUG: ok', a[y][x], x, y)
                a[y][x] = 1
            else:
                #print('DEBUG: ok-0', a[y][x], x, y)
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
    if params['f'] == 'f2c':
        myfun = f2c

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
    print('drawing %s... %s iter=%d' % (params['name'], png_file, params['iter']))
    if params['reuse'] == False:
        a = im2arr(params['src'])
        a = norm_a(a)
        params['a'] = a
    h, w = np.shape(params['a']) # y,x
    print('shape:', np.shape(params['a']))
    im = Image.new('RGB', (params['w'], params['h']), (0, 0, 0))    # RGB for video use
    draw = ImageDraw.Draw(im)
    f = params['call']
    a = f(draw, params)
    im = im.resize((320, 240), resample=0, box=None)
    im.save(png_file, dpi=(300,300), pnginfo=append_myself())
    show_benchmark(start_time)
    return a


def life2_image(src, f):
    odir = ''
    params1 = {'name': 'LIFE2', 'call': life2d, 'w': 320, 'h': 240, 'src': src, 'f': f, 'iter': 1, 'reuse': False}
    art_painter2(params1, odir+'zz-life2d-001-'+f+'.png')
    params1 = {'name': 'LIFE2', 'call': life2d, 'w': 320, 'h': 240, 'src': src, 'f': f, 'iter': 2, 'reuse': False}
    art_painter2(params1, odir+'zz-life2d-002-'+f+'.png')
    params1 = {'name': 'LIFE2', 'call': life2d, 'w': 320, 'h': 240, 'src': src, 'f': f, 'iter': 4, 'reuse': False}
    art_painter2(params1, odir+'zz-life2d-003-'+f+'.png')
    params1 = {'name': 'LIFE2', 'call': life2d, 'w': 320, 'h': 240, 'src': src, 'f': f, 'iter': 8, 'reuse': False}
    art_painter2(params1, odir+'zz-life2d-004-'+f+'.png')

def life2_video(src, f, video_name, frames):
    image_tmp = 'life-tmp.png'   #tmp img file
    #fcc = -1 # will ask for video codec
    #fcc = cv2.VideoWriter_fourcc(*"XVID")
    fcc = cv2.VideoWriter_fourcc(*"MJPG")

    canvas = (320, 240)
    video = cv2.VideoWriter(video_name, fcc, 25, canvas)
    params1 = {'name': 'LIFE2', 'call': life2d, 'w': 320, 'h': 240, 'src': src, 'f': f, 'iter': 1, 'reuse': True}
    params1['a'] = norm_a(im2arr(params1['src']))

    im = Image.open(params1['src'])
    im = im.resize(canvas, resample=0, box=None)
    im.save(image_tmp, dpi=(300,300))
    ima = cv2.imread(image_tmp)
    for f in range(10):
        video.write(ima)

    for n in range(frames):
        print('frame', n)
        params1['a'] = art_painter2(params1, image_tmp)
        ima = cv2.imread(image_tmp)
        for f in range(4):
            video.write(ima)
    cv2.destroyAllWindows()
    video.release()


# ---

src = 'test-src4-life2.png'

# img
if True:
    life2_image(src=src, f='f2a')
    life2_image(src=src, f='f2b')
    life2_image(src=src, f='f2c')

# video
if True:
    life2_video(src=src, f='f2a', video_name='life-video-f2a.avi', frames=80)
    life2_video(src=src, f='f2b', video_name='life-video-f2b.avi', frames=45)
    life2_video(src=src, f='f2c', video_name='life-video-f2c.avi', frames=40)

