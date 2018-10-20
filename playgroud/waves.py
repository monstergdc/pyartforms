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
    fz = float(params['z'])
    for z in range(params['z']):
        ndx = gr*z/params['z']
        color = gradient(params['c1'], params['c2'], params['c3'], ndx, gr-1)
        #color = (255, 255, 255) # debug!
        a = float(z)/fz # why bad w/o float on 2.7/linux? and ok on 3.6/win
        dx = h/2 * (1-a)
        if z == 0:
            da = 0
        else:
            da = random.randint(0, 180)
        points = []
        for n in range(w):
            y =  h/2 + dx * math.sin(c*(n*a+da))
            points.extend((n, int(y)))
        draw.line(points, fill=color, width=8)

def waves_mux(draw, params):
    waves2(draw, params['par1'])
    waves2(draw, params['par2'])

