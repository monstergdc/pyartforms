from PIL import Image, ImageDraw
import random, math
import cv2
import os
from drawtools import circle, box, triangle, gradient, gradient2


# ZX Spectrum images drawn in Python
# (c)2018 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz
# https://pillow.readthedocs.io/en/3.1.x/reference/ImageDraw.html
# cre: 20180405
# upd; 20180406, 07
# upd; 20180428, 30 -- vid

# params
canvas = (256, 192)
step = 8
step2 = 4
video_name = 'video.avi'
image = 'tmp.png'   #tmp img file
#fcc = -1
#fcc = cv2.VideoWriter_fourcc(*"XVID")
fcc = cv2.VideoWriter_fourcc(*"MJPG")
dt = 200

c = math.pi/180
x0 = canvas[0] / 2
y0 = canvas[1] / 2

# ZX colors
C_0 = 192
C_1 = 252
ZXC0 = [(0,0,0), (0,0,C_0), (C_0,0,0), (C_0,0,C_0), (0,C_0,0), (0,C_0,C_0), (C_0,C_0,0), (C_0,C_0,C_0)]
ZXC1 = [(0,0,0), (0,0,C_1), (C_1,0,0), (C_1,0,C_1), (0,C_1,0), (0,C_1,C_1), (C_1,C_1,0), (C_1,C_1,C_1)]
CMAP_ = [ZXC0[0],ZXC0[1],ZXC0[2],ZXC0[3],ZXC0[4],ZXC0[5],ZXC0[6],ZXC0[7],
       ZXC1[0],ZXC1[1],ZXC1[2],ZXC1[3],ZXC1[4],ZXC1[5],ZXC1[6],ZXC1[7],
       ]
CMAP__ = [ZXC0[0],ZXC0[1],ZXC1[1],ZXC0[2],ZXC1[2],ZXC0[3],ZXC1[3],ZXC0[4],
       ZXC1[4],ZXC0[5],ZXC1[5],ZXC0[6],ZXC1[6],ZXC0[7],ZXC1[7],
       ]

CMAP8 = [ZXC0[0],ZXC0[1],ZXC1[1],ZXC0[2],ZXC1[2],ZXC0[3],ZXC1[3],ZXC0[4],
       ZXC1[4],ZXC0[5],ZXC1[5],ZXC0[6],ZXC1[6],ZXC0[7],ZXC1[7],
       ]

# ---

def paint0(draw, ou, box_or_cir, frame):
    for r in range(18):
        for n in range(8):
            nn = (n+3-3)%8
            cx = ZXC1[nn]
            da = 360/8*(c+frame)
            x = x0+step*(5+r)*math.cos(n*da+r*36*c)
            y = y0+step*(5+r)*math.sin(n*da+r*36*c)
            if box_or_cir == False:
                circle(draw, x, y, 32-r, fill=(cx), outline=ou)
            else:
                box(draw, x, y, 32-r, fill=(cx), outline=ou)

def paint1(draw, ou, box_or_cir, frame):
    for r in range(18):
        for n in range(8):
            nn = (n+3-3)%8
            cx = ZXC1[nn]
            da = 360/8*(c+frame)
            x = x0+step*(5+r+frame)*math.cos(n*da+r*36*c)
            y = y0+step*(5+r+frame)*math.sin(n*da+r*36*c)
            if box_or_cir == False:
                circle(draw, x, y, 32+1-1.7*(r+frame), fill=(cx), outline=ou)
            else:
                box(draw, x, y, 32+1-1.7*(r+frame), fill=(cx), outline=ou)

def paint2(draw, ou, box_or_cir, frame):
    for r in range(18):
        for n in range(8):
            nn = (n+3-3)%8
            cx = ZXC1[nn]
            da = 360/8*c
            x = x0+step*(5+r+frame)*math.cos(n*da+r*36*1.1*c)
            y = y0+step*(5+r+frame)*math.sin(n*da+r*36*c)
            if box_or_cir == False:
                circle(draw, x, y, 32+1-1.7*r, fill=(cx), outline=ou)
            else:
                box(draw, x, y, 32+1-1.7*r, fill=(cx), outline=ou)

def paint3a(draw, ou, box_or_cir, frame):
    for r in range(18):
        for n in range(8):
            nn = (r+3-3)%8
            cx = ZXC1[nn]
            da = 360/8*(c+frame)
            x = x0+step*(5+r+frame)*math.cos(n*da+r*72*c)
            y = y0+step*(5+r)*math.sin(n*da+r*72*c)
            if box_or_cir == False:
                circle(draw, x, y, 32+1-1.7*r, fill=(cx), outline=ou)
            else:
                box(draw, x, y, 32+1-1.7*r, fill=(cx), outline=ou)

def paint3b(draw, ou, box_or_cir, frame):
    for r in range(18):
        for n in range(8):
            nn = (n+3-3)%8
            cx = ZXC1[nn]
            da = 360/8*(c+frame)
            x = x0+step*(5+r)*math.cos(n*da+r*72*c)
            y = y0+step*(5+r)*math.sin(n*da+r*72*c)
            if box_or_cir == False:
                circle(draw, x, y, 32+1-1.7*r*frame, fill=(cx), outline=ou)
            else:
                box(draw, x, y, 32+1-1.7*r*frame, fill=(cx), outline=ou)

def paint3c(draw, ou, box_or_cir, frame):
    for r in range(18):
        for n in range(8):
            nn = (r+n)%8
            cx = ZXC1[nn]
            da = 360/8*(c+frame)
            x = x0+step*(5+r)*math.cos(n*da+r*72*c)
            y = y0+step*(5+r)*math.sin(n*da+r*72*c)
            if box_or_cir == False:
                circle(draw, x, y, 32+1-1.9*r, fill=(cx), outline=ou)
            else:
                box(draw, x, y, 32+1-1.9*r, fill=(cx), outline=ou)

def paint3d(draw, ou, box_or_cir, frame):
    for r in range(18):
        for n in range(8):
            nn = (r+1)%15
            cx = CMAP__[nn]
            da = 360/8*c
            x = x0+step*(5+r+frame*3)*math.cos(n*da+r*72*c)
            y = y0+step*(5+r+frame*2)*math.sin(n*da+r*72*c)
            if box_or_cir == False:
                circle(draw, x, y, 32+1-1.7*r+frame, fill=(cx), outline=ou)
            else:
                box(draw, x, y, 32+1-1.7*r, fill=(cx), outline=ou)

def paint4(draw, ou, box_or_cir, frame):
    for n in range(15+15):
        x1 = 0+n*step2
        x2 = canvas[0]-n*step2
        da = 360/8*(c+frame)
        y1 = 0+n*step2-32-32*math.cos(da*c)
        y2 = canvas[0]-n*step-32-32*math.sin(da*c)
        cn = n % 8
        cx = ZXC1[cn]
        xy = [(x1, y1), (x2, y2)]
        draw.ellipse(xy, fill=(cx), outline=None)

# ---

def call_painter(n, do_ou, box_or_cir, png, frame=0):
    im = Image.new('RGB', canvas, (0, 0, 0))
    draw = ImageDraw.Draw(im)
    if do_ou == True:
        ou = (0, 0, 0)
    else:
        ou = None
    if n == 0:
        paint0(draw, ou, box_or_cir, frame)
    if n == 1:
        paint1(draw, ou, box_or_cir, frame)
    if n == 2:
        paint2(draw, ou, box_or_cir, frame)
    if n == 3:
        paint3a(draw, ou, box_or_cir, frame)
    if n == 4:
        paint3b(draw, ou, box_or_cir, frame)
    if n == 5:
        paint3c(draw, ou, box_or_cir, frame)
    if n == 6:
        paint3d(draw, ou, box_or_cir, frame)
    if n == 7:
        paint4(draw, ou, box_or_cir, frame)
    im.save(png)

# ---

video = cv2.VideoWriter(video_name, fcc, 25, canvas)
for n in range(dt):
    call_painter(0, True, False, image, n/25/100)
    video.write(cv2.imread(image))
for n in range(dt):
    call_painter(0, True, True, image, n/25/100)
    video.write(cv2.imread(image))
for n in range(dt):
    call_painter(1, True, False, image, n/25/100)
    video.write(cv2.imread(image))
for n in range(dt):
    call_painter(1, True, True, image, n/25/100)
    video.write(cv2.imread(image))
for n in range(dt):
    call_painter(2, True, False, image, n/25/100)
    video.write(cv2.imread(image))
for n in range(dt):
    call_painter(2, True, True, image, n/25/100)
    video.write(cv2.imread(image))
for n in range(dt):
    call_painter(3, True, False, image, n/25/100)
    video.write(cv2.imread(image))
for n in range(dt):
    call_painter(3, True, True, image, n/25/100)
    video.write(cv2.imread(image))
for n in range(dt):
    call_painter(4, True, False, image, n/25/100)
    video.write(cv2.imread(image))
for n in range(dt):
    call_painter(4, True, True, image, n/25/100)
    video.write(cv2.imread(image))
for n in range(dt):
    call_painter(5, True, False, image, n/25/100)
    video.write(cv2.imread(image))
for n in range(dt):
    call_painter(5, True, True, image, n/25/100)
    video.write(cv2.imread(image))
for n in range(dt):
    call_painter(6, True, False, image, n/25)
    video.write(cv2.imread(image))
for n in range(dt):
    call_painter(6, True, True, image, n/25)
    video.write(cv2.imread(image))
for n in range(dt*2):
    call_painter(7, True, True, image, n/10)
    video.write(cv2.imread(image))

cv2.destroyAllWindows()
video.release()
