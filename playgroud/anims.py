
# ANIMS v1.0, Python version
# (c)2018 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz
# anim#1/anim#2 - recreated from seeing as in some GIFs I've once seen (so concept isn't mine)
# cre: 20180505
# upd: 20180506

# orig GIFs md5:
# #1: ad2bde22541ac1b05b2c08fd805ebafe *001.gif
# #2: 927339ac93af260455892d15e0f1f5c3 *CM128.gif

# see: https://pillow.readthedocs.io/en/3.1.x/reference/ImageDraw.html

# TODO:
# - ?


from PIL import Image, ImageDraw, ImageFilter
import random, math, os, sys
import cv2
from drawtools import *

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

# ---

def main():
    image = 'tmp.png'   #tmp img file
    #fcc = -1
    #fcc = cv2.VideoWriter_fourcc(*"XVID")
    fcc = cv2.VideoWriter_fourcc(*"MJPG")

    o = Anim1()
    video_name = 'anim-01-video.avi'
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

# ---

    o = Anim2()
    video_name = 'anim-02-video.avi'
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


if __name__ == '__main__':
    main()
