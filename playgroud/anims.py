#! /usr/bin/env python
# -*- coding: utf-8 -*-

# ANIMS v1.0, Python version
# (c)2018-2021 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz
# anim#1/anim#2 - recreated from seeing as in some GIFs I've once seen (so concept isn't mine)
# cre: 20180505
# upd: 20180506, 12
# upd: 20180928, 30
# upd: 20181020
# upd: 20210507

# orig GIFs md5:
# #1: ad2bde22541ac1b05b2c08fd805ebafe *001.gif
# #2: 927339ac93af260455892d15e0f1f5c3 *CM128.gif
# #3: ?
# #4: 7dafd915911faf3e14678fefe163d7f1 *DSC58.gif

# see: https://pillow.readthedocs.io/en/3.1.x/reference/ImageDraw.html

# TODO:
# - fin anim #3 proper
# - fin anim #4
# - fin anim #7
# - opt easy call smears and such
# - common draw class
# - opt cont paint over prev frame image


from PIL import Image, ImageDraw, ImageFilter
import random, math, os, sys
import cv2
from drawtools import *
from color_defs import * # for anim7

image = 'tmp.png'   #tmp img file
c = math.pi/180
s2 = math.sqrt(2)/2

class Anim1():
    state = []
    nx = 10
    ny = 10

    def _init__(self):
        self.init((0, 0), 0, 0)

    def init(self, canvas, steps, phase):
        self.dt = 0
        self.canvas = canvas
        self.steps = steps
        self.phase = phase
        self.bw = canvas[0]/self.nx
        self.bh = canvas[1]/self.ny
        self.state = [[0 for x in range(self.nx)] for y in range(self.ny)]

    def rect(self, draw, x0, y0, w, h, a, fill):
        x1 = s2*w*math.cos(c*(a-45))
        y1 = s2*h*math.sin(c*(a-45))
        x2 = s2*w*math.cos(c*(a+45))
        y2 = s2*h*math.sin(c*(a+45))
        x3 = s2*w*math.cos(c*(a+45+90))
        y3 = s2*h*math.sin(c*(a+45+90))
        x4 = s2*w*math.cos(c*(a+45+180))
        y4 = s2*h*math.sin(c*(a+45+180))
        points = [(x0+x1, y0+y1), (x0+x2, y0+y2), (x0+x3, y0+y3), (x0+x4, y0+y4)]
        draw.polygon(points, fill=fill, outline=None)

    def drawframe(self, image):
        for x in range(self.nx):
            for y in range(self.ny):            
                self.state[y][x] = self.state[y][x] + 360/4/self.steps

        if self.phase == 0:
            im = Image.new('RGB', self.canvas, (80, 80, 80))
        else:
            im = Image.new('RGB', self.canvas, (255, 255, 255))
        draw = ImageDraw.Draw(im)
        for y in range(self.ny):
            for x in range(self.nx):
                position = (x*self.bw+self.bw/2, y*self.bh+self.bh/2)
                if (x&1 == 0 and y&1 == 1) or (x&1 == 1 and y&1 == 0):
                    if self.phase == 1:
                        color = (80, 80, 80)
                        self.rect(draw, position[0], position[1], self.bw, self.bh, self.state[y][x], color)
                else:
                    if self.phase == 0:
                        color = (255, 255, 255)
                        self.rect(draw, position[0], position[1], self.bw, self.bh, self.state[y][x], color)
        im.save(image)
        self.dt += 1


class Anim2():
    state = []
    nx = 9+2
    ny = 9+2

    def _init__(self):
        self.init((0, 0), 0, 0)

    def init(self, canvas, steps, phase):
        self.dt = 0
        self.canvas = canvas
        self.steps = steps
        self.phase = phase
        self.bw = canvas[0]/self.nx
        self.bh = canvas[1]/self.ny
        self.an = 0
        self.state = [[0 for x in range(self.nx)] for y in range(self.ny)]

    def rect(self, draw, x0, y0, w, h, a, fill):
        x1 = s2*w*math.cos(c*(a-45))
        y1 = s2*h*math.sin(c*(a-45))
        x2 = s2*w*math.cos(c*(a+45))
        y2 = s2*h*math.sin(c*(a+45))
        x3 = s2*w*math.cos(c*(a+45+90))
        y3 = s2*h*math.sin(c*(a+45+90))
        x4 = s2*w*math.cos(c*(a+45+180))
        y4 = s2*h*math.sin(c*(a+45+180))
        points = [(x0+x1, y0+y1), (x0+x2, y0+y2), (x0+x3, y0+y3), (x0+x4, y0+y4)]
        draw.polygon(points, fill=fill, outline=(80, 80, 80))

    def drawframe(self, image):
        xa = math.cos(c*self.an)
        ya = math.sin(c*self.an)
        da = 360/4/self.steps*3

        for i in range(11):
            x = int(self.nx/2+xa*i)
            y = int(self.ny/2+ya*i)
            if x >= 0 and y >= 0 and x <= 10 and y <= 10:
                self.state[y][x] += da

        for x in range(self.nx):
            for y in range(self.ny):
                if self.state[y][x] > 0:
                    self.state[y][x] = self.state[y][x] + da
                if self.state[y][x] >= 90:
                    self.state[y][x] = 0

        self.an += 360/self.steps

        color = (192, 192, 192)
        im = Image.new('RGB', self.canvas, (80, 80, 80))
        draw = ImageDraw.Draw(im)
        for y in range(self.ny):
            for x in range(self.nx):
                position = (x*self.bw+self.bw/2, y*self.bh+self.bh/2)
                if (x <= 1+2 or y <= 1+2 or x >= 1+6 or y >= 1+6) and (x>0 and y>0 and x<10 and y<10):
                    self.rect(draw, position[0], position[1], self.bw, self.bh, self.state[y][x], color)
                else:
                    nic = 0
        im.save(image)
        self.dt += 1

# http://aleph.se/andart2/math/fractals-and-steiner-chains/
# https://en.wikipedia.org/wiki/Steiner_chain

class Anim3():
    # 400: 240/160 == 3/5 do 2/5 z 5 -> 160: 100/60
    #z = 1/5

    def _init__(self):
        self.init((0, 0), 0, 0)

    def init(self, canvas, level, width):
        self.dt = 0
        self.canvas = canvas
        self.level = level
        self.width = width
        self.x0 = self.canvas[0]/2
        self.y0 = self.canvas[1]/2
        self.r0 = (self.canvas[0]-16)/2

    def mycir000(self, draw, x, y, r, w):
        pts = []
        lim = 360*4
        for a in range(lim):
            xc = x + r * math.cos(c*a/lim*360)
            yc = y + r * math.sin(c*a/lim*360)
            pts.extend((xc, yc))
        draw.line(pts, fill=(0, 0, 0), width=w)

    def mycir(self, draw, x, y, r, w):
        color = (0, 0, 0)
        circle(draw, x, y, r, None, color)
        for rx in range(int(w/2)):
            circle(draw, x, y, r+rx*0.5, None, color)
            circle(draw, x, y, r-rx*0.5, None, color)

    def drawlevel(self, draw, level, x1, y1, r1):
        if level == 0:
            return
        self.mycir(draw, x1, y1, r1, self.width)

        x = x1
        y = y1
        r = r1
        self.drawlevel(draw, level-1, x, y, r)
        x = x1 - r1 * 2/5
        y = y1
        r = r1 * 3/5
        self.drawlevel(draw, level-1, x, y, r)
        x = x1 + r1 - r1 * 2/5 * 3/5 - r1 * 2/5 * 2/5 * 2
        y = y1
        r = r1 * 2/5 * 3/5
        self.drawlevel(draw, level-1, x, y, r)
        x = x1 + r1 - r1 * 2/5 * 2/5
        y = y1
        r = r1 * 2/5 * 2/5
        self.drawlevel(draw, level-1, x, y, r)

        x = x1 + r1 * 2/5 * 4/5 + r1 * 1/5 * 1/5 * 0.6 # approx!
        y = y1 - r1 * 3/5 + r1 * 1/5 * 2/5 - r1 * 1/5 * 1/5 * 1.18 # approx!
        r = r1 * 2/5 * 4/5 + r1 * 1/5 * 1/5 * 0.4 # approx!
        self.drawlevel(draw, level-1, x, y, r)

        x = x1 + r1 * 2/5 * 4/5 + r1 * 1/5 * 1/5 * 0.6 # approx!
        y = y1 + r1 * 3/5 - r1 * 1/5 * 2/5 + r1 * 1/5 * 1/5 * 1.18 # approx!
        r = r1 * 2/5 * 4/5 + r1 * 1/5 * 1/5 * 0.4 # approx!
        self.drawlevel(draw, level-1, x, y, r)


    def drawframe(self, image):
        im = Image.new('RGB', self.canvas, (255, 255, 255))
        draw = ImageDraw.Draw(im)

        self.drawlevel(draw, self.level, self.x0, self.y0, self.r0)

##        x = self.x0
##        y = self.y0
##        r = self.r0
##        self.mycir(draw, x, y, r)
##        x = self.x0 - self.r0 * 2/5
##        y = self.y0
##        r = self.r0 * 3/5
##        self.mycir(draw, x, y, r)
##        x = self.x0 + self.r0 - self.r0 * 2/5 * 3/5 - self.r0 * 2/5 * 2/5 * 2
##        y = self.y0
##        r = self.r0 * 2/5 * 3/5
##        self.mycir(draw, x, y, r)
##        x = self.x0 + self.r0 - self.r0 * 2/5 * 2/5
##        y = self.y0
##        r = self.r0 * 2/5 * 2/5
##        self.mycir(draw, x, y, r)
##
##        x = self.x0 + self.r0 * 2/5 * 4/5 + self.r0 * 1/5 * 1/5 * 0.6 # approx!
##        y = self.y0 - self.r0 * 3/5 + self.r0 * 1/5 * 2/5 - self.r0 * 1/5 * 1/5 * 1.18 # approx!
##        r = self.r0 * 2/5 * 4/5 + self.r0 * 1/5 * 1/5 * 0.4 # approx!
##        self.mycir(draw, x, y, r)
##
##        x = self.x0 + self.r0 * 2/5 * 4/5 + self.r0 * 1/5 * 1/5 * 0.6 # approx!
##        y = self.y0 + self.r0 * 3/5 - self.r0 * 1/5 * 2/5 + self.r0 * 1/5 * 1/5 * 1.18 # approx!
##        r = self.r0 * 2/5 * 4/5 + self.r0 * 1/5 * 1/5 * 0.4 # approx!
##        self.mycir(draw, x, y, r)

        im.save(image)
        self.dt += 1

# 3 black strips divided by white ones, center white then 8 rows each diff angle speed and variable len (same angle)
class Anim4():
    mar = 56 # margin
    count = 8 # count of circles
    strips = 3 # count of strips
    r0 = 48 # inner radius (white patch)
    bg = (255, 255, 255) # bg color

    def _init__(self):
        self.init((0, 0), 0)

    def init(self, canvas):
        self.dt = 0
        self.canvas = canvas

    def drawframe(self, image):
        im = Image.new('RGB', self.canvas, self.bg)
        draw = ImageDraw.Draw(im)
        dr = (self.canvas[0]/2-self.mar-self.r0)/self.count # assume canvas w=h
        da = 360/2/self.strips
        for x in range(self.count):
            drx = dr*(x+1)
            #drx = dr*x
            xy = [(self.mar+drx,self.mar+drx), (self.canvas[0]-self.mar-drx,self.canvas[1]-self.mar-drx)]
            draw.pieslice(xy, 0, 360, fill=self.bg, outline=None)
            af = self.dt*(self.count-x)
            for n in range(self.strips):
                start = da*(2*n+0)+af
                end = da*(2*n+1)+af
                draw.pieslice(xy, start, end, fill=(0,0,0), outline=None)
        draw.pieslice([(self.canvas[0]/2-self.r0/2, self.canvas[1]/2-self.r0/2), (self.canvas[0]/2+self.r0/2, self.canvas[1]/2+self.r0/2)], 0, 360, fill=(255,255,255), outline=None)

        im.save(image)
        self.dt += 1


class Anim5():
    state = []
    colors = []
    nx = 10
    ny = 10

    def _init__(self):
        self.init((0, 0), 0, 0)

    def init(self, canvas):
        self.dt = 0
        self.canvas = canvas
        self.bw = canvas[0]/self.nx
        self.bh = canvas[1]/self.ny
        self.angle = 0 # par
        self.speed = 3 # par
        self.state = [[random.randint(0, int(100*x/self.nx)) for x in range(self.nx)] for y in range(self.ny)]
        self.colors = [[(random.randint(96, 255), random.randint(96, 255), 0) for x in range(self.nx)] for y in range(self.ny)]

    def rect(self, draw, x0, y0, w, h, a, fill):
        x1 = s2*w*math.cos(c*(a-45))
        y1 = s2*h*math.sin(c*(a-45))
        x2 = s2*w*math.cos(c*(a+45))
        y2 = s2*h*math.sin(c*(a+45))
        x3 = s2*w*math.cos(c*(a+45+90))
        y3 = s2*h*math.sin(c*(a+45+90))
        x4 = s2*w*math.cos(c*(a+45+180))
        y4 = s2*h*math.sin(c*(a+45+180))
        points = [(x0+x1, y0+y1), (x0+x2, y0+y2), (x0+x3, y0+y3), (x0+x4, y0+y4)]
        draw.polygon(points, fill=fill, outline=None)

    def drawframe(self, image):
        for y in range(self.ny):
            for x in range(self.nx):
                self.state[y][x] += 1
                if self.state[y][x] > 100:
                    self.state[y][x] = 0

        im = Image.new('RGB', self.canvas, (0, 0, 0))
        draw = ImageDraw.Draw(im)
        for y in range(self.ny):
            for x in range(self.nx):
                position = (x*self.bw+self.bw/2, y*self.bh+self.bh/2)
                #size = self.state[y][x] / 100 # alt opt
                size = 0.5 + 0.4 * math.sin(c*self.state[y][x] / 100 * 360 * self.speed)
                self.rect(draw, position[0], position[1], self.bw*size, self.bh*size, self.angle, self.colors[y][x])

        im.save(image)
        self.dt += 1


class Anim6():
    def _init__(self):
        self.init((0, 0))

    def init(self, canvas):
        self.dt = 0
        self.canvas = canvas

    def fnc1(self, x, y, dt):
        return int(abs((x*math.sin(c*x/2)+y*math.cos(c*y/2+dt*2*c))*10))

    def fnc2(self, x, y, dt):
        return int(abs((x*math.sin(c*x+dt*3*c)+y*math.cos(c*y))*10))

    def fnc3(self, x, y, dt):
        return int(abs((x*math.sin(c*y/2)+y*math.cos(c*x/2+dt*3*c))*10))

    def drawframe(self, image):
        im = Image.new('RGB', self.canvas, (0, 0, 0))
        draw = ImageDraw.Draw(im)
        for y in range(self.canvas[1]):
            for x in range(self.canvas[0]):
                cr = self.fnc1(x, y, self.dt) & 255
                cg = self.fnc2(x, y, self.dt) & 255
                cb = self.fnc3(x, y, self.dt) & 255
                draw.point((x, y), fill=(cr, cg, cb))

        im.save(image)
        self.dt += 1


class Anim7():
    def _init__(self):
        self.init((0, 0))

    def init(self, canvas):
        self.dt = 0
        self.canvas = canvas

    def drawframe(self, image, params):
        im = Image.new('RGB', self.canvas, (0, 0, 0))
        draw = ImageDraw.Draw(im)

        w = self.canvas[0]
        h = self.canvas[1]
        radius = h/2 * params['scale']
        cnt = params['n']
        colorer = params['color']
        drc = 0.97 # !
        a_s = 0
        a_e = params['a_e']
        da = params['da']

        for i in range(cnt):
            color = new_colorer(colorer, i, cnt)
            draw.pieslice((w/2-radius, h/2-radius, w/2+radius, h/2+radius), a_s, a_e, fill=color)
            radius = radius * drc
            a_s = a_s + da
            a_e = a_e + da

        im.save(image)
        self.dt += 1

# ---

def do_anim1(fcc, video_name):
    o = Anim1()
    canvas = (512, 512)
    video = cv2.VideoWriter(video_name, fcc, 25, canvas)

    for rep in range(3):
        steps = 25
        o.init(canvas, steps, 0)
        for n in range(steps):
            o.drawframe(image)
            ima = cv2.imread(image)
            video.write(ima)
        o.init(canvas, steps, 1)
        for n in range(steps):
            o.drawframe(image)
            ima = cv2.imread(image)
            video.write(ima)

    cv2.destroyAllWindows()
    video.release()

def do_anim2(fcc, video_name):
    o = Anim2()

    canvas = (512, 512)
    video = cv2.VideoWriter(video_name, fcc, 25, canvas)

    for rep in range(3):
        steps = 100
        o.init(canvas, steps, 0)
        for n in range(steps):
            o.drawframe(image)
            ima = cv2.imread(image)
            video.write(ima)

    cv2.destroyAllWindows()
    video.release()

def do_anim3(fcc, video_name, steps):
    o = Anim3()

    canvas = (2480, 2480)
    o.init(canvas, 5, 44)
    o.drawframe('steiner_chain-one.png') # one

#    canvas = (512, 512)
#    video = cv2.VideoWriter(video_name, fcc, 25, canvas)

#    o.init(canvas, 5, 4)
#    for n in range(steps):
#        o.drawframe(image)
#        ima = cv2.imread(image)
#        video.write(ima)

#    cv2.destroyAllWindows()
#    video.release()

def do_anim4(fcc, video_name, steps):
    o = Anim4()

    canvas = (512, 512)
    video = cv2.VideoWriter(video_name, fcc, 25, canvas)

    o.init(canvas)
    for n in range(steps):
        o.drawframe(image)
        ima = cv2.imread(image)
        video.write(ima)

    cv2.destroyAllWindows()
    video.release()

def do_anim5(fcc, video_name, steps):
    o = Anim5()

    canvas = (800, 600)
    video = cv2.VideoWriter(video_name, fcc, 25, canvas)

    o.init(canvas)
    for n in range(steps):
        o.drawframe(image)
        ima = cv2.imread(image)
        video.write(ima)

    cv2.destroyAllWindows()
    video.release()

def do_anim6(fcc, video_name, steps):
    o = Anim6()

    canvas = (240, 120)
    video = cv2.VideoWriter(video_name, fcc, 25, canvas)

    o.init(canvas)
    for n in range(steps):
        o.drawframe(image)
        ima = cv2.imread(image)
        video.write(ima)

    cv2.destroyAllWindows()
    video.release()

def do_anim7(fcc, video_name, steps):
    o = Anim7()

    canvas = (720, 576)
    video = cv2.VideoWriter(video_name, fcc, 25, canvas)

#    da in [90, 89, 85, 80, 45, 12, 5]
#    a_e in [90, 60, 45, 35, 10, 5]
#n 36*1 to *4
# 'color': 'bw' 'red' 'Number3' 'ProgramCat'

    o.init(canvas)

    params = {'n': 36*1-35, 'color': 'wryb', 'da': 12, 'a_e': 45, 'scale': 3.4}
    for n in range(steps):
        o.drawframe(image, params)
        ima = cv2.imread(image)
        for m in range(2): #speed
            video.write(ima)
        params['n'] = params['n']+1

    params = {'n': 36*1-35, 'color': 'happy', 'da': 12, 'a_e': 30, 'scale': 3.4}
    for n in range(steps):
        o.drawframe(image, params)
        ima = cv2.imread(image)
        for m in range(2): #speed
            video.write(ima)
        params['n'] = params['n']+1

    params = {'n': 36*1, 'color': 'happy', 'da': 4, 'a_e': 30, 'scale': 1.0}
    for n in range(steps):
        o.drawframe(image, params)
        ima = cv2.imread(image)
        for m in range(2): #speed
            video.write(ima)
        params['da'] = params['da']+1

    params = {'n': 36*1, 'color': 'happy', 'da': 12, 'a_e': 10, 'scale': 1.0}
    for n in range(steps):
        o.drawframe(image, params)
        ima = cv2.imread(image)
        for m in range(2): #speed
            video.write(ima)
        params['a_e'] = params['a_e']+1

    cv2.destroyAllWindows()
    video.release()

# ---

def main():
    #fcc = -1  # select
    #fcc = cv2.VideoWriter_fourcc(*"XVID")
    fcc = cv2.VideoWriter_fourcc(*"MJPG")

    if False:
        do_anim1(fcc, video_name = 'anim-01-video.avi')
        do_anim2(fcc, video_name = 'anim-02-video.avi')
        do_anim3(fcc, video_name = 'anim-03-video.avi', steps = 25)
        do_anim4(fcc, video_name = 'anim-04-video.avi', steps = 300)
        do_anim5(fcc, video_name = 'anim-05-video.avi', steps = 300)
#        do_anim6(fcc, video_name = 'anim-06-video.avi', steps = 300)    # slow one!

    do_anim7(fcc, video_name = 'anim-07-video.avi', steps = 200)

if __name__ == '__main__':
    main()
