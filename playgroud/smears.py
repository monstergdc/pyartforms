#! /usr/bin/env python
# -*- coding: utf-8 -*-

# PyArtForms - Python generative art forms paint algorithms (artificial artist)
# experimental 'smears' paint algorithms, v1.0
# (c)2017-2021 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz

# #1 'cruel red smears', not only red
# #2 circles
# #3 triangles
# #4 poly
# #5 new smears aka star flowers
# #6 circle ripples
# #7 grayish rects mess
# #8 just rectangles, may flux (tested, ok) --- finish: new colorer, new params, more variants in defs
# #9 rays from center
# #10 long beziers
# #11 horizontal gradients with suprizes (tested, ok) --- finish new colorer
# #12 opart-like boxes/circles/triangles (tested, ok/so-so)
# #13 opart-like single big poly (tested, ok)
# #14 opart-like cicrles xor-cut by triangles (tested, ok)
# #15 opart-like circle-interference patterns (...)
# #16 opart-like circles (tested, ok)
# #17 scottish grid (tested, so-so)
# #18 slim colorful circles (tested, ok)
# #19 op-art grid (tested, ok)
# #20 <new 2020 in progress>
# #21 
# #22 
# #23 
# #24
# #25 

# cre: 20180430
# upd: 20180501, 02, 03
# cre: 20180805, 07, 08
# upd: 20180928, 29
# upd: 20181019, 20
# upd: 20190105, 06, 12, 13, 18, 19, 21, 22
# upd: 20190306, 11, 29, 30
# upd: 20190414, 15, 17, 18, 22, 24, 26, 27
# upd: 20200507, 10
# upd: 20210106, 15, 16, 19, 20, 21, 22
# upd: 20210515, 16, 22, 23, 24

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

def init_common(params):
    random.seed()
    w = params['w']
    h = params['h']
    if 'n' in params:
        cnt = params['n']
    else:
        cnt = None
    return w, h, cnt

# ---

def mazy1(draw, params):
    """ ? """
    w, h, cnt = init_common(params)
    if 'mar' in params:
        mar = params['mar']
    else:
        mar = 0
    if 'v' in params:
        v = params['v']
    else:
        v = 0
    ts = [t/100.0 for t in range(101)] # par?
    sc = float(h) / 3507 # lame par!
    wx = int(float(params['penw']) * sc)
    if wx <= 0:
        wx = 1

    for n in range(cnt):
        po = [(random.randint(0+mar, w-mar), random.randint(0+mar, h-mar)),
              (random.randint(0+mar, w-mar), random.randint(0+mar, h-mar)),
              (random.randint(0+mar, w-mar), random.randint(0+mar, h-mar)),
              (random.randint(0+mar, w-mar), random.randint(0+mar, h-mar))]

        if 'color' in params:
            if params['color'] == 'rg':
                color = gradient2((255,255,0), (255,0,0), random.randint(0, 255), 255)
            else:
                color = new_colorer(params['color'], n, cnt)
        else:
            color = (0,0,0)
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
            old = False
            if params['mode'] == 'red':
                color = (r ^ random.randint(0, 48), 0, 0)
                old = True
            if params['mode'] == 'black':
                rr = random.randint(0, 48)
                color = (rr, rr, rr)
                old = True
            if old == False:
                color = new_colorer(params['mode'], n, cnt)
            if 'addblack' in params: # todo: (re)use
                if params['addblack'] == True and random.randint(0, 100) > 80:
                    color = (0,0,0)
            if 'addalpha' in params:
                color = add_alpha(color, params['addalpha'])
            bezier = make_bezier(po)
            points = bezier(ts)
            draw.line(points, fill=color, width=wx)

def mazy2(draw, params):
    """ ? """
    w, h, cnt = init_common(params)
    cntm = params['m']
    v = int(h/50)
    #v = int(h/20) # test2
    #v = int(h/200) # test3
    if cntm <= 0:
        cntm = 1

    for n in range(cnt):
        r1 = random.randint(int(h*0.15), int(h*0.45))
        po = [(random.randint(-r1, w+r1), random.randint(-r1, h+r1)),
            (random.randint(-r1, w+r1), random.randint(-r1, h+r1))]
        r0 = random.randint(int(r1*0.7), int(r1*0.99))
        if r0 < cntm:
            r0 = cntm
        de = 1/cntm
        for m in range(cntm):
            #v = int((cntm-m)/cntm * h/20) # test4
            # w/ v=0 interesting too?
            po[:] = [(xy[0]+random.randint(0, v)-random.randint(0, v), xy[1]+random.randint(0, v)-random.randint(0, v)) for xy in po]
            color = new_colorer(params['color'], m, cntm)
            if 'addalpha' in params:
                color = add_alpha(color, params['addalpha'])
            circle(draw, po[0][0], po[0][1], int(r0*(1-m*de)), fill=color, outline=None)

def mazy3(draw, params):
    """ ? """
    w, h, cnt = init_common(params)

    def r(p, d):
        return int(p/2+random.randint(int(-p/d), int(p/d)))
    def r3(p):
        return r(p, 3)
    def r2(p):
        return r(p, 2)

    # todo: what is/was cycle for???
    pold = [(r2(w), r2(h)), (r2(w), r2(h)), (r2(w), r2(h))]
    #d = 1.3 # par?
    d = 0.5 # par?
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
    """ ? """
    w, h, cnt = init_common(params)
    sc = 2.1 # base, ok (2.05 -> 2.1)
    if 'sc' in params:
        sc = params['sc']
    if sc <= 0:
        sc = 1
    #sc = 0.7 # so, so

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
    """ ? """
    w, h, cnt = init_common(params) # cnt unused
    colors = params['colors']
    c = math.pi/180

    dg = h*0.037 # thickness, par
    #dg = h*0.01 # TEST interesting...
    r0 = h/2*0.93 # base radius, par
    #r0 = h/2*1.5 # TEST
    rOut = float(h)*0.77 # outer circle radius, par
    #rOut = float(h)*0.3 # TEST
    sc = float(h)/2480 # par
    step = 10 # par (?)
    n = 10 # count of all 'stars', const, par
    for i in range(n):
        a = random.randint(4, 28)  # number of 'spikes', par
        rv = random.randint(20, int(300/a*2))  # 'spike' amplitude, [todo: correlate with a - less if a big] par
        if i == 0:
            x0 = w/2
            y0 = h/2
        else:
            axy = c*(i-1)*360/8 # par
            x0 = w/2 + rOut * math.cos(axy)
            y0 = h/2 + rOut * math.sin(axy)
        bands = 16 # par r decrease steps, also related to num colors
        #bands = len(colors)*3 # test
        for m in range(bands):
            points = []
            for n in range(int(360*step)):
                angle = c*float(n)/float(step)
                r = r0 + sc * (rv * math.sin(angle*a)) - m*dg
                x = x0 + r * math.cos(angle)
                y = y0 + r * math.sin(angle)
                points.extend((x, y))

            color = colors[m%len(colors)]   # TODO: fix: not new not old
            if 'addalpha' in params:
                color = add_alpha(color, params['addalpha'])
            draw.polygon(points, fill=color, outline=params['outline'])

def mazy6(draw, params):
    """ Co-centered circle groups """
    w, h, cnt = init_common(params)
    if 'useblack' in params:
        useblack = params['useblack']
    else:
        useblack = False

    for m in range(cnt):
        x = random.randint(int(w/2-w/3), int(w/2+w/3))
        y = random.randint(int(h/2-h/3), int(h/2+h/3))
        #todo: start with big 1st?
        r = random.randint(int(h/25), int(h/7)) # par
        n_r = random.randint(3, 16) # par
        for n in range(n_r):
            nn = n_r - n
            ro = int(r*(1+nn*nn*0.015)) # todo: par, and more other par
            if n & 1 and useblack == True:
                color = (0, 0, 0)
            else:
                color = new_colorer(params['mode'], n, n_r)
                try:
                    color
                except NameError:
                    print('ERROR: undefined color mode, using black', params['mode'])
                    color = (0,0,0)
            circle(draw, x, y, ro, fill=color, outline=None)

def mazy7(draw, params):
    """ Random rectangles """
    w, h, cnt = init_common(params)
    cnt = params['cnt'] # todo: cnt -> n, then common
    hdiv = int(h/30) # dflt
    if 'div' in params:
        d = int(params['div'])
        if d <= 0:
            d = 1
        hdiv = int(h/d)

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
            w1 = hdiv
            h1 = hdiv

        color = (0,0,0)
        if params['cmode'] == 'std':
            color = gradient2((255,255,255), (0,0,0), m, cnt)
        if params['cmode'] == 'inv':    # or inverse
            color = gradient2((0,0,0), (255,255,255), m, cnt)
        if params['cmode'] == 'rnd':    # or rnd
            ci = random.randint(0, 255)
            color = (ci,ci,ci)
        if params['cmode'] == 'color':    # color
            color = colors_happy[random.randint(0, len(colors_happy)-1)]
        if params['cmode'] == 'wryb':
            color = colors_fwd[random.randint(0, len(colors_fwd)-1)]
        if params['cmode'] == 'BeachTowels':
            color = colors_BeachTowels[random.randint(0, len(colors_BeachTowels)-1)]
        if params['cmode'] == 'MoonlightBytes6':
            color = colors_MoonlightBytes6[random.randint(0, len(colors_MoonlightBytes6)-1)]
        if params['cmode'] == 'RainbowDash':
            color = colors_RainbowDash[random.randint(0, len(colors_RainbowDash)-1)]
        # todo: new colorer proper

        if 'addalpha' in params:
            color = add_alpha(color, params['addalpha'])

        rect(draw, x1, y1, w1, h1, fill=color, outline=None)

def mazy8(draw, params):
    """ Block grid with random colors """
    w, h, cnt = init_common(params) # cnt unused
    xcnt = params['xcnt']
    ycnt = params['ycnt']

    # todo: new par use ext
    alpha_flux_p = 50
    alpha_flux_p = None
    alpha_flux_vmin = 20
    alpha_flux_vmax = 90-40

    flux_p = None
    v = 0
    if 'flux_p' in params:
        flux_p = params['flux_p']
    if 'v' in params:
        v = params['v']

    border = 0
    if 'border' in params:
        border = params['border']

    w1 = int(w/xcnt)
    h1 = int(h/ycnt)
    for y in range(ycnt-border*2):
        for x in range(xcnt-border*2):
            x1 = x*w1 + int(w1/2) + border*w1
            y1 = y*h1 + int(h1/2) + border*h1
            ci = random.randint(0, 7)
            # todo: new colorer FULLY proper (range)
            color = new_colorer(params['color'], ci, -1)
            if alpha_flux_p != None and alpha_flux_p > 0: # rnd flux
                if random.randint(0, 100) > alpha_flux_p:
                    ar = random.randint(alpha_flux_vmin, alpha_flux_vmax)
                    color = add_alpha(color, ar)
            vx = vy = vw = vh = 0
            if flux_p != None and flux_p > 0: # rnd flux
                if random.randint(0, 100) > flux_p:
                    vx = float(w1)*(random.randint(0, v)-random.randint(0, v))/100.0
                    vy = float(h1)*(random.randint(0, v)-random.randint(0, v))/100.0
                    vw = float(w1)*(random.randint(0, v)-random.randint(0, v))/100.0
                    vh = float(h1)*(random.randint(0, v)-random.randint(0, v))/100.0
            rect(draw, x1+vx, y1+vy, w1+vw, h1+vh, fill=color, outline=None)

def mazy9(draw, params):
    """ 'Warp' effect - triangles around center, opt center point shifted """
    w, h, cnt = init_common(params)
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
        if params['color'] == 'BeachTowels':
            if rndc == True:
                color = colors_BeachTowels[random.randint(0, len(colors_BeachTowels)-1)]
            else:
                color = colors_BeachTowels[n%len(colors_BeachTowels)]
        if params['color'] == 'gits':
            if rndc == True:
                color = colors_gits[random.randint(0, len(colors_gits)-1)]
            else:
                color = colors_gits[n%len(colors_gits)]
        # todo: new colorer proper
        #test
        #color = (color[0], color[1], color[2], 100)
        #
        triangle(draw, po, fill=color, outline=None)

def mazy10(draw, params):
    """ Random bezier threads or aeas """
    w, h, cnt = init_common(params)
    mode = params['mode']

    # todo: fix make threads no-lame
    # todo: for closed make internal pts bigger while 1st+last with margin?
    # todo: 1-2 bezier stripes then rnd mutate?

    #np = 1800 #par
    np = 5000 #par
    ts = [t/float(np) for t in range(np+1)]
    sc = float(h) / 3507 # todo: not like that?
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
        if params['color'] == 'blue_const':
            color = (16,48,255)
        if params['color'] == 'happy':
            color = colors_happy[n%len(colors_happy)]
        if params['color'] == 'rg':
            color = gradient2((255,255,0), (255,0,0), random.randint(0, 255), 255)
        if params['color'] == 'red':
            color = gradient2((0,0,0), (255,0,0), random.randint(0, 255), 255)
        if params['color'] == 'wryb':
            color = colors_fwd[n%len(colors_fwd)]
        # todo: new colorer proper

        if 'addalpha' in params:
            color = add_alpha(color, params['addalpha'])

        bezier = make_bezier(po)
        points = bezier(ts)
        if params['mode'] == 'line':
            draw.line(points, fill=color, width=wx)
        if params['mode'] == 'fill':
            draw.polygon(points, fill=color, outline=None)

def mazy11(draw, params):
    """ Horizontal gradients with suprizes """
    w, h, cnt = init_common(params)

    dy = float(h)/cnt
    if dy*cnt < h:  # lame fix for small images
        cnt += 3
    steps = 256 # const, max rational limit for RGB24 gradient
    if steps > w:
        steps = w
    dx = float(w)/steps
    for n in range(cnt):
        if params['color'] == 'happy':
            cx = colors_happy
        if params['color'] == 'BeachTowels':
            cx = colors_BeachTowels
        if params['color'] == 'Rainbow':
            cx = colors_Rainbow
        if params['color'] == 'MoonlightBytes6':
            cx = colors_MoonlightBytes6
        if params['color'] == 'MetroUI':
            cx = colors_MetroUI
        if params['color'] == 'ProgramCat':
            cx = colors_ProgramCat
        if params['color'] == 'wryb':
            cx = colors_fwd
        if params['color'] == 'yorb':
            cx = colors_yorb
        csize = len(cx)
        n1 = random.randint(0, csize-1)
        n2 = n%csize
        n3 = random.randint(0, csize-1)
        color1 = cx[n1]
        color2 = cx[n2]
        color3 = cx[n3]
        # todo: new colorer proper
        for step in range(steps):
            color = gradient(color1, color2, color3, step, steps)
            x = step*dx
            y = n*dy
            xy = [(x, y), (x+dx, y+dy)]
            draw.rectangle(xy, fill=color, outline=None)

def mazy12(draw, params):
    """ Opart-like boxes/circles/triangles """
    w, h, cnt = init_common(params)
    c = math.pi/180
    o = params['o']
    v = False
    if 'v' in params:
        v = params['v']
    rc = 1.0
    if 'rc' in params:
        rc = params['rc']
    w0 = w/2
    h0 = h/2
    r = int(h/2/2 * rc)
    for i in range(cnt):
        a = c*i/cnt*360
        x = int(w0+r*math.cos(a))
        y = int(h0+r*math.sin(a))
        if v:
            va = random.randint(int(-h0/8), int(h0/8)) # par
            vx = random.randint(int(-w0/8), int(w0/8)) # par
            vy = random.randint(int(-h0/8), int(h0/8)) # par
        else:
            va = 0
            vx = 0
            vy = 0
        if i&1 == 0:
            co = (0,0,0)
            ou = (255,255,255)
        else:
            co = (255,255,255)
            ou = (0,0,0)
        if o == 'box':
            rect(draw, x+vx, y+vy, r+va, r+va, fill=co, outline=ou)
        if o == 'cir':
            circle(draw, x+vx, y+vy, r+va, fill=co, outline=ou)
        if o == 'tri':
            vx1 = random.randint(int(-w0/2), int(w0/2)) # par
            vx2 = random.randint(int(-w0/2), int(w0/2)) # par
            vx3 = random.randint(int(-w0/2), int(w0/2)) # par
            vy1 = random.randint(int(-h0/2), int(h0/2)) # par
            vy2 = random.randint(int(-h0/2), int(h0/2)) # par
            vy3 = random.randint(int(-h0/2), int(h0/2)) # par
            points = [(x+vx1, y+vy1), (x+vx2, y+vy2), (x+vx3, y+vy3)]
            triangle(draw, points, fill=co, outline=ou)

def mazy13(draw, params):
    """ Opart-like single big poly """
    w, h, cnt = init_common(params)
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
    """ Opart-like cicrles xor-cut by triangles """
    w, h, cnt = init_common(params)
    c = math.pi/180
    if w > h:
        sc = w/2*1.5/cnt
    else:
        sc = h/2*1.5/cnt
    if 'm' in params:
        cnt2 = params['m']
        if cnt2 < 4:
            cnt2 = 4
    else:
        cnt2 = 4 # some min
    v = 0
    if 'div' in params:
        v = params['div']
        if v > 0:
            v = w/v

    im1 = Image.new('RGB', (params['w'], params['h']), params['Background'])
    im2 = Image.new('RGB', (params['w'], params['h']), params['color']) # note: 2nd image is reversed
    draw1 = ImageDraw.Draw(im1)
    draw2 = ImageDraw.Draw(im2)

    for n in range(cnt): # centered circles 1st
        r = int(sc*(cnt-n))
        if n&1 == 0:
            co = params['Background']
        else:
            co = params['color']
        circle(draw1, int(w/2), int(h/2), r, fill=co, outline=None)

    po = [(int(w/2), int(h/2)), (0, 0), (0, 0)]
    da = float(360)/cnt2
    r = w
    for n in range(cnt2):
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
        if n&1 == 0:
            color = params['Background']
        else:
            color = params['color']
        triangle(draw2, po, fill=color, outline=None)

    imout = ImageChops.difference(im1, im2)
    params['im'].paste(imout, (0, 0))
    draw1 = None
    draw2 = None
    im1 = None
    im2 = None
    imout = None

def mazy15(draw, params):
    """ ? """
    w, h, cnt = init_common(params)
    c = math.pi/180
    if w > h:
        sc = w/2*1.5/cnt  # note: off-screen to fill all
    else:
        sc = h/2*1.5/cnt
    ys1 = 0
    xs1 = 0
    if 'xs1' in params:
        xs1 = params['xs1']
    if 'ys1' in params:
        ys1 = params['ys1']
    ys2 = 0
    xs2 = 0
    if 'xs2' in params:
        xs2 = params['xs2']
    if 'ys2' in params:
        ys2 = params['ys2']

    def draw_it(d, xs, ys):
        if n&1 == 0:
            co = params['Background']
        else:
            co = params['color']
        if params['style'] == 'circle':
            circle(d, int(w/2+xs), int(h/2+ys), r, fill=co, outline=None)
        else:
            xywh = [(int(w/2+xs-r/2), int(h/2+ys-r/2)), (int(w/2+xs+r/2), int(h/2+ys+r/2))]
            d.rectangle(xywh, fill=co, outline=None)

    im1 = Image.new('RGB', (params['w'], params['h']), params['Background'])
    im2 = Image.new('RGB', (params['w'], params['h']), params['color']) # note: 2nd image is reversed in 'polarity' for better difference effect
    draw1 = ImageDraw.Draw(im1)
    draw2 = ImageDraw.Draw(im2)

    # circles #1
    for n in range(cnt):
        r = int(sc*(cnt-n))
        if 'mode' in params:
            if params['mode'] == 'linear':
                if 'xs1v' in params:
                    xs1 = xs1 + params['xs1v']
                if 'ys1v' in params:
                    ys1 = ys1 + params['ys1v']
            if params['mode'] == 'circle':
                a0 = c*n/cnt*360
                if 'xs1v' in params:
                    xs1 = params['ys1v']*math.cos(a0)
                if 'ys1v' in params:
                    ys1 = params['ys1v']*math.sin(a0)
        draw_it(draw1, xs1, ys1)
    # circles #2
    for n in range(cnt):
        r = int(sc*(cnt-n))
        if 'mode' in params:
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
        draw_it(draw2, xs2, ys2)

    imout = ImageChops.difference(im1, im2) # only this is cool
    params['im'].paste(imout, (0, 0))
    im1 = Image.new('RGB', (1, 1), (0,0,0)) # that is probably lame way to free memory
    im2 = Image.new('RGB', (1, 1), (0,0,0))
    imout = Image.new('RGB', (1, 1), (0,0,0))
    draw1 = ImageDraw.Draw(im1) # does it free mem?
    draw2 = ImageDraw.Draw(im2) # does it free mem?

def mazy16(draw, params):
    """ Opart-like circles """
    w, h, cnt = init_common(params)
    c = math.pi/180
    if w > h:
        sc = w/2
    else:
        sc = h/2
    rcoef = params['rcoef']
    acoef = params['acoef']
    rscale = params['rscale']

    for n in range(cnt):
        r = int(sc * (cnt-n)/cnt*rcoef)
        if n&1 == 0:
            co = params['Background']
            ou = params['color']
        else:
            co = params['color']
            ou = params['Background']
        #ou = None
        a0 = c*n/cnt*360 * acoef
        xs2 = rscale*sc/2*math.cos(a0)
        ys2 = rscale*sc/2*math.sin(a0)
        circle(draw, int(w/2+xs2), int(h/2+ys2), r, fill=co, outline=ou)

def mazy17(draw, params):
    """ Scottish grid """
    w, h, cnt = init_common(params)
    v = params['v']
    if v < 1:
        v = 1

    for z in range(cnt):
        ndx = random.randint(0, cnt)
        color = new_colorer(params['color'], ndx, cnt)
        if 'addalpha' in params:
            color = add_alpha(color, params['addalpha'])
        x = random.randint(0, w)
        y = random.randint(0, h)
        lw = random.randint(1, v)
        xy = [(0, y), (w, y+lw)]
        draw.rectangle(xy, fill=color, outline=None)
        xy = [(x, 0), (x+lw, h)]
        draw.rectangle(xy, fill=color, outline=None)

def mazy18(draw, params):
    """ Random circle bundles """
    w, h, cnt = init_common(params)
    v = params['v']
    r0v = w
    if 'r0v' in params:
        r0v = params['r0v']

    for n in range(cnt):
        x = random.randint(0, w)
        y = random.randint(0, h)
        r0 = random.randint(0, r0v)
        for m in range(params['m']):
            r = r0 + random.randint(-v, v)
            color = new_colorer(params['color'], n, cnt) # note: alpha for outline does not seem to work
            for th in range(5): # test/par
                circle(draw, x, y, r+th*0.15, fill=None, outline=color)

def mazy19(draw, params):
    """ Chequered opart grids with x variations """
    w, h, cnt = init_common(params)
    c = math.pi/180
    nx = cnt
    ny = params['m']
    dx = int(2*w/nx)
    dy = int(2*h/ny)
    c_white = (255,255,255)
    c_black = (0,0,0)
    if 'c_white' in params:
        c_white = params['c_white']
    if 'c_black' in params:
        c_black = params['c_black']
    if params['mode'] == 'exp':
        fncx = []
        coef = 17 # par / const 17 good for 40
        for x in range(coef): # precalc
            fx = 2.0*math.exp(-x/4)
            fncx.append(fx)
    if params['mode'] == 'sin':
        fncx2 = []
        coef2 = nx # ?
        for x in range(coef2): # precalc
            fx = abs(1.1*math.sin(x/coef2*360*2*c)) #par x2
            fncx2.append(fx)
    dxmap = []
    f = 0
    x = 0
    while f < w+dx:  # fill whole width
        fx = 0
        if x > 0:
            if params['mode'] == 'grid':
                fx = dx
            if params['mode'] == 'lin':
                fx = dx*f/(w+dx)*1.01
            if params['mode'] == 'exp':
                if x < coef:
                    fx = dx * fncx[x]
                else:
                    if x < 2*coef:
                        ndx = coef-(x-coef)-1
                        fx = dx * fncx[ndx]
                    else:
                        fx = dx
            if params['mode'] == 'sin':
                if x < coef2:
                    fx = dx * fncx2[x]
                else:
                    fx = dx
        if fx < 1:
            fx = 1
        f = f + fx
        dxmap.append(f)
        x += 1
    for y in range(ny):
        for x in range(len(dxmap)-1):
            b = ((x&1) == 1 and (y&1) == 1) or ((x&1) == 0 and (y&1) == 0)
            if b == True:
                cx = c_white
            else:
                cx = c_black
            xp = dxmap[x]
            xy = [(xp, y*dy), (xp+(dxmap[x+1]-dxmap[x]), y*dy+dy)]
            draw.rectangle(xy, fill=cx, outline=None)

# future fun

def mazy20(draw, params):
    w, h, cnt = init_common(params)
    m = params['mode']
    c = math.pi/180
    #d = 8 # pixel
    d = 2 # pixel
    xs = int(w/d/2)
    ys = int(h/d/2)
    for y in range(int(h/d)):
        for x in range(int(w/d)):

            """
            vr = 32+128+128*math.sin(x*c)*math.cos(y*c)
            vg = 32+128+128*math.cos(4*x*c)*math.cos(y*c)
            vb = 32+128+64*(math.cos(3*x*c)+math.sin(2*y*c))
            if m == '1':
                cx = (int(vr), int(vr), int(vr))
            if m == '2':
                cx = (int(vg), int(vg), int(vg))
            if m == '3':
                cx = (int(vb), int(vb), int(vb))
            """

            """
            vr = 32+64+64*(math.sin(8*x*c)+math.cos(8*y*c))
            vg = 32+64+64*(math.sin(8*y*c)+math.cos(8*x*c))
            vb = 32+64+64*(math.sin(4*y*c)+math.sin(4*x*c))
            cx = (int(vr),int(vg),int(vb))
            """

            #vr = 2000*math.exp(-x/100)
            #vr = 2000*math.exp(-x/50)
            #vg = vr #2000*math.exp(-x/100)+x
            #vb = vr #2000*math.exp(-x/100)+x*2

            """
            a = 0
            b = 0
#            if m == '1':
#                b = 0
#            if m == '2':
#                b = 10
#            if m == '3':
#                b = 100
            vr = (x+a)*1*math.sin((x+b)*c*2)+y*1*math.cos(y*c*2)
            a = 10
            b = 50
            vg = (x+a)*1*math.sin((x+b)*c*2)+y*1*math.cos(y*c*2)
            b = 20
            b = 100
            vb = (x+a)*1*math.sin((x+b)*c*2)+y*1*math.cos(y*c*2)
            vr = int(vr) % 255
            vg = int(vg) % 255
            vb = int(vb) % 255
            cx = (int(vr), int(vg), int(vb))

            hue = int(vr) % 255
            saturation = 244
            vb = 2000*math.exp(-x/50)
            luminance = int(vb) % 255
            #luminance = 192 # int(vb * 0.7)

            vr = 2000*math.exp(-x/100)
            vg = 2000*math.exp(-y/100)
            hue = int(vr) % 255
            saturation = 244
            luminance = int(vg) % 255

            cx = 'hsl(%d, %d%%, %d%%)' % (hue, saturation, luminance)
            """

            """
            v = (1*math.sqrt((x-xs)*(x-xs)+(y-ys)*(y-ys)))
            #v = (1*math.sqrt((x-xs)*(x-xs)+(y-ys)*(y-ys))) * (math.sin(3.5*c*x)*math.cos(c*x)+math.sin(4*c*y)*math.cos(4*c*x))
            #v = 32+128+128 * (math.sin(4*c*x)*math.cos(c*x)+math.sin(c*y)*math.cos(4*c*x)) / 2
            cx = (int(abs(v)), int(0), int(0))
            """
            """
            vr = (20*math.sqrt((x-xs)*(x-xs)+(y-ys)*(y-ys)))
            vg = (20*math.sqrt((x-xs*0.6)*(x-xs*0.6)+(y-ys)*(y-ys)))
            vb = (20*math.sqrt((x-xs)*(x-xs)+(y-ys*0.6)*(y-ys*0.6)))
            cx = (int(vr)%255, int(vg)%255, int(vb)%255)
            """
            """
            vr = 64*(math.cos(2*x*c)+math.sin(2*y*c))
            vg = 64*(math.cos(3*y*c)+math.sin(3*x*c))
            vb = 64*(math.cos(3*x*c)+math.sin(2*y*c))
            def sca(x):
                if x < 0:
                    if x < 32:
                        return 0
                    else:
                        return 64
                if x > 32:
                    return 192
                else:
                    return 128
            vr1 = sca(vr)
            vg1 = sca(vg)
            vb1 = sca(vb)
            cx = (vr1,vg1,vb1)
            """

            """
            f0 = 1 + math.cos(x*c*2)
            f1 = 1 + math.cos(y*c*4)
            f0 = int(f0*255)
            f1 = int(5+f1*25)
            cx = 'hsl(%d, %d%%, %d%%)' % (f0, 80, f1)
            """

            #v = (8*math.sqrt((x-xs)*(x-xs)+(y-ys)*(y-ys))) / 4 # opt w/o /4
            v0 = math.sqrt((x-xs)*(x-xs)+(y-ys)*(y-ys))
            v = 3 + math.cos(x*c*1) + math.sin(y*c*1) - math.sin(v0*c*1) # to ok
            v = v * 254
            f0 = int(v) % 255
            #v = (2*math.sqrt((x-xs)*(x-xs)+(y-ys)*(y-ys)))
            #f1 = int(v*100) % 100
            #f1 = random.randint(20, 80) #ok1
            f1 = random.randint(45, 70)
            cx = 'hsl(%d, %d%%, %d%%)' % (f0, 80, f1)
            
            xy = [(x*d, y*d), (x*d+d, y*d+d)]
            draw.rectangle(xy, fill=cx, outline=None)
    # ... todo: fin
    return 0

def mazy21(draw, params):
    w, h, cnt = init_common(params)
    # ...
    return 0

def mazy22(draw, params):
    w, h, cnt = init_common(params)
    # ...
    return 0

def mazy23(draw, params):
    w, h, cnt = init_common(params)
    # ...
    return 0

def mazy24(draw, params):
    w, h, cnt = init_common(params)
    # ...
    return 0
