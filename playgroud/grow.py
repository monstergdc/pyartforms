#! /usr/bin/env python
# -*- coding: utf-8 -*-

# GROWING PLANTS v3.0 - tree growing algorithm, Python version from old Pascal code
# loosely based on article in "ENTER" 2/93
# (c)1993 Noniewicz.com (orig Turbo Pascal v1.6)
# (c)2011 Noniewicz.com (unf. Delphi ver start)
# (c)2014-2015, 2017, 2018 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz
# cre: 20180430
# upd: 20180501, 02, 03
# upd: 20181020

# see: https://pillow.readthedocs.io/en/3.1.x/reference/ImageDraw.html
# http://pillow.readthedocs.io/en/5.1.x/reference/ImageFilter.html

# TODO:
# appendable/restartable == anim per grow step | esp randoms
# leaves / fruits / polygons
# colors (variable)
# trunk - thickness / color
# split code

from PIL import Image, ImageDraw, ImageFilter
import random, math, string
import cv2
import os, sys
from datetime import datetime as dt
from bezier import make_bezier
from drawtools import *


XPI = math.pi/180

class Branch():
    def __init__(self, start, stop, thickness, level, angle, color, width, bclass):
        self.start = start
        self.stop = stop
        self.thickness = thickness
        self.level = level
        self.angle = angle
        self.color = color
        self.width = width
        self.bclass = bclass

class Grow():
    def _init__(self):
        self.branches = []

    def myrnd(self, x):
        if x <= 0:
            return 0
        return random.randint(0, x)

    def add(self, one):
        self.branches.append(one)

    def generate0(self, iter, xyz0, blen, a):
        if iter == 0:
            return

        pw = self.params['PenWidth']
        if self.params['ThickDecPerIter'] > 0:
            pw = pw - (self.params['Iterations']-iter) / self.params['ThickDecPerIter']
        if pw < 1:
            pw = 1

        # calc and store new/current branch
        aa = (a+180)*XPI
        sin1 = math.sin(aa)
        cos1 = math.cos(aa)
        delta1 = 0 # test # par
        xyz0 = (xyz0[0]+delta1*cos1, xyz0[1]+delta1*sin1)
        xyz = (xyz0[0]+blen*cos1, xyz0[1]+blen*sin1)
        color = self.params['Color']
        r = random.randint(64, 256)
        color = (64,r,64) # test
        bc = 0 # line
#        if iter == 1:
#            color = (255,0,0) # test # par
#            bc = 1 # rect/ellipse # test # par
        self.add(Branch(xyz0, xyz, pw, iter, aa, color, int(pw), bc))

        # calc next
        newlen1 = blen*self.params['BranchDecrementFactor']/100
        tmp = int(newlen1*self.params['BranchVariationFactor']/100)
        newlen1 = newlen1 - self.myrnd(tmp) + self.myrnd(tmp)
        newlen2 = blen*self.params['BranchDecrementFactor']/100
        tmp = int(newlen2*self.params['BranchVariationFactor']/100)
        newlen2 = newlen2 - self.myrnd(tmp) + self.myrnd(tmp)
        tmp = int(a*self.params['AngleVariation']/100)
        newa = a - self.myrnd(tmp) + self.myrnd(tmp)
        tmp = int(self.params['AngleSpread']*self.params['AngleSpreadVariation']/100)
        newas = self.params['AngleSpread'] - self.myrnd(tmp) + self.myrnd(tmp)

        if self.params['RndIterCutOff'] == True:
            if random.randint(0, 100) > 90: # par val / iter
                return

        # call next
        self.generate0(iter-1, xyz, newlen1, newa-newas)
        self.generate0(iter-1, xyz, newlen2, newa+newas)

    def clear(self):
        self.branches = []

    def generate(self, params):
        self.clear()
        self.params = params
        random.seed()
        self.generate0(params['Iterations'], params['p0'], params['BranchLen'], params['AngleStart'])

    def generate_more(self, params):
        self.params = params
        random.seed()
        self.generate0(params['Iterations'], params['p0'], params['BranchLen'], params['AngleStart'])

    def draw_branch(self, draw, b):
        if b.bclass == 0:
            draw.line((b.start[0], b.start[1], b.stop[0], b.stop[1]), fill=b.color, width=b.width)
        if b.bclass == 1:
            draw.rectangle((b.start[0], b.start[1], b.stop[0], b.stop[1]), fill=b.color, outline=None)
        if b.bclass == 2:
            draw.ellipse((b.start[0], b.start[1], b.stop[0], b.stop[1]), fill=b.color, outline=(0,200,0))

    def draw(self, canvas, image):
        im = Image.new('RGB', canvas, (0, 0, 0))
        draw = ImageDraw.Draw(im)
        for i in range(len(self.branches)):
            self.draw_branch(draw, self.branches[i])
        im.save(image)

    def get_tree(self):
        return self.branches

    def set_tree(self, new):
        self.branches = new

    def get_params(self):
        return self.params

    def set_params(self, new):
        self.params = new

# ---

def gen(g, canvas, params, dt, image, video):
    for n in range(dt):
        g.generate(params)
        g.draw(canvas, image)
        ima = cv2.imread(image)
        video.write(ima)
        video.write(ima)

def main():
    g = Grow()
    canvas = (1024, 768)

    params = {
        'p0': (canvas[0]/2, canvas[1]-80),
        'Iterations': 12,
        'BranchLen': 130,
        'AngleStart': 90.0,
        'BranchDecrementFactor': 75,
        'BranchVariationFactor': 5,
        'AngleVariation': 25,
        'AngleSpread': 45.0,
        'AngleSpreadVariation': 25,
        'RndIterCutOff': False,
        'Color': (255, 255, 255),
        'PenWidth': 1,
        'ThickDecPerIter': 0,
    }
    g.generate(params)
    g.draw(canvas, image = 'tree0.png')

# ---

    video_name = 'tree-video.avi'
    image = 'tree-tmp.png'   #tmp img file
    #fcc = -1
    #fcc = cv2.VideoWriter_fourcc(*"XVID")
    fcc = cv2.VideoWriter_fourcc(*"MJPG")
    dt = 20

    canvas = (720, 576)
    video = cv2.VideoWriter(video_name, fcc, 25, canvas)

    params = {
        'p0': (canvas[0]/2, canvas[1]-50),
        'Iterations': 1,
        'BranchLen': 10,
        'AngleStart': 90.0,
        'BranchDecrementFactor': 75,
        'BranchVariationFactor': 10,
        'AngleVariation': 20,
        'AngleSpread': 45.0-30.0,
        'AngleSpreadVariation': 20,
        'RndIterCutOff': False,
        'Color': (255, 255, 255),
        'PenWidth': 1,
        'ThickDecPerIter': 0,
    }
    g.clear()
    for n in range(15):
        #g.generate_more(params)
        g.generate(params)
        g.draw(canvas, image)
        ima = cv2.imread(image)
        video.write(ima)
        video.write(ima)
        video.write(ima)
        params['BranchLen'] = 7 + params['BranchLen']
        params['AngleSpread'] = 2.0 + params['AngleSpread']

        #g.generate_more(params)
        g.generate(params)
        g.draw(canvas, image)
        ima = cv2.imread(image)
        video.write(ima)
        video.write(ima)
        video.write(ima)
        params['Iterations'] = 1 + params['Iterations']

    ima = cv2.imread(image)
    for n in range(50):
        video.write(ima)

# ---

    params = {
        'p0': (canvas[0]/2, canvas[1]-50),
        'Iterations': 1,
        'BranchLen': 10,
        'AngleStart': 90.0,
        'BranchDecrementFactor': 70,
        'BranchVariationFactor': 10,
        'AngleVariation': 15,
        'AngleSpread': 11.0,
        'AngleSpreadVariation': 10,
        'RndIterCutOff': False,
        'Color': (255, 255, 255),
        'PenWidth': 1,
        'ThickDecPerIter': 0,
    }
    g.clear()
    for n in range(15):
        #g.generate_more(params)
        g.generate(params)
        g.draw(canvas, image)
        ima = cv2.imread(image)
        video.write(ima)
        video.write(ima)
        video.write(ima)
        params['BranchLen'] = 7 + params['BranchLen']
        params['AngleSpread'] = 0.5 + params['AngleSpread']

        #g.generate_more(params)
        g.generate(params)
        g.draw(canvas, image)
        ima = cv2.imread(image)
        video.write(ima)
        video.write(ima)
        video.write(ima)
        params['Iterations'] = 1 + params['Iterations']

    ima = cv2.imread(image)
    for n in range(50):
        video.write(ima)

# ---
    return
# ---

    params = {
        'p0': (canvas[0]/2, canvas[1]-80),
        'Iterations': 10,
        'BranchLen': 100,
        'AngleStart': 90.0,
        'BranchDecrementFactor': 75,
        'BranchVariationFactor': 5,
        'AngleVariation': 25,
        'AngleSpread': 45.0,
        'AngleSpreadVariation': 25,
        'RndIterCutOff': False,
        'Color': (255, 255, 255),
        'PenWidth': 1,
        'ThickDecPerIter': 0,
    }
    gen(g, canvas, params, dt, image, video)

    params = {
        'p0': (canvas[0]/2, canvas[1]-80),
        'Iterations': 12,
        'BranchLen': 120,
        'AngleStart': 90.0,
        'BranchDecrementFactor': 75,
        'BranchVariationFactor': 5,
        'AngleVariation': 25,
        'AngleSpread': 45.0,
        'AngleSpreadVariation': 25,
        'RndIterCutOff': False,
        'Color': (255, 255, 255),
        'PenWidth': 8,
        'ThickDecPerIter': 1,
    }
    gen(g, canvas, params, dt, image, video)

    params = {
        'p0': (canvas[0]/2, canvas[1]/2),
        'Iterations': 10,
        'BranchLen': 120,
        'AngleStart': 90.0,
        'BranchDecrementFactor': 75,
        'BranchVariationFactor': 1,
        'AngleVariation': 1,
        'AngleSpread': 90.0,
        'AngleSpreadVariation': 1,
        'RndIterCutOff': False,
        'Color': (255, 255, 255),
        'PenWidth': 1,
        'ThickDecPerIter': 0,
    }
    gen(g, canvas, params, dt, image, video)

    params = {
        'p0': (canvas[0]/2, canvas[1]-100),
        'Iterations': 11,
        'BranchLen': 120,
        'AngleStart': 90.0,
        'BranchDecrementFactor': 70,
        'BranchVariationFactor': 10,
        'AngleVariation': 10,
        'AngleSpread': 22.0,
        'AngleSpreadVariation': 10,
        'RndIterCutOff': False,
        'Color': (255, 255, 255),
        'PenWidth': 1,
        'ThickDecPerIter': 0,
    }
    gen(g, canvas, params, dt, image, video)


    cv2.destroyAllWindows()
    video.release()


if __name__ == '__main__':
    main()
