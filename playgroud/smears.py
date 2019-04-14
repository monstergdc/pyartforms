#! /usr/bin/env python
# -*- coding: utf-8 -*-

# experimental paint algorithms (artificial artist) in Python, v1.0
# (c)2017-2019 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz
# #1 cruel red smears
# #2 circles
# #3 triangles
# #4 poly
# #5 new smears (star flowers)
# #6 circle ripples
# #7 grayish rects mess
# #8 just rectangles, may flux
# #9 rays from center
# #10 long beziers
# #11 horizontal gradients with suprizes
# #12 opart-like boxes/circles
# #13 single big poly
# #14 ?
# #15 ?
# #16 
# #17
# #18 
# cre: 20180430
# upd: 20180501, 02, 03
# cre: 20180805, 07, 08
# upd: 20180928, 29
# upd: 20181019, 20
# upd: 20190105, 06, 12, 13, 18, 19, 21, 22
# upd: 20190306, 11, 29, 30
# upd: 20190414

# see:
# https://pillow.readthedocs.io/en/3.1.x/reference/ImageDraw.html
# http://pillow.readthedocs.io/en/5.1.x/reference/ImageFilter.html

# TODO:
# - ?


from PIL import Image, ImageDraw, ImageChops
import random, math, string, os, sys
from bezier import make_bezier
from drawtools import *
from color_defs import *

# ---

def mazy1(draw, params):
    w = params['w']
    h = params['h']
    random.seed()
    ts = [t/100.0 for t in range(101)]
    v = params['v']
    sc = float(h) / 3507 # lame par!
    wx = int(float(params['penw']) * sc)
    if wx <= 0:
        wx = 1

    for n in range(params['n']):
        po = [(random.randint(0, w), random.randint(0, h)),
              (random.randint(0, w), random.randint(0, h)),
              (random.randint(0, w), random.randint(0, h)),
              (random.randint(0, w), random.randint(0, h))]

        if 'color' in params:
            if params['color'] == 'happy':
                color = colors_happy[n%8]
            if params['color'] == 'wryb':
                color = colors_fwd[n%8]
            if params['color'] == 'rg':
                color = gradient2((255,255,0), (255,0,0), random.randint(0, 255), 255)
            if params['color'] == 'psych':
                color = colors_p[n%8]
        else:
            color = old_colorer(params)
        if 'addalpha' in params:
            color = add_alpha(color, params['addalpha'])
        r = color[0]
        g = color[1]
        b = color[2]

        if params['prefill'] == True:
            bezier = make_bezier(po)
            points = bezier(ts)
            draw.polygon(points, fill=color, outline=None)

        for m in range(params['m']):
            if params['keep'] == True:
                po0 = po[0]
                po3 = po[3]
            vsc = int(v*sc)
            po[:] = [(xy[0]+random.randint(0, vsc)-random.randint(0, vsc), xy[1]+random.randint(0, vsc)-random.randint(0, vsc)) for xy in po]
            if params['keep'] == True:
                po[0] = po0
                po[3] = po3
            if params['mode'] == 'red':
                color = (r ^ random.randint(0, 48), 0, 0)
            if params['mode'] == 'color':
                color = (r ^ random.randint(0, 48), g ^ random.randint(0, 48), b ^ random.randint(0, 48))
            if params['mode'] == 'black':
                rr = random.randint(0, 48)
                color = (rr, rr, rr)
            if params['mode'] == 'happy':
                color = colors_happy[n%8]
            if params['mode'] == 'wryb':
                color = colors_fwd[n%8]
            if params['mode'] == 'psych':
                color = colors_p[n%8]
                if random.randint(0, 100) > 80: # todo: as opt/par
                    color = (0,0,0)
            if 'addalpha' in params:
                color = add_alpha(color, params['addalpha'])
            bezier = make_bezier(po)
            points = bezier(ts)
            draw.line(points, fill=color, width=wx)

def mazy2(draw, params):
    w = params['w']
    h = params['h']
    cnt = params['n']
    cntm = params['m']
    v = int(h/50)
    random.seed()
    if cntm <= 0:
        cntm = 1

    for n in range(cnt):
        r1 = random.randint(int(h*0.15), int(h*0.4))
        po = [(random.randint(-r1, w+r1), random.randint(-r1, h+r1)),
            (random.randint(-r1, w+r1), random.randint(-r1, h+r1))]
        r0 = random.randint(int(r1*0.7), int(r1*0.99))
        if r0 < cntm:
            r0 = cntm
        de = 1/cntm
        for m in range(cntm):
            po[:] = [(xy[0]+random.randint(0, v)-random.randint(0, v), xy[1]+random.randint(0, v)-random.randint(0, v)) for xy in po]
            color = new_colorer(params['color'], m, cntm)
            circle(draw, po[0][0], po[0][1], int(r0*(1-m*de)), fill=color, outline=None)

def mazy3(draw, params):
    w = params['w']
    h = params['h']
    cnt = params['n']
    random.seed()

    def r(p, d):
        return int(p/2+random.randint(int(-p/d), int(p/d)))
    def r3(p):
        return r(p, 3)
    def r2(p):
        return r(p, 2)

    pold = [(r2(w), r2(h)), (r2(w), r2(h)), (r2(w), r2(h))]
    #d = 1.3 # par?
    d = 0.5
    for n in range(cnt):
        if params['mode'] == 'center':
            po = [(r(w, d), r(h, d)), (r(w, d), r(h, d)), (r(w, d), r(h, d))]
            cycle = -1
            d = d + 0.06 # par
        if params['mode'] == 'xcenter':
            d = 2.2 # par
            po = [(int(w/2), int(h/2)), (r(w, d), r(h, d)), (r(w, d), r(h, d))]
            cycle = -1
        if params['mode'] == 'rnd':
            d = 2.2 # par
            po = [(r(w, d), r(h, d)), (r(w, d), r(h, d)), (r(w, d), r(h, d))]
            cycle = -1
        if cycle == 0:
            po[0] = pold[0]
            po[1] = pold[1]
        if cycle == 1:
            po[1] = pold[1]
            po[2] = pold[2]
        if cycle == 2:
            po[2] = pold[2]
            po[0] = pold[0]
        pold = po

        color = new_colorer(params['color'], n, cnt)
        if 'addalpha' in params:
            color = add_alpha(color, params['addalpha'])

        triangle(draw, po, fill=color, outline=None)

def mazy4(draw, params):
    w = params['w']
    h = params['h']
    cnt = params['n']
    # todo: par
    sc = 2.05 # orig
    #sc = 1.0
    #sc = 3.0
    #sc = 0.7
    random.seed()

    if sc == 0:
        sc = 1
    sx = int(w/sc)
    sy = int(h/sc)
    for n in range(cnt):
        if params['mode'] == 'center':
            w0 = w/2
            h0 = h/2
        else:
            w0 = random.randint(0, w)
            h0 = random.randint(0, h)
        po = [(w0+random.randint(-sx, sx), h0+random.randint(-sy, sy)),
              (w0+random.randint(-sx, sx), h0+random.randint(-sy, sy)),
              (w0+random.randint(-sx, sx), h0+random.randint(-sy, sy)),
              (w0+random.randint(-sx, sx), h0+random.randint(-sy, sy)),
              (w0+random.randint(-sx, sx), h0+random.randint(-sy, sy)),
              (w0+random.randint(-sx, sx), h0+random.randint(-sy, sy)),
              (w0+random.randint(-sx, sx), h0+random.randint(-sy, sy)),
              (w0+random.randint(-sx, sx), h0+random.randint(-sy, sy)),
              (w0+random.randint(-sx, sx), h0+random.randint(-sy, sy)),
              (w0+random.randint(-sx, sx), h0+random.randint(-sy, sy)),
              (w0+random.randint(-sx, sx), h0+random.randint(-sy, sy)),
              (w0+random.randint(-sx, sx), h0+random.randint(-sy, sy)),
              (w0+random.randint(-sx, sx), h0+random.randint(-sy, sy)),
              (w0+random.randint(-sx, sx), h0+random.randint(-sy, sy)),
              (w0+random.randint(-sx, sx), h0+random.randint(-sy, sy)),
              (w0+random.randint(-sx, sx), h0+random.randint(-sy, sy)),
              (w0+random.randint(-sx, sx), h0+random.randint(-sy, sy)),
              (w0+random.randint(-sx, sx), h0+random.randint(-sy, sy)),
              (w0+random.randint(-sx, sx), h0+random.randint(-sy, sy)),
              (w0+random.randint(-sx, sx), h0+random.randint(-sy, sy))
              ]

        color = new_colorer(params['color'], n, cnt)
        if 'addalpha' in params:
            color = add_alpha(color, params['addalpha'])

        draw.polygon(po, fill=color, outline=None)

def mazy5(draw, params):
    w = params['w']
    h = params['h']
    colors = params['colors']
    random.seed()
    c = math.pi/180

    dg = h*0.037 # thickness
    r0 = h/2*0.93 # base radius
    rOut = float(h)*0.77 # outer circle radous
    sc = float(h)/2480
    step = 10
    for i in range(int(8+1)):
        a = random.randint(6, 24)
        rv = random.randint(20, 350)
        if i == 0:
            x0 = w/2
            y0 = h/2
        else:
            axy = c*(i-1)*360/8
            x0 = w/2 + rOut * math.cos(axy)
            y0 = h/2 + rOut * math.sin(axy)
        for m in range(16):
            points = []
            for n in range(int(360*step)):
                angle = c*float(n)/float(step)
                r = r0 + sc * (rv * math.sin(angle*a)) - m*dg
                x = x0 + r * math.cos(angle)
                y = y0 + r * math.sin(angle)
                points.extend((x, y))

            color = colors[m%8]

            if 'addalpha' in params:
                color = add_alpha(color, params['addalpha'])

            draw.polygon(points, fill=color, outline=params['outline'])

def mazy6(draw, params):
    w = params['w']
    h = params['h']
    cnt = params['cnt']
    useblack = params['useblack']
    random.seed()

    #c_ndx = 7
    for m in range(cnt):
        x = random.randint(int(w/2-w/3), int(w/2+w/3))
        y = random.randint(int(h/2-h/3), int(h/2+h/3))
        r = random.randint(int(h/25), int(h/6))
        n_r = random.randint(3, 15)
        c_ndx = 7
        for n in range(n_r):
            nn = n_r - n
            ro = int(r*(1+nn*nn*0.015))
            if n & 1 and useblack == True:
                c = (0, 0, 0)
                circle(draw, x, y, ro, fill=c, outline=None)
            else:
                if params['mode'] == 'red':
                    color = (255, 0, 0)
                if params['mode'] == 'rg':
                    color = gradient2((255,0,0), (255,255,0), n, n_r)
                if params['mode'] == 'gb':
                    color = gradient2((64,255,64), (64,64,255), n, n_r)
                if params['mode'] == 'black':
                    color = (255, 255, 255)
                if params['mode'] == 'blue':
                    color = colors_b[c_ndx]
                if params['mode'] == 'happy':
                    color = colors_happy[c_ndx]
                if params['mode'] == 'bwx':
                    color = colors_bwx[c_ndx]
                if params['mode'] == 'psych':
                    color = colors_p[c_ndx]

                circle(draw, x, y, ro, fill=color, outline=None)
            c_ndx = c_ndx - 1
            if c_ndx < 0:
                c_ndx = 7

def mazy7(draw, params):
    w = params['w']
    h = params['h']
    cnt = params['cnt']
    random.seed()

    for m in range(cnt):
        x1 = random.randint(int(w/2-w/3), int(w/2+w/3))
        y1 = random.randint(int(h/2-h/3), int(h/2+h/3))
        w1 = 0
        h1 = 0

        if params['mode'] == 'dec': # big2small any
            sc = (m+1)/cnt
            if sc == 0:
                sc = 1
            wm = int(w/8 * 1/sc)
            hm = int(w/8 * 1/sc)
            w1 = random.randint(int(w/35), wm)
            h1 = random.randint(int(w/35), hm)

        if params['mode'] == 'decp': # big2small rect prop
            sc = (m+1)/cnt
            if sc == 0:
                sc = 1
            wm = int(w/7 * 1/sc)
            hm = int(h/7 * 1/sc)
            w1 = random.randint(int(w/35), wm)
            h1 = random.randint(int(h/35), hm)

        if params['mode'] == 'const':   # const small sqare
            w1 = int(h/30)
            h1 = int(h/30)

        color = (0,0,0)
        if params['cmode'] == 'std':
            color = gradient2((255,255,255), (0,0,0), m, cnt)
        if params['cmode'] == 'inv':    # or inverse
            color = gradient2((0,0,0), (255,255,255), m, cnt)
        if params['cmode'] == 'rnd':    # or rnd
            ci = random.randint(0, 255)
            color = (ci,ci,ci)
        if params['cmode'] == 'color':    # color
            color = colors_happy[random.randint(0, 7)]
        if params['cmode'] == 'wryb':
            color = colors_fwd[random.randint(0, 7)]

        if 'addalpha' in params:
            color = add_alpha(color, params['addalpha'])

        rect(draw, x1, y1, w1, h1, fill=color, outline=None)

def mazy8(draw, params):
    w = params['w']
    h = params['h']
    xcnt = params['xcnt']
    ycnt = params['ycnt']
#    v = 20 #par

    w1 = int(w/xcnt)
    h1 = int(h/ycnt)
    for y in range(ycnt):
        for x in range(xcnt):
            x1 = x*w1 + int(w1/2)
            y1 = y*h1 + int(h1/2)
            ci = random.randint(0, 7)
            color = colors_happy[ci]
            # test
#            if random.randint(0, 100) > 50: #par
#                ar = random.randint(80, 200) #par
#                color = add_alpha(color, ar)
#            if random.randint(0, 100) > 80: #par
#                vx = float(x1)*(random.randint(0, v)-random.randint(0, v))/100.0
#                vy = float(y1)*(random.randint(0, v)-random.randint(0, v))/100.0
#                vw = float(w)*(random.randint(0, v)-random.randint(0, v))/100.0
#                vh = float(h)*(random.randint(0, v)-random.randint(0, v))/100.0
#            else:
#                vx = vy = vw = vh = 0
            vx = vy = vw = vh = 0
            #
            rect(draw, x1+vx, y1+vy, w1+vw, h1+vh, fill=color, outline=None)

def mazy9(draw, params):
    w = params['w']
    h = params['h']
    cnt = params['n']
    random.seed()
    c = math.pi/180
    if 'v' in params: 
        v = params['v']
    else:
        v = 0
    if 'rndc' in params: 
        rndc = params['rndc']
    else:
        rndc = False

    po = [(int(w/2), int(h/2)), (0, 0), (0, 0)]
    da = float(360)/cnt
    r = w
    for n in range(cnt):
        if v > 0:
            v1 = random.randint(int(-v), int(v))
            v2 = random.randint(int(-v), int(v))
            po[0] = (int(w/2)+v1, int(h/2)+v2)
        x = w/2 + r * math.cos(c*da*n)
        y = h/2 + r * math.sin(c*da*n)
        po[1] = (x, y)
        x = w/2 + r * math.cos(c*da*(n+1))
        y = h/2 + r * math.sin(c*da*(n+1))
        po[2] = (x, y)

        ci = random.randint(0, 255)
        if params['color'] == 'red':
            color = gradient2((0,0,0), (255,0,0), ci, 255)
        if params['color'] == 'rg':
            color = gradient2((255,0,0), (255,255,0), ci, 255)
        if params['color'] == 'bw':
            color = gradient2((0,0,0), (255,255,255), ci, 255)
        if params['color'] == 'happy':
            if rndc == True:
                color = colors_happy[random.randint(0, 7)]
            else:
                color = colors_happy[n%8]
        if params['color'] == 'psych':
            if rndc == True:
                color = colors_p[random.randint(0, 7)]
            else:
                color = colors_p[n%8]
        #test
        #color = (color[0], color[1], color[2], 100)
        #
        triangle(draw, po, fill=color, outline=None)


def mazy10(draw, params):
    w = params['w']
    h = params['h']
    cnt = params['n']
    mode = params['mode']
    random.seed()
    np = 1800 #par
    ts = [t/float(np) for t in range(np+1)]
    sc = float(h) / 3507
    wx = int(float(params['penw']) * sc)
    if wx <= 0:
        wx = 1

    def rwh():
        ex = 1
        if params['open'] == True:
            return (random.randint(-w*ex, w*(ex+1)), random.randint(-h*ex, h*(ex+1)))
        else:
            return (random.randint(0, w), random.randint(0, h))

    for n in range(cnt):
        po = [rwh()]
        for x in range(params['complexity']):
            po.extend([rwh()])
        if params['color'] == 'happy':
            color = colors_happy[n%8]
        if params['color'] == 'rg':
            color = gradient2((255,255,0), (255,0,0), random.randint(0, 255), 255)
        if params['color'] == 'red':
            color = gradient2((0,0,0), (255,0,0), random.randint(0, 255), 255)
        if params['color'] == 'wryb':
            color = colors_fwd[n%8]

        if 'addalpha' in params:
            color = add_alpha(color, params['addalpha'])

        bezier = make_bezier(po)
        points = bezier(ts)
        if params['mode'] == 'line':
            draw.line(points, fill=color, width=wx)
        if params['mode'] == 'fill':
            draw.polygon(points, fill=color, outline=None)

# TODO: canvas 800 or 2000 - fix width - issue only on srv?!
# TODO: also like 11 only more freq + diagonals + symetric opt?
def mazy11(draw, params):
    w = params['w']
    h = params['h']
    cnt = params['n']
    random.seed()
    dy = int(h/cnt)
    if dy*cnt < h:  # lame fix for small images
        cnt += 3
    steps = 512 #const, max rational limit
    if steps > w:
        steps = w
    dx = w/steps
    for n in range(cnt):
        n1 = random.randint(0, 7)
        n2 = n%8
        n3 = random.randint(0, 7)
        color1 = colors_happy[n1]
        color2 = colors_happy[n2]
        color3 = colors_happy[n3]
        for step in range(steps):
            color = gradient(color1, color2, color3, step, steps)
            rect(draw, int(step*dx+dx/2), int(n*dy+dy/2), int(dx), int(dy), fill=color, outline=None)

def mazy12(draw, params):
    w = params['w']
    h = params['h']
    cnt = params['n']
    o = params['o']
    v = params['v']
    random.seed()
    c = math.pi/180
    w0 = w/2
    h0 = h/2
    color = params['color']
    r = int(h/2/2)
    for i in range(cnt):
        a = c*i/cnt*360
        x = int(w0+r*math.cos(a))
        y = int(h0+r*math.sin(a))
        if v:
            va = random.randint(int(-h0/5), int(h0/5)) # par
        else:
            va = 0
        if i&1 == 0:
            co = (0,0,0)
            if color != None:
                co = new_colorer(color, random.randint(0, 7), 0)
            if o == 'box':
                rect(draw, x, y, r+va, r+va, fill=co, outline=None)
            if o == 'cir':
                circle(draw, x, y, r+va, fill=co, outline=None)
        else:
            co = (255,255,255)
            if color != None:
                co = new_colorer(color, random.randint(0, 7), 0)
            if o == 'box':
                rect(draw, x, y, r+va, r+va, fill=co, outline=(0,0,0))
            if o == 'cir':
                circle(draw, x, y, r+va, fill=co, outline=(0,0,0))

def mazy13(draw, params):
    w = params['w']
    h = params['h']
    cnt = params['n']
    random.seed()

    w0 = w/2
    h0 = h/2
    sc = 1.0
    sx = int(w/sc)
    sy = int(h/sc)
    po = []
    for n in range(cnt):
        newp = (w0+random.randint(-sx, sx), h0+random.randint(-sy, sy))
        po.append(newp)
    color = params['color']
    draw.polygon(po, fill=color, outline=None)

def mazy14(draw, params):
    w = params['w']
    h = params['h']
    cnt = params['n']
    random.seed()
    c = math.pi/180
    if w > h:
        sc = w/2*1.5/cnt
    else:
        sc = h/2*1.5/cnt

    im1 = Image.new('RGB', (params['w'], params['h']), params['Background'])
    im2 = Image.new('RGB', (params['w'], params['h']), params['color']) # note: 2nd image is reversed
    draw1 = ImageDraw.Draw(im1)
    draw2 = ImageDraw.Draw(im2)

    # centered circles
    for n in range(cnt):
        r = int(sc*(cnt-n))
        if n&1 == 0:
            co = params['Background']
        else:
            co = params['color']
        circle(draw1, int(w/2), int(h/2), r, fill=co, outline=None)

    # spirals from center - rework, it's bad!
    spirals_cnt = cnt
    spiral_steps = 112 #par
    if w > h:
        spiral_width = int(w/2*1.5/spirals_cnt)
    else:
        spiral_width = int(h/2*1.5/spirals_cnt)
    for n in range(spirals_cnt):
        for m in range(spiral_steps):
            r = m * spiral_width * 1 #par
            a = (c*m*360/spiral_steps)*4 + (c*n*360/spirals_cnt) #par
            newp = (int(w/2)+r*math.cos(a), int(h/2)+r*math.sin(a))
            if m == 0:
                oldp = newp
            draw2.line([(oldp[0], oldp[1]), (newp[0], newp[1])], fill=params['Background'], width=spiral_width)
            oldp = newp
    imout = ImageChops.difference(im1, im2)
    params['im'].paste(imout, (0, 0))

def mazy15(draw, params):
    w = params['w']
    h = params['h']
    cnt = params['n']
    random.seed()
    c = math.pi/180
    if w > h:
        sc = w/2*1.5/cnt  # note: off-screen to fill all
    else:
        sc = h/2*1.5/cnt

    im1 = Image.new('RGB', (params['w'], params['h']), params['Background'])
    im2 = Image.new('RGB', (params['w'], params['h']), params['color']) # note: 2nd image is reversed in 'polarity' for better difference effect
    draw1 = ImageDraw.Draw(im1)
    draw2 = ImageDraw.Draw(im2)

    # centered circles #1
    for n in range(cnt):
        r = int(sc*(cnt-n))
        if n&1 == 0:
            co = params['Background']
        else:
            co = params['color']
        if params['style'] == 'circle':
            circle(draw1, int(w/2), int(h/2), r, fill=co, outline=None)
        else:
            xywh = [(int(w/2-r/2), int(h/2-r/2)), (int(w/2+r/2), int(h/2+r/2))]
            draw1.rectangle(xywh, fill=co, outline=None)

# todo: also move 1st circles | freq (var) for circle opt

    # de-centered circles #2
    ys2 = 0
    xs2 = 0
    if 'xs2' in params:
        xs2 = params['xs2']
    if 'ys2' in params:
        ys2 = params['ys2']
    for n in range(cnt):
        r = int(sc*(cnt-n))
        if n&1 == 0:
            co = params['Background']
        else:
            co = params['color']
        if 'mode' in params:
            if params['mode'] == 'rnd':
                if 'xs2v' in params:
                    xs2 = random.randint(-params['xs2v'], params['xs2v'])
                if 'ys2v' in params:
                    ys2 = random.randint(-params['ys2v'], params['ys2v'])
            if params['mode'] == 'linear':
                if 'xs2v' in params:
                    xs2 = xs2 + params['xs2v']
                if 'ys2v' in params:
                    ys2 = ys2 + params['ys2v']
            if params['mode'] == 'circle':
                a0 = c*n/cnt*360
                if 'xs2v' in params:
                    xs2 = params['ys2v']*math.cos(a0)
                if 'ys2v' in params:
                    ys2 = params['ys2v']*math.sin(a0)
        if params['style'] == 'circle':
            circle(draw2, int(w/2+xs2), int(h/2+ys2), r, fill=co, outline=None)
        else:
            xywh = [(int(w/2+xs2-r/2), int(h/2+ys2-r/2)), (int(w/2+xs2+r/2), int(h/2+ys2+r/2))]
            draw1.rectangle(xywh, fill=co, outline=None)

    imout = ImageChops.difference(im1, im2)
    params['im'].paste(imout, (0, 0))

# future fun

def mazy16(draw, params):
    w = params['w']
    h = params['h']
    cnt = params['n']
    # ...
    return 0

def mazy17(draw, params):
    w = params['w']
    h = params['h']
    cnt = params['n']
    random.seed()
    # ...
    return 0

def mazy18(draw, params):
    w = params['w']
    h = params['h']
    cnt = params['n']
    random.seed()
    # ...
    return 0
