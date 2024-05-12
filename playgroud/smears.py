#! /usr/bin/env python
# -*- coding: utf-8 -*-

# PyArtForms - Python generative art forms paint algorithms (artificial artist), v1.0
# (c)2017-2024 Noniewicz.com, Jakub Noniewicz aka MoNsTeR/GDC
# experimental 'smears' paint algorithms - core algorithm definitions
"""
cre: 20180430
upd: 20180501, 02, 03
upd: 20180805, 07, 08
upd: 20180928, 29
upd: 20181019, 20
upd: 20190105, 06, 12, 13, 18, 19, 21, 22
upd: 20190306, 11, 29, 30
upd: 20190414, 15, 17, 18, 22, 24, 26, 27
upd: 20200507, 10
upd: 20210106, 15, 16, 19, 20, 21, 22
upd: 20210515, 16, 22, 23, 24, 25, 26, 27
upd: 20210606, 07, 10, 11, 12, 13, 14, 17, 18, 19, 20
upd: 20240224, 25
upd: 20240304
upd: 20240512
"""

# #01 [...] 'cruel red smears', not only red
# #02 [tested, ok] circle worms
# #03 [tested, ok] crazy trangles --- finish: more par, opt less random?
# #04 [tested, ok] self-crossed filled polygons
# #05 [...] star flowers --- finish: a lot here
# #06 [...] circle ripples - co-centered circle groups --- finish: par + misc
# #07 [tested, ok] random rectangles - grayish and colorish rects mess --- finish: new colorer proper
# #08 [tested, ok] just rectangles, may flux --- finish: new params, more variants in defs
# #09 [tested, ok] 'Warp' effect - triangle rays from center, opt center point shifted rnd
# #10 [...] long beziers
# #11 [tested, ok] horizontal gradients with suprizes
# #12 [tested, ok/so-so] opart-like boxes/circles/triangles
# #13 [tested, ok] opart-like single big poly (like #04?)
# #14 [tested, ok/so-so] opart-like cicrles xor-cut by triangles
# #15 [tested, ok, predictable] opart-like or color circle-interference patterns
# #16 [tested, ok, predictable] opart-like circles
# #17 [tested, ok] scottish-like grid --- finish: postproc satur 75 up + light 10 up? | 0,0 missing in rnd issue
# #18 [tested, ok] slim colorful circles --- finish: more par or var th*, more with self-call
# #19 [tested, ok, predictable] opart-like grid
# #20 [tested, ok, predictable] opart-like / papercut-like / video feedback-like 'dragon' effect
# #21 [tested, ok, predictable] opart-like scaled and pasted frames
# #22 [...] pie slice effects --- finish: reduce total count, mimosrod opt?
# #23 [tested, ok, predictable] Sierpinski's triangle fractal
# #24 [tested, ok, predictable] rotated traingles --- finish: reduce total count, more par ver, mimosrod opt, a scale par
# #25 [tested, ok] waves#1 --- finish: more par
# #26 [tested, ok] waves#2 --- finish: more par, simplify code
# #27 [tested, ok] multishaped polygon mess --- finish: more par
# future fun:
# #28 [...]
# #29 [...]
# #30 [...]
# #31 [...] filled triangles
# #32 [...]
# #33
# #34
# #35
# #36

# see:
# https://pillow.readthedocs.io/en/stable/

# note: now required at least pillow version 5.3.0, tested on 7.2.0, my prev was 5.0.0

# TODO:
# - ?


from PIL import Image, ImageDraw, ImageChops, ImageOps #, ImageMorph, ImageMath # test
import random, math, string, os, sys, copy
from bezier import make_bezier
from drawtools import *
from color_defs import *


"""
import PIL
print('PIL',PIL.__version__)
"""

# ---

def mazy1(draw, params):
    """ ? """
    w, h, cnt = init_common(params)
    mar = 0
    if 'mar' in params:
        mar = params['mar']
    v = 0
    if 'v' in params:
        v = params['v']
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
    """ circle worms """
    w, h, cnt = init_common(params)
    cntm = params['m']
    if cntm <= 0:
        cntm = 1
    sc = 50 # dflt
    if 'sc' in params:
        sc = params['sc']
    if sc > 0:
        v = int(h/sc)
    else:
        v = 0

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
            po[:] = [(xy[0]+random.randint(0, v)-random.randint(0, v), xy[1]+random.randint(0, v)-random.randint(0, v)) for xy in po]
            color = new_colorer(params['color'], m, cntm)
            if 'addalpha' in params:
                if params['addalpha'] > 0:
                    color = add_alpha(color, params['addalpha'])
            circle(draw, po[0][0], po[0][1], int(r0*(1-m*de)), fill=color, outline=None)

def mazy3(draw, params):
    """ crazy trangles """
    w, h, cnt = init_common(params)

    def r(p, d):
        return int(p/2+random.randint(int(-p/d), int(p/d)))

    d = 0.5 # par, 1.3, 2.2 ? # todo: ext par
    da = 0.06 # dflt, how quickly they get smaller in center mode, 0.5 ok too
    if 'da' in params:
        da = params['da']
    for n in range(cnt):
        if params['mode'] == 'center':
            po = [(r(w, d), r(h, d)), (r(w, d), r(h, d)), (r(w, d), r(h, d))]
            d = d + da
        if params['mode'] == 'xcenter':
            d = 2.2 # par
            po = [(int(w/2), int(h/2)), (r(w, d), r(h, d)), (r(w, d), r(h, d))]
        if params['mode'] == 'rnd':
            d = 2.2 # par
            po = [(r(w, d), r(h, d)), (r(w, d), r(h, d)), (r(w, d), r(h, d))]
        color = new_colorer(params['color'], n, cnt)
        if 'addalpha' in params:
            if params['addalpha'] > 0:
                color = add_alpha(color, params['addalpha'])
        triangle(draw, po, fill=color, outline=None)

def mazy4(draw, params):
    """ self-crossed filled polygons """
    w, h, cnt = init_common(params)
    sc = 2.1 # dflt
    if 'sc' in params:
        sc = params['sc']
    if sc <= 0:
        sc = 1
    sx = int(w/sc)
    sy = int(h/sc)
    p_cnt = 20 # dflt
    if 'pc' in params:
        p_cnt = params['pc']
    mode = 'center'
    if 'mode' in params:
        mode = params['mode']

    for n in range(cnt):
        if mode == 'center':
            w0 = w/2
            h0 = h/2
        else:
            w0 = random.randint(0, w)
            h0 = random.randint(0, h)
        po = []
        for p in range(p_cnt):
            po.extend((w0+random.randint(-sx, sx), h0+random.randint(-sy, sy)))
        color = new_colorer(params['color'], n, cnt)
        if 'addalpha' in params:
            color = add_alpha(color, params['addalpha'])
        draw.polygon(po, fill=color, outline=None)

def mazy5(draw, params):
    """ star flowers """
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
    """ circle ripples - co-centered circle groups """
    w, h, cnt = init_common(params)
    useblack = False
    if 'useblack' in params:
        useblack = params['useblack']
    n_r_max = 16 # par
    r_min = int(h/25) # par
    r_max = int(h/7) # par
    #r_max = int(h/3) # par
    #r_max = int(h/15) # par
    # todo: start w big r_mx then go to lower? == start with big 1st
    # todo: mix color modes maybe?

    for m in range(cnt):
        x = random.randint(int(w/2-w/3), int(w/2+w/3))
        y = random.randint(int(h/2-h/3), int(h/2+h/3))
        r = random.randint(r_min, r_max)
        n_r = random.randint(3, n_r_max)
        for n in range(n_r):
            nn = n_r - n
            ro = int(r*(1+nn*nn*0.015)) # par
            if n & 1 and useblack == True:
                color = (0, 0, 0)
            else:
                color = new_colorer(params['mode'], n, n_r)
                try:
                    color
                except NameError:
                    print('ERROR: undefined color mode, using black', params['mode'])
                    color = (0,0,0)
            #color = add_alpha(color, 100) # todo
            circle(draw, x, y, ro, fill=color, outline=None)

def mazy7(draw, params):
    """ random rectangles - grayish and colorish rects mess """
    w, h, cnt = init_common(params)
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
        # todo: new colorer proper
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

    # todo: opt dodatkowe 'cienkie'

    flux_p = None
    v = 0
    if 'flux_p' in params:
        flux_p = params['flux_p']
    if 'v' in params:
        v = params['v']
    border = 0
    if 'border' in params:
        border = params['border']
    ou = None
    if 'ou' in params:
        ou = params['ou']

    w1 = int(w/xcnt)
    h1 = int(h/ycnt)
    max_c = len(get_colors(params['color']))
    for y in range(ycnt-border*2):
        for x in range(xcnt-border*2):
            x1 = x*w1 + int(w1/2) + border*w1
            y1 = y*h1 + int(h1/2) + border*h1
            ci = random.randint(0, max_c-1)
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
            rect(draw, x1+vx, y1+vy, w1+vw, h1+vh, fill=color, outline=ou)

def mazy9(draw, params):
    """ 'Warp' effect - triangle rays from center, opt center point shifted rnd """
    w, h, cnt = init_common(params)
    w2 = int(w/2)
    h2 = int(h/2)
    c = math.pi/180
    v = 0
    if 'v' in params: 
        v = params['v']
    rndc = False
    if 'rndc' in params: 
        rndc = params['rndc']

    po = [(w2, h2), (0, 0), (0, 0)]
    da = c * float(360)/cnt
    r = w
    for n in range(cnt):
        if v > 0:
            po[0] = (w2+random.randint(int(-v), int(v)), h2+random.randint(int(-v), int(v)))
        x = w2 + r * math.cos(da*n)
        y = h2 + r * math.sin(da*n)
        po[1] = (x, y)
        x = w2 + r * math.cos(da*(n+1))
        y = h2 + r * math.sin(da*(n+1))
        po[2] = (x, y)

        if params['color'] == 'red' or params['color'] == 'bw': # todo: more? + both modes as one?
            ci = random.randint(0, 255)
            color = new_colorer(params['color'], ci, 255)
        else:
            cx = get_colors(params['color'])
            if cx == None:
                raise Exception('Undefined color: '+params['color']) # todo: err only, no raise/crash
            cx_len = len(cx)
            if rndc == True:
                color = cx[random.randint(0, cx_len-1)]
            else:
                color = cx[n%cx_len]
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
    """ Horizontal gradients with surprizes """
    w, h, cnt = init_common(params)
    cx = get_colors(params['color'])
    csize = len(cx)

    dy = float(h)/cnt
    if dy*cnt < h: # lame fix for small images
        cnt += 3
    steps = 256 # const, max rational limit for RGB24 gradient
    if steps > w:
        steps = w
    dx = float(w)/steps
    for n in range(cnt):
        n1 = random.randint(0, csize-1)
        n2 = n%csize
        n3 = random.randint(0, csize-1)
        color1 = cx[n1]
        color2 = cx[n2]
        color3 = cx[n3]
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
    """ opart-like or color circle-interference patterns, predictable (no rnd parts) """
    w, h, cnt = init_common(params)
    c = math.pi/180
    scc = 1.5 # par
    if w > h:
        sc = w/2*scc/cnt  # note: off-screen to fill all
    else:
        sc = h/2*scc/cnt
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

    colorer = None
    if 'colorer' in params:
        colorer = params['colorer']

    def draw_it(draw, xs, ys, r):
        if n&1 == 0:
            if colorer == None:
                co = params['Background']
            else:
                co = new_colorer(colorer, n, cnt)
        else:
            if colorer == None:
                co = params['color']
            else:
                co = new_colorer(colorer, n, cnt)
        circle(draw, int(w/2+xs), int(h/2+ys), r, fill=co, outline=None)

    im1 = Image.new('RGB', (params['w'], params['h']), params['Background'])
    im2 = Image.new('RGB', (params['w'], params['h']), params['color']) # note: 2nd image is reversed in 'polarity' for better difference effect
    draw1 = ImageDraw.Draw(im1)
    draw2 = ImageDraw.Draw(im2)

    for n in range(cnt): # circles #1
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
                    xs1 = params['xs1v']*math.cos(a0)
                if 'ys1v' in params:
                    ys1 = params['ys1v']*math.sin(a0)
        draw_it(draw1, xs1, ys1, r)
    for n in range(cnt): # circles #2
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
                    xs2 = params['xs2v']*math.cos(a0)
                if 'ys2v' in params:
                    ys2 = params['ys2v']*math.sin(a0)
        draw_it(draw2, xs2, ys2, r)

    if colorer == None:
        imout = ImageChops.difference(im1, im2) # only difference is cool for bw
    else:
        imout = ImageChops.blend(im1, im2, 0.5) # only blend for color now

    params['im'].paste(imout, (0, 0))
    im1 = None
    im2 = None
    imout = None

def mazy16(draw, params):
    """ Opart-like circles, predictable (no rnd parts) """
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
    """ Scottish-like grid """
    w, h, cnt = init_common(params)
    vv = params['v']
    v = int(w*vv)

    for z in range(cnt):
        ndx = random.randint(0, cnt)
        color = new_colorer(params['color'], ndx, cnt)
        if 'addalpha' in params:
            if params['addalpha'] > 0:
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

    if 'multi' in params:
        multi = params['multi']
        for p in multi:
            p['w'] = params['w']
            p['h'] = params['h']
            p['call'] = params['call']
            p['color'] = params['color']
            p['name'] = params['name']
            mazy18(draw, p)
        return

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
            thn = 3 # par
            thd = 0.2 # par
            thw = 2 # par
            for th in range(thn):
                circle_w(draw, x, y, r+th*thd, fill=None, outline=color, width=thw) # note width, v 5.3.0+
# was
#            for th in range(5):
#                circle(draw, x, y, r+th*0.15, fill=None, outline=color)

def mazy19(draw, params):
    """ Chequered opart grids with x variations, predictable (no rnd parts) """
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

def mazy20(draw, params):
    """ opart-like / papercut-like / video feedback-like 'dragon' effect, predictable (no rnd parts) """
    w, h, cnt = init_common(params)
    da = params['da']
    dd = 10 # dflt
    if 'dd' in params:
        dd = params['dd']
        if dd < 1:
            dd = 1
    dx = int(w/dd)
    dy = int(h/dd)
    sc = 0.75 # dflt
    if 'sc' in params:
        sc = params['sc']
    nw = int(sc*w)
    nh = int(sc*h)

    xy = [(dx, dy), (w-dx, h-dy)]
    draw.rectangle(xy, fill=params['Foreground'], outline=None)
    xy = [(dx*2, dy*2), (w-dx*2, h-dy*2)]
    draw.rectangle(xy, fill=params['Background'], outline=None)

    for n in range(cnt):
        im1 = params['im']
        im1 = im1.resize((nw, nh), Image.BICUBIC)
        im1 = im1.rotate(da, Image.BICUBIC)
        params['im'].paste(im1, (int((w-nw)/2), int((h-nh)/2)))
    im1 = None

    if 'invert' in params:
        if params['invert'] == True:
            params['im'] = invert_image(params['im'])

def mazy21(draw, params):
    """ opart-like scaled and pasted frames, predictable (no rnd parts) """
    w, h, cnt = init_common(params)
    dx = int(w/10)
    dy = int(h/10)
    sc = 0.666
    nw = int(sc*w)
    nh = int(sc*h)
    mode = 0
    if 'mode' in params:
        mode = params['mode']

    xy = [(dx, dy), (w-dx, h-dy)]
    draw.rectangle(xy, fill=params['Foreground'], outline=None)
    xy = [(dx*2, dy*2), (w-dx*2, h-dy*2)]
    draw.rectangle(xy, fill=params['Background'], outline=None)

    for n in range(cnt):
        im1 = params['im'].resize((nw, nh), Image.BICUBIC)
        xx = int(nw/2)
        yy = int(nh/2)
        if mode == 0:
            params['im'].paste(im1, (0+int(nw/2/2), 0+int(nh/2/2))) #center
        if mode == 1:
            params['im'].paste(im1, (0, 0)) #l/u
        if mode == 2:
            params['im'].paste(im1, (xx, yy)) #r/d
        if mode == 3 or mode == 4: # l/u + r/d - extravagant
            if n&1 == 0:
                params['im'].paste(im1, (0, 0)) #l/u
            else:
                params['im'].paste(im1, (xx, yy)) #r/d
        if mode == 4 or mode == 5:
            params['im'].paste(im1, (0+int(nw/3), 0+int(nh/3))) # lame
        if mode == 6: # maxxx fract like
            nn = n&3
            if nn == 0:
                params['im'].paste(im1, (0, 0))
            if nn == 1:
                params['im'].paste(im1, (xx, 0))
            if nn == 2:
                params['im'].paste(im1, (0, yy))
            if nn == 3:
                params['im'].paste(im1, (xx, yy))
    im1 = None

    if 'invert' in params:
        if params['invert'] == True:
            params['im'] = invert_image(params['im'])

def mazy22(draw, params):
    """ pie slice effects """
    w, h, cnt = init_common(params)
    colorer = params['color']
    do_rnd = False
    if 'rnd' in params:
        do_rnd = params['rnd']

    drc = 0.97
    if 'drc' in params:
        drc = params['drc']
    a_s = 0
    a_e = 35
    if 'a_e' in params:
        a_e = params['a_e']
    da = 12
    if 'da' in params:
        da = params['da']

    #note: some nice: drc a_e da
    #0.97, 90, 12
    #0.97, 35, 12
    #0.97, 10, 12
    #0.97, 90, 45 # good for colorsets
    #0.97, 90 90 # special
    #0.97, 90 89 # special + good for colorsets
    #0.97, 90 85 # special + good for colorsets
    #0.97, 90 80 # special + good for colorsets
    #0.9, 90, 45

    radius = h/2 * 1.0 # par

    for i in range(cnt):
        if do_rnd:
            a_s = random.randint(0, 360) # par x2
            a_e = random.randint(0, 360) # par x2
            drc = random.randint(92, 98)/100 # par x2
            if i == cnt-1:
                a_s = 0
                a_e = 360
        if params['Background'] == (255,255,255) and do_rnd and params['color'] == 'bw': # rev bw color in this special case
            color = new_colorer(colorer, cnt-1-i, cnt)
        else:
            color = new_colorer(colorer, i, cnt)
        draw.pieslice((w/2-radius, h/2-radius, w/2+radius, h/2+radius), a_s, a_e, fill=color)
        radius = radius * drc
        if not do_rnd:
            a_s = a_s + da
            a_e = a_e + da

def mazy23(draw, params):
    """ Sierpinski's triangle fractal, predictable (no rnd parts) """
    # https://en.wikipedia.org/wiki/Sierpi%C5%84ski_triangle
    w, h, cnt = init_common(params)
    limit0 = cnt
    margin = 5/100
    if 'margin' in params:
        margin = params['margin']
    dd = h*margin
    color = (255, 255, 255)
    if 'color1' in params:
        color = params['color1']
    color2 = (0, 0, 0)
    if 'color2' in params:
        color2 = params['color2']
    colorer = None
    if 'colorer' in params:
        colorer = params['colorer']
    colorer_mode = None
    if 'colorer_mode' in params:
        colorer_mode = params['colorer_mode']

    def m23(draw, limit, a, htr, ofsx, ofsy):
        if limit <= 0:
            return
        a /= 2
        htr = 0.5 * math.sqrt(3) * a

        c2 = color2
        if colorer != None and colorer_mode == 0:
            c2 = new_colorer(colorer, limit, limit0) # mode=0

        xx1 = wo+a/4 +(0.5) # note: 0.5 'visual' fix
        xx2 = wo+a/2
        xx3 = wo+a-a/4 -(0.5)
        yy1 = h-dd-htr/2 +(0.5)
        yy2 = h-dd -(0.5)

        fix_x = ofsx
        fix_y = ofsy
        po = [(int(xx1+fix_x), int(yy1+fix_y)), (int(xx2+fix_x), int(yy2+fix_y)), (int(xx3+fix_x), int(yy1+fix_y))]
        if colorer != None and colorer_mode == 1:
            c2 = new_colorer(colorer, limit+0, limit0) # mode=1
        triangle(draw, po, fill=c2, outline=None)
        m23(draw, limit-1, a, htr, fix_x, fix_y)

        fix_x = a + ofsx
        fix_y = ofsy
        po = [(int(xx1+fix_x), int(yy1+fix_y)), (int(xx2+fix_x), int(yy2+fix_y)), (int(xx3+fix_x), int(yy1+fix_y))]
        if colorer != None and colorer_mode == 1:
            c2 = new_colorer(colorer, limit+1, limit0) # mode=1
        triangle(draw, po, fill=c2, outline=None)
        m23(draw, limit-1, a, htr, fix_x, fix_y)

        fix_x = a/2 + ofsx
        fix_y = -htr + ofsy
        po = [(int(xx1+fix_x), int(yy1+fix_y)), (int(xx2+fix_x), int(yy2+fix_y)), (int(xx3+fix_x), int(yy1+fix_y))]
        if colorer != None and colorer_mode == 1:
            c2 = new_colorer(colorer, limit+2, limit0) # mode=1
        triangle(draw, po, fill=c2, outline=None)
        m23(draw, limit-1, a, htr, fix_x, fix_y)

    a = h-dd-dd # start side len, todo: try par >> w?
    wo = (w-a)/2
    htr = 0.5 * math.sqrt(3) * a # start triangle h
    po = [(wo, h-dd), (wo+a/2, h-dd-htr), (wo+a, h-dd)]
    triangle(draw, po, fill=color, outline=None) # main
    po = [(wo+a/4, h-dd-htr/2), (wo+a/2, h-dd), (wo+a-a/4, h-dd-htr/2)]
    triangle(draw, po, fill=color2, outline=None) # 1st cut
    m23(draw, limit0-1, a, htr, 0, 0) # recurent inside

def mazy24(draw, params):
    """ rotated traingles, predictable (no rnd parts) """
    w, h, cnt = init_common(params)
    cx = w/2
    cy = h/2 + h/12 # 'y center' slightly moved down, nicer this way
    c = math.pi/180
    colorer = params['colorer']
    ou = None
    if 'ou' in params:
        ou = params['ou']

    a_sc = 0.93 # par
    a_base = 1.0
    if 'a_base' in params:
        a_base = params['a_base']
    an_sc = 1.0
    if 'an_sc' in params:
        an_sc = params['an_sc']

    a = h*a_base
    for i in range(cnt):
        htr = 0.5 * math.sqrt(3) * a
        po = [(cx-a/2, cy-htr/2), (cx, cy+htr/2), (cx+a/2, cy-htr/2)]
        ce = (1/3*(po[0][0]+po[1][0]+po[2][0]), 1/3*(po[0][1]+po[1][1]+po[2][1])) # actual triangle center is here (triangle centroid)
        an = i/cnt * 360 * c * an_sc
        po_ = [rotate_point(po[0], ce[0], ce[1], an), rotate_point(po[1], ce[0], ce[1], an), rotate_point(po[2], ce[0], ce[1], an)]
        color = new_colorer(colorer, i, cnt)
        if 'addalpha' in params:
            color = add_alpha(color, params['addalpha'])
        triangle(draw, po_, fill=color, outline=ou)
        a = a * a_sc

def mazy25(draw, params):
    """ waves#1 """
    # todo: par + more like it?
    w, h, cnt = init_common(params)
    c = math.pi/180

    fd = 100.0*params['f0']
    div = float(cnt*2+4+(-4)) # par
    if div == 0:
        div = 1
    if params['horizontal'] == True:
        rn = w
        dx = h/div
    else:
        rn = h
        dx = w/div
    mofs0 = 0 # par, was 2

    rnd_color = True # par
    rnd_color = False

    for z in range(cnt):
        if rnd_color:
            ndx = random.randint(0, cnt)
        else:
            ndx = z
        color = new_colorer(params['color'], ndx, cnt)
        if 'addalpha' in params:
            color = add_alpha(color, params['addalpha'])
        aofs1 = random.randint(0, 360)
        aofs2 = random.randint(0, 360)
        aofs3 = random.randint(0, 360)
        aofs4 = random.randint(0, 360)
        fofs1 = random.randint(0, 100)/fd*1
        fofs2 = random.randint(0, 100)/fd*1
        fofs3 = random.randint(0, 100)/fd*2
        fofs4 = random.randint(0, 100)/fd*2
        mofs1 = (z+mofs0)*dx

        y = 0
        for n in range(rn):
            nsc = float(n)/float(rn)*360*10 # par 10
            x_in =  mofs1 + dx * (1 + (math.sin(c*(nsc*fofs1+aofs1))+2*math.sin(c*(nsc*fofs3+aofs3)))/3)
            x_out = mofs1 + dx * (1 + (math.sin(c*(nsc*fofs2+aofs2))+2*math.sin(c*(nsc*fofs4+aofs4)))/3)
            if params['horizontal'] == True:
                xy = [(y, x_in), (y, h - x_out)]
            else:
                xy = [(x_in, y), (w - x_out, y)]
            draw.rectangle(xy, fill=color, outline=None) # 1px rects?
            y += 1

def mazy26(draw, params):
    """ waves#2 """
    if 'par1' in params and 'par2' in params:
        mazy26(draw, params['par1'])
        mazy26(draw, params['par2'])
        return

    w, h, cnt = init_common(params)

    # todo: uproscic kod (czemu 2x?) | exp par
    w = params['w']
    h = params['h']
    cnt = params['n']
    random.seed()
    c = math.pi/180

    sc = 3.0  #par was 4
    if params['horizontal'] == True:
        rn = w
        dx = h/float(cnt)*sc
    else:
        rn = h
        dx = w/float(cnt)*sc

    for z in range(cnt):
        ndx = random.randint(0, cnt)
        color = new_colorer(params['color'], ndx, cnt)
        if 'addalpha' in params:
            color = add_alpha(color, params['addalpha'])
        aofs1 = random.randint(0, 360)
        aofs2 = random.randint(0, 360)
        aofs3 = random.randint(0, 360)
        aofs4 = random.randint(0, 360)
        fofs1 = random.randint(0, 100)/100.0*1 # par
        fofs2 = random.randint(0, 100)/100.0*1 # par
        fofs3 = random.randint(0, 100)/100.0*2 # par
        fofs4 = random.randint(0, 100)/100.0*2 # par
        mofs1 = float(z*dx)
        am1 = 1.0 # par
        am2 = 1.0 # par
        am3 = 3.0 # par was 2
        am4 = 3.0 # par was 2

        y = 0
        points1 = []
        points2 = []
        points1a = []
        points2a = []
        for n in range(rn):
            nsc = float(n)/float(rn)*360*10 # par 10
            x_in =  int(mofs1 + dx * (1 + (am1*math.sin(c*(nsc*fofs1+aofs1))+am3*math.sin(c*(nsc*fofs3+aofs3)))))
            x_out = int(mofs1 + dx * (1 + (am2*math.sin(c*(nsc*fofs2+aofs2))+am4*math.sin(c*(nsc*fofs4+aofs4)))))
            if params['horizontal'] == True:
                points1.extend((y, x_in))
                points2.extend((y, x_out))
            else:
                points1.extend((x_in, y))
                points2.extend((x_out, y))
            y += 1
        lw = random.randint(1, int(w/30)) #par, opt big->small?

        points1a[:] = [xy for xy in points1]
        points2a[:] = [xy for xy in points2]
        for a in range(int(len(points1a)/2)):
            ndx = int(len(points1a)/2)-1-a
            if params['horizontal'] == True:
                points1.extend((points1a[ndx*2], lw+points1a[ndx*2+1]))
            else:
                points1.extend((lw+points1a[ndx*2], points1a[ndx*2+1]))
        for a in range(int(len(points2a)/2)):
            ndx = int(len(points2a)/2)-1-a
            if params['horizontal'] == True:
                points2.extend((points2a[ndx*2], lw+points2a[ndx*2+1]))
            else:
                points2.extend((lw+points2a[ndx*2], points2a[ndx*2+1]))
        draw.polygon(points1, fill=color, outline=color)
        draw.polygon(points2, fill=color, outline=color)

def mazy27(draw, params):
    """ multishaped polygon mess """
    w, h, cnt = init_common(params)
    colorer = params['colorer']
    addalpha = 0
    if 'addalpha' in params:
        addalpha = params['addalpha']
    saturation_factor = 1.5 # dflt
    if 'saturation' in params:
        saturation_factor = params['saturation']
    minsides = 3
    maxsides = 8
    if 'minsides' in params:
        minsides = params['minsides']
    if 'maxsides' in params:
        maxsides = params['maxsides']
    if minsides < 3:
        minsides = 3
    if maxsides < 3:
        maxsides = 3
    maxangle = 90
    if 'maxangle' in params:
        maxangle = params['maxangle']

    rmin = int(h/30)
    if 'rmin' in params:
        rmin = params['rmin']
    rmax = h/4 # h h/2 # h/4
    if 'rmax' in params:
        rmax = params['rmax']
    rsc = 0.997 # 0
    if 'rsc' in params:
        rsc = params['rsc']

    ofs = int(h/4) # centers this much off-screen
    for n in range(cnt):
        color = new_colorer(colorer, n, cnt)
        if addalpha > 0:
            color = add_alpha(color, addalpha)
        r = random.randint(rmin, int(rmax))
        cx = random.randint(-ofs, w+ofs)
        cy = random.randint(-ofs, h+ofs)
        if maxangle > 0:
            a = random.randint(0, maxangle)
        else:
            a = 0
        sides = random.randint(minsides, maxsides)
        nsided(draw, sides, cx, cy, r, a, color, None)
        if rsc > 0:
            rmax = rmax * rsc
            if rmax < rmin:
                rmax = rmin
    if addalpha > 0 and saturation_factor > 0:
        params['im'] = enhace(params['im'], saturation_factor)

# future fun

def mazy28(draw, params):
    """ ? """
    # fin or remove
    w, h, cnt = init_common(params)
    c = math.pi/180

    cnt = 400
    sx = int(w/cnt)
    color = (0xd4,0x8a,0x3e)
    aofs1 = 0
    fofs1 = 3
    fofs3 = 1
    am1 = 3
    am3 = 1
    dx = sx/3

    po = [(w,0), (0, 0)]
    x = 0
    y = h
    for n in range(cnt):
        aofs2 = random.randint(0, 90)
        aofs3 = random.randint(0, 180)
        fofs2 = random.randint(1, 5)
        am2 = random.randint(1, 15)
        nsc = float(n)/float(cnt)*360*3 # par
        f = int(dx * (2 + (am1*math.sin(c*(nsc*fofs1+aofs1))+am2*math.sin(c*(nsc*fofs2+aofs2))+am3*math.sin(c*(nsc*fofs3+aofs3)))))
        po.extend((x, y))
        y -= f
        x += sx
    draw.polygon(po, fill=color, outline=None)

def mazy29(draw, params):
    """ ? """
    # note: hard one, probably will fail
    w, h, cnt = init_common(params)
    c = math.pi/180

    color = (255,255,255)
    hb = int(h/10)
    y0 = (hb/2)
    cnt = 300
    dx = int(w/cnt)
    bcnt = 5

    def f1(p):
        x = p[0]
        y = p[1] + hb*2
        return (x, y)

    po = [] # build one model block
    po.append((0,y0))
    for n in range(cnt):
        pn = (dx*n, y0)
        po.append(pn)
    po.append((w, y0))
    po.append((w, y0+hb))
    for n in range(cnt):
        po.append((w-dx*n, y0+hb))
    po.append((0, y0+hb))

    poall = [None] * bcnt # copy block bcnt times
    for n in range(bcnt):
        if n == 0:
            poall[n] = copy.deepcopy(po)
        else:
            po[:] = (f1(p) for p in po)
            poall[n] = copy.deepcopy(po)

    s1 = 1
    s2 = 1 + cnt + 2

    # test sin wave - remove later?
    for n in range(bcnt):
        for x in range(cnt):
            #fn = 30*math.sin(c*x/cnt*360*4
            fn = 0
            for f in range(10):
                fn += (20+f*2)*math.sin(c*x/cnt*360*(1+f*2))
            tup = poall[n][s1+x]
            tup = (tup[0], tup[1]+fn) # change y-s
            poall[n][s1+x] = tup
            tup = poall[n][s2+cnt-x]
            tup = (tup[0], tup[1]+fn) # change y-s
            poall[n][s2+cnt-x] = tup

    """
    def dist(p, sm):
        start = sm['start']
        ds = math.sqrt((start[0]-p[0])*(start[0]-p[0])+(start[1]-p[1])*(start[1]-p[1]))
        is_affecting = ds < sm['radius']
        inte = sm['intensity']*math.exp(-ds*0.05)*1000
        intex = inte*math.cos(c*sm['angle'])
        intey = inte*math.sin(c*sm['angle'])
        return ds, inte, intex, intey, is_affecting

    def apply_smear(sm):
        for m in range(cnt):
            for n in range(bcnt):
                tup = poall[n][s1+m]
                ds, inte, intex, intey, is_affecting = dist(tup, sm)
                if is_affecting:
                    tup = (tup[0]+intex, tup[1]+intey) # change
                    poall[n][s1+m] = tup
                tup = poall[n][s2+cnt-m]
                ds, inte, intex, intey, is_affecting = dist(tup, sm)
                if is_affecting:
                    tup = (tup[0]+intex, tup[1]+intey) # change
                    poall[n][s2+cnt-m] = tup

    # todo: smear with intensity ~ 1/range and params: angle + radius + strength + len
    sme1 = {'start': (w/2, h/2), 'angle': 45, 'radius': 400, 'intensity': 100, 'length': 300}
    apply_smear(sme1)
    sme2 = {'start': (w/4, h/4), 'angle': 15, 'radius': 400, 'intensity': 100, 'length': 300}
    apply_smear(sme2)
    """

    for n in range(bcnt):
        #po = poall[n]
        po = poall[bcnt-1-n] # rev order for test
        color = (255,255, int(255*n/bcnt))
        draw.polygon(po, fill=color, outline=None)
    #circle(draw, sme1['start'][0], sme1['start'][1], sme1['radius'], fill=None, outline=(0,0,255))
    #circle(draw, sme2['start'][0], sme2['start'][1], sme2['radius'], fill=None, outline=(0,0,255))

def mazy30(draw, params):
    """ ? """
    w, h, cnt = init_common(params)
    w2 = int(w/2)
    h2 = int(h/2)

    cnt = 100*2 # par
    r0 = h*0.3 # par
    v = 200+100 # par
    sc = 1.0 # par
    rv = 200 # par
    asc = 10 # par 6 50

    po = []
    for n in range(cnt):
        a = math.pi/180 * 360 * float(n/cnt) # par
        rv = random.randint(100,500) # test
        r = r0 + sc * (rv * math.sin(asc*a))
        #r = r0
        po.append((int(w2+r*math.cos(a)), int(h2+r*math.sin(a))))

    def fr0(p):
        # par x2
        if random.randint(0, 100) > 80:
            return (p[0]+random.randint(-v,v), p[1]+random.randint(-v,v))
            #return (p[0]+random.randint(-v,v), p[1])
        else:
            return p

    def fr(p):
        return p
        #return (p[0]+random.randint(-v,v), p[1]+random.randint(-v,v))

    po[:] = (fr(xy) for xy in po)
    draw.polygon(po, fill=(255, 255, 0), outline=None) # par
    po.append((po[0][0], po[0][1]))
    draw.line(po, fill=(255,0,0), width=3) # par

    # opt
    if False:
        ts = [t/2000.0 for t in range(2001)]
        #ts = [t/20.0 for t in range(21)]
        bezier = make_bezier(po)
        points = bezier(ts)
        draw.polygon(points, fill=(255, 0, 0), outline=(255,255,255))

def mazy31(draw, params):
    """ cool filled triangles (with outline) """
    # note: may not be scale invariant, check & fix for it?
    # todo: also outlined variants
    # todo: also all par proper
    w, h, cnt = init_common(params)
    c = math.pi/180
    random.seed()
    y0 = h/2
    x0 = w/2
    steps = params['steps']
    amp = h/2*0.97 # par!
    mode = params['mode'] #0..5

    i = 0
    for a in range(steps):
        r = amp*(1-a/steps) # todo opt par scalling factor eg. non-linear
        ra = amp * ((1 - a / steps) ** 2)  # Changed to exponential decrease for more drama
        aa = a/steps # full 360 - takie sobie
    
        if mode == 0:
            aa = a/steps/3 # not full 360
        elif mode == 1:
            aa = a/steps/2 # not full 360
        elif mode == 2:
            aa = a/steps/6 # not full 360
        elif mode == 3:
            aa = a/steps/0.5 # ok!
        elif mode == 4:
            r = amp*math.exp(-a/8) # scale down exp
        elif mode == 5:
            ar = random.randint(-steps, steps)
            aa = (a+ar)/steps/6 # not full 360
            r += random.randint(-15, 4) # +flux # par!

        # by ChatCPT 4.0
        elif mode == 6:
            aa = math.sin(a / steps * math.pi) / 3  # Sine wave adjustment
        elif mode == 7:
            aa = a / steps / 2 + 0.1 * math.sin(a * 10)  # Adding sinusoidal fluctuation
        elif mode == 8:
            aa = a / steps / 6 + 0.1 * math.cos(a * 5)  # Cosine wave adjustment
        elif mode == 9:
            aa = a / steps / 0.5  # Larger angular spread
        elif mode == 10:
            r = amp * math.exp(-a / 20)  # Slower exponential decrease
        elif mode == 11:
            ar = random.randint(-steps, steps)
            aa = (a + ar) / steps / 6  # Random angular adjustment
            ra += random.randint(-15, 15)  # Random radius fluctuation
        elif mode == 12:
            r = amp * math.exp(-a / 10) + random.randint(-10, 10)
            aa = a / steps + 0.05 * math.sin(a * 5)  # Sinusoidal adjustment
        elif mode == 13:
            r = ra

        aa1 = (aa+0)*360*c
        aa2 = (aa+0.3333)*360*c
        aa3 = (aa+0.6666)*360*c

        x1 = x0 + r * math.cos(aa1)
        y1 = y0 + r * math.sin(aa1)
        x2 = x0 + r * math.cos(aa2)
        y2 = y0 + r * math.sin(aa2)
        x3 = x0 + r * math.cos(aa3)
        y3 = y0 + r * math.sin(aa3)
        points = [(x1, y1), (x2, y2), (x3, y3)]

        f = (0, 0, 0)
        #o = None
        o = (255, 255, 255) # par!
        if a & 1 == 1:
            f = (255, 255, 255)
            o = (0, 0, 0) # par!
        if 'color' in params:
            f = new_colorer(params['color'], a, steps)
        triangle(draw, points, fill=f, outline=o)

def mazy32(draw, params):
    """ cykloidy ? """
    # todo: more par / thick + opt multiline / more stuff
    w, h, cnt = init_common(params)
    c = math.pi/180
    y0 = h/2
    x0 = w/2
    steps = params['n']

    total = 16 #?
    for n in range(total):
        po = []
        rn = 1 - n/total #?
        r1 = 120 + 220 * rn #?
        r2 = 30 + 30 * rn #?
        for f in range(steps):
            a = f/steps*c*360 # full circle?
            b = a*(4+n*3)
            x = x0+r1*math.cos(a)+r2*math.cos(b)
            y = y0+r1*math.sin(a)+r2*math.sin(b)
            po.append((int(x), int(y)))
        #draw.polygon(po, fill=(0, 0, 0), outline=(255,0,0)) #1
        #draw.polygon(po, fill=None, outline=(0,0,0)) #2
        cn = 'happy'
        cn = 'wryb'
        cn = 'any_rnd'
        cn = 'psych'
        cn = 'MoonlightBytes6'
        f = new_colorer(cn, n, total)
        #if 'addalpha' in params:
        #f = add_alpha(f, params['addalpha'])
        f = add_alpha(f, 128+16)
        #draw.polygon(po, fill=f, outline=(0,0,0))
        #draw.polygon(po, fill=f, outline=None)
        draw.polygon(po, fill=f, outline=(255-f[0], 255-f[1], 255-f[2]))

def mazy33(draw, params):
    """ ? """
    w, h, cnt = init_common(params)
    # ...
    return 0

def mazy34(draw, params):
    """ ? """
    w, h, cnt = init_common(params)
    # ...
    return 0

def mazy35(draw, params):
    """ ? """
    w, h, cnt = init_common(params)
    # ...
    return 0

def mazy36(draw, params):
    """ ? """
    w, h, cnt = init_common(params)
    # ...
    return 0
