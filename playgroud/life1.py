#! /usr/bin/env python
# -*- coding: utf-8 -*-

# drawing life in Python
# (c)2018 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz
# https://pillow.readthedocs.io/en/3.1.x/reference/ImageDraw.html
# cre: 20180503
# upd; 20180504
# upd; 20181019, 20

# TODO:
# - ?

from PIL import Image, ImageDraw, ImageFilter
import random, math, string, os, sys
from drawtools import *



def f1(x):
    if random.randint(0, 100) >= 90:
        return 1
    return 0

def f2a(x, row, n):
    z = 0
    if x > 1+1 and x < n-1-1:
        suma = row[x-2] + row[x-1] + row[x] + row[x+1] + row[x+2]
        if suma == 0:
            z = 0
            if random.randint(0, 100) >= 95:
                z = 1
        if suma == 1:
            z = 1
        if suma == 2:
            z = row[x]
        if suma == 3:
            z = row[x] ^ 1
        if suma == 4:
            z = row[x] ^ 1
        if suma == 5:
            z = 0
    return z

def f2b(x, row, n):
    z = 0
    if x > 1 and x < n-1:
        suma = row[x-1] + row[x] + row[x+1]
        if suma == 0:
            z = 0
        if suma == 1:
            z = row[x] ^ 1
        if suma == 2:
            z = row[x]
        if suma == 3:
            z = 0
    return z

def f2c(x, row, n):
    z = 0
    if x > 1+1 and x < n-1-1:
        suma = row[x-2] + row[x-1] + row[x] + row[x+1] + row[x+2]
        if suma == 0:
            z = 0
        if suma == 1:
            z = row[x]
        if suma == 2:
            z = 1
        if suma == 3:
            z = row[x] ^ 1
        if suma == 4:
            z = row[x]
        if suma == 5:
            z = 0
    return z

def f2d(x, row, n):
    z = 0
    if x > 1+1 and x < n-1-1:
        suma = row[x-2] + row[x-1] + row[x] + row[x+1] + row[x+2]
        if suma == 0:
            z = 0
        if suma == 1:
            z = row[x]
        if suma == 2:
            z = 1
        if suma == 3:
            z = row[x-1]
        if suma == 4:
            z = row[x+1]
        if suma == 5:
            z = 0
    return z

def f2e(x, row, n):
    z = 0
    if x > 1+1+1 and x < n-1-1-1:
        suma = row[x-3] + row[x-2] + row[x-1] + row[x] + row[x+1] + row[x+2] + row[x+3]
        if suma == 0:
            z = 0
        if suma == 1:
            z = 0
        if suma == 2:
            z = row[x]
        if suma == 3:
            z = 1
        if suma == 4:
            z = 1
        if suma == 5:
            z = row[x]
        if suma == 6:
            z = 0
        if suma == 7:
            z = 0
    return z

def f2f(x, row, n):
    z = 0
    if x > 1 and x < n-1:
        suma = row[x]
        for i in range(3):
            pm = x - random.randint(0, 5)
            pp = x + random.randint(0, 5)
            if pm > 1:
                suma += row[pm]
            if pp < n-1:
                suma += row[pp]
        if suma == 0:
            z = 0
        if suma == 1:
            z = 0
        if suma == 2:
            z = row[x]
        if suma == 3:
            z = 1
        if suma == 4:
            z = 1
        if suma == 5:
            z = row[x]
        if suma >= 6:
            z = 0
    return z

def f2g(x, row, n):
    z = 0
    if x > 1 and x < n-1:
        suma = row[x]
        pm = x - random.randint(0, 4)
        pp = x + random.randint(0, 4)
        if pm > 1:
            suma += row[pm]
        if pp < n-1:
            suma += row[pp]
        pm = x - random.randint(0, 10)
        pp = x + random.randint(0, 10)
        if pm > 1:
            suma -= row[pm]
        if pp < n-1:
            suma -= row[pp]
        if suma <= 0:
            z = 0
        if suma == 1:
            z = row[x] ^ 1
        if suma == 2:
            z = 1
        if suma == 3:
            z = 0
        if suma >= 4:
            z = row[x]
    return z


def life(draw, params):
    """
    Draw life rendering.
    Each row is subsequent generation of some population.
    Different population control (evolution) functions can be applied.
    """

    random.seed()
    row = []
    row[:] = [f1(x) for x in range(params['w'])]
    n = len(row)

    if params['f'] == 'f2a':
        myfun = f2a
    if params['f'] == 'f2b':
        myfun = f2b
    if params['f'] == 'f2c':
        myfun = f2c
    if params['f'] == 'f2d':
        myfun = f2d
    if params['f'] == 'f2e':
        myfun = f2e
    if params['f'] == 'f2f':
        myfun = f2f
    if params['f'] == 'f2g':
        myfun = f2g
    
    y = 0
    for y in range(params['h']):
        points = []
        for i in range(params['w']):
            if row[i] == 1:
                points.extend((i, y))
        draw.point(points, fill=params['Color'])
        rownew = []
        rownew[:] = [myfun(x, row, n) for x in range(params['w'])]
        row = rownew
        y += 1

