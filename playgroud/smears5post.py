
# paint algorithms (artificial artist), v1.0, Python version
# (c)2018 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz
# #5 nowe mazy postporc
# cre: 20180928
# upd: 20181020

# see:
# https://pillow.readthedocs.io/en/3.1.x/reference/ImageDraw.html
# http://pillow.readthedocs.io/en/5.1.x/reference/ImageFilter.html

# TODO:
# - ?


from PIL import Image, ImageDraw, ImageFilter
#from PIL import ImageMath
import random, math, string, os, sys
from drawtools import *


def m5post1():
    odir = '!!!mazy-out\\'
    for n in range(3):
        for m in range(3):
            fn1 = odir+'mazy5-%dx%d-01-%03d.png' % (4960, 3507, n+1) # mazy5-4960x3507-01-001.png
            fn2 = odir+'mazy5-%dx%d-01-%03d.png' % (4960, 3507, m+1) # mazy5-4960x3507-01-001.png
            if m != n:
                print(fn1)
                print(fn2)
                a1 = im2arr(fn1)
                a2 = im2arr(fn2)
                a1 ^= a2  # ?
                xx_im = Image.fromarray(a1, mode='L')
                xx_im.save(odir+'mazy5-post-%03d_%03d.png' % (n+1, m+1))

def m5post2():
    odir = '!!!mazy-out\\'
    for n in range(3):
        for m in range(3):
            fn1 = odir+'mazy5-%dx%d-01-%03d.png' % (4960, 3507, n+1) # mazy5-4960x3507-01-001.png
            fn2 = odir+'mazy5-%dx%d-02-%03d.png' % (4960, 3507, m+1) # mazy5-4960x3507-01-001.png
            if m != n:
                print(fn1)
                print(fn2)
                im1 = Image.open(fn1)
                im2 = Image.open(fn2)
                rgb1 = im1.split()
                rgb2 = im2.split()
                bands = [rgb2[0], rgb2[1], rgb1[2]]
                out = Image.merge('RGB', bands)
                out.save(odir+'mazy5-postX-%03d_%03d.png' % (n+1, m+1))

def m5post3():
    odir = '!!!mazy-out\\'
    for n in range(3):
        for m in range(3):
            fn1 = odir+'mazy5-%dx%d-03-%03d.png' % (4960, 3507, n+1) # mazy5-4960x3507-01-001.png
            fn2 = odir+'mazy5-%dx%d-03-%03d.png' % (4960, 3507, m+1) # mazy5-4960x3507-01-001.png
            if m != n:
                print(fn1)
                print(fn2)
                im1 = Image.open(fn1)
                im2 = Image.open(fn2)
                rgb1 = im1.split()
                rgb2 = im2.split()
                bands = [rgb1[0], rgb2[1], rgb1[2]]
                out = Image.merge('RGB', bands)
                out.save(odir+'mazy5-postXX-%03d_%03d.png' % (n+1, m+1))

#m5post1()
m5post2()
m5post3()
