
# paint algorithms (artificial artist), v1.0, Python version
# #1 waves
# (c)2017-2018 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz
# cre: 20180505
# upd: 201805??

# see:
# https://pillow.readthedocs.io/en/3.1.x/reference/ImageDraw.html
# http://pillow.readthedocs.io/en/5.1.x/reference/ImageFilter.html

# TODO:
# - ?


from PIL import Image, ImageDraw, ImageFilter
import random, math, string, os, sys
from bezier import make_bezier
from datetime import datetime as dt
from drawtools import get_canvas, circle, box, triangle, gradient, gradient2


def waves1(params, fn):
    start_time = dt.now()
    w = params['w']
    h = params['h']
    print('waves1...', fn)
    random.seed()
    c = math.pi/180
    im = Image.new('RGB', (w, h), params['bg'])
    draw = ImageDraw.Draw(im)

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
        fd = 100
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

    im.save(fn)
    time_elapsed = dt.now() - start_time
    print('smazy done. elapsed time: {}'.format(time_elapsed))

# ---

def do_waves1(cnt, w, h, odir):

    params1 = {
        'w': w, 'h': h, 'bg': (224, 244, 0),
        'z': 14,
        'horizontal': False,
        'gradient': 256,
        'c1': (0,0,255),
        'c2': (0,255,255),
        'c3': (255,255,255),
    }
    params2 = {
        'w': w, 'h': h, 'bg': (224, 244, 0),
        'z': 12,
        'horizontal': True,
        'gradient': 256,
        'c1': (0,0,0),
        'c2': (0,255,0),
        'c3': (255,255,0),
    }
    params3 = {
        'w': w, 'h': h, 'bg': (0, 0, 0),
        'z': 9,
        'horizontal': False,
        'gradient': 24,
        'c1': (0,0,0),
        'c2': (255,0,0),
        'c3': (255,255,0),
    }

    for n in range(cnt):
        waves1(params1, odir+'waves1-%dx%d-01-%03d.png' % (w, h, n+1))
        waves1(params2, odir+'waves1-%dx%d-02-%03d.png' % (w, h, n+1))
        waves1(params3, odir+'waves1-%dx%d-03-%03d.png' % (w, h, n+1))

# ---

def main():
    start_time = dt.now()
    cnt = 5
    ca = get_canvas('A3')
    w = ca[0]
    h = ca[1]
    odir = ''
    do_waves1(cnt, w, h, odir)
    time_elapsed = dt.now() - start_time
    print('ALL done. elapsed time: {}'.format(time_elapsed))


if __name__ == '__main__':
    main()
